# -*- coding: utf-8 -*-
"""
build_manifest.py —— 解析 w3ccoo.com Python 教程左侧目录，生成课程清单。

工作原理：
    1. 抓取任意一篇教程页（如 python-intro.html），它的侧边栏包含全部章节链接。
    2. 侧边栏里：
         - <h2 class="left">      顶级分类（Python 教程 / NumPy / 机器学习 ...）
         - <a class="overview_*"> 子分类（Python 变量 / 字符串 / 列表 ...）
         - 普通 <a>               具体页面
    3. 按文档顺序遍历，把每个页面归类到所属分类，输出 course_manifest.json。

为什么用这个网站：
    w3ccoo.com 是 W3Schools Python 教程的中文镜像，内容免费公开、结构清晰，
    适合作为系统学习 Python 的资料来源。
"""

import json
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://www.w3ccoo.com/python/"
SEED_URL = "https://www.w3ccoo.com/python/python-intro.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python-Learning/1.0"}
OUTPUT = Path(__file__).parent / "course_manifest.json"

# 顶级分类 -> 我们想要的中文目录编号前缀（便于后面整理成有序文件夹）。
# 顺序即学习顺序：先打基础，再到数据结构、函数、进阶、第三方库、数据库。
SECTION_ORDER = {
    "Python教程": "01-Python核心基础",
    "Python文件处理": "02-文件处理",
    "PythonNumPy": "03-NumPy科学计算",
    "PythonSciPy": "04-SciPy科学计算",
    "Python机器学习": "05-机器学习入门",
    "PythonMySQL": "06-MySQL数据库",
    "PythonMongoDB": "07-MongoDB数据库",
    "Python参考手册": "08-参考手册",
    "Python模块参考": "09-常用模块参考",
    "Python如何使用": "10-实战小技巧",
    "Python高级教程": "11-Python进阶HOWTO",
    "Python实例": "12-练习与测验",
}


def _norm(s: str) -> str:
    """去掉空白字符，用于分类名匹配（网页里空格数量不稳定）。"""
    return re.sub(r"\s+", "", s)


# 用去空格后的分类名做键，避免“Python教程”与“Python 教程”匹配不上。
SECTION_ORDER_NORM = SECTION_ORDER  # 键本身已是去空格形式


def folder_for(section: str) -> str:
    """根据顶级分类名返回带编号的文件夹名。"""
    return SECTION_ORDER_NORM.get(_norm(section), section)


def fetch(url: str) -> str:
    """抓取页面并返回 HTML 文本。失败则抛出异常让上层处理。"""
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding  # 自动识别编码，避免中文乱码
    return resp.text


def parse_sidebar(html: str) -> list[dict]:
    """从侧边栏解析出 [{section, subsection, url, title}] 的有序列表。"""
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.find(id="leftmenuinnerinner")
    if nav is None:
        raise RuntimeError("没有找到侧边栏 #leftmenuinnerinner，网页结构可能已变化。")

    sections = []
    current_section = "Python 教程"          # 默认分类
    current_subsection = ""                  # 当前子分类（如“Python 变量”）
    seen = set()                             # 去重：有些链接会重复出现

    # 遍历侧边栏中的 h2 与 a 标签，保持文档顺序
    for el in nav.find_all(["h2", "a"]):
        if el.name == "h2":
            text = el.get_text(strip=True)
            if text:                         # 进入新的顶级分类
                current_section = text
                current_subsection = ""
        elif el.name == "a":
            href = el.get("href", "")
            title = el.get_text(strip=True)
            if not href or not title:
                continue
            # 只保留属于本 Python 教程的 .html 链接
            if "/python/" not in href or not href.endswith(".html"):
                continue
            if href in seen:
                continue
            seen.add(href)
            # 带 overview 类的是子分类标题，同时它本身也是一个页面
            if "overview" in (el.get("class") or []):
                current_subsection = title
            sections.append({
                "section": current_section,
                "subsection": current_subsection,
                "url": href,
                "title": title,
            })
    return sections


def slugify(title: str) -> str:
    """把中文标题转成安全的文件名：保留中文、字母、数字，其余变下划线。"""
    title = title.strip()
    # 去掉常见标点和空格
    title = re.sub(r"[\\/:*?\"<>|]", "", title)
    title = re.sub(r"\s+", "_", title)
    return title


def build():
    print(f"抓取侧边栏源页：{SEED_URL}")
    html = fetch(SEED_URL)
    print("解析目录结构 ...")
    pages = parse_sidebar(html)
    print(f"共发现 {len(pages)} 个章节页面。")

    # 按顶级分类分组，并附上编号前缀
    by_section: dict[str, list[dict]] = {}
    for p in pages:
        sec = p["section"]
        by_section.setdefault(sec, []).append(p)

    manifest = {
        "source": BASE,
        "total_pages": len(pages),
        "sections": [],
    }
    for sec_name, items in by_section.items():
        folder = folder_for(sec_name)
        manifest["sections"].append({
            "section": sec_name,
            "folder": folder,
            "count": len(items),
            "pages": items,
        })

    OUTPUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已生成课程清单：{OUTPUT}")
    print("\n各分类页面数量：")
    for s in manifest["sections"]:
        print(f"  {s['folder']:<28} {s['count']:>3} 篇")
    return manifest


if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print(f"出错：{e}", file=sys.stderr)
        sys.exit(1)
