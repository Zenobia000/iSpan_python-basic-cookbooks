# Chapter 8: 序列資料：元組與字串 | Tuples and Strings

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3-4 小時 |
| **難度等級** | ⭐⭐⭐ (中階) |
| **先備知識** | Ch01-Ch07 (變數、運算子、條件、迴圈、列表) |
| **學習目標** | 掌握 Python 兩大不可變序列的核心概念與應用 |
| **實作重點** | 元組解包、字串方法、文字處理、資料驗證 |

---

## 學習目標 | Learning Objectives

### 知識層次 (Knowledge)
- [ ] 理解元組（Tuple）的定義與特性
- [ ] 理解字串（String）作為不可變序列的本質
- [ ] 認識可變（Mutable）vs 不可變（Immutable）的差異
- [ ] 了解元組與列表的使用場景差異
- [ ] 掌握字串的 30+ 個常用方法

### 理解層次 (Comprehension)
- [ ] 解釋為什麼需要不可變資料型態
- [ ] 分析元組解包（Unpacking）的運作原理
- [ ] 比較字串操作與列表操作的異同
- [ ] 說明字串的不可變性對程式設計的影響

### 應用層次 (Application)
- [ ] 使用元組解包簡化程式碼
- [ ] 運用字串方法進行文字處理
- [ ] 實作字串切片技巧
- [ ] 應用 f-string 進行格式化輸出
- [ ] 實現字串與列表的互轉

### 分析層次 (Analysis)
- [ ] 設計文字分析工具（字數統計、字元頻率）
- [ ] 開發資料驗證器（密碼、Email、電話）
- [ ] 建構文字清理工具（去空白、標準化）

---

## 核心概念 | Key Concepts

### 概念地圖

```
序列資料 (Sequence)
│
├── 可變序列 (Mutable)
│   └── 列表 (List) → [1, 2, 3]
│
└── 不可變序列 (Immutable)
    ├── 元組 (Tuple) → (1, 2, 3)
    │   ├── 特性：一旦創建無法修改
    │   ├── 應用：多回傳值、字典鍵、資料保護
    │   └── 操作：解包、索引、切片
    │
    └── 字串 (String) → "hello"
        ├── 本質：字元的不可變序列
        ├── 索引與切片：s[0], s[1:3]
        ├── 字串方法：30+ 個常用方法
        │   ├── 大小寫：upper(), lower(), title()
        │   ├── 搜尋：find(), index(), startswith()
        │   ├── 分割：split(), join(), strip()
        │   ├── 替換：replace(), format()
        │   └── 判斷：isdigit(), isalpha(), isupper()
        └── 格式化：f-string, format(), %
```

### First Principles 分析

#### 1️⃣ 為什麼需要不可變資料型態？

**問題根源**：
```python
# 可變資料的風險
data = [1, 2, 3]
backup = data        # 這只是參考，不是複製！
data.append(4)       # backup 也改變了！
print(backup)        # [1, 2, 3, 4]
```

**解決方案**：
```python
# 不可變資料的安全性
original = (1, 2, 3)
reference = original
# original.append(4)  # 錯誤！無法修改
# 要改變必須創建新物件
modified = original + (4,)
print(original)      # (1, 2, 3) - 保持不變
```

**核心原理**：
- **資料完整性**：防止意外修改
- **多執行緒安全**：不用擔心資料競爭
- **可作為字典鍵**：因為雜湊值不變
- **效能優化**：記憶體共享更安全

#### 2️⃣ 元組的本質：不可變的列表

**最小實作**：
```python
# Python 內部如何儲存元組（概念示意）
class SimpleTuple:
    def __init__(self, *items):
        self._items = list(items)  # 內部使用列表存儲
        self._frozen = True        # 標記為凍結

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        raise TypeError("tuple 不支援修改")
```

**設計哲學**：
- 語法簡潔：`(1, 2, 3)` vs `[1, 2, 3]`
- 語意明確：用 `()` 表示「固定、不變」
- 解包語法：`x, y = (1, 2)` 自然直觀

#### 3️⃣ 字串的本質：字元序列

**Python 如何表示字串**：
```python
# 字串 = 不可變的字元序列
s = "Python"
# 等價於 s = ('P', 'y', 't', 'h', 'o', 'n') 的概念

# 支援序列操作
print(s[0])        # 'P' - 索引
print(s[1:4])      # 'yth' - 切片
print(len(s))      # 6 - 長度
print('y' in s)    # True - 成員檢查
```

**不可變性的影響**：
```python
# 字串操作不改變原字串，而是返回新字串
text = "hello"
result = text.upper()  # 返回新字串 "HELLO"
print(text)            # "hello" - 原字串不變
```

#### 4️⃣ 字串方法的設計原則

**方法分類**：
```python
# 1. 轉換類（返回新字串）
"hello".upper()         # "HELLO"
"  hi  ".strip()        # "hi"

# 2. 搜尋類（返回索引或布林值）
"hello".find('l')       # 2
"hello".startswith('h') # True

# 3. 判斷類（返回布林值）
"123".isdigit()         # True
"abc".isalpha()         # True

# 4. 分割/組合類
"a,b,c".split(',')      # ['a', 'b', 'c']
'-'.join(['a', 'b'])    # 'a-b'
```

---

## 課程教材 | Course Materials

### 檔案說明表

| 檔案名稱 | 類型 | 說明 | 預估時間 |
|:---------|:-----|:-----|:---------|
| `README.md` | 文件 | 本章節完整指南 | 15 分鐘 |
| `01-lecture.ipynb` | 講義 | 12 個範例教學 | 90 分鐘 |
| `02-worked-examples.ipynb` | 詳解 | 5 個完整解題示範 | 45 分鐘 |
| `03-practice.ipynb` | 練習 | 15 題課堂練習 | 30 分鐘 |
| `04-exercises.ipynb` | 作業 | 20 題課後習題 | 60 分鐘 |
| `05-solutions.ipynb` | 解答 | 完整解答與說明 | 30 分鐘 |
| `quiz.ipynb` | 測驗 | 25 題自我評量 | 20 分鐘 |

**總學習時數**：約 3.5-4 小時

---

## 能力檢核清單 | Competency Checklist

### Level 1: 基礎能力 ✓

**元組基礎**：
- [ ] 能創建單元素、空元組、多元素元組
- [ ] 能使用索引存取元組元素
- [ ] 能使用 `len()`, `max()`, `min()` 等函式
- [ ] 理解元組的不可變性

**字串基礎**：
- [ ] 能使用索引與切片操作字串
- [ ] 能使用 `+`, `*` 運算子
- [ ] 能使用 `len()` 計算字串長度
- [ ] 能使用 `in` 檢查子字串

### Level 2: 進階能力 ⚡

**元組解包**：
- [ ] 能使用基本解包 `x, y = (1, 2)`
- [ ] 能使用星號解包 `first, *rest = (1, 2, 3)`
- [ ] 能在函式中使用多回傳值
- [ ] 能使用元組作為字典的鍵

**字串方法**：
- [ ] 熟練使用 10+ 個字串方法
- [ ] 能使用 `split()` 與 `join()` 處理 CSV 資料
- [ ] 能使用 `strip()`, `lstrip()`, `rstrip()` 清理資料
- [ ] 能使用 `replace()` 進行文字替換
- [ ] 能使用 f-string 格式化輸出

### Level 3: 應用能力 🚀

**實務應用**：
- [ ] 能開發文字清理工具
- [ ] 能實作資料驗證（Email、密碼、電話）
- [ ] 能進行文字分析（字數、詞頻統計）
- [ ] 能處理多行文字資料
- [ ] 能正確選擇元組或列表

---

## 教學建議 | Teaching Tips

### 授課要點

#### 1. 強調不可變性的重要性（20 分鐘）
```python
# 用實例展示可變 vs 不可變
# 列表（可變）
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)  # [1, 2, 3, 4] - 意外改變！

# 元組（不可變）
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple1.append(4)  # 錯誤！
tuple1 = tuple1 + (4,)  # 必須創建新物件
print(tuple2)  # (1, 2, 3) - 保持原樣
```

#### 2. 元組解包的實用性（30 分鐘）
```python
# 傳統寫法
def get_user_info():
    return ["張三", 25, "taipei@example.com"]

result = get_user_info()
name = result[0]
age = result[1]
email = result[2]

# 元組解包寫法
def get_user_info():
    return "張三", 25, "taipei@example.com"  # 自動打包為元組

name, age, email = get_user_info()  # 一行搞定！
```

#### 3. 字串方法速查表（30 分鐘）

**大小寫轉換**：
```python
s = "Python Programming"
s.upper()      # "PYTHON PROGRAMMING"
s.lower()      # "python programming"
s.title()      # "Python Programming"
s.capitalize() # "Python programming"
s.swapcase()   # "pYTHON pROGRAMMING"
```

**搜尋與判斷**：
```python
s = "hello world"
s.find('world')      # 6 (找到回傳索引)
s.find('xyz')        # -1 (找不到)
s.index('world')     # 6 (找到回傳索引)
# s.index('xyz')     # ValueError (找不到拋出錯誤)
s.startswith('he')   # True
s.endswith('ld')     # True
'wor' in s           # True
```

**分割與合併**：
```python
# 分割
"a,b,c".split(',')           # ['a', 'b', 'c']
"a b c".split()              # ['a', 'b', 'c'] (預設分割空白)
"apple".split('p')           # ['a', '', 'le']

# 合併
'-'.join(['a', 'b', 'c'])    # 'a-b-c'
''.join(['h', 'i'])          # 'hi'
```

**清理空白**：
```python
s = "  hello  "
s.strip()   # "hello" (兩端)
s.lstrip()  # "hello  " (左端)
s.rstrip()  # "  hello" (右端)

# 也可清理其他字元
"***hello***".strip('*')  # "hello"
```

#### 4. 實務案例教學（40 分鐘）

**案例 1：CSV 資料解析**
```python
data = "張三,25,taipei@example.com"
name, age, email = data.split(',')
age = int(age)
print(f"姓名：{name}, 年齡：{age}, Email：{email}")
```

**案例 2：密碼驗證**
```python
def validate_password(password):
    """密碼必須：8+ 字元、含大小寫、含數字"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
```

**案例 3：文字分析**
```python
text = "Python is awesome. Python is easy."
words = text.lower().replace('.', '').split()
word_count = len(words)
unique_words = len(set(words))
print(f"總字數：{word_count}, 不重複字數：{unique_words}")
```

### 常見學習困難

#### 困難 1：單元素元組的語法
```python
# ❌ 錯誤：這不是元組，是整數
not_tuple = (1)
print(type(not_tuple))  # <class 'int'>

# ✅ 正確：需要加逗號
is_tuple = (1,)
print(type(is_tuple))   # <class 'tuple'>

# 空元組不需要逗號
empty = ()
```

#### 困難 2：字串的不可變性
```python
# ❌ 錯誤：無法修改字串
s = "hello"
# s[0] = 'H'  # TypeError

# ✅ 正確：創建新字串
s = 'H' + s[1:]  # "Hello"
```

#### 困難 3：find() vs index() 的差異
```python
s = "hello"

# find() - 找不到返回 -1
print(s.find('z'))  # -1

# index() - 找不到拋出錯誤
# print(s.index('z'))  # ValueError

# 建議使用 find() 較安全
if s.find('z') != -1:
    print("找到了")
else:
    print("找不到")
```

#### 困難 4：split() 與 join() 的對稱性
```python
# split() - 字串 → 列表
text = "a-b-c"
parts = text.split('-')  # ['a', 'b', 'c']

# join() - 列表 → 字串 (注意語法！)
result = '-'.join(parts)  # 'a-b-c'

# ❌ 常見錯誤
# parts.join('-')  # 錯誤！列表沒有 join 方法

# ✅ 正確記憶法：「分隔符號.join(列表)」
```

### 教學節奏建議

| 時段 | 內容 | 時間 |
|:-----|:-----|:-----|
| 第 1 節 | 元組基礎、解包、應用 | 50 分鐘 |
| 第 2 節 | 字串基礎、索引切片 | 50 分鐘 |
| 第 3 節 | 字串方法（大小寫、搜尋、分割） | 60 分鐘 |
| 第 4 節 | 綜合應用、實務案例 | 50 分鐘 |

---

## 延伸閱讀 | Further Reading

### 官方文件
- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

### 推薦文章
- [Understanding Python's Immutability](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)
- [String Formatting in Python](https://realpython.com/python-string-formatting/)
- [Python String Methods Cheat Sheet](https://www.datacamp.com/cheat-sheet/python-string-methods-cheat-sheet)

### 實務應用
- 文字探勘（Text Mining）
- 自然語言處理（NLP）基礎
- 資料清理（Data Cleaning）
- CSV/JSON 資料解析

### 進階主題
- 正規表達式（Regular Expressions）
- Unicode 與編碼
- 字串效能優化（`str.join()` vs `+`）
- `collections.namedtuple` 進階應用

---

## 下一章預告

**Chapter 9: 字典與集合 | Dictionaries and Sets**
- 鍵值對資料結構
- 字典的 CRUD 操作
- 集合的數學運算
- 字典與 JSON

---

*本章節遵循 First Principles 教學法，從基礎概念到實務應用，循序漸進建立完整知識體系。*
