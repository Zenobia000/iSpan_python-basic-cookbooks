#!/usr/bin/env python3
"""
批量完成 Ch18-Ch30 章節開發
根據 Ch01 的標準模板自動生成所有必要檔案
"""

import os
import json
from pathlib import Path

# 章節資訊配置
CHAPTERS_CONFIG = {
    "ch18-inheritance": {
        "title": "繼承與多型 | Inheritance and Polymorphism",
        "hours": 3.5,
        "difficulty": "中階",
        "prerequisites": ["Ch16: 類別與物件", "Ch17: 封裝與資訊隱藏"],
        "topics": ["繼承", "super()", "方法覆寫", "多型", "MRO", "抽象基類"],
        "examples_count": 6,
        "exercises_count": 12
    },
    "ch19-special-methods": {
        "title": "特殊方法與運算子重載 | Special Methods and Operator Overloading",
        "hours": 3.5,
        "difficulty": "中階",
        "prerequisites": ["Ch16: 類別與物件", "Ch18: 繼承與多型"],
        "topics": ["__init__", "__str__", "__repr__", "__len__", "__getitem__", "運算子重載"],
        "examples_count": 7,
        "exercises_count": 12
    },
    "ch20-exceptions": {
        "title": "例外處理機制 | Exception Handling",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": ["Ch04: 條件判斷", "Ch12: 函式設計基礎"],
        "topics": ["try-except", "finally", "else", "多重例外", "例外層級"],
        "examples_count": 6,
        "exercises_count": 12
    },
    "ch21-custom-exceptions": {
        "title": "自訂例外與 raise | Custom Exceptions and raise",
        "hours": 2.5,
        "difficulty": "中階",
        "prerequisites": ["Ch16: 類別與物件", "Ch20: 例外處理機制"],
        "topics": ["自訂 Exception", "raise", "assert", "例外鏈", "上下文管理器"],
        "examples_count": 5,
        "exercises_count": 10
    },
    "ch22-debugging": {
        "title": "除錯技術 | Debugging Techniques",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": ["Ch20: 例外處理機制"],
        "topics": ["print debugging", "logging", "pdb", "常見錯誤", "除錯策略"],
        "examples_count": 6,
        "exercises_count": 12
    },
    "ch23-file-io": {
        "title": "檔案操作基礎 | File I/O Basics",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": ["Ch08: 序列資料：元組與字串", "Ch20: 例外處理機制"],
        "topics": ["open()", "read/write", "with statement", "文字檔", "編碼"],
        "examples_count": 7,
        "exercises_count": 12
    },
    "ch24-json": {
        "title": "結構化資料：JSON | Structured Data: JSON",
        "hours": 2.5,
        "difficulty": "中階",
        "prerequisites": ["Ch09: 映射資料：字典", "Ch23: 檔案操作基礎"],
        "topics": ["json.dump", "json.load", "dumps/loads", "JSON 格式", "編碼問題"],
        "examples_count": 6,
        "exercises_count": 10
    },
    "ch25-csv": {
        "title": "結構化資料：CSV | Structured Data: CSV",
        "hours": 2.5,
        "difficulty": "中階",
        "prerequisites": ["Ch07: 序列資料：列表", "Ch23: 檔案操作基礎"],
        "topics": ["csv.reader", "csv.writer", "DictReader", "DictWriter", "Excel 相容性"],
        "examples_count": 6,
        "exercises_count": 10
    },
    "ch26-paths": {
        "title": "路徑與檔案系統 | Paths and File Systems",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": ["Ch23: 檔案操作基礎"],
        "topics": ["pathlib.Path", "os.path", "跨平台路徑", "檔案系統操作", "目錄管理"],
        "examples_count": 6,
        "exercises_count": 12
    },
    "ch27-modules": {
        "title": "自訂模組與套件 | Custom Modules and Packages",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": ["Ch12: 函式設計基礎"],
        "topics": ["import", "__init__.py", "__name__", "套件結構", "模組搜尋路徑"],
        "examples_count": 6,
        "exercises_count": 12
    },
    "ch28-package-management": {
        "title": "套件管理與虛擬環境 | Package Management and Virtual Environments",
        "hours": 2.5,
        "difficulty": "中階",
        "prerequisites": ["Ch27: 自訂模組與套件"],
        "topics": ["pip", "requirements.txt", "venv", "虛擬環境", "套件版本管理"],
        "examples_count": 5,
        "exercises_count": 10
    },
    "ch29-code-style": {
        "title": "程式碼風格與文件 | Code Style and Documentation",
        "hours": 2.5,
        "difficulty": "中階",
        "prerequisites": ["Ch12: 函式設計基礎", "Ch16: 類別與物件"],
        "topics": ["PEP 8", "docstring", "type hints", "命名規範", "code linting"],
        "examples_count": 6,
        "exercises_count": 10
    },
    "ch30-version-control": {
        "title": "版本控制基礎 | Version Control Basics",
        "hours": 3,
        "difficulty": "中階",
        "prerequisites": [],
        "topics": ["git init", "commit", "branch", "merge", ".gitignore", "GitHub"],
        "examples_count": 6,
        "exercises_count": 12
    }
}


def create_notebook_structure(cells):
    """建立 Jupyter Notebook JSON 結構"""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


def create_markdown_cell(text):
    """建立 Markdown Cell"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.split('\n')
    }


def create_code_cell(code):
    """建立 Code Cell"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": code.split('\n')
    }


def generate_readme(chapter_key, config):
    """生成 README.md"""
    prereqs = '\n'.join([f"- {p}" for p in config['prerequisites']]) if config['prerequisites'] else "- 無特定先修要求"
    topics_list = '\n'.join([f"- {t}" for t in config['topics']])

    return f"""# {config['title']}

## 📘 章節資訊

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | {config['hours']} 小時 |
| **難度等級** | {config['difficulty']} ⭐⭐⭐ |
| **先備知識** | {', '.join(config['prerequisites']) if config['prerequisites'] else '無'} |
| **相關章節** | 與前後章節整合 |

---

## 🎯 學習目標

### Bloom 認知層次

#### 1. 知識 (Knowledge)
- [ ] 理解本章核心概念的基本定義
- [ ] 記憶主要術語與語法

#### 2. 理解 (Comprehension)
- [ ] 解釋概念的運作原理
- [ ] 說明使用情境與時機

#### 3. 應用 (Application)
- [ ] 在實際程式中正確使用
- [ ] 解決實務問題

#### 4. 分析 (Analysis)
- [ ] 比較不同方法的優劣
- [ ] 辨識最佳實踐模式

---

## 🔑 核心概念

### 主要議題
{topics_list}

### First Principles 分析

**為什麼需要這個概念？**
這部分內容將幫助學習者從第一原理理解為什麼這個主題存在，它解決了什麼問題。

**基本原理**
從最基礎的概念出發，逐步建立完整的理解框架。

---

## 📚 重要術語

| 中文 | English | 說明 |
|:-----|:--------|:-----|
| 待補充 | - | - |

---

## 📖 教材內容

### 檔案結構

| 檔案 | 用途 | 建議學習時間 |
|:-----|:-----|:-------------|
| `README.md` | 章節導讀（本文件） | 15 分鐘 |
| `01-lecture.ipynb` | 完整講義（含 {config['examples_count']} 個範例） | {int(config['hours'] * 30)} 分鐘 |
| `02-worked-examples.ipynb` | 詳解範例 | 30 分鐘 |
| `03-practice.ipynb` | 課堂練習 | 40 分鐘 |
| `04-exercises.ipynb` | 課後習題（{config['exercises_count']} 題） | 60 分鐘 |
| `05-solutions.ipynb` | 習題解答 | 30 分鐘 |
| `quiz.ipynb` | 自我測驗 | 20 分鐘 |

### 學習流程建議

```
預習 → 講義學習 → 課堂練習 → 課後習題 → 自我測驗 → 複習
```

---

## ✅ 實作能力檢核

學完本章後，你應該能夠：

### 基本能力
- [ ] 基本能力項目 1
- [ ] 基本能力項目 2

### 進階能力
- [ ] 進階能力項目 1
- [ ] 進階能力項目 2

### 應用能力
- [ ] 應用能力項目 1
- [ ] 應用能力項目 2

---

## 💡 理論重點

### 核心觀念

```python
# 範例程式碼
# 此處展示本章最核心的概念
```

---

## 👨‍🏫 教學建議

### 授課要點

1. **引入動機**：說明為什麼需要學習此主題
2. **循序漸進**：從簡單範例開始，逐步增加複雜度
3. **實作為主**：鼓勵學生多動手練習

### 常見困難點

1. **困難點 1**
   - 問題描述
   - 解決方案

2. **困難點 2**
   - 問題描述
   - 解決方案

3. **困難點 3**
   - 問題描述
   - 解決方案

---

## 📚 延伸資源

### 官方文件
- [Python 官方文件](https://docs.python.org/zh-tw/3/)

### 推薦閱讀
- 相關書籍或文章

### 延伸主題
- 進階主題 1
- 進階主題 2

---

## ❓ 常見問題 FAQ

### Q1: 常見問題 1？
A: 回答

### Q2: 常見問題 2？
A: 回答

---

## 🗺️ 本章與課程架構的關係

```
前置章節 → 本章 → 後續章節
```

---

**版本記錄**
- v1.0 (2025-10-05): 初版建立
- 作者：課程開發團隊

**學習成功標準**
完成所有練習與測驗，正確率達 80% 以上

---

[← 上一章]() | [回目錄](../../README.md) | [下一章 →]()
"""


def check_and_complete_chapter(chapter_dir, chapter_key, config):
    """檢查並補全章節檔案"""
    chapter_path = Path(chapter_dir)

    if not chapter_path.exists():
        print(f"❌ 資料夾不存在: {chapter_dir}")
        return False

    required_files = [
        "README.md",
        "01-lecture.ipynb",
        "02-worked-examples.ipynb",
        "03-practice.ipynb",
        "04-exercises.ipynb",
        "05-solutions.ipynb",
        "quiz.ipynb"
    ]

    missing_files = []
    for file in required_files:
        if not (chapter_path / file).exists():
            missing_files.append(file)

    if missing_files:
        print(f"\n📝 {chapter_key} 缺少檔案: {', '.join(missing_files)}")

        for file in missing_files:
            file_path = chapter_path / file

            if file == "README.md":
                content = generate_readme(chapter_key, config)
                file_path.write_text(content, encoding='utf-8')
                print(f"  ✅ 已建立 {file}")

            elif file.endswith('.ipynb'):
                # 建立基本的 notebook 結構
                cells = [
                    create_markdown_cell(f"# {config['title']}\n\n本檔案內容待補充")
                ]
                notebook = create_notebook_structure(cells)
                file_path.write_text(json.dumps(notebook, indent=2, ensure_ascii=False), encoding='utf-8')
                print(f"  ✅ 已建立 {file} (基礎框架)")

    else:
        print(f"✅ {chapter_key} 所有檔案完整")

    return True


def main():
    """主程式"""
    base_dir = Path("fundamentals")

    print("=" * 60)
    print(" Ch18-Ch30 章節完整性檢查與補全工具")
    print("=" * 60)

    for chapter_key, config in CHAPTERS_CONFIG.items():
        chapter_dir = base_dir / chapter_key
        check_and_complete_chapter(chapter_dir, chapter_key, config)

    print("\n" + "=" * 60)
    print(" 檢查完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
