# Chapter 29: 程式碼風格與文件 | Code Style and Documentation

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Chapter 12 (函式), Chapter 16 (類別), Chapter 27 (模組) |
| **相關章節** | Chapter 27 (模組與套件), Chapter 28 (套件管理) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠:

### 知識面（Knowledge）
- **列出** PEP 8 的主要規範條目
- **定義** docstring, type hints, code smell 的概念
- **說明** 程式碼風格對維護性的影響

### 理解面（Comprehension）
- **解釋** 為什麼需要統一的程式碼風格
- **比較** 好壞程式碼範例的差異
- **歸納** 命名規範的原則（snake_case, PascalCase）

### 應用面（Application）
- **運用** PEP 8 規範撰寫符合標準的程式碼
- **實作** 函式、類別、模組的 docstring
- **解決** 常見的程式碼風格問題

### 分析面（Analysis）
- **分析** 現有程式碼的風格問題
- **診斷** 使用 flake8, black 等工具檢查程式碼
- **選擇** 適合團隊的程式碼風格指南

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
程式碼風格與文件
├── PEP 8 風格指南
│   ├── 縮排與空格
│   ├── 行長度限制（79 字元）
│   ├── 空行規範
│   └── 命名規範
│
├── Docstring 文件字串
│   ├── 單行 docstring
│   ├── 多行 docstring
│   ├── Google Style
│   └── NumPy/Sphinx Style
│
├── Type Hints 型態提示
│   ├── 函式參數型態
│   ├── 回傳值型態
│   ├── 變數型態標註
│   └── Optional, Union, List 等
│
├── 命名規範
│   ├── 變數：snake_case
│   ├── 常數：UPPER_CASE
│   ├── 類別：PascalCase
│   └── 私有：_leading_underscore
│
└── 程式碼品質工具
    ├── flake8（語法檢查）
    ├── black（自動格式化）
    ├── pylint（程式碼評分）
    └── mypy（型態檢查）
```

### First Principles 解析

#### 為什麼需要程式碼風格？
**根本問題**: 程式碼是給人讀的,不是給機器讀的

**最小實作**:
```python
# 難以閱讀的程式碼
def f(x,y):z=x+y;return z

# 易於閱讀的程式碼
def add_numbers(first_number, second_number):
    """計算兩個數字的和"""
    result = first_number + second_number
    return result
```

**推導過程**:
1. 程式需要維護 → 需要被理解
2. 理解需要一致性 → 需要風格規範
3. 規範需要執行 → 需要自動化工具

#### 為什麼需要文件？
**根本問題**: 程式碼無法完整表達「為什麼」和「如何使用」

**實例說明**:
```python
# 沒有文件
def calc(n):
    return n * 0.08

# 有文件
def calculate_sales_tax(price):
    """計算商品的銷售稅（稅率 8%）

    Args:
        price (float): 商品原價

    Returns:
        float: 應繳稅額
    """
    TAX_RATE = 0.08
    return price * TAX_RATE
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 程式碼風格 | Code Style | 程式碼的格式與命名慣例 |
| 風格指南 | Style Guide | 程式碼風格的規範文件（如 PEP 8） |
| 文件字串 | Docstring | 函式/類別/模組的說明文字 |
| 型態提示 | Type Hints | 標註變數/參數的型態（PEP 484） |
| 程式碼異味 | Code Smell | 暗示程式碼品質問題的特徵 |
| 重構 | Refactoring | 改善程式碼結構但不改變功能 |
| Linter | Linter | 檢查程式碼風格與錯誤的工具 |
| Formatter | Formatter | 自動格式化程式碼的工具 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（5 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（3-5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（10 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 20 分鐘 | 學習驗收 |

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後,請確認您能夠:

### 基本能力
- [ ] 能遵循 PEP 8 撰寫 Python 程式碼
- [ ] 能為函式撰寫 docstring
- [ ] 能使用正確的命名規範（snake_case, PascalCase）
- [ ] 能撰寫有意義的註解

### 進階能力
- [ ] 能使用 type hints 標註型態
- [ ] 能撰寫符合 Google/NumPy 風格的文件
- [ ] 能使用 flake8 檢查程式碼
- [ ] 能使用 black 自動格式化程式碼

### 應用能力
- [ ] 能重構不符合規範的舊程式碼
- [ ] 能識別並修正 code smells
- [ ] 能建立專案的風格指南文件
- [ ] 能在團隊中推廣程式碼品質文化

---

## 📝 理論重點（Key Theoretical Points）

### 1. PEP 8 核心規範

#### 縮排與空格
```python
# ✅ 正確：使用 4 個空格縮排
def my_function():
    if True:
        print("Hello")

# ❌ 錯誤：使用 tab 或 2 個空格（不一致）
def my_function():
  if True:
        print("Hello")  # 混用空格數量
```

#### 行長度
```python
# ✅ 正確：每行不超過 79 字元
result = some_function(
    first_argument,
    second_argument,
    third_argument
)

# ❌ 錯誤：單行過長
result = some_function(first_argument, second_argument, third_argument, fourth_argument, fifth_argument)
```

#### 空行規範
```python
# ✅ 正確：函式間 2 個空行,方法間 1 個空行
def function_one():
    pass


def function_two():  # 2 個空行
    pass


class MyClass:
    def method_one(self):
        pass

    def method_two(self):  # 1 個空行
        pass
```

### 2. 命名規範

| 類型 | 規範 | 範例 |
|:-----|:-----|:-----|
| 模組 | lowercase | `my_module.py` |
| 套件 | lowercase | `mypackage/` |
| 類別 | PascalCase | `class MyClass:` |
| 函式 | snake_case | `def my_function():` |
| 變數 | snake_case | `my_variable = 10` |
| 常數 | UPPER_CASE | `MAX_SIZE = 100` |
| 私有 | _leading | `_private_var` |
| 魔法方法 | __double__ | `__init__` |

### 3. Docstring 規範

#### 單行 docstring
```python
def square(x):
    """計算平方"""
    return x ** 2
```

#### 多行 docstring (Google Style)
```python
def calculate_area(length, width):
    """計算長方形面積

    Args:
        length (float): 長度（公尺）
        width (float): 寬度（公尺）

    Returns:
        float: 面積（平方公尺）

    Raises:
        ValueError: 當長度或寬度為負數時

    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("長度和寬度必須為正數")
    return length * width
```

### 4. Type Hints

```python
from typing import List, Dict, Optional, Union

# 函式型態提示
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 容器型態
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Optional（可能為 None）
def find_user(user_id: int) -> Optional[Dict[str, str]]:
    # 返回用戶資料或 None
    pass

# Union（多種型態）
def process_data(data: Union[str, int, List]) -> str:
    return str(data)

# 變數型態標註
age: int = 25
names: List[str] = ["Alice", "Bob"]
config: Dict[str, int] = {"timeout": 30}
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **對比教學法**:
   - 展示好壞程式碼對照
   - 讓學生體會可讀性差異

2. **實際工具演示**:
   - 現場使用 flake8 檢查程式碼
   - 展示 black 自動格式化效果

3. **團隊協作情境**:
   - 強調風格統一對團隊的重要性
   - 分享業界實際案例

### 常見學生困難點

#### 困難點 1: 不理解為何需要風格規範
**症狀**: 「程式能跑就好,何必在意格式？」

**解決方法**:
- 展示維護舊程式碼的困難
- 讓學生閱讀他人不規範的程式碼
- 強調專業開發的標準

#### 困難點 2: docstring 寫什麼內容
**症狀**: 只寫「這是一個函式」等無意義內容

**解決方法**:
```python
# ❌ 無意義 docstring
def add(a, b):
    """加法函式"""  # 函式名稱已經說明了
    return a + b

# ✅ 有價值的 docstring
def calculate_discount(price, discount_rate):
    """計算折扣後的價格

    Args:
        price (float): 原價（必須 > 0）
        discount_rate (float): 折扣率（0.0-1.0）

    Returns:
        float: 折扣後價格

    Example:
        >>> calculate_discount(100, 0.2)  # 8 折
        80.0
    """
    return price * (1 - discount_rate)
```

#### 困難點 3: type hints 語法陌生
**症狀**: 不知道如何標註複雜型態

**解決方法**:
- 從簡單型態開始（int, str, float）
- 逐步引入 List, Dict, Optional
- 使用 mypy 驗證型態正確性

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **PEP 8 口訣**: 4 空格縮排,79 字元行,2 行分函式
- **命名口訣**: 變數蛇形爬,類別駱駝峰,常數全大寫
- **Docstring 口訣**: 寫什麼(What)、為什麼(Why)、如何用(How)

### 實作練習建議
1. **重構練習**: 找一段舊程式碼,按 PEP 8 重構
2. **文件練習**: 為之前章節的函式補充 docstring
3. **工具練習**: 安裝並使用 flake8, black

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)

### 推薦閱讀
- *Clean Code* by Robert C. Martin
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)

### 工具資源
- [Black](https://black.readthedocs.io/) - 自動格式化工具
- [Flake8](https://flake8.pycqa.org/) - 風格檢查工具
- [Pylint](https://pylint.org/) - 程式碼分析工具
- [mypy](http://mypy-lang.org/) - 靜態型態檢查

### 延伸主題（進階學習）
- 程式碼複雜度分析（Cyclomatic Complexity）
- 重構模式（Refactoring Patterns）
- 測試驅動開發（TDD）中的文件
- API 文件自動生成（Sphinx, MkDocs）

---

## ❓ 常見問題（FAQ）

**Q1: PEP 8 是強制的嗎？**
A: 不是法律強制,但是 Python 社群的強烈建議。大型專案和開源專案通常會嚴格遵循。

**Q2: type hints 會影響程式執行嗎？**
A: 不會！Type hints 只是註解,不影響執行效能。但可以用 mypy 等工具進行靜態檢查。

**Q3: 何時該寫註解,何時該寫 docstring？**
A:
- **Docstring**: 函式/類別/模組的用途與使用方式
- **註解**: 解釋複雜演算法、商業邏輯、待辦事項（TODO）

**Q4: 團隊成員不願遵循風格規範怎麼辦？**
A: 1) 使用 pre-commit hook 自動檢查 2) 引入 CI/CD 自動化檢查 3) 展示規範帶來的好處

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12（函式）**: 為函式撰寫 docstring
- **Chapter 16（類別）**: 為類別撰寫文件
- **Chapter 27（模組）**: 為模組撰寫文件

### 後續章節
- **Chapter 30（版本控制）**: 結合 Git 進行程式碼審查

### 對應的 Milestone 專案
- **Milestone 8: 專案重構**（結合 Ch27-30 的知識）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布,基於教科書標準結構

---

## 🎯 成功標準（Success Criteria）

完成本章學習後,您應該能夠:
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能用 flake8 檢查並修正程式碼風格問題
- ✅ 能為自己的專案撰寫完整的文件

---

**學習提醒**: 程式碼風格不是追求完美,而是追求一致性！寫程式碼就像寫文章,好的格式讓讀者更容易理解。
