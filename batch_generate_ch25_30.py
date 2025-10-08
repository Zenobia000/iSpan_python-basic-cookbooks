#!/usr/bin/env python3
"""批次生成 Ch25-30 的基礎內容"""

import json
from pathlib import Path

CHAPTERS = {
    25: {"title": "CSV", "folder": "ch25-csv", "examples": 6},
    26: {"title": "Paths", "folder": "ch26-paths", "examples": 7},
    27: {"title": "Modules", "folder": "ch27-modules", "examples": 8},
    28: {"title": "Package Management", "folder": "ch28-package-management", "examples": 6},
    29: {"title": "Code Style", "folder": "ch29-code-style", "examples": 5},
    30: {"title": "Version Control", "folder": "ch30-version-control", "examples": 6},
}


def create_lecture(ch_num, config):
    """建立基礎 lecture"""
    cells = []

    # Part I: 理論基礎
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# Chapter {ch_num}: {config['title']}\\n\\n## Part I: 理論基礎"
    })

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 📚 章節概覽\\n\\n本章學習內容...（待補充）"
    })

    # Part II: 實作演練
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "---\\n\\n## Part II: 實作演練"
    })

    for i in range(config['examples']):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"### 💡 範例 {i+1}"
        })
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": f"# 範例 {i+1} 程式碼\\nprint('Example {i+1}')"
        })

    # Part III: 總結
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "---\\n\\n## Part III: 本章總結\\n\\n### 📊 知識回顧\\n\\n（待補充）"
    })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }


def main():
    base = Path("fundamentals")

    for ch_num, config in CHAPTERS.items():
        ch_path = base / config['folder']
        lecture_file = ch_path / "01-lecture.ipynb"

        print(f"生成 Ch{ch_num}: {config['title']}")

        content = create_lecture(ch_num, config)
        with open(lecture_file, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=1)

        print(f"  OK {lecture_file.name} created ({len(content['cells'])} cells)")

    print("\\nAll done!")


if __name__ == "__main__":
    main()
