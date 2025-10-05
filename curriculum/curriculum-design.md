# Python 程式設計基礎教程
## 課程設計指南 | Curriculum Design Guide

> **教學理念**：基於 First Principles → Fundamentals → Body of Knowledge 框架，採用大學教科書標準結構，以學習者為中心的漸進式教學設計。

---

## 📚 教科書式課程架構

### 大學教科書設計原則
本課程遵循國際知名程式設計教科書的組織方式（如 *Introduction to Python* by Guttag, *Python Programming* by Zelle），採用以下結構：

```
每章結構（Each Chapter Structure）
├── 📖 Learning Objectives（學習目標）
├── 🔑 Key Concepts（核心概念）
├── 📝 Theoretical Foundation（理論基礎）
├── 💡 Worked Examples（詳解範例）
├── 🛠️ Hands-on Practice（實作練習）
├── 🎯 Case Study（案例研究）
├── 📊 Chapter Summary（本章總結）
├── ✍️ Review Questions（複習問題）
├── 💻 Programming Exercises（程式練習）
└── 🔗 Further Reading（延伸閱讀）
```

---

## 📋 目錄
1. [課程設計三層架構](#課程設計三層架構)
2. [Jupyter Notebook 標準結構](#jupyter-notebook-標準結構)
3. [資料夾結構規範](#資料夾結構規範)
4. [每個資料夾的 README 標準格式](#每個資料夾的-readme-標準格式)
5. [學習路徑與時程規劃](#學習路徑與時程規劃)
6. [教學法與評量策略](#教學法與評量策略)

---

## 🎯 課程設計三層架構

### Layer 1: First Principles（第一原理層）

### 1. 計算的本質三要素
| 原理 | Python 對應 | 為何不可或缺 |
|:-----|:------------|:-------------|
| **資料（Data）** | 變數、資料型態 | 程式處理的對象，是一切運算的基礎 |
| **運算（Computation）** | 運算子、函式、方法 | 對資料進行轉換的規則，實現邏輯 |
| **控制（Control Flow）** | if/for/while、函式呼叫 | 決定程式執行順序，處理決策與重複 |

### 2. 抽象化三層次
```
L3: 抽象（函式、類別、模組）
     ↑ 封裝可重用邏輯
L2: 結構（資料結構）
     ↑ 組織資料
L1: 基本型態（int, str, bool）
     ↑ 表達最小資料單元
```

### 3. 程式設計的不可違背定律
- **順序執行原則**：程式碼由上而下、由左而右執行（除非有控制流改變）
- **型態一致性**：操作必須符合資料型態的規範
- **作用域規則**：變數的可見範圍由定義位置決定
- **DRY 原則（Don't Repeat Yourself）**：重複邏輯應抽象為函式或類別

---

## Fundamentals: 核心課程模組

### 快速入門路徑（Minimum Viable Knowledge）

#### 🎯 階段一：建立程式思維（Week 1-2）
**目標**：讓學習者能夠「用程式表達想法」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F1-變數與型態** | int, float, str, bool, type() | 能宣告變數並理解型態轉換 |
| **F2-運算與表達式** | 算術/比較/邏輯運算子 | 能寫出正確的運算式求值 |
| **F3-輸入與輸出** | print(), input(), f-string | 能與使用者互動並格式化輸出 |

**First Principles Check**：
- ✅ 資料（變數）✅ 運算（運算子）✅ 互動（I/O）

**Milestone Project**: **簡易計算機** - 輸入兩數與運算符號，輸出結果

---

#### 🎯 階段二：掌控程式流程（Week 3-4）
**目標**：學會「讓程式做決策與重複動作」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F4-條件判斷** | if/elif/else, 巢狀判斷 | 能根據條件執行不同邏輯 |
| **F5-迴圈控制** | for/while, range(), break/continue | 能處理重複任務與序列走訪 |

**First Principles Check**：
- ✅ 控制流（條件與迴圈）

**Milestone Project**: **終極密碼遊戲** - 整合 input、條件、迴圈、邊界檢查

---

#### 🎯 階段三：組織與管理資料（Week 5-6）
**目標**：能「有效儲存與操作多筆資料」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F6-序列資料** | list, tuple, 索引/切片 | 能新增/刪除/修改序列元素 |
| **F7-映射資料** | dict, key-value 操作 | 能用字典儲存與查詢結構化資料 |
| **F8-集合資料** | set, 聯集/交集/差集 | 理解去重與集合運算應用 |
| **F9-字串處理** | 字串方法, split/join/replace | 能處理文字資料的常見任務 |

**First Principles Check**：
- ✅ 抽象層次 L2（資料結構）

**Milestone Project**: **學生成績管理系統** - 用 dict 儲存學生資料，list 儲存成績，計算平均

---

#### 🎯 階段四：建立可重用邏輯（Week 7-8）
**目標**：學會「將程式模組化」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F10-函式設計** | def, 參數/回傳值, docstring | 能將重複邏輯封裝為函式 |
| **F11-作用域與生命週期** | global/local, 變數可見性 | 理解變數作用域，避免命名衝突 |
| **F12-Lambda 與高階函式** | lambda, map/filter/sorted | 能用簡潔語法處理資料轉換 |

**First Principles Check**：
- ✅ 抽象層次 L3（函式封裝）
- ✅ DRY 原則實踐

**Milestone Project**: **文字處理工具箱** - 建立多個文字處理函式（統計字數、轉換大小寫、分詞等）

---

#### 🎯 階段五：物件導向思維（Week 9-10）
**目標**：學會「用物件模擬真實世界」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F13-類別與物件** | class, __init__, 屬性/方法 | 能設計類別並建立實例 |
| **F14-封裝與繼承** | 私有屬性, 繼承, super() | 理解 OOP 的封裝與繼承機制 |

**First Principles Check**：
- ✅ 抽象層次 L3（類別抽象）

**Milestone Project**: **銀行帳戶系統** - Account 基類，SavingsAccount/CheckingAccount 子類

---

#### 🎯 階段六：錯誤處理與除錯（Week 11）
**目標**：寫出「穩健可靠的程式」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F15-異常處理** | try/except/finally, raise | 能捕捉與處理執行時錯誤 |
| **F16-除錯技巧** | print 除錯, traceback 閱讀 | 能快速定位與修復程式錯誤 |

**Milestone Project**: **健壯的使用者註冊系統** - 驗證輸入格式，處理各種異常情況

---

#### 🎯 階段七：檔案與外部資料（Week 12）
**目標**：能「處理外部資料來源」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F17-檔案操作** | open(), read/write, with 語法 | 能讀寫文字檔案 |
| **F18-JSON 資料** | json.load/dump, 序列化 | 能處理結構化資料交換格式 |
| **F19-路徑與目錄** | os/pathlib, 檔案系統操作 | 能遍歷目錄與操作檔案路徑 |

**Milestone Project**: **待辦事項管理程式** - 資料持久化至 JSON，支援新增/刪除/查詢

---

#### 🎯 階段八：模組化與協作（Week 13-14）
**目標**：建立「可維護的專案結構」

| 模組 | 核心概念 | 實作能力檢核 |
|:-----|:---------|:-------------|
| **F20-自訂模組** | import, __name__ == "__main__" | 能將程式拆分為多個模組 |
| **F21-套件管理** | pip, requirements.txt, 虛擬環境 | 能安裝與管理第三方套件 |
| **F22-程式碼風格** | PEP 8, 註解與 docstring 規範 | 寫出符合 Python 社群標準的程式 |

**Milestone Project**: **個人專案重構** - 將前面的 Milestone 專案模組化並符合 PEP 8

---

## Body of Knowledge: 完整知識體系

### Python 初學者知識圖譜（對照 SWEBOK）

```
┌─────────────────────────────────────────────────────┐
│          Python Fundamentals Body of Knowledge       │
└─────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   📦 Core Syntax    🔧 Problem Solving   🏗️ Engineering
                                                Practices
```

### 1. Core Syntax（核心語法）- 75% 課程時數
#### 1.1 資料型態系統
- **Primitives**: int, float, bool, str, NoneType
- **Collections**: list, tuple, dict, set
- **Type Operations**: 轉換、檢查、比較

#### 1.2 控制結構
- **Sequential**: 順序執行
- **Conditional**: if/elif/else, 三元運算子
- **Iterative**: for/while, break/continue/pass
- **Exceptional**: try/except/finally/raise

#### 1.3 函式與抽象
- **Function Basics**: def, parameters, return
- **Scope**: global/nonlocal/local
- **Advanced**: lambda, *args/**kwargs, decorators（進階）
- **Built-in Functions**: len, range, enumerate, zip, map, filter

#### 1.4 物件導向
- **Class Basics**: class, __init__, self
- **Attributes & Methods**: instance/class attributes, methods
- **Inheritance**: 單繼承, super(), method overriding
- **Encapsulation**: 私有屬性（_var, __var）

#### 1.5 模組與套件
- **Import Mechanisms**: import, from...import, as
- **Standard Library**: os, sys, json, datetime, random, math
- **Package Management**: pip, virtual environments

#### 1.6 檔案與 I/O
- **File Operations**: open/read/write, context manager (with)
- **Data Formats**: txt, csv, json
- **Path Operations**: os.path, pathlib

---

### 2. Problem Solving（解題能力）- 15% 課程時數
#### 2.1 演算法思維（入門級）
- **Search**: 線性搜尋
- **Sort**: 泡沫排序概念（理解即可）
- **Traversal**: 序列走訪、巢狀迴圈

#### 2.2 常見問題模式
- **Accumulation**: 累加、計數、尋找最大最小值
- **Filtering**: 篩選符合條件的資料
- **Transformation**: 資料格式轉換
- **Validation**: 輸入驗證、邊界檢查

#### 2.3 除錯策略
- **Print Debugging**: 策略性放置 print()
- **Error Reading**: 理解 Traceback 訊息
- **Rubber Duck Method**: 向他人解釋程式邏輯

---

### 3. Engineering Practices（工程實務）- 10% 課程時數
#### 3.1 程式碼品質
- **Naming**: 有意義的變數/函式命名
- **PEP 8**: 縮排、命名慣例、行長限制
- **Comments**: 何時註解、如何寫 docstring

#### 3.2 專案結構
- **Directory Layout**: 模組化目錄結構
- **Version Control**: Git 基本操作（init, add, commit, push）
- **Documentation**: README, inline comments

#### 3.3 協作與學習
- **Reading Code**: 閱讀他人程式碼的能力
- **Stack Overflow**: 如何提問與搜尋解答
- **Official Docs**: Python 官方文件導覽

---

### 能力檢核表（Competency Checklist）

#### 🟢 Level 1: 基礎操作（完成 F1-F5）
- [ ] 能宣告變數並使用基本型態
- [ ] 能寫出正確的條件判斷與迴圈
- [ ] 能用 print/input 與使用者互動
- [ ] 能閱讀並理解簡單程式碼（50 行以內）

#### 🟡 Level 2: 資料處理（完成 F6-F12）
- [ ] 能靈活運用 list/dict/set 解決問題
- [ ] 能設計函式並理解參數傳遞
- [ ] 能用字串方法處理文字資料
- [ ] 能使用 list comprehension 簡化程式碼

#### 🟠 Level 3: 抽象設計（完成 F13-F16）
- [ ] 能設計類別並運用繼承
- [ ] 能處理常見異常並撰寫健壯程式
- [ ] 能重構程式碼提升可讀性
- [ ] 能獨立除錯中等複雜度程式（200 行左右）

#### 🔵 Level 4: 專案實作（完成 F17-F22）
- [ ] 能處理檔案與結構化資料（JSON/CSV）
- [ ] 能將程式拆分為多個模組
- [ ] 能使用第三方套件（requests, pandas 入門）
- [ ] 能完成 500-1000 行的個人專案

---

## 課程路徑圖

### 學習時間軸（14 週完整路徑）
```
Week 1-2  ━━━━━━━━━━━━━━━━━━━━━━━━━━  F1-F3   基本語法
                                           ↓ Milestone: 計算機
Week 3-4  ━━━━━━━━━━━━━━━━━━━━━━━━━━  F4-F5   控制流
                                           ↓ Milestone: 終極密碼
Week 5-6  ━━━━━━━━━━━━━━━━━━━━━━━━━━  F6-F9   資料結構
                                           ↓ Milestone: 成績管理
Week 7-8  ━━━━━━━━━━━━━━━━━━━━━━━━━━  F10-F12 函式設計
                                           ↓ Milestone: 工具箱
Week 9-10 ━━━━━━━━━━━━━━━━━━━━━━━━━━  F13-F14 物件導向
                                           ↓ Milestone: 銀行系統
Week 11   ━━━━━━━━━━━━━━━━━━━━━━━━━━  F15-F16 異常處理
                                           ↓ Milestone: 註冊系統
Week 12   ━━━━━━━━━━━━━━━━━━━━━━━━━━  F17-F19 檔案處理
                                           ↓ Milestone: 待辦事項
Week 13-14━━━━━━━━━━━━━━━━━━━━━━━━━━  F20-F22 模組化
                                           ↓ Final Project: 專案重構
```

### 快速路徑（6 週濃縮版）
適合有其他語言經驗的學習者：
```
Week 1: F1-F5   (基礎語法+控制流)
Week 2: F6-F9   (資料結構)
Week 3: F10-F12 (函式)
Week 4: F13-F14 (OOP)
Week 5: F15-F19 (異常+檔案)
Week 6: F20-F22 (模組化) + Final Project
```

---

## 資料夾結構規劃

### 新架構設計原則
1. **模組編號對應 Fundamentals**（F1-F22）
2. **每模組包含完整學習素材**（理論+實作+測驗）
3. **明確區分核心課程與進階內容**
4. **專案導向的學習驗證**

### 完整目錄結構
```
iSpan_python-basic-cookbooks/
│
├── 📁 curriculum/                    # 課程規劃文件
│   ├── curriculum-design.md          # 本文件
│   ├── learning-roadmap.md           # 學習路徑圖
│   ├── competency-checklist.md       # 能力檢核表
│   └── assessment-rubrics.md         # 評量標準
│
├── 📁 fundamentals/                  # 核心課程模組
│   │
│   ├── 📁 F01-variables-and-types/   # 變數與型態
│   │   ├── lecture.ipynb             # 講義
│   │   ├── exercises.ipynb           # 練習題
│   │   ├── solutions.ipynb           # 解答
│   │   └── README.md                 # 模組說明
│   │
│   ├── 📁 F02-operators/             # 運算與表達式
│   ├── 📁 F03-io/                    # 輸入與輸出
│   ├── 📁 F04-conditionals/          # 條件判斷
│   ├── 📁 F05-loops/                 # 迴圈控制
│   ├── 📁 F06-sequences/             # 序列資料 (list, tuple)
│   ├── 📁 F07-dictionaries/          # 映射資料 (dict)
│   ├── 📁 F08-sets/                  # 集合資料 (set)
│   ├── 📁 F09-strings/               # 字串處理
│   ├── 📁 F10-functions/             # 函式設計
│   ├── 📁 F11-scope/                 # 作用域
│   ├── 📁 F12-lambda/                # Lambda 與高階函式
│   ├── 📁 F13-classes/               # 類別與物件
│   ├── 📁 F14-inheritance/           # 封裝與繼承
│   ├── 📁 F15-exceptions/            # 異常處理
│   ├── 📁 F16-debugging/             # 除錯技巧
│   ├── 📁 F17-files/                 # 檔案操作
│   ├── 📁 F18-json/                  # JSON 資料
│   ├── 📁 F19-paths/                 # 路徑與目錄
│   ├── 📁 F20-modules/               # 自訂模組
│   ├── 📁 F21-packages/              # 套件管理
│   └── 📁 F22-style/                 # 程式碼風格
│
├── 📁 milestones/                    # 階段性專案
│   ├── 📁 M01-calculator/            # 簡易計算機
│   ├── 📁 M02-guessing-game/         # 終極密碼
│   ├── 📁 M03-grade-system/          # 成績管理系統
│   ├── 📁 M04-text-toolkit/          # 文字工具箱
│   ├── 📁 M05-bank-account/          # 銀行帳戶系統
│   ├── 📁 M06-user-registration/     # 使用者註冊系統
│   ├── 📁 M07-todo-app/              # 待辦事項管理
│   └── 📁 M08-final-project/         # 期末專案重構
│
├── 📁 advanced/                      # 進階選修內容
│   ├── 📁 A01-comprehensions/        # 進階推導式
│   ├── 📁 A02-decorators/            # 裝飾器
│   ├── 📁 A03-generators/            # 生成器
│   ├── 📁 A04-context-managers/      # 上下文管理器
│   └── 📁 A05-async-basics/          # 非同步入門
│
├── 📁 resources/                     # 學習資源
│   ├── cheatsheets/                  # 速查表
│   │   ├── data-types.md
│   │   ├── string-methods.md
│   │   ├── list-methods.md
│   │   └── built-in-functions.md
│   ├── references/                   # 參考資料
│   │   ├── python-glossary.md        # Python 術語表
│   │   ├── common-errors.md          # 常見錯誤解析
│   │   └── best-practices.md         # 最佳實踐
│   └── tools/                        # 工具安裝指南
│       ├── jupyter-setup.md
│       ├── vscode-setup.md
│       └── git-basics.md
│
├── 📁 legacy/                        # 舊課程內容（保留參考）
│   ├── Module2/
│   ├── Module3/
│   └── ...
│
├── CLAUDE.md                         # Claude Code 指引
├── README.md                         # 專案說明
├── requirements.txt                  # Python 套件需求
└── .gitignore                        # Git 忽略規則
```

### 檔案命名規範

#### Jupyter Notebook
- **講義**: `lecture.ipynb`
- **練習**: `exercises.ipynb`
- **解答**: `solutions.ipynb`
- **補充**: `supplement.ipynb`

#### Python Script
- **範例**: `example_<topic>.py`
- **練習**: `practice_<topic>.py`
- **測驗**: `quiz_<topic>.py`

#### Markdown
- **模組說明**: `README.md`
- **學習筆記**: `notes.md`
- **參考資料**: `reference.md`

### 每個 Fundamental 模組的標準結構
```
F01-variables-and-types/
├── README.md              # 🎯 學習目標、prerequisite、時長估計
├── lecture.ipynb          # 📚 主要講義（理論+範例）
├── exercises.ipynb        # ✏️ 練習題（含提示）
├── solutions.ipynb        # ✅ 完整解答
├── quiz.py                # 📝 自我測驗（選擇題+程式題）
└── assets/                # 🖼️ 圖片、資料檔案（如果需要）
    └── diagram.png
```

---

## 實施建議

### 教學策略
1. **每週 3 小時編排**：
   - 1.5 小時：理論講解 + live coding
   - 1 小時：實作練習
   - 0.5 小時：Q&A + 除錯指導

2. **Milestone 驗收點**：
   - 每完成一個 Milestone 專案，進行 code review
   - 確認學習者能獨立完成，再進入下一階段

3. **漸進式難度**：
   - F1-F5：手把手教學（提供完整範例）
   - F6-F12：半開放練習（提供框架）
   - F13-F22：開放專案（僅提供需求規格）

### 評量方式
- **形成性評量（60%）**：每週練習題完成度
- **總結性評量（40%）**：8 個 Milestone 專案品質
- **加分項**：程式碼風格、創意解法、協助同儕

### First Principles 教學法應用
在每個模組開始時，先問三個問題：
1. **這個概念解決什麼根本問題？**（Why）
2. **它的最小可行實作是什麼？**（What）
3. **如何從基本原理推導出進階用法？**（How）

範例（F10-函式設計）：
- Why: 避免重複程式碼（DRY 原則）
- What: `def add(a, b): return a + b`（最小函式）
- How: 參數 → 預設值 → *args → **kwargs（逐步擴展）

---

## 版本記錄
- **v1.0** (2025-10-05): 初版發布，基於 First Principles 框架設計
- 後續更新請記錄於此

---

## 附錄：與原課程對照表

| 原模組 | 新模組對應 | 調整說明 |
|:------|:----------|:---------|
| Module2 (Data Types) | F1, F6-F9 | 拆分為基本型態與資料結構 |
| Module3 (Flow Control) | F3, F4, F5 | 加入 I/O，獨立條件與迴圈 |
| Module4 (Data Structures) | F6, F7, F8, F9 | 細分各資料結構，增加練習 |
| Module5 (Functions) | F10, F11, F12 | 加強作用域與高階函式 |
| Module6 (OOP) | F13, F14 | 強化繼承與封裝概念 |
| Module7 (Exception) | F15, F16 | 加入除錯技巧模組 |
| Module8 (File Handling) | F17, F18, F19 | 拆分檔案/JSON/路徑操作 |
| Module9 (Modules) | F20, F21, F22 | 加入套件管理與程式碼風格 |

---

**文件維護者**：請在課程實施過程中，持續更新本文件以反映教學經驗與學生回饋。
