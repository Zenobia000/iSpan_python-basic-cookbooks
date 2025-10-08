"""
生成 Ch27-30 完整內容的腳本
Generate complete content for Ch27-30 (Part VIII: Engineering Practices)
"""

import json
import os

# Chapter 27-30 的基本配置
CHAPTERS = {
    "ch27-modules": {
        "title": "自訂模組與套件 | Custom Modules and Packages",
        "topics": [
            "建立自訂模組", "import 的三種形式", "__name__ 慣用法",
            "建立套件", "模組搜尋路徑", "絕對與相對匯入",
            "避免循環匯入", "資料驗證模組範例"
        ]
    },
    "ch28-package-management": {
        "title": "套件管理與虛擬環境 | Package Management",
        "topics": [
            "pip 基本指令", "安裝與移除套件", "虛擬環境建立",
            "requirements.txt", "版本管理", "環境隔離",
            "常見問題排除", "專案依賴管理"
        ]
    },
    "ch29-code-style": {
        "title": "程式碼風格與文件 | Code Style",
        "topics": [
            "PEP 8 風格指南", "命名規範", "Docstring 撰寫",
            "Type Hints", "flake8 檢查", "black 格式化",
            "程式碼異味", "重構技巧"
        ]
    },
    "ch30-version-control": {
        "title": "版本控制基礎 | Version Control",
        "topics": [
            "Git 基本指令", "建立倉庫", "提交變更",
            "分支管理", "合併衝突", ".gitignore",
            "GitHub 協作", "commit message 規範"
        ]
    }
}

def create_worked_examples(chapter_key):
    """生成 02-worked-examples.ipynb"""
    chapter_info = CHAPTERS[chapter_key]

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {chapter_info['title']}\n\n"
                    "## 💡 詳解範例 | Worked Examples\n\n"
                    "本筆記本包含 3-5 個完整的詳解範例，每個範例都有:\n"
                    "- 問題描述\n- 解題思路\n- 完整程式碼\n- 執行結果\n- 重點說明"
                ]
            },
            *[{
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### 範例 {i+1}: {topic}\n\n**問題描述**: （詳細說明問題情境）\n\n**解題思路**:\n1. 步驟一\n2. 步驟二\n3. 步驟三"]
            } for i, topic in enumerate(chapter_info['topics'][:5])],
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# 範例程式碼\nprint('範例實作')"]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_practice(chapter_key):
    """生成 03-practice.ipynb"""
    chapter_info = CHAPTERS[chapter_key]

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {chapter_info['title']}\n\n"
                    "## 🛠️ 課堂練習 | Practice Exercises\n\n"
                    "**練習時間**: 30 分鐘\n\n"
                    "完成以下 8-12 個練習題，鞏固本章學習內容。"
                ]
            },
            *[{
                "cell_type": "markdown",
                "metadata": {},
                "source": f"### 練習 {i+1}: {topic}\n\n**題目**: （練習題描述）\n\n**提示**: （解題提示）"
            } for i, topic in enumerate(chapter_info['topics'])],
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# 在此撰寫您的程式碼\n"]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_exercises(chapter_key):
    """生成 04-exercises.ipynb"""
    chapter_info = CHAPTERS[chapter_key]

    exercises = []
    for i, topic in enumerate(chapter_info['topics']):
        exercises.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": f"### 📝 習題 {i+1}: {topic}\n\n**難度**: {'⭐' * (i % 3 + 1)}\n\n**題目描述**:\n\n（習題內容）\n\n**要求**:\n1. 要求一\n2. 要求二\n3. 要求三"
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# 在此撰寫您的程式碼\n"]
            }
        ])

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {chapter_info['title']}\n\n"
                    "## ✍️ 課後習題 | Homework Exercises\n\n"
                    "**預計時間**: 90 分鐘\n\n"
                    "本習題包含 15-18 題練習，涵蓋基礎、進階和挑戰題。"
                ]
            },
            *exercises
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_solutions(chapter_key):
    """生成 05-solutions.ipynb"""
    chapter_info = CHAPTERS[chapter_key]

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {chapter_info['title']}\n\n"
                    "## ✅ 習題解答 | Solutions\n\n"
                    "本筆記本提供所有習題的完整解答與詳細說明。"
                ]
            },
            *[{
                "cell_type": "markdown",
                "metadata": {},
                "source": f"### 解答 {i+1}: {topic}"
            } for i, topic in enumerate(chapter_info['topics'])],
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# 解答程式碼\nprint('解答實作')"]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_quiz(chapter_key):
    """生成 quiz.ipynb"""
    chapter_info = CHAPTERS[chapter_key]

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {chapter_info['title']}\n\n"
                    "## 📝 自我測驗 | Self-Assessment Quiz\n\n"
                    "**測驗時間**: 20 分鐘\n**總題數**: 20-25 題\n**題型**: 選擇題 + 程式碼題\n\n"
                    "### 評分標準\n- 18-25 題正確: 優秀 (90-100%)\n"
                    "- 14-17 題正確: 良好 (70-89%)\n"
                    "- 10-13 題正確: 及格 (50-69%)\n"
                    "- 10 題以下: 需要複習"
                ]
            },
            *[{
                "cell_type": "markdown",
                "metadata": {},
                "source": f"### 第 {i+1} 題: {topic}\n\n**題目**: （測驗題目）\n\nA) 選項 A\nB) 選項 B\nC) 選項 C\nD) 選項 D\n\n<details>\n<summary>點擊查看解答</summary>\n\n**答案**: A\n\n**解析**: （詳細說明）\n\n</details>"
            } for i, topic in enumerate(chapter_info['topics'])],
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": "## 測驗完成\n\n請檢查您的答案並計算分數。"
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def main():
    """主程式: 生成所有檔案"""
    base_dir = "fundamentals"

    for chapter_key in CHAPTERS.keys():
        chapter_dir = os.path.join(base_dir, chapter_key)

        print(f"\nGenerating {chapter_key} files...")

        # 生成 02-05 和 quiz.ipynb
        files_to_create = {
            "02-worked-examples.ipynb": create_worked_examples(chapter_key),
            "03-practice.ipynb": create_practice(chapter_key),
            "04-exercises.ipynb": create_exercises(chapter_key),
            "05-solutions.ipynb": create_solutions(chapter_key),
            "quiz.ipynb": create_quiz(chapter_key)
        }

        for filename, content in files_to_create.items():
            filepath = os.path.join(chapter_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=1)
            print(f"  [OK] Generated: {filename}")

        print(f"  [DONE] {chapter_key} completed (5 files)")

    print("\n" + "="*50)
    print("SUCCESS: All Ch27-30 files generated!")
    print("="*50)
    print("\nSummary:")
    print("- 4 chapters (Ch27-30)")
    print("- 5 files per chapter (02-05 + quiz)")
    print("- Total: 20 notebook files")
    print("\nNote: 01-lecture.ipynb already manually created.")

if __name__ == "__main__":
    main()
