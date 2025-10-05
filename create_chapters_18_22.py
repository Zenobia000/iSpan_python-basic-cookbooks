"""
批量生成 Ch18-Ch22 的教材檔案
這個腳本會生成所有必要的 Jupyter Notebook 檔案
"""

import json
import os
from pathlib import Path

# 基礎路徑
BASE_PATH = Path(r"D:\python_workspace\github\iSpan_python-basic-cookbooks\fundamentals")

# 章節定義
CHAPTERS = {
    "ch18-inheritance-polymorphism": {
        "title": "繼承與多型 | Inheritance and Polymorphism",
        "number": 18
    },
    "ch19-special-methods": {
        "title": "特殊方法與運算子重載 | Special Methods and Operator Overloading",
        "number": 19
    },
    "ch20-exception-handling": {
        "title": "例外處理機制 | Exception Handling",
        "number": 20
    },
    "ch21-custom-exceptions": {
        "title": "自訂例外與 raise | Custom Exceptions and raise",
        "number": 21
    },
    "ch22-debugging": {
        "title": "除錯技術 | Debugging Techniques",
        "number": 22
    }
}

def create_practice_notebook(chapter_title, chapter_num):
    """創建課堂練習 notebook"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Chapter {chapter_num}: {chapter_title} - 課堂練習\n\n",
                    "## 🛠️ Practice Exercises\n\n",
                    "本檔案包含課堂練習題，請在課堂上完成。\n\n",
                    "**注意**：請先完成 01-lecture.ipynb 和 02-worked-examples.ipynb\n\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 練習 1\n\n",
                    "### 題目\n",
                    "(題目將根據章節主題設計)\n\n",
                    "### 提示\n",
                    "- 參考講義的範例\n",
                    "- 一步步思考\n\n",
                    "### 解答空間"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 在此撰寫你的程式碼\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## 練習 2\n\n",
                    "### 題目\n",
                    "(題目將根據章節主題設計)\n\n",
                    "### 解答空間"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 在此撰寫你的程式碼\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## 練習 3\n\n",
                    "### 題目\n",
                    "(題目將根據章節主題設計)\n\n",
                    "### 解答空間"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 在此撰寫你的程式碼\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## 📝 課堂練習完成檢核\n\n",
                    "完成練習後，請確認：\n",
                    "- [ ] 所有程式碼都能正確執行\n",
                    "- [ ] 理解每個題目的解題思路\n",
                    "- [ ] 能向同學解釋你的解法\n\n",
                    "**下一步**：完成 04-exercises.ipynb 課後習題"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_exercises_notebook(chapter_title, chapter_num):
    """創建課後習題 notebook"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Chapter {chapter_num}: {chapter_title} - 課後習題\n\n",
                    "## ✍️ Exercises\n\n",
                    "本檔案包含 12 題課後習題，難度從基礎到挑戰。\n\n",
                    "**難度標示**：\n",
                    "- ⭐ 基礎（1-5 題）\n",
                    "- ⭐⭐ 中級（6-9 題）\n",
                    "- ⭐⭐⭐ 挑戰（10-12 題）\n\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 基礎題（⭐）\n\n",
                    "### 習題 1\n",
                    "**難度**：⭐\n\n",
                    "**題目**：(根據章節主題設計)\n\n",
                    "**要求**：\n",
                    "1. 要求 1\n",
                    "2. 要求 2"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 習題 1 解答\n",
                    "pass"
                ]
            }
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"---\n\n### 習題 {i}\n**難度**：{'⭐' if i <= 5 else '⭐⭐' if i <= 9 else '⭐⭐⭐'}\n\n**題目**：(根據章節主題設計)"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [f"# 習題 {i} 解答\npass"]
            } for i in range(2, 13)
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## 📊 完成度檢核\n\n",
                    "- [ ] 完成所有基礎題（1-5）\n",
                    "- [ ] 完成所有中級題（6-9）\n",
                    "- [ ] 挑戰進階題（10-12）\n",
                    "- [ ] 對照 05-solutions.ipynb 檢查答案\n\n",
                    "**完成後**：進行 quiz.ipynb 自我測驗"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_solutions_notebook(chapter_title, chapter_num):
    """創建習題解答 notebook"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Chapter {chapter_num}: {chapter_title} - 習題解答\n\n",
                    "## ✅ Solutions\n\n",
                    "本檔案提供 04-exercises.ipynb 的完整解答。\n\n",
                    "**使用建議**：\n",
                    "1. 先自行完成習題\n",
                    "2. 再對照本解答\n",
                    "3. 理解不同解法的優缺點\n\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## 習題 1 解答\n\n",
                    "### 參考解法"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 習題 1 參考解法\n",
                    "# (完整解答)\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### 解題重點\n",
                    "- 重點 1\n",
                    "- 重點 2\n\n",
                    "### 常見錯誤\n",
                    "- 錯誤 1：說明\n",
                    "- 錯誤 2：說明"
                ]
            }
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"---\n\n## 習題 {i} 解答"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [f"# 習題 {i} 參考解法\npass"]
            } for i in range(2, 13)
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_quiz_notebook(chapter_title, chapter_num):
    """創建測驗 notebook"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Chapter {chapter_num}: {chapter_title} - 自我測驗\n\n",
                    "## 📝 Quiz\n\n",
                    "本測驗包含選擇題和程式題，用於檢核學習成效。\n\n",
                    "**目標分數**：70 分以上通過\n\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Part 1: 選擇題（每題 5 分，共 50 分）\n\n",
                    "### 1. (根據章節主題設計)\n",
                    "A) 選項 A  \n",
                    "B) 選項 B  \n",
                    "C) 選項 C  \n",
                    "D) 選項 D  \n\n",
                    "**你的答案**：___"
                ]
            }
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### {i}. (根據章節主題設計)\nA) 選項 A  \nB) 選項 B  \nC) 選項 C  \nD) 選項 D  \n\n**你的答案**：___"]
            } for i in range(2, 11)
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## Part 2: 程式題（每題 10 分，共 50 分）\n\n",
                    "### 程式題 1\n",
                    "**題目**：(根據章節主題設計)\n\n",
                    "**要求**：\n",
                    "1. 要求 1\n",
                    "2. 要求 2"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 程式題 1 解答\n",
                    "pass"
                ]
            }
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"---\n\n### 程式題 {i}\n**題目**：(根據章節主題設計)"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [f"# 程式題 {i} 解答\npass"]
            } for i in range(2, 6)
        ] + [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n\n",
                    "## 📊 答案與評分\n\n",
                    "### 選擇題答案\n",
                    "1. (答案)  \n",
                    "2. (答案)  \n",
                    "3. (答案)  \n",
                    "4. (答案)  \n",
                    "5. (答案)  \n",
                    "6. (答案)  \n",
                    "7. (答案)  \n",
                    "8. (答案)  \n",
                    "9. (答案)  \n",
                    "10. (答案)\n\n",
                    "### 程式題評分標準\n",
                    "- 功能正確（60%）\n",
                    "- 程式碼品質（30%）\n",
                    "- 效率與最佳化（10%）\n\n",
                    "**總分**：_____ / 100\n\n",
                    "**通過標準**：≥ 70 分"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_chapter_files(chapter_dir, chapter_info):
    """為指定章節創建所有檔案"""
    chapter_path = BASE_PATH / chapter_dir
    chapter_path.mkdir(parents=True, exist_ok=True)

    title = chapter_info["title"]
    num = chapter_info["number"]

    # 只創建尚未手動創建的檔案
    files_to_create = {
        "03-practice.ipynb": create_practice_notebook,
        "04-exercises.ipynb": create_exercises_notebook,
        "05-solutions.ipynb": create_solutions_notebook,
        "quiz.ipynb": create_quiz_notebook
    }

    for filename, creator_func in files_to_create.items():
        filepath = chapter_path / filename
        # 只有檔案不存在或檔案很小(空模板)時才創建
        if not filepath.exists() or filepath.stat().st_size < 1000:
            notebook_content = creator_func(title, num)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(notebook_content, f, ensure_ascii=False, indent=1)
            print(f"✅ 創建：{chapter_dir}/{filename}")
        else:
            print(f"⏭️  跳過：{chapter_dir}/{filename} (已存在)")

def main():
    """主程式"""
    print("開始批量創建 Ch18-Ch22 的教材檔案...\n")

    for chapter_dir, chapter_info in CHAPTERS.items():
        print(f"\n處理 {chapter_dir}...")
        create_chapter_files(chapter_dir, chapter_info)

    print("\n\n✅ 所有檔案創建完成！")
    print("\n下一步：")
    print("1. 手動完善每個章節的 README.md")
    print("2. 手動完善每個章節的 01-lecture.ipynb")
    print("3. 手動完善每個章節的 02-worked-examples.ipynb")
    print("4. 根據章節主題補充練習題和測驗題")

if __name__ == "__main__":
    main()
