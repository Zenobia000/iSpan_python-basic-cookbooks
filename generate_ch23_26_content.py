#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自動生成 Ch23-Ch26 完整教材內容
根據 Ch01 的標準格式，生成高品質的 Jupyter Notebook 教材
"""

import json
import os
from pathlib import Path

# 章節配置
CHAPTERS = {
    "ch23-file-io": {
        "title_zh": "檔案操作基礎",
        "title_en": "File I/O Basics",
        "topics": ["open函式", "read/write", "with語句", "編碼處理", "異常處理", "日誌系統", "批次處理"],
        "examples": [
            {
                "title": "安全讀取檔案 - 完整異常處理",
                "description": "實作一個函式，安全地讀取檔案，處理所有可能的異常",
                "difficulty": "基礎"
            },
            {
                "title": "批次文字檔案合併",
                "description": "讀取多個 txt 檔案，合併成單一檔案",
                "difficulty": "中級"
            },
            {
                "title": "日誌分析工具",
                "description": "讀取日誌檔案，統計ERROR、WARNING等級的數量",
                "difficulty": "中級"
            },
            {
                "title": "檔案內容搜尋與替換",
                "description": "在檔案中搜尋特定文字，並替換成新文字",
                "difficulty": "進階"
            }
        ],
        "exercises": [
            ("建立 greeting.txt，寫入問候語", "基礎", "檔案寫入"),
            ("讀取 data.txt 並計算行數", "基礎", "檔案讀取"),
            ("實作 append_log() 函式", "基礎", "附加模式"),
            ("複製檔案內容到新檔案", "基礎", "讀寫結合"),
            ("統計檔案中的字數", "中級", "文字處理"),
            ("反轉檔案內容（最後一行變第一行）", "中級", "列表操作"),
            ("刪除檔案中的空白行", "中級", "條件過濾"),
            ("實作簡易設定檔讀取器（key=value格式）", "中級", "字串解析"),
            ("Big5轉UTF-8編碼轉換工具", "進階", "編碼處理"),
            ("實作檔案備份函式（加上時間戳記）", "進階", "datetime模組"),
            ("批次重新命名檔案（加上編號前綴）", "挑戰", "os模組"),
            ("實作簡易文字檔案加密/解密工具", "挑戰", "綜合應用")
        ]
    },
    "ch24-json": {
        "title_zh": "結構化資料: JSON",
        "title_en": "Structured Data: JSON",
        "topics": ["json模組", "dump/load", "dumps/loads", "ensure_ascii", "indent", "API資料處理"],
        "examples": [
            {
                "title": "學生資料JSON儲存與讀取",
                "description": "將學生字典資料儲存為JSON，再讀取回來",
                "difficulty": "基礎"
            },
            {
                "title": "設定檔管理系統",
                "description": "使用JSON儲存應用程式設定，支援讀取/更新",
                "difficulty": "中級"
            },
            {
                "title": "巢狀資料處理",
                "description": "處理包含列表和字典的複雜JSON結構",
                "difficulty": "中級"
            },
            {
                "title": "模擬API資料解析",
                "description": "解析模擬的API JSON回應，提取所需資訊",
                "difficulty": "進階"
            }
        ],
        "exercises": [
            ("儲存個人資料到JSON檔案", "基礎", "dump基本用法"),
            ("從JSON讀取並顯示資料", "基礎", "load基本用法"),
            ("JSON與字串互轉（dumps/loads）", "基礎", "記憶體操作"),
            ("儲存購物清單到JSON", "基礎", "列表處理"),
            ("實作通訊錄JSON管理", "中級", "字典操作"),
            ("格式化輸出JSON（indent=2）", "中級", "美化輸出"),
            ("處理中文JSON（ensure_ascii=False）", "中級", "編碼問題"),
            ("合併多個JSON檔案", "中級", "字典合併"),
            ("驗證JSON格式是否正確", "進階", "異常處理"),
            ("實作簡易資料庫（JSON儲存）", "進階", "CRUD操作"),
            ("JSON資料扁平化處理", "挑戰", "遞迴"),
            ("實作JSON Schema驗證", "挑戰", "進階應用")
        ]
    },
    "ch25-csv": {
        "title_zh": "結構化資料: CSV",
        "title_en": "Structured Data: CSV",
        "topics": ["csv模組", "reader/writer", "DictReader/DictWriter", "Excel相容性", "pandas預覽"],
        "examples": [
            {
                "title": "學生成績CSV讀寫",
                "description": "讀取CSV成績單，計算平均分數",
                "difficulty": "基礎"
            },
            {
                "title": "使用DictReader處理有標題的CSV",
                "description": "以字典形式讀取CSV，更易於理解",
                "difficulty": "中級"
            },
            {
                "title": "CSV資料過濾與匯出",
                "description": "讀取CSV，篩選符合條件的資料，寫入新CSV",
                "difficulty": "中級"
            },
            {
                "title": "Excel相容CSV處理（中文、逗號）",
                "description": "處理包含中文、逗號的CSV，確保Excel正確開啟",
                "difficulty": "進階"
            }
        ],
        "exercises": [
            ("建立簡單的CSV檔案（3欄x5列）", "基礎", "writer基本用法"),
            ("讀取CSV並顯示所有內容", "基礎", "reader基本用法"),
            ("計算CSV檔案的列數與欄數", "基礎", "資料統計"),
            ("使用DictWriter寫入有標題的CSV", "基礎", "字典寫入"),
            ("合併兩個CSV檔案", "中級", "檔案合併"),
            ("CSV轉JSON格式", "中級", "格式轉換"),
            ("從CSV提取特定欄位", "中級", "欄位選擇"),
            ("CSV排序（按某欄位）", "中級", "資料排序"),
            ("處理包含逗號的欄位（引號處理）", "進階", "特殊字元"),
            ("實作CSV資料驗證工具", "進階", "資料清洗"),
            ("CSV轉Excel格式（.xlsx）", "挑戰", "openpyxl模組"),
            ("大型CSV分批處理（避免記憶體不足）", "挑戰", "效能優化")
        ]
    },
    "ch26-paths": {
        "title_zh": "路徑與檔案系統",
        "title_en": "Paths and File Systems",
        "topics": ["pathlib模組", "Path物件", "os.path", "檔案操作", "目錄遍歷", "跨平台路徑"],
        "examples": [
            {
                "title": "使用pathlib建立和管理路徑",
                "description": "展示Path物件的基本操作",
                "difficulty": "基礎"
            },
            {
                "title": "檔案系統資訊獲取",
                "description": "取得檔案大小、修改時間、是否存在等資訊",
                "difficulty": "中級"
            },
            {
                "title": "遞迴遍歷目錄",
                "description": "搜尋目錄下所有特定副檔名的檔案",
                "difficulty": "中級"
            },
            {
                "title": "跨平台路徑處理",
                "description": "處理Windows和Linux路徑差異",
                "difficulty": "進階"
            }
        ],
        "exercises": [
            ("取得當前工作目錄", "基礎", "Path.cwd()"),
            ("檢查檔案是否存在", "基礎", ".exists()"),
            ("取得檔案的父目錄", "基礎", ".parent"),
            ("取得檔案名稱與副檔名", "基礎", ".name, .suffix"),
            ("建立多層目錄結構", "中級", ".mkdir(parents=True)"),
            ("取得目錄下所有檔案", "中級", ".iterdir()"),
            ("搜尋特定副檔名的檔案", "中級", ".glob('*.txt')"),
            ("取得檔案大小與修改時間", "中級", ".stat()"),
            ("計算目錄總大小", "進階", "遞迴統計"),
            ("實作檔案搜尋工具（類似find指令）", "進階", "綜合應用"),
            ("批次移動檔案到分類資料夾", "挑戰", "檔案組織"),
            ("實作檔案同步工具（比對兩個目錄）", "挑戰", "進階專案")
        ]
    }
}


def generate_worked_examples_notebook(chapter_key, chapter_info):
    """生成 02-worked-examples.ipynb"""
    cells = []

    # 標題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# {chapter_info['title_zh']} | {chapter_info['title_en']}\n\n## 📝 詳解範例 | Worked Examples\n\n---\n\n## 💡 本檔案目的\n\n本檔案提供 **4 個循序漸進的詳解範例**，每個範例包含：\n1. **問題描述**：實際應用情境\n2. **分析思路**：如何拆解問題\n3. **逐步實作**：程式碼 + 註解\n4. **執行結果**：預期輸出\n5. **知識點總結**：學到什麼\n\n---"
    })

    # 生成範例
    for i, example in enumerate(chapter_info['examples'], 1):
        # 範例標題
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"## 範例 {i}：{example['title']}\n\n### 📋 問題描述\n{example['description']}\n\n難度：{example['difficulty']}\n\n### 🔍 分析思路\n1. （根據題目拆解步驟）\n2. （思考需要哪些技術）\n3. （設計資料結構）\n\n### 💻 逐步實作"
        })

        # 程式碼（預留空間供人工完善）
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": f"# 範例 {i} 程式碼\n# TODO: 根據需求實作完整程式碼\n\nprint(\"範例 {i}：{example['title']}\")\n# 實作內容..."
        })

        # 知識點總結
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"### 📚 知識點總結\n- ✅ （知識點 1）\n- ✅ （知識點 2）\n- ✅ （知識點 3）\n\n---"
        })

    return {
        "cells": cells,
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


def generate_practice_notebook(chapter_key, chapter_info):
    """生成 03-practice.ipynb"""
    cells = []

    # 標題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# {chapter_info['title_zh']} | {chapter_info['title_en']}\n\n## 🛠️ 課堂練習 | Practice\n\n---\n\n## 📋 練習說明\n\n本檔案包含 **6 個課堂練習**，用於現場實作，鞏固學習成果。\n\n**建議流程**：\n1. 閱讀題目要求\n2. 獨立思考解法\n3. 實際撰寫程式碼\n4. 執行測試\n5. 若遇到困難，可參考 `02-worked-examples.ipynb` 的範例\n\n**預計時間**：30 分鐘\n\n---"
    })

    # 生成練習題（取前6個）
    for i, (title, difficulty, topic) in enumerate(chapter_info['exercises'][:6], 1):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"## 練習 {i}：{title}\n\n**難度**：{difficulty} | **主題**：{topic}\n\n### 題目要求\n（詳細需求描述）\n\n### 提示\n- 提示 1\n- 提示 2"
        })

        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": "# 在此撰寫你的程式碼\n\n"
        })

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": "---"
        })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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


def generate_exercises_notebook(chapter_key, chapter_info):
    """生成 04-exercises.ipynb"""
    cells = []

    # 標題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# {chapter_info['title_zh']} | {chapter_info['title_en']}\n\n## ✍️ 課後習題 | Exercises\n\n---\n\n## 📋 習題說明\n\n本檔案包含 **{len(chapter_info['exercises'])} 題**，難度分級如下：\n- 🟢 **基礎題（1-4）**：熟悉基本語法\n- 🟡 **中級題（5-8）**：綜合應用\n- 🔴 **進階題（9-10）**：深入思考\n- 🟣 **挑戰題（11-12）**：擴展學習\n\n**建議完成時間**：90-120 分鐘\n\n**完成後請對照** `05-solutions.ipynb` **檢視解答**\n\n---"
    })

    # 生成所有習題
    for i, (title, difficulty, topic) in enumerate(chapter_info['exercises'], 1):
        # 難度圖示
        difficulty_icon = {
            "基礎": "🟢",
            "中級": "🟡",
            "進階": "🔴",
            "挑戰": "🟣"
        }.get(difficulty, "⚪")

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"## {difficulty_icon} 習題 {i}：{title}\n\n**難度**：{difficulty} | **主題**：{topic}\n\n### 題目要求\n（詳細需求描述）\n\n### 範例輸入/輸出\n```\n（範例）\n```"
        })

        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": "# 在此撰寫你的程式碼\n\n"
        })

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": "---"
        })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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


def generate_solutions_notebook(chapter_key, chapter_info):
    """生成 05-solutions.ipynb"""
    cells = []

    # 標題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# {chapter_info['title_zh']} | {chapter_info['title_en']}\n\n## ✅ 習題解答 | Solutions\n\n---\n\n## 📋 使用說明\n\n本檔案提供 **04-exercises.ipynb** 的完整解答。\n\n**建議使用方式**：\n1. ⚠️ **先自行完成習題**，不要直接看解答\n2. ✅ 完成後，對照本檔案檢查答案\n3. 📝 理解不同解法的優缺點\n4. 💡 學習更簡潔或更高效的寫法\n\n---"
    })

    # 生成所有解答
    for i, (title, difficulty, topic) in enumerate(chapter_info['exercises'], 1):
        difficulty_icon = {
            "基礎": "🟢",
            "中級": "🟡",
            "進階": "🔴",
            "挑戰": "🟣"
        }.get(difficulty, "⚪")

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"## {difficulty_icon} 習題 {i} 解答：{title}\n\n### 解題思路\n1. （分析步驟）\n2. （關鍵技巧）\n\n### 程式碼實作"
        })

        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": f"# 習題 {i} 參考解答\n# TODO: 實作完整解答\n\nprint(\"習題 {i} 解答\")\n# 程式碼..."
        })

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": "### 知識點回顧\n- ✅ （重點 1）\n- ✅ （重點 2）\n\n### 其他解法\n（若有多種解法，可在此說明）\n\n---"
        })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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


def generate_quiz_notebook(chapter_key, chapter_info):
    """生成 quiz.ipynb"""
    cells = []

    # 標題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": f"# {chapter_info['title_zh']} | {chapter_info['title_en']}\n\n## 📝 自我測驗 | Quiz\n\n---\n\n## 📋 測驗說明\n\n本測驗包含：\n- **Part A: 選擇題（10 題）** - 每題 5 分，共 50 分\n- **Part B: 程式題（5 題）** - 每題 10 分，共 50 分\n- **總分：100 分** | **及格：70 分**\n\n**建議時間**：25 分鐘\n\n---"
    })

    # Part A: 選擇題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part A: 選擇題（50 分）\n\n請選擇最適合的答案。"
    })

    for i in range(1, 11):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"### 第 {i} 題（5 分）\n\n（題目內容）\n\n(A) 選項 A  \n(B) 選項 B  \n(C) 選項 C  \n(D) 選項 D  \n\n**你的答案**：\n\n---"
        })

    # Part B: 程式題
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part B: 程式題（50 分）\n\n請撰寫程式碼完成以下任務。"
    })

    for i in range(1, 6):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": f"### 程式題 {i}（10 分）\n\n**題目**：（描述）\n\n**範例輸入/輸出**：\n```\n（範例）\n```"
        })

        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": "# 在此撰寫你的程式碼\n\n"
        })

        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": "---"
        })

    # 評分標準
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "## 📊 評分標準\n\n### Part A 選擇題解答\n1. (A/B/C/D)\n2. (A/B/C/D)\n... (在完成後填入正確答案)\n\n### Part B 程式題評分重點\n1. 程式題 1：（評分標準）\n2. 程式題 2：（評分標準）\n...\n\n---\n\n## 🎯 學習建議\n\n- **70 分以上**：恭喜！已充分掌握本章內容\n- **60-69 分**：基本概念良好，建議複習弱項\n- **60 分以下**：需要重新學習本章，完成所有練習題"
    })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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


def main():
    """主程式：生成所有章節的所有檔案"""
    base_dir = Path("fundamentals")

    for chapter_key, chapter_info in CHAPTERS.items():
        chapter_dir = base_dir / chapter_key
        print(f"\nProcessing {chapter_key} - {chapter_info['title_zh']}...")

        # 生成各個 notebook（跳過已存在的README和lecture）
        notebooks = {
            "02-worked-examples.ipynb": generate_worked_examples_notebook,
            "03-practice.ipynb": generate_practice_notebook,
            "04-exercises.ipynb": generate_exercises_notebook,
            "05-solutions.ipynb": generate_solutions_notebook,
            "quiz.ipynb": generate_quiz_notebook
        }

        for filename, generator_func in notebooks.items():
            file_path = chapter_dir / filename

            # 檢查檔案是否已有實質內容（超過1KB）
            if file_path.exists() and file_path.stat().st_size > 1024:
                print(f"  [SKIP] {filename} (already has content)")
                continue

            print(f"  [GEN] {filename}...")
            notebook_content = generator_func(chapter_key, chapter_info)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(notebook_content, f, ensure_ascii=False, indent=1)

            print(f"  [DONE] {filename}")

    print("\n" + "=" * 60)
    print("All files generated successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Open notebooks and fill in code examples")
    print("2. Complete exercise descriptions")
    print("3. Write quiz questions")
    print("4. Ensure all code is executable")


if __name__ == "__main__":
    main()
