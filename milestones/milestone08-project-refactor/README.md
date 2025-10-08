# Milestone 08: 專案模組化重構 | Project Refactoring

> **整合章節 | Integrated Chapters**: Ch27-30 (Part VIII: Engineering Practices)
> **預估時間 | Estimated Time**: 8-12 小時
> **難度 | Difficulty**: ★★★★☆ (Advanced)
> **類型 | Type**: Refactoring & Best Practices

---

## 📋 專案資訊 | Project Information

### 整合知識點 | Knowledge Integration

本專案整合以下章節的工程實務技能：

| 章節 | 核心技能 | 應用重點 |
|:-----|:---------|:---------|
| **Ch27: 模組與套件** | 模組化設計 | 將單一檔案拆解為多個模組，設計套件結構 |
| **Ch28: 套件管理** | 虛擬環境與依賴管理 | 建立虛擬環境，管理 requirements.txt |
| **Ch29: 程式碼風格** | PEP 8 與文件規範 | 重構程式碼符合 PEP 8，撰寫完整文件 |
| **Ch30: 版本控制** | Git 基本操作 | 使用 Git 追蹤重構過程，撰寫標準 commit |

### 專案目標 | Project Objectives

選擇 **M01-M07 任一專案**進行模組化重構，將原本的單一檔案程式轉換為符合工程標準的專案結構：

1. **模組化設計** - 將功能拆解為獨立模組
2. **套件組織** - 建立清晰的檔案與目錄結構
3. **程式碼品質** - 套用 PEP 8 規範與型別提示
4. **完整文件** - 撰寫 README、docstring、註解
5. **版本控制** - 使用 Git 管理重構流程

---

## 🎯 學習成果 | Learning Outcomes

完成本專案後，你將能夠：

### 知識層次 (Knowledge)
- [ ] 理解模組化設計的原則與優勢
- [ ] 掌握 Python 套件結構的標準慣例
- [ ] 熟悉 PEP 8 程式碼風格規範
- [ ] 了解專案文件的重要性與撰寫方式

### 技能層次 (Skills)
- [ ] 能將單一檔案程式拆解為多個模組
- [ ] 能設計清晰的模組介面與職責分離
- [ ] 能使用 Git 管理開發流程
- [ ] 能撰寫專業的 README 與 docstring

### 態度層次 (Attitude)
- [ ] 養成模組化思考的習慣
- [ ] 重視程式碼可讀性與可維護性
- [ ] 建立專業的開發流程意識
- [ ] 培養持續重構與改進的態度

---

## 📝 重構任務說明 | Refactoring Tasks

### 任務概述

從 **M01-M07** 中選擇一個已完成的專案，進行以下重構：

```
原始狀態：
solution.ipynb (單一檔案，200-400 行)

↓ 重構後 ↓

專案結構：
my_project/
├── README.md              # 專案說明文件
├── requirements.txt       # 依賴清單
├── .gitignore            # Git 忽略檔案
├── src/                  # 原始碼目錄
│   ├── __init__.py
│   ├── main.py           # 主程式入口
│   ├── core.py           # 核心邏輯
│   ├── ui.py             # 使用者界面
│   └── utils.py          # 工具函式
└── tests/                # 測試目錄（選做）
    └── test_core.py
```

### 重構目標

#### 基本需求 (70 分)

1. **模組化拆解 (25 分)**
   - 將程式拆解為至少 3 個模組
   - 每個模組職責明確（單一職責原則）
   - 模組間透過明確介面溝通

2. **程式碼品質 (20 分)**
   - 符合 PEP 8 命名規範
   - 使用 type hints 標註函式參數與回傳值
   - 移除冗餘程式碼與重複邏輯

3. **文件撰寫 (15 分)**
   - README.md 包含專案說明、安裝步驟、使用方式
   - 所有函式與類別都有 docstring
   - 關鍵邏輯有註解說明

4. **版本控制 (10 分)**
   - 使用 Git 管理重構過程
   - 至少 5 個有意義的 commit
   - 撰寫清楚的 commit message

#### 進階需求 (30 分)

5. **進階模組設計 (10 分)**
   - 使用 `__init__.py` 簡化匯入
   - 設計清晰的公開 API（`__all__`）
   - 適當使用私有函式（`_function`）

6. **錯誤處理強化 (10 分)**
   - 自訂例外類別
   - 完整的輸入驗證
   - 友善的錯誤訊息

7. **專案管理 (10 分)**
   - 建立虛擬環境
   - requirements.txt 列出所有依賴
   - .gitignore 正確設定
   - 程式可透過 `python -m` 執行

---

## 🛠️ 重構步驟 | Refactoring Steps

### 階段一：規劃與分析 (2-3 小時)

#### Step 1: 選擇專案並分析結構

```python
# 選擇建議：
# - M01-M03: 適合初次重構（結構簡單）
# - M04-M06: 適合一般練習（複雜度中等）
# - M07: 適合進階挑戰（功能完整）
```

**任務清單**：
- [ ] 選擇要重構的專案
- [ ] 閱讀原始程式碼，理解所有功能
- [ ] 識別可獨立的功能模組
- [ ] 繪製模組關係圖（手繪或工具）

#### Step 2: 設計模組架構

**模組拆解原則**：

1. **核心邏輯模組 (core.py)**
   - 商業邏輯與資料處理
   - 不依賴使用者輸入輸出
   - 可獨立測試

2. **使用者界面模組 (ui.py)**
   - 所有 `input()` 與 `print()` 操作
   - 選單顯示與互動流程
   - 錯誤訊息顯示

3. **資料管理模組 (data.py / storage.py)**
   - 檔案讀寫操作
   - 資料驗證與轉換
   - JSON/CSV 處理

4. **工具模組 (utils.py / helpers.py)**
   - 通用輔助函式
   - 常數定義
   - 格式化工具

5. **主程式模組 (main.py)**
   - 程式入口點
   - 整合各模組功能
   - 主流程控制

**範例：M07 Todo App 模組設計**

```
todo_app/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式，整合所有功能
│   ├── task.py           # Task 類別定義
│   ├── task_manager.py   # TaskManager 類別，管理任務清單
│   ├── storage.py        # 檔案讀寫功能
│   ├── ui.py             # 選單與使用者互動
│   └── utils.py          # 日期驗證、格式化等工具
└── data/
    └── tasks.json        # 資料檔案
```

#### Step 3: 建立專案目錄結構

```bash
# 建立目錄
mkdir my_project
cd my_project
mkdir src data tests

# 建立基本檔案
touch README.md requirements.txt .gitignore
touch src/__init__.py src/main.py src/core.py src/ui.py src/utils.py

# 初始化 Git
git init
git add .
git commit -m "chore: 初始化專案結構"
```

---

### 階段二：重構實作 (4-6 小時)

#### Step 4: 拆解模組（由下而上）

**建議順序**：

1. **先拆解工具模組 (utils.py)**
   - 獨立的輔助函式
   - 不依賴其他模組
   - 容易測試

2. **再拆解核心模組 (core.py)**
   - 商業邏輯
   - 資料結構與演算法
   - 可能依賴 utils

3. **最後拆解 UI 模組 (ui.py)**
   - 使用者互動
   - 依賴 core 模組
   - 負責顯示與輸入

4. **整合主程式 (main.py)**
   - 匯入所有模組
   - 協調模組間呼叫
   - 控制主流程

**重構檢核清單**：
- [ ] 每個函式長度 < 50 行
- [ ] 每個模組 < 300 行
- [ ] 函式命名清楚表達功能
- [ ] 移除所有 magic numbers
- [ ] 複雜邏輯有註解說明

#### Step 5: 套用 PEP 8 規範

**命名規範**：

```python
# 模組名稱：小寫，底線分隔
# task_manager.py ✓
# TaskManager.py ✗

# 類別名稱：大駝峰
class TaskManager:  # ✓
class task_manager:  # ✗

# 函式/變數：小寫，底線分隔
def add_task(task_name: str) -> bool:  # ✓
def AddTask(taskName):  # ✗

# 常數：大寫，底線分隔
MAX_TASKS = 100  # ✓
maxTasks = 100   # ✗

# 私有成員：前綴一個底線
def _validate_input(data):  # 私有函式
    pass

class User:
    def __init__(self):
        self._password = ""  # 私有屬性
```

**格式規範**：

```python
# 每行最多 79 字元
# 運算子前後有空格
result = (value1 + value2) * factor  # ✓
result=(value1+value2)*factor        # ✗

# 逗號後有空格
my_list = [1, 2, 3, 4]  # ✓
my_list = [1,2,3,4]     # ✗

# 函式間空兩行
def function1():
    pass


def function2():  # 空兩行
    pass

# 類別內方法間空一行
class MyClass:
    def method1(self):
        pass

    def method2(self):  # 空一行
        pass
```

**使用工具自動檢查**：

```bash
# 安裝檢查工具
pip install flake8 black

# 檢查風格問題
flake8 src/

# 自動格式化
black src/
```

#### Step 6: 加入型別提示 (Type Hints)

```python
# 基本型別提示
def calculate_total(price: float, quantity: int) -> float:
    """計算總價

    Args:
        price: 單價
        quantity: 數量

    Returns:
        總價
    """
    return price * quantity

# 複雜型別提示
from typing import List, Dict, Optional, Union

def process_tasks(
    tasks: List[Dict[str, str]],
    filter_status: Optional[str] = None
) -> List[Dict[str, str]]:
    """處理任務清單

    Args:
        tasks: 任務清單
        filter_status: 篩選狀態（可選）

    Returns:
        處理後的任務清單
    """
    if filter_status:
        return [t for t in tasks if t['status'] == filter_status]
    return tasks

# 類別屬性型別提示
class Task:
    """任務類別"""

    def __init__(
        self,
        title: str,
        priority: int = 1,
        completed: bool = False
    ) -> None:
        self.title: str = title
        self.priority: int = priority
        self.completed: bool = completed
```

#### Step 7: 撰寫完整文件

**README.md 範本**：

```markdown
# 專案名稱

簡短描述專案功能（1-2 句）

## 功能特色

- 功能 1
- 功能 2
- 功能 3

## 安裝步驟

1. 建立虛擬環境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

```bash
python -m src.main
```

或

```bash
cd src
python main.py
```

## 專案結構

```
project/
├── src/           # 原始碼
├── data/          # 資料檔案
└── tests/         # 測試檔案
```

## 授權

本專案為教學用途
```

**Docstring 範本（Google Style）**：

```python
def complex_function(
    param1: str,
    param2: int,
    param3: Optional[List[str]] = None
) -> Dict[str, any]:
    """函式簡短描述（一行）

    可選的詳細說明（多行）。解釋函式的目的、
    演算法、特殊行為等。

    Args:
        param1: 參數 1 的說明
        param2: 參數 2 的說明
        param3: 參數 3 的說明（可選）

    Returns:
        回傳值的說明，包含資料結構

    Raises:
        ValueError: 何時會拋出此例外
        TypeError: 何時會拋出此例外

    Examples:
        >>> result = complex_function("test", 42)
        >>> print(result)
        {'status': 'success'}
    """
    if param2 < 0:
        raise ValueError("param2 必須為正整數")

    # 實作...
    return {'status': 'success'}
```

---

### 階段三：測試與優化 (2-3 小時)

#### Step 8: 功能測試

**手動測試清單**：

```python
# 測試檢核表
# [ ] 所有原始功能正常運作
# [ ] 邊界條件測試（空輸入、極端值）
# [ ] 錯誤處理測試（無效輸入）
# [ ] 檔案讀寫測試（不存在的檔案、權限問題）
# [ ] 程式可正常啟動與結束
```

**進階：撰寫單元測試（選做）**

```python
# tests/test_core.py
import unittest
from src.core import calculate_total, validate_input

class TestCore(unittest.TestCase):
    """核心功能測試"""

    def test_calculate_total(self):
        """測試總價計算"""
        self.assertEqual(calculate_total(10.5, 2), 21.0)
        self.assertEqual(calculate_total(5, 0), 0)

    def test_validate_input(self):
        """測試輸入驗證"""
        self.assertTrue(validate_input("valid"))
        self.assertFalse(validate_input(""))

if __name__ == '__main__':
    unittest.main()
```

#### Step 9: Git 版本控制

**Commit 策略**：

```bash
# 1. 初始提交
git add .
git commit -m "chore: 初始化專案結構"

# 2. 拆解模組（每個模組一個 commit）
git add src/utils.py
git commit -m "refactor: 拆解工具模組"

git add src/core.py
git commit -m "refactor: 拆解核心邏輯模組"

git add src/ui.py
git commit -m "refactor: 拆解使用者介面模組"

# 3. 套用 PEP 8
git add src/
git commit -m "style: 套用 PEP 8 規範與型別提示"

# 4. 撰寫文件
git add README.md src/
git commit -m "docs: 新增 README 與 docstring"

# 5. 最終測試
git add .
git commit -m "test: 完成功能測試與修正"
```

**Commit Message 規範**：

```
<type>: <subject>

<body>（可選）

<footer>（可選）
```

**Type 類型**：
- `feat`: 新功能
- `fix`: 修正 bug
- `refactor`: 重構（不改變功能）
- `style`: 程式碼風格調整
- `docs`: 文件更新
- `test`: 測試相關
- `chore`: 雜項（建置、設定等）

#### Step 10: 最終檢查

**完成檢核清單**：

```markdown
## 模組化設計
- [ ] 至少 3 個獨立模組
- [ ] 每個模組職責明確
- [ ] 模組間耦合度低
- [ ] 使用 __init__.py 管理匯入

## 程式碼品質
- [ ] 符合 PEP 8 命名規範
- [ ] 所有函式都有型別提示
- [ ] 沒有 magic numbers
- [ ] 沒有重複程式碼
- [ ] 通過 flake8 檢查（或僅少量警告）

## 文件撰寫
- [ ] README.md 包含安裝與使用說明
- [ ] 所有函式都有 docstring
- [ ] 複雜邏輯有註解
- [ ] requirements.txt 列出依賴

## 版本控制
- [ ] 初始化 Git repository
- [ ] 至少 5 個有意義的 commit
- [ ] Commit message 清楚明確
- [ ] .gitignore 正確設定

## 功能測試
- [ ] 所有原始功能正常
- [ ] 邊界條件測試通過
- [ ] 錯誤處理正常運作
- [ ] 程式可正常啟動與結束

## 專案管理
- [ ] 建立虛擬環境
- [ ] 可透過 python -m src.main 執行
- [ ] 資料檔案組織清楚
- [ ] 無敏感資訊（密碼、金鑰等）
```

---

## 📊 評分標準 | Grading Rubric

### 基本需求 (70 分)

| 評分項目 | 配分 | 評分標準 |
|:---------|:-----|:---------|
| **模組化拆解** | 25 | ★★★★★ (25): 拆解為 4+ 模組，職責明確，介面清晰<br>★★★★☆ (20): 拆解為 3 模組，職責大致明確<br>★★★☆☆ (15): 拆解為 2 模組，部分職責不清<br>★★☆☆☆ (10): 僅形式上拆解，未真正模組化<br>★☆☆☆☆ (5): 幾乎未拆解 |
| **程式碼品質** | 20 | ★★★★★ (20): 完全符合 PEP 8，型別提示完整<br>★★★★☆ (16): 大部分符合 PEP 8，有型別提示<br>★★★☆☆ (12): 部分符合 PEP 8，型別提示不完整<br>★★☆☆☆ (8): 命名規範不一致<br>★☆☆☆☆ (4): 程式碼品質不佳 |
| **文件撰寫** | 15 | ★★★★★ (15): README 完整，docstring 詳細<br>★★★★☆ (12): README 完整，docstring 簡略<br>★★★☆☆ (9): README 簡略，部分 docstring<br>★★☆☆☆ (6): 文件不完整<br>★☆☆☆☆ (3): 幾乎沒有文件 |
| **版本控制** | 10 | ★★★★★ (10): 5+ commits，訊息清楚，.gitignore 正確<br>★★★★☆ (8): 5+ commits，訊息尚可<br>★★★☆☆ (6): 3-4 commits<br>★★☆☆☆ (4): 僅 1-2 commits<br>★☆☆☆☆ (2): 未使用 Git |

### 進階需求 (30 分)

| 評分項目 | 配分 | 評分標準 |
|:---------|:-----|:---------|
| **進階模組設計** | 10 | 使用 `__init__.py`、`__all__`、私有函式設計 |
| **錯誤處理強化** | 10 | 自訂例外、完整驗證、友善錯誤訊息 |
| **專案管理** | 10 | 虛擬環境、requirements.txt、可透過 python -m 執行 |

### 額外加分項目 (最多 +10 分)

- **單元測試** (+5): 撰寫測試案例，覆蓋核心功能
- **CLI 介面優化** (+3): 使用 argparse 提供命令列參數
- **日誌系統** (+2): 使用 logging 模組記錄操作
- **程式碼分析報告** (+2): 附上 flake8/pylint 分析結果
- **效能優化** (+3): 改善演算法效率，附上效能比較

---

## 🎯 各專案重構提示 | Refactoring Tips by Project

### M01: 簡易計算機 (Simple Calculator)

**原始結構**：
- 單一檔案，約 100-150 行
- 基本四則運算
- 簡單的輸入輸出

**建議模組拆解**：

```
calculator/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── operations.py     # 運算函式 (add, subtract, multiply, divide)
│   ├── ui.py             # 使用者界面與選單
│   └── utils.py          # 輸入驗證、格式化
└── README.md
```

**重構重點**：
1. 將四則運算拆解為獨立函式
2. 加入型別提示與 docstring
3. 強化除以零的錯誤處理
4. 新增運算歷史記錄（進階）

---

### M02: 終極密碼遊戲 (Number Guessing Game)

**原始結構**：
- 單一檔案，約 150-200 行
- 遊戲邏輯、計分、輸入驗證混合

**建議模組拆解**：

```
guessing_game/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── game.py           # Game 類別（遊戲邏輯）
│   ├── player.py         # Player 類別（玩家資訊）
│   ├── ui.py             # 顯示與輸入
│   └── utils.py          # 輸入驗證、隨機數產生
└── README.md
```

**重構重點**：
1. 將遊戲狀態封裝為 `Game` 類別
2. 分離遊戲邏輯與使用者界面
3. 加入難度等級設定（進階）
4. 記錄最佳成績（進階）

---

### M03: 學生成績管理系統 (Grade Management System)

**建議模組拆解**：

```
grade_system/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── student.py        # Student 類別
│   ├── grade_manager.py  # GradeManager 類別（CRUD）
│   ├── statistics.py     # 統計分析函式
│   ├── storage.py        # 檔案讀寫
│   ├── ui.py             # 選單與顯示
│   └── utils.py          # 驗證、格式化
├── data/
│   └── students.json
└── README.md
```

**重構重點**：
1. `Student` 類別封裝學生資料
2. `GradeManager` 類別管理學生清單
3. 分離統計運算與顯示邏輯
4. 檔案讀寫獨立為 `storage` 模組

---

### M04: 文字處理工具箱 (Text Toolkit)

**建議模組拆解**：

```
text_toolkit/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── analyzers.py      # 分析函式（字數、詞頻等）
│   ├── transformers.py   # 轉換函式（大小寫、反轉等）
│   ├── validators.py     # 驗證函式（email、密碼等）
│   ├── ui.py             # 使用者界面
│   └── utils.py          # 輔助函式
└── README.md
```

**重構重點**：
1. 將分析、轉換、驗證功能分離
2. 使用高階函式處理文字處理
3. 加入正則表達式驗證（進階）

---

### M05: 銀行帳戶系統 (Banking System)

**建議模組拆解**：

```
banking_system/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── account.py        # Account 類別
│   ├── savings_account.py  # SavingsAccount 類別（繼承）
│   ├── checking_account.py # CheckingAccount 類別（繼承）
│   ├── bank.py           # Bank 類別（管理多個帳戶）
│   ├── transaction.py    # Transaction 類別（交易記錄）
│   ├── storage.py        # 檔案讀寫
│   ├── ui.py             # 使用者界面
│   └── exceptions.py     # 自訂例外（InsufficientFunds 等）
└── README.md
```

**重構重點**：
1. 類別繼承結構清晰
2. 封裝帳戶餘額（私有屬性）
3. 自訂例外處理
4. 交易記錄功能（進階）

---

### M06: 使用者註冊系統 (User Registration System)

**建議模組拆解**：

```
registration_system/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── user.py           # User 類別
│   ├── auth.py           # 驗證邏輯（登入、註冊）
│   ├── validators.py     # 輸入驗證（email、密碼強度）
│   ├── storage.py        # 檔案讀寫
│   ├── encryption.py     # 密碼加密（進階）
│   ├── ui.py             # 使用者界面
│   └── exceptions.py     # 自訂例外
└── README.md
```

**重構重點**：
1. 密碼不以明文儲存（使用 hashlib）
2. Email 格式驗證（正則表達式）
3. 登入失敗次數限制（進階）
4. Session 管理（進階）

---

### M07: 待辦事項管理 (Todo App) ⭐ 推薦

**建議模組拆解**：

```
todo_app/
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程式
│   ├── task.py           # Task 類別
│   ├── task_manager.py   # TaskManager 類別
│   ├── storage.py        # JSON 檔案讀寫
│   ├── ui.py             # 選單與顯示
│   ├── utils.py          # 日期驗證、格式化
│   └── exceptions.py     # 自訂例外
├── data/
│   └── tasks.json
└── README.md
```

**重構重點**：
1. `Task` 類別完整封裝任務資料
2. `TaskManager` 類別負責任務清單管理
3. 檔案讀寫獨立為 `storage` 模組
4. 日期處理與驗證獨立為 `utils` 模組
5. 自訂例外處理（TaskNotFound、InvalidDate 等）

**詳細範例請參考 `solution.ipynb`**

---

## 🎓 教師指引 | Teaching Guidelines

### 教學目標

1. **培養模組化思維**：讓學生理解「職責分離」的重要性
2. **建立工程意識**：養成重視程式碼品質的習慣
3. **學習專業流程**：體驗真實專案的開發流程

### 建議教學流程

#### 課堂示範 (2 小時)

1. **示範重構過程** (60 分鐘)
   - 選擇 M01 或 M02 作為範例
   - 即時展示從單一檔案到模組化的過程
   - 強調「為什麼這樣拆解」的思考過程

2. **程式碼風格示範** (30 分鐘)
   - 展示 PEP 8 常見違規與修正
   - 示範如何使用 flake8 與 black
   - 說明 type hints 的寫法與好處

3. **Git 操作示範** (30 分鐘)
   - 示範基本 Git 工作流程
   - 說明 commit message 規範
   - 展示 .gitignore 的設定

### 評分重點

1. **模組化設計 (40%)**
   - 是否真正做到職責分離
   - 模組介面是否清晰
   - 模組間耦合度是否低

2. **程式碼品質 (30%)**
   - 命名是否清楚
   - 是否符合 PEP 8
   - 型別提示是否完整

3. **文件品質 (20%)**
   - README 是否清楚
   - Docstring 是否完整
   - 註解是否恰當

4. **版本控制 (10%)**
   - Commit 是否有意義
   - Commit message 是否清楚
   - .gitignore 是否正確

### 常見問題與解答

**Q1: 學生不知道如何拆解模組**

解答：
- 提供「模組拆解檢核表」
- 從「功能」角度思考（輸入、處理、輸出）
- 從「資料」角度思考（資料結構、資料操作）
- 提供範例專案結構參考

**Q2: 學生覺得 PEP 8 太繁瑣**

解答：
- 說明業界標準的重要性
- 展示不遵守 PEP 8 的程式碼有多難讀
- 使用自動格式化工具（black）降低負擔
- 只要求核心規範（命名、縮排、空格）

**Q3: 學生不會寫 docstring**

解答：
- 提供 docstring 範本
- 說明 Google Style 的格式
- 示範簡單函式的 docstring
- 使用 IDE 外掛自動產生骨架

**Q4: 學生不熟悉 Git 操作**

解答：
- 提供 Git 操作流程圖
- 只要求基本指令（add, commit, status）
- 提供 commit message 範本
- 允許使用 GUI 工具（GitKraken、SourceTree）

---

## 🚀 延伸挑戰 | Extension Challenges

完成基本需求後，可嘗試：

1. **效能優化** - 使用 cProfile 分析效能瓶頸，改善演算法
2. **CLI 介面** - 使用 argparse 提供命令列參數
3. **日誌系統** - 使用 logging 模組記錄操作
4. **設定檔管理** - 使用 JSON/YAML 儲存設定
5. **持續整合** - 設定 GitHub Actions 自動檢查

---

## 📚 參考資源 | References

- [PEP 8 官方文件](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Git 官方教學](https://git-scm.com/book/zh-tw/v2)
- [Python Modules 官方文件](https://docs.python.org/3/tutorial/modules.html)

---

## ✅ 提交清單 | Submission Checklist

```markdown
## 必要檔案
- [ ] README.md（包含安裝與使用說明）
- [ ] requirements.txt（列出所有依賴）
- [ ] .gitignore（排除不必要的檔案）
- [ ] src/ 目錄（包含所有原始碼）
- [ ] 至少 3 個模組檔案

## 程式碼品質
- [ ] 所有檔案符合 PEP 8 命名規範
- [ ] 所有函式都有型別提示
- [ ] 所有函式都有 docstring
- [ ] 通過 flake8 檢查（或僅少量警告）

## 功能測試
- [ ] 所有原始功能正常運作
- [ ] 邊界條件測試通過
- [ ] 錯誤處理正常運作

## 版本控制
- [ ] 初始化 Git repository
- [ ] 至少 5 個有意義的 commit
- [ ] Commit message 清楚明確
```

---

🎓 **恭喜你完成 Python 基礎課程所有專案！** 🚀
