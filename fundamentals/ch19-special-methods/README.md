# Chapter 19: 特殊方法與運算子重載 | Special Methods and Operator Overloading

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐⭐☆ (進階) |
| **先備知識** | Chapter 16-18（類別、封裝、繼承） |
| **相關章節** | Chapter 16（類別定義）、Chapter 18（繼承） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的常用特殊方法（magic methods）及其用途
- **定義** 運算子重載（operator overloading）的概念
- **說明** `__str__` 與 `__repr__` 的差異

### 理解面（Comprehension）
- **解釋** 為什麼特殊方法能讓自訂類別像內建型別一樣使用
- **比較** 不同類型的特殊方法（初始化、表示、運算、比較、容器）
- **歸納** 上下文管理器協定（context manager protocol）的運作原理

### 應用面（Application）
- **運用** `__init__`、`__str__`、`__repr__` 實作完整的類別表示
- **實作** 運算子重載（+、-、*、/、==、<等）
- **建立** 可迭代物件與上下文管理器

### 分析面（Analysis）
- **分析** 何時應該/不應該使用運算子重載
- **診斷** 特殊方法實作錯誤導致的問題
- **選擇** 適合特定情境的特殊方法組合

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
特殊方法與運算子重載
├── 基本特殊方法
│   ├── __init__（初始化）
│   ├── __str__（使用者友善的字串表示）
│   ├── __repr__（開發者友善的字串表示）
│   └── __del__（解構器）
│
├── 運算子重載
│   ├── 算術運算子（__add__, __sub__, __mul__, __truediv__）
│   ├── 比較運算子（__eq__, __lt__, __le__, __gt__, __ge__, __ne__）
│   ├── 單元運算子（__neg__, __pos__, __abs__）
│   └── 複合賦值（__iadd__, __isub__ 等）
│
├── 容器特殊方法
│   ├── __len__（長度）
│   ├── __getitem__（索引存取）
│   ├── __setitem__（索引賦值）
│   ├── __delitem__（刪除項目）
│   ├── __contains__（成員測試）
│   └── __iter__（迭代器）
│
├── 進階特殊方法
│   ├── __call__（可呼叫物件）
│   ├── __enter__ / __exit__（上下文管理器）
│   ├── __getattr__ / __setattr__（屬性存取）
│   └── __hash__（可雜湊物件）
│
└── 型態轉換
    ├── __int__, __float__, __str__, __bool__
    └── __bytes__, __complex__
```

### First Principles 解析

#### 為什麼需要特殊方法？
**根本問題**：如何讓自訂類別的物件像內建型別一樣自然地使用？

**情境說明**：
```python
# 內建型別可以這樣用
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b          # 串接
print(len(a))      # 取得長度
print(a[0])        # 索引存取

# 我們希望自訂類別也能這樣用
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2       # 向量相加（需要 __add__）
print(len(v1))     # 取得維度（需要 __len__）
print(v1[0])       # 取得分量（需要 __getitem__）
```

**最小實作**：
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """定義 + 運算子的行為"""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        """定義 print() 的輸出格式"""
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

**推導過程**：
1. Python 看到 `v1 + v2` → 尋找 `v1.__add__(v2)` 方法
2. 如果找到 → 執行該方法，返回結果
3. 如果找不到 → TypeError: unsupported operand type(s)

#### 為什麼 `__str__` 和 `__repr__` 要分開？
**根本問題**：物件需要兩種不同的字串表示方式

**設計理念**：
- `__str__`：給終端使用者看的（易讀、美觀）
- `__repr__`：給開發者看的（完整、可重建）

**實例說明**：
```python
from datetime import datetime

now = datetime(2025, 10, 5, 14, 30)

# str() 或 print() → 呼叫 __str__
print(str(now))     # "2025-10-05 14:30:00"（易讀）

# repr() 或直接輸入變數 → 呼叫 __repr__
print(repr(now))    # "datetime.datetime(2025, 10, 5, 14, 30)"（可重建）

# 黃金法則：eval(repr(obj)) == obj
eval(repr(now)) == now  # True
```

#### 為什麼需要上下文管理器？
**根本問題**：資源需要正確的取得與釋放（即使發生例外）

**傳統做法的問題**：
```python
# 容易忘記關閉
f = open("data.txt")
data = f.read()
# 如果這裡發生例外，檔案不會關閉！
f.close()
```

**上下文管理器的解決方案**：
```python
# 保證一定會關閉
with open("data.txt") as f:
    data = f.read()
# 無論是否發生例外，__exit__ 都會執行
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 特殊方法 | Magic Method / Dunder Method | 以雙底線開頭和結尾的方法（如 `__init__`） |
| 運算子重載 | Operator Overloading | 為自訂類別定義運算子（+、-、==等）的行為 |
| 雙底線方法 | Dunder Method | Double UNDERscore 的簡稱 |
| 字串表示 | String Representation | 物件轉換為字串的方式 |
| 上下文管理器 | Context Manager | 支援 `with` 敘述的物件（有 `__enter__` 和 `__exit__`） |
| 序列協定 | Sequence Protocol | 實作 `__len__` 和 `__getitem__` 的物件 |
| 可呼叫物件 | Callable Object | 實作 `__call__` 的物件，可像函式一樣呼叫 |
| 可迭代物件 | Iterable | 實作 `__iter__` 的物件，可用於 for 迴圈 |
| 可雜湊物件 | Hashable | 實作 `__hash__` 和 `__eq__` 的物件，可作為字典鍵 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（7 個範例） | 90 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（4 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（8 題） | 40 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 120 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（15 選擇 + 5 程式） | 30 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解特殊方法的目的
2. **上課**（130 min）：
   - 講義學習（90 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（40 min）：完成 `03-practice.ipynb`
4. **課後複習**（120 min）：
   - 完成習題（90 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（30 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能實作 `__init__`、`__str__`、`__repr__` 三個基本方法
- [ ] 能解釋 `__str__` 與 `__repr__` 的差異與使用情境
- [ ] 能使用 `__len__` 和 `__getitem__` 實作序列協定
- [ ] 能重載基本算術運算子（+、-、*、/）

### 進階能力
- [ ] 能重載比較運算子（==、<、>等）
- [ ] 能實作 `__call__` 建立可呼叫物件
- [ ] 能使用 `__enter__` 和 `__exit__` 建立上下文管理器
- [ ] 能實作完整的容器類別（支援索引、長度、迭代）

### 應用能力
- [ ] 能判斷何時應該/不應該使用運算子重載
- [ ] 能為複數運算、向量運算等數學類別設計完整的特殊方法
- [ ] 能設計資源管理類別（檔案、資料庫連線等）
- [ ] 能除錯特殊方法相關的錯誤

---

## 📝 理論重點（Key Theoretical Points）

### 1. 常用特殊方法總覽

#### 基本方法
| 方法 | 呼叫時機 | 用途 |
|:-----|:---------|:-----|
| `__init__(self, ...)` | 建立物件時 | 初始化屬性 |
| `__str__(self)` | `str(obj)` 或 `print(obj)` | 使用者友善的字串 |
| `__repr__(self)` | `repr(obj)` 或互動式環境 | 開發者友善的字串 |
| `__del__(self)` | 物件被銷毀時 | 清理資源（少用） |

#### 算術運算子
| 方法 | 運算子 | 範例 |
|:-----|:-------|:-----|
| `__add__(self, other)` | `+` | `obj1 + obj2` |
| `__sub__(self, other)` | `-` | `obj1 - obj2` |
| `__mul__(self, other)` | `*` | `obj1 * obj2` |
| `__truediv__(self, other)` | `/` | `obj1 / obj2` |
| `__floordiv__(self, other)` | `//` | `obj1 // obj2` |
| `__mod__(self, other)` | `%` | `obj1 % obj2` |
| `__pow__(self, other)` | `**` | `obj1 ** obj2` |

#### 比較運算子
| 方法 | 運算子 | 範例 |
|:-----|:-------|:-----|
| `__eq__(self, other)` | `==` | `obj1 == obj2` |
| `__ne__(self, other)` | `!=` | `obj1 != obj2` |
| `__lt__(self, other)` | `<` | `obj1 < obj2` |
| `__le__(self, other)` | `<=` | `obj1 <= obj2` |
| `__gt__(self, other)` | `>` | `obj1 > obj2` |
| `__ge__(self, other)` | `>=` | `obj1 >= obj2` |

#### 容器方法
| 方法 | 呼叫時機 | 用途 |
|:-----|:---------|:-----|
| `__len__(self)` | `len(obj)` | 返回容器大小 |
| `__getitem__(self, key)` | `obj[key]` | 索引存取 |
| `__setitem__(self, key, value)` | `obj[key] = value` | 索引賦值 |
| `__delitem__(self, key)` | `del obj[key]` | 刪除項目 |
| `__contains__(self, item)` | `item in obj` | 成員測試 |
| `__iter__(self)` | `for x in obj` | 返回迭代器 |

### 2. `__str__` vs `__repr__` 的最佳實踐

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """使用者友善：簡潔、易讀"""
        return f"{self.name}, {self.age} 歲"

    def __repr__(self):
        """開發者友善：完整、可重建"""
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 25)
print(str(p))   # Alice, 25 歲
print(repr(p))  # Person(name='Alice', age=25)

# 在互動式環境直接輸入變數 → 呼叫 __repr__
>>> p
Person(name='Alice', age=25)
```

**設計原則**：
- 如果只實作一個，實作 `__repr__`（Python 會在找不到 `__str__` 時使用 `__repr__`）
- `__repr__` 應該盡可能讓 `eval(repr(obj))` 能重建物件
- `__str__` 可以更自由，專注於可讀性

### 3. 運算子重載的最佳實踐

✅ **適合使用運算子重載的情境**：
- 數學物件（向量、矩陣、複數）
- 自訂容器（串接、合併）
- 明確且直覺的運算（+ 表示相加、< 表示小於）

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """向量相加：直覺且符合數學定義"""
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # 清楚明瞭
```

❌ **不適合使用運算子重載的情境**：
- 運算意義不明確（+ 代表什麼？）
- 容易混淆（< 是比較日期還是字母順序？）
- 違反直覺（`person1 + person2` 是什麼意思？）

```python
# 不良範例
class Person:
    def __add__(self, other):
        """這是什麼意思？結婚？生小孩？合併朋友？"""
        return ???  # 意義不明確，不應使用 +
```

### 4. 上下文管理器協定

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """進入 with 區塊時執行：取得資源"""
        print(f"連接到 {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection  # 返回值賦給 as 後的變數

    def __exit__(self, exc_type, exc_value, traceback):
        """離開 with 區塊時執行：釋放資源"""
        print(f"關閉連接到 {self.db_name}")
        self.connection = None
        # 返回 True 會抑制例外，返回 False 或 None 會重新拋出例外
        return False

# 使用上下文管理器
with DatabaseConnection("mydb") as conn:
    print(f"使用 {conn}")
    # 即使這裡發生例外，__exit__ 也會執行
# 離開 with 區塊後，__exit__ 已執行
```

**`__exit__` 參數說明**：
- `exc_type`：例外類型（如果沒有例外則為 None）
- `exc_value`：例外實例
- `traceback`：追蹤物件

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從內建型別的行為出發**：
   - 先展示 `[1, 2] + [3, 4]`、`len("hello")`
   - 再說明這些都是特殊方法在背後運作
   - 使用 `dir(list)` 展示所有特殊方法

2. **強調 Pythonic 的設計哲學**：
   - "讓自訂類別看起來像內建類別"
   - "顯式優於隱式"（不要濫用運算子重載）
   - "簡單優於複雜"（只實作真正需要的方法）

3. **實際演示除錯過程**：
   ```python
   # 故意忘記實作 __str__
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

   p = Point(1, 2)
   print(p)  # <__main__.Point object at 0x...>（不友善）
   ```

4. **比較不同實作方式**：
   - 使用 vs 不使用運算子重載
   - 使用 vs 不使用上下文管理器
   - 讓學生體會特殊方法帶來的便利性

### 常見學生困難點

#### 困難點 1：`__str__` 和 `__repr__` 的混淆

**症狀**：不知道該實作哪一個，或兩者內容相同

**解決方法**：
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """給讀者看：書名 - 作者"""
        return f"{self.title} - {self.author}"

    def __repr__(self):
        """給程式設計師看：完整重建資訊"""
        return f"Book('{self.title}', '{self.author}')"

b = Book("Python 入門", "張三")

# 使用者情境
print(f"推薦書籍：{b}")  # 推薦書籍：Python 入門 - 張三

# 除錯情境
books = [b]
print(books)  # [Book('Python 入門', '張三')]
```

**記憶口訣**：
- `__str__`：Str = Show（展示給使用者）
- `__repr__`：Repr = Reproduce（重建給開發者）

#### 困難點 2：運算子重載的返回值錯誤

**症狀**：忘記返回新物件，或返回 None

```python
# 錯誤示範
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x  # 錯誤：修改了原物件
        self.y += other.y
        # 錯誤：沒有返回值

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2  # result 是 None！
```

**正確做法**：
```python
class Vector:
    def __add__(self, other):
        # 返回新的 Vector 物件，不修改原物件
        return Vector(self.x + other.x, self.y + other.y)
```

**原則**：算術運算子（+、-、*、/）應該返回新物件，不修改原物件（不可變性）

#### 困難點 3：上下文管理器的 `__exit__` 返回值

**症狀**：不理解返回 True/False 的差異

```python
class MyContext:
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"發生例外：{exc_value}")
            return True  # 吞掉例外，with 區塊後的程式繼續執行
            # return False  # 重新拋出例外，程式中斷

with MyContext():
    raise ValueError("測試例外")
# 如果返回 True：這行會執行
# 如果返回 False：這行不會執行，程式崩潰
```

**建議**：
- 預設返回 `False` 或 `None`（讓例外正常傳播）
- 只有在明確要抑制例外時才返回 `True`

#### 困難點 4：過度使用運算子重載

**症狀**：為每個類別都實作大量運算子，造成意義不明

```python
# 不良範例
class User:
    def __add__(self, other):
        """兩個使用者相加是什麼意思？"""
        return ???

    def __sub__(self, other):
        """使用者相減？？？"""
        return ???
```

**建議**：
- 只重載意義明確的運算子
- 當運算意義不明確時，使用命名方法（如 `merge_with()`）
- 參考 Python 的 Zen："Explicit is better than implicit"

---

## 💡 學習技巧（Learning Strategies）

### 記憶技巧

**特殊方法分類記憶**：
1. **生命週期**：`__init__`（出生）、`__del__`（死亡）
2. **表示法**：`__str__`（外表）、`__repr__`（DNA）
3. **運算**：`__add__`（加）、`__sub__`（減）...（數學老師）
4. **比較**：`__eq__`（等於）、`__lt__`（小於）...（裁判）
5. **容器**：`__len__`（大小）、`__getitem__`（取出）...（盒子）
6. **進階**：`__call__`（可呼叫）、`__enter__`/`__exit__`（門衛）

### 實作練習建議

1. **先從數學物件開始**：
   - 實作一個 `Fraction` 類別（分數運算）
   - 實作一個 `Complex` 類別（複數運算）
   - 這些運算意義明確，容易理解

2. **實作自訂容器**：
   - 實作一個只能存正整數的列表
   - 實作一個有大小限制的堆疊
   - 練習 `__len__`、`__getitem__`、`__setitem__`

3. **建立資源管理器**：
   - 實作一個檔案操作上下文管理器
   - 實作一個計時器上下文管理器（測量 with 區塊執行時間）
   - 練習 `__enter__` 和 `__exit__`

### 除錯技巧

```python
# 使用 dir() 查看所有特殊方法
print([m for m in dir(list) if m.startswith('__')])

# 檢查特殊方法是否存在
class MyClass:
    pass

print(hasattr(MyClass, '__add__'))  # False

# 查看方法解析順序
print(MyClass.__mro__)
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Data Model - Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#context-manager-types)
- [contextlib Module](https://docs.python.org/3/library/contextlib.html)

### 推薦閱讀
- Ramalho, L. (2022). *Fluent Python* (2nd ed.), Chapter 1, 11, 13, 15
- Beazley, D., & Jones, B. K. (2013). *Python Cookbook* (3rd ed.), Chapter 8
- Phillips, D. (2018). *Python 3 Object-Oriented Programming* (3rd ed.), Chapter 3

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化特殊方法呼叫過程
- [Real Python: Operator and Function Overloading](https://realpython.com/operator-function-overloading/)

### 延伸主題（進階學習）
- 描述器協定（Descriptor Protocol）：`__get__`、`__set__`、`__delete__`
- 元類別（Metaclass）：`__new__`、`__init__` 在類別層級
- 抽象基底類別（ABC）：`collections.abc` 模組
- `functools.total_ordering` 裝飾器（自動產生比較方法）

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候應該實作 `__repr__` 而不是 `__str__`？**
A: 當你只想實作一個時，選擇 `__repr__`。Python 會在找不到 `__str__` 時自動使用 `__repr__`。`__repr__` 的目標是提供完整資訊，理想上能讓 `eval(repr(obj))` 重建物件。

**Q2: 為什麼 `a += b` 有時會修改 `a`，有時不會？**
A: 取決於是否實作 `__iadd__`（in-place add）。如果有實作，`+=` 會修改原物件並返回 self；如果沒實作，Python 會使用 `__add__` 並重新賦值（`a = a + b`），這會建立新物件。

```python
# 列表有 __iadd__（會修改原物件）
a = [1, 2]
b = [3, 4]
id_before = id(a)
a += b
id_after = id(a)
print(id_before == id_after)  # True（同一個物件）

# 元組沒有 __iadd__（會建立新物件）
a = (1, 2)
b = (3, 4)
id_before = id(a)
a += b
id_after = id(a)
print(id_before == id_after)  # False（不同物件）
```

**Q3: `__eq__` 和 `__hash__` 有什麼關係？**
A: 如果你重寫了 `__eq__`，也應該重寫 `__hash__`（或將其設為 None）。Python 的規則是：`a == b` 為 True 時，`hash(a) == hash(b)` 也必須為 True。

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# 現在 Point 可以作為字典鍵或放入集合
points = {Point(1, 2), Point(3, 4)}
```

**Q4: 如何實作鏈式比較（如 `a < b < c`）？**
A: Python 會自動將 `a < b < c` 轉換為 `a < b and b < c`。你只需要實作 `__lt__` 即可。如果想實作所有比較方法，可使用 `functools.total_ordering` 裝飾器，只需實作 `__eq__` 和一個排序方法（如 `__lt__`），其他會自動產生。

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    # __le__, __gt__, __ge__ 會自動產生！
```

**Q5: 上下文管理器一定要用類別實作嗎？**
A: 不一定。可以使用 `contextlib.contextmanager` 裝飾器將生成器函式轉換為上下文管理器：

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("進入")
    yield "資源"  # __enter__ 返回的值
    print("離開")

with my_context() as resource:
    print(f"使用 {resource}")
# 輸出：
# 進入
# 使用 資源
# 離開
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 16（類別定義）**：必須熟悉類別的基本語法
- **Chapter 17（封裝）**：理解屬性存取機制
- **Chapter 18（繼承）**：特殊方法的繼承與覆寫

### 後續章節
- **Chapter 20（例外處理）**：上下文管理器與例外的互動
- **Chapter 27（模組）**：標準函式庫中的特殊方法應用（如 `collections.abc`）

### 對應的 Milestone 專案
- **Milestone 5: 銀行系統**（會用到運算子重載進行帳戶操作）
- **Milestone 7: Todo App**（會用到上下文管理器管理檔案）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能實作一個完整的數學類別（如向量、矩陣、分數）
- ✅ 能建立自訂的上下文管理器管理資源
- ✅ 能解釋何時應該/不應該使用運算子重載

---

**學習提醒**：特殊方法是 Python 進階功能的核心。掌握它們能讓你的程式碼更 Pythonic、更優雅。但記住：不要濫用運算子重載，保持程式碼的清晰性與可讀性！
