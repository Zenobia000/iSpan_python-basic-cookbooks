#!/usr/bin/env python3
"""
批量創建課程檔案腳本
Batch file creation script for Python curriculum
"""

import os
import json

# 課程結構定義
CHAPTERS = [
    {"num": "02", "name": "operators", "title": "運算子與表達式", "en": "Operators and Expressions", "hours": 3, "difficulty": 1},
    {"num": "03", "name": "io", "title": "輸入輸出與格式化", "en": "Input/Output and Formatting", "hours": 3, "difficulty": 1},
    {"num": "04", "name": "conditionals", "title": "條件判斷", "en": "Conditional Statements", "hours": 4, "difficulty": 2},
    {"num": "05", "name": "loops", "title": "迴圈控制", "en": "Loop Constructs", "hours": 4, "difficulty": 2},
    {"num": "06", "name": "advanced-iteration", "title": "迴圈進階技巧", "en": "Advanced Iteration", "hours": 3, "difficulty": 2},
    {"num": "07", "name": "lists", "title": "序列資料：列表", "en": "Sequences: Lists", "hours": 4, "difficulty": 2},
    {"num": "08", "name": "tuples-strings", "title": "序列資料：元組與字串", "en": "Sequences: Tuples & Strings", "hours": 3, "difficulty": 2},
    {"num": "09", "name": "dictionaries", "title": "映射資料：字典", "en": "Mappings: Dictionaries", "hours": 4, "difficulty": 2},
    {"num": "10", "name": "sets", "title": "集合資料", "en": "Sets and Set Operations", "hours": 3, "difficulty": 2},
    {"num": "11", "name": "comprehensions", "title": "推導式與生成器", "en": "Comprehensions", "hours": 3, "difficulty": 3},
    {"num": "12", "name": "functions", "title": "函式設計基礎", "en": "Function Fundamentals", "hours": 4, "difficulty": 2},
    {"num": "13", "name": "scope", "title": "作用域與生命週期", "en": "Scope and Lifetime", "hours": 3, "difficulty": 3},
    {"num": "14", "name": "higher-order-functions", "title": "高階函式與 Lambda", "en": "Higher-Order Functions", "hours": 3, "difficulty": 3},
    {"num": "15", "name": "recursion", "title": "遞迴思維", "en": "Recursive Thinking", "hours": 3, "difficulty": 3},
    {"num": "16", "name": "classes", "title": "類別與物件", "en": "Classes and Objects", "hours": 4, "difficulty": 3},
    {"num": "17", "name": "encapsulation", "title": "封裝與資訊隱藏", "en": "Encapsulation", "hours": 3, "difficulty": 3},
    {"num": "18", "name": "inheritance", "title": "繼承與多型", "en": "Inheritance and Polymorphism", "hours": 4, "difficulty": 3},
    {"num": "19", "name": "special-methods", "title": "特殊方法與運算子重載", "en": "Special Methods", "hours": 3, "difficulty": 4},
    {"num": "20", "name": "exceptions", "title": "例外處理機制", "en": "Exception Handling", "hours": 4, "difficulty": 2},
    {"num": "21", "name": "custom-exceptions", "title": "自訂例外與 raise", "en": "Custom Exceptions", "hours": 3, "difficulty": 3},
    {"num": "22", "name": "debugging", "title": "除錯技術", "en": "Debugging Techniques", "hours": 3, "difficulty": 2},
    {"num": "23", "name": "file-io", "title": "檔案操作基礎", "en": "File Operations", "hours": 4, "difficulty": 2},
    {"num": "24", "name": "json", "title": "結構化資料：JSON", "en": "Structured Data: JSON", "hours": 3, "difficulty": 2},
    {"num": "25", "name": "csv", "title": "結構化資料：CSV", "en": "Structured Data: CSV", "hours": 3, "difficulty": 2},
    {"num": "26", "name": "paths", "title": "路徑與檔案系統", "en": "Paths and File Systems", "hours": 3, "difficulty": 2},
    {"num": "27", "name": "modules", "title": "自訂模組與套件", "en": "Custom Modules and Packages", "hours": 4, "difficulty": 3},
    {"num": "28", "name": "package-management", "title": "套件管理與虛擬環境", "en": "Package Management", "hours": 3, "difficulty": 2},
    {"num": "29", "name": "code-style", "title": "程式碼風格與文件", "en": "Code Style and Documentation", "hours": 3, "difficulty": 2},
    {"num": "30", "name": "version-control", "title": "版本控制基礎", "en": "Version Control Basics", "hours": 3, "difficulty": 2},
]

MILESTONES = [
    {"num": "02", "name": "guessing-game", "title": "終極密碼遊戲", "en": "Number Guessing Game", "chapters": "4-6"},
    {"num": "03", "name": "grade-system", "title": "學生成績管理系統", "en": "Grade Management System", "chapters": "7-11"},
    {"num": "04", "name": "text-toolkit", "title": "文字處理工具箱", "en": "Text Processing Toolkit", "chapters": "12-15"},
    {"num": "05", "name": "banking-system", "title": "銀行帳戶系統", "en": "Banking System", "chapters": "16-19"},
    {"num": "06", "name": "user-registration", "title": "使用者註冊系統", "en": "User Registration System", "chapters": "20-22"},
    {"num": "07", "name": "todo-app", "title": "待辦事項管理程式", "en": "Todo List Application", "chapters": "23-26"},
    {"num": "08", "name": "project-refactor", "title": "個人專案模組化重構", "en": "Project Refactoring", "chapters": "27-30"},
]

def get_difficulty_stars(level):
    """返回難度星級"""
    return "⭐" * level + "☆" * (5 - level)

def create_chapter_readme(chapter):
    """創建章節 README"""
    content = f"""# Chapter {chapter['num']}: {chapter['title']} | {chapter['en']}

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | {chapter['hours']} 小時 |
| **難度等級** | {get_difficulty_stars(chapter['difficulty'])} ({chapter['difficulty']}/5) |
| **先備知識** | Chapter {int(chapter['num'])-1} |
| **相關章節** | （待補充） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** （待補充）
- **定義** （待補充）
- **說明** （待補充）

### 理解面（Comprehension）
- **解釋** （待補充）
- **比較** （待補充）
- **歸納** （待補充）

### 應用面（Application）
- **運用** （待補充）
- **實作** （待補充）
- **解決** （待補充）

### 分析面（Analysis）
- **分析** （待補充）
- **診斷** （待補充）
- **選擇** （待補充）

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
（待補充）
```

### First Principles 解析

#### 為什麼需要...？
**根本問題**：（待補充）

**最小實作**：
```python
# 待補充
```

**推導過程**：（待補充）

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| （待補充） | （待補充） | （待補充） |

---

## 📚 教材內容（Course Materials）

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例 | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題 | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 20 分鐘 | 學習驗收 |

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] （待補充）
- [ ] （待補充）

### 進階能力
- [ ] （待補充）
- [ ] （待補充）

### 應用能力
- [ ] （待補充）
- [ ] （待補充）

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. （待補充）
2. （待補充）

### 常見學生困難點

#### 困難點 1：（待補充）
**症狀**：（待補充）

**解決方法**：（待補充）

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [官方文件連結](https://docs.python.org/3/)

### 推薦閱讀
- （待補充）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布

---

**學習提醒**：請確保完成所有練習題，不要只是閱讀解答！
"""
    return content

def create_milestone_readme(milestone):
    """創建 Milestone README"""
    content = f"""# Milestone {milestone['num']}: {milestone['title']} | {milestone['en']}

## 🎯 專案目標（Project Objectives）

本專案旨在整合以下章節所學：
- **Chapters {milestone['chapters']}**: （待補充具體章節）

---

## 📋 專案描述（Project Description）

### 情境說明
（待補充）

### 功能需求

#### 基本需求（必須完成）
1. （待補充）
2. （待補充）

#### 進階需求（選做）
1. （待補充）
2. （待補充）

### 技術規格
- **Python 版本**：3.8+
- **使用技術**：（待補充）
- **預計程式碼行數**：（待補充）

---

## 🏗️ 專案結構（Project Structure）

```
milestone{milestone['num']}-{milestone['name']}/
├── README.md              # 本文件
├── requirements.ipynb     # 詳細需求規格
├── starter-code.ipynb     # 起始程式碼框架
└── solution.ipynb         # 參考解答
```

---

## 📚 學習成果（Learning Outcomes）

完成此專案後，您將能夠：
1. （待補充）
2. （待補充）

---

## 🔧 開發步驟建議（Development Guide）

### Phase 1: 分析與設計（XX 分鐘）
（待補充）

### Phase 2: 核心功能實作（XX 分鐘）
（待補充）

### Phase 3: 測試與優化（XX 分鐘）
（待補充）

---

## ✅ 評分標準（Grading Rubric）

| 項目 | 優秀 (90-100) | 良好 (75-89) | 及格 (60-74) | 不及格 (<60) |
|:-----|:-------------|:------------|:------------|:------------|
| 功能完整性 | （待補充） | （待補充） | （待補充） | （待補充） |
| 程式碼品質 | （待補充） | （待補充） | （待補充） | （待補充） |

---

## 🎓 教師指引（Instructor Notes）

### 評分重點
- （待補充）

### 常見問題與解答
**Q**: （待補充）
**A**: （待補充）

---

## 🚀 延伸挑戰（Extension Challenges）

完成基本需求後，可嘗試：
1. （待補充）
2. （待補充）

---

**專案難度**：{get_difficulty_stars(2)} (待調整)
**預計完成時間**：2-3 小時
**建議完成期限**：Week X
"""
    return content

def create_empty_notebook(title, chapter_num=""):
    """創建空白 Notebook 模板"""
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {title}\n\n（待補充內容）"]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    return json.dumps(notebook, indent=1, ensure_ascii=False)

def main():
    import sys
    import io
    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    base_dir = os.path.dirname(os.path.abspath(__file__))

    print("開始創建所有檔案...")

    # 1. 創建所有章節的 README
    for chapter in CHAPTERS:
        chapter_dir = os.path.join(base_dir, "fundamentals", f"ch{chapter['num']}-{chapter['name']}")
        readme_path = os.path.join(chapter_dir, "README.md")

        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(create_chapter_readme(chapter))
            print(f"✅ 創建: {readme_path}")

        # 創建空白 Notebooks
        notebooks = [
            ("01-lecture.ipynb", f"Chapter {chapter['num']}: {chapter['title']} - 講義"),
            ("02-worked-examples.ipynb", f"Chapter {chapter['num']}: 詳解範例"),
            ("03-practice.ipynb", f"Chapter {chapter['num']}: 課堂練習"),
            ("04-exercises.ipynb", f"Chapter {chapter['num']}: 課後習題"),
            ("05-solutions.ipynb", f"Chapter {chapter['num']}: 習題解答"),
            ("quiz.ipynb", f"Chapter {chapter['num']}: 自我測驗"),
        ]

        for nb_file, nb_title in notebooks:
            nb_path = os.path.join(chapter_dir, nb_file)
            if not os.path.exists(nb_path):
                with open(nb_path, 'w', encoding='utf-8') as f:
                    f.write(create_empty_notebook(nb_title, chapter['num']))
                print(f"  ✅ 創建: {nb_file}")

    # 2. 創建所有 Milestone 的 README
    for milestone in MILESTONES:
        milestone_dir = os.path.join(base_dir, "milestones", f"milestone{milestone['num']}-{milestone['name']}")
        readme_path = os.path.join(milestone_dir, "README.md")

        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(create_milestone_readme(milestone))
            print(f"✅ 創建: {readme_path}")

        # 創建 Milestone Notebooks
        milestone_nbs = [
            ("requirements.ipynb", f"Milestone {milestone['num']}: 需求規格"),
            ("starter-code.ipynb", f"Milestone {milestone['num']}: 起始程式碼"),
            ("solution.ipynb", f"Milestone {milestone['num']}: 參考解答"),
        ]

        for nb_file, nb_title in milestone_nbs:
            nb_path = os.path.join(milestone_dir, nb_file)
            if not os.path.exists(nb_path):
                with open(nb_path, 'w', encoding='utf-8') as f:
                    f.write(create_empty_notebook(nb_title))
                print(f"  ✅ 創建: {nb_file}")

    print("\n✅ 所有檔案創建完成！")
    print(f"\n📊 統計:")
    print(f"  - 章節數: {len(CHAPTERS)}")
    print(f"  - Milestone 數: {len(MILESTONES)}")
    print(f"  - 總檔案數: {len(CHAPTERS) * 7 + len(MILESTONES) * 4}")

if __name__ == "__main__":
    main()
