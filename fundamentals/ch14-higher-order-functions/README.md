# Chapter 14: 高階函式與 Lambda | Higher-Order Functions and Lambda

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐⭐☆ (4/5) |
| **先備知識** | Chapter 12（函式設計基礎）、Chapter 13（作用域與生命週期） |
| **相關章節** | Chapter 15（遞迴）、Chapter 20（例外處理）、Chapter 16-17（類別與物件） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠:

### 知識面（Knowledge）
- **列出** 高階函式的定義與特徵（接受函式為參數、回傳函式）
- **定義** Lambda 表達式的語法與限制
- **說明** Python 內建高階函式：map()、filter()、reduce()、sorted()

### 理解面（Comprehension）
- **解釋** 為什麼需要高階函式（抽象化、代碼複用、函式式編程）
- **比較** Lambda vs def、函式式 vs 命令式編程風格
- **歸納** 裝飾器（decorator）的基本原理與作用

### 應用面（Application）
- **運用** map()、filter()、reduce() 處理資料轉換與過濾
- **實作** 使用 Lambda 簡化代碼（排序、事件處理）
- **解決** 使用裝飾器擴展函式功能（計時、日誌、驗證）

### 分析面（Analysis）
- **分析** 何時使用 Lambda vs 完整函式定義
- **診斷** 高階函式的性能考量（vs 列表推導式）
- **選擇** 適合使用函式式編程的場景

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
高階函式與 Lambda
├── 第一級函式（First-Class Functions）
│   ├── 函式可賦值給變數
│   ├── 函式可作為參數傳遞
│   ├── 函式可作為回傳值
│   └── 函式可存入資料結構
│
├── Lambda 表達式
│   ├── 語法：lambda 參數: 運算式
│   ├── 匿名函式（無需 def）
│   ├── 單一運算式（無 return）
│   └── 使用場景與限制
│
├── 內建高階函式
│   ├── map(func, iterable)
│   │   ├── 對每個元素應用函式
│   │   ├── 回傳迭代器
│   │   └── vs 列表推導式
│   ├── filter(func, iterable)
│   │   ├── 過濾符合條件的元素
│   │   ├── 回傳迭代器
│   │   └── vs 列表推導式 + if
│   ├── reduce(func, iterable)
│   │   ├── 累積運算（需導入 functools）
│   │   ├── 二元函式逐對運算
│   │   └── 常見用途（求和、求積）
│   └── sorted(iterable, key=func)
│       ├── key 參數接受函式
│       ├── 自訂排序規則
│       └── Lambda 的典型應用
│
├── 函式回傳函式
│   ├── 工廠函式（Factory Function）
│   ├── 函式組合（Function Composition）
│   ├── 部分應用（Partial Application）
│   └── 閉包的應用
│
├── 裝飾器基礎（Decorator Basics）
│   ├── 裝飾器是高階函式
│   ├── @syntax 語法糖
│   ├── 常見裝飾器應用
│   │   ├── 計時器（timing）
│   │   ├── 日誌（logging）
│   │   └── 驗證（validation）
│   └── functools.wraps
│
└── 函式式編程概念
    ├── 純函式（Pure Function）
    ├── 不可變性（Immutability）
    ├── 函式組合
    └── 聲明式 vs 命令式
```

### First Principles 解析

#### 為什麼需要高階函式？

**根本問題**：如何抽象化「行為模式」而非「資料」？

**問題演示**：
```python
# 情境：我們有三個類似的操作
numbers = [1, 2, 3, 4, 5]

# 操作 1：所有數字平方
squares = []
for n in numbers:
    squares.append(n ** 2)

# 操作 2：所有數字加 10
plus_ten = []
for n in numbers:
    plus_ten.append(n + 10)

# 操作 3：所有數字轉字串
strings = []
for n in numbers:
    strings.append(str(n))

# 問題：
# 1. 代碼重複：三個迴圈結構完全相同
# 2. 難以維護：改變迭代邏輯需要修改三處
# 3. 無法抽象：「對每個元素應用操作」這個模式無法提取
```

**高階函式的解決方案**：
```python
# 使用 map（高階函式）
numbers = [1, 2, 3, 4, 5]

# 將「操作」參數化
squares = list(map(lambda x: x ** 2, numbers))
plus_ten = list(map(lambda x: x + 10, numbers))
strings = list(map(str, numbers))

# 優點：
# 1. 消除重複：迭代邏輯只寫一次（在 map 內部）
# 2. 易於維護：改變迭代方式只需修改 map 的實作
# 3. 抽象化行為：「對每個元素應用函式」成為可複用的模式
```

**推導過程**：
1. **發現重複模式**：許多操作都是「對每個元素做某事」
2. **抽象化需求**：需要將「某事」參數化
3. **函式作為數據**：如果函式可以像數據一樣傳遞，就能參數化行為
4. **高階函式誕生**：接受函式為參數的函式 → map, filter, reduce

#### 為什麼需要 Lambda 表達式？

**根本問題**：如何簡潔地表達「一次性使用」的小函式？

**問題演示**：
```python
# 情境：按名字長度排序
names = ["Alice", "Bob", "Charlotte", "David"]

# 方法 1：定義完整函式（繁瑣）
def get_length(name):
    return len(name)

sorted_names = sorted(names, key=get_length)

# 問題：
# 1. 冗長：為了一次性使用定義完整函式
# 2. 命名困難：需要為簡單操作想名字
# 3. 命名空間污染：get_length 函式可能不會再用到
```

**Lambda 的解決方案**：
```python
# 使用 Lambda（匿名函式）
sorted_names = sorted(names, key=lambda name: len(name))

# 優點：
# 1. 簡潔：一行表達完整邏輯
# 2. 無需命名：不用為簡單操作想名字
# 3. 就地定義：函式定義在使用的地方，清晰易讀
```

**Lambda 的限制**：
```python
# ❌ Lambda 不能包含多條語句
# lambda x: print(x); return x * 2  # SyntaxError

# ❌ Lambda 不能包含賦值語句
# lambda x: y = x * 2  # SyntaxError

# ❌ Lambda 不能包含複雜邏輯
# 如果需要 if-elif-else、迴圈等，請使用 def

# ✅ 何時使用 Lambda：
# 1. 單一運算式
# 2. 一次性使用
# 3. 作為高階函式的參數
```

#### 為什麼需要裝飾器？

**根本問題**：如何在不修改函式代碼的情況下，擴展函式功能？

**問題演示**：
```python
# 情境：需要為多個函式添加計時功能
import time

def slow_function():
    # 需要計時
    start = time.time()
    time.sleep(1)
    result = "done"
    end = time.time()
    print(f"Execution time: {end - start:.2f}s")
    return result

def another_function():
    # 又需要計時（代碼重複）
    start = time.time()
    time.sleep(0.5)
    result = "finished"
    end = time.time()
    print(f"Execution time: {end - start:.2f}s")
    return result

# 問題：
# 1. 代碼重複：每個函式都要寫計時邏輯
# 2. 關注點混雜：業務邏輯與計時邏輯混在一起
# 3. 難以維護：修改計時方式需要改所有函式
```

**裝飾器的解決方案**：
```python
import time
from functools import wraps

# 定義裝飾器（高階函式）
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

# 使用裝飾器
@timer
def slow_function():
    time.sleep(1)
    return "done"

@timer
def another_function():
    time.sleep(0.5)
    return "finished"

# 優點：
# 1. 關注點分離：業務邏輯與計時邏輯分開
# 2. 代碼複用：計時邏輯只寫一次
# 3. 易於維護：修改計時方式只需改裝飾器
# 4. 清晰易讀：@timer 明確表達「這個函式被計時」
```

**裝飾器本質**：
```python
# @decorator 語法糖等價於：
@timer
def func():
    pass

# 等價於：
def func():
    pass
func = timer(func)  # 用裝飾器包裝原函式
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 高階函式 | Higher-Order Function | 接受函式為參數或回傳函式的函式 |
| 第一級函式 | First-Class Function | 函式可像一般值一樣被傳遞、賦值、回傳 |
| Lambda 表達式 | Lambda Expression | 匿名函式，使用 `lambda` 關鍵字定義 |
| 匿名函式 | Anonymous Function | 沒有名稱的函式 |
| 裝飾器 | Decorator | 修改或擴展函式行為的高階函式 |
| 映射 | Map | 對序列每個元素應用函式 |
| 過濾 | Filter | 篩選序列中符合條件的元素 |
| 歸約 | Reduce | 將序列歸約為單一值 |
| 函式組合 | Function Composition | 將多個函式串接成一個新函式 |
| 部分應用 | Partial Application | 固定函式的部分參數 |
| 柯里化 | Currying | 將多參數函式轉換為單參數函式鏈 |
| 純函式 | Pure Function | 無副作用且相同輸入產生相同輸出的函式 |
| 函式式編程 | Functional Programming | 以函式為核心的編程範式 |
| 命令式編程 | Imperative Programming | 以狀態修改為核心的編程範式 |
| 聲明式編程 | Declarative Programming | 描述「做什麼」而非「怎麼做」 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（12 個範例） | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（18 題） | 60 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（25 題） | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（20 min）：閱讀本 README，理解高階函式的必要性
2. **上課**（90 min）：
   - 講義學習（60 min）：`01-lecture.ipynb`
   - 範例演練（30 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（80 min）：
   - 完成習題（60 min）：`04-exercises.ipynb`
   - 對照解答（20 min）：`05-solutions.ipynb`
5. **自我測驗**（20 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能理解函式作為第一級物件的概念
- [ ] 能使用 Lambda 表達式定義簡單函式
- [ ] 能使用 map() 轉換資料
- [ ] 能使用 filter() 過濾資料
- [ ] 能使用 sorted() 的 key 參數自訂排序

### 進階能力
- [ ] 能使用 reduce() 進行累積運算
- [ ] 能撰寫回傳函式的函式（工廠函式）
- [ ] 能實作簡單的裝飾器
- [ ] 能理解 @syntax 裝飾器語法糖
- [ ] 能使用 functools.partial 進行部分應用
- [ ] 能比較函式式 vs 命令式編程風格

### 應用能力
- [ ] 能判斷何時使用 Lambda vs def
- [ ] 能選擇 map/filter vs 列表推導式
- [ ] 能設計實用的裝飾器（計時、日誌、快取）
- [ ] 能組合多個函式建立處理管道
- [ ] 能在實際專案中應用函式式編程思維

---

## 📝 理論重點（Key Theoretical Points）

### 1. 第一級函式（First-Class Functions）

```python
# 函式可賦值給變數
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # 函式賦值給變數
print(say_hello("Alice"))  # Hello, Alice!

# 函式可存入資料結構
operations = [abs, str.upper, len]
for op in operations:
    print(op([-5, "hello", [1, 2, 3]]))

# 函式可作為參數傳遞
def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x * 2, 5))  # 20
```

### 2. Lambda 表達式語法

```python
# 語法：lambda 參數列表: 運算式
# 等價於 def 函式
lambda x: x ** 2
# 等價於：
def square(x):
    return x ** 2

# 多參數 Lambda
lambda x, y: x + y
# 等價於：
def add(x, y):
    return x + y

# 無參數 Lambda
lambda: 42
# 等價於：
def get_answer():
    return 42

# Lambda 使用場景
# 1. 作為高階函式參數
sorted([3, 1, 4], key=lambda x: -x)  # [4, 3, 1]

# 2. 字典的默認值
from collections import defaultdict
d = defaultdict(lambda: 0)

# 3. 事件處理（GUI 編程）
# button.onClick(lambda: print("Clicked!"))
```

### 3. map()、filter()、reduce()

```python
# map(func, iterable) - 轉換每個元素
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# filter(func, iterable) - 過濾元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# reduce(func, iterable) - 累積運算
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
# 120 (1 * 2 * 3 * 4 * 5)

# vs 列表推導式
squares = [x ** 2 for x in numbers]  # 更 Pythonic
evens = [x for x in numbers if x % 2 == 0]  # 更 Pythonic
```

### 4. 裝飾器基礎

```python
# 最簡單的裝飾器
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 等價於：
# say_hello = my_decorator(say_hello)

say_hello()
# 輸出：
# Before function call
# Hello!
# After function call

# 帶參數的裝飾器
from functools import wraps

def decorator(func):
    @wraps(func)  # 保留原函式的元數據
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
```

### 5. 函式組合與部分應用

```python
# 函式組合
def compose(f, g):
    return lambda x: f(g(x))

double = lambda x: x * 2
increment = lambda x: x + 1
double_then_increment = compose(increment, double)
print(double_then_increment(5))  # 11

# 部分應用（functools.partial）
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從問題切入**：
   - 先展示重複代碼的痛點（多個類似迴圈）
   - 引出「如何抽象化行為」的需求
   - 自然引入高階函式概念

2. **循序漸進**：
   - 第一步：函式賦值給變數（建立「函式是物件」的概念）
   - 第二步：函式作為參數（map, filter）
   - 第三步：函式回傳函式（閉包、裝飾器）
   - 第四步：Lambda 表達式（簡化語法）

3. **對比教學**：
   - Lambda vs def（何時使用）
   - map/filter vs 列表推導式（可讀性、性能）
   - 函式式 vs 命令式（風格差異）
   - 裝飾器 vs 直接修改函式（維護性）

4. **實用案例**：
   - 資料處理管道（ETL）
   - 事件驅動編程（GUI、Web）
   - 中介軟體（Flask/Django）
   - 快取與記憶化

### 常見學生困難點

#### 困難點 1：Lambda 語法限制

**症狀**：學生嘗試在 Lambda 中寫多行代碼

**錯誤示範**：
```python
# ❌ 學生常犯錯誤
lambda x:
    y = x * 2
    return y + 1
# SyntaxError
```

**解決方法**：
```python
# ✅ 正確方法：使用 def
def process(x):
    y = x * 2
    return y + 1

# Lambda 只用於單一運算式
lambda x: x * 2 + 1  # 可以
```

**教學重點**：
- Lambda = 單一運算式
- 需要多行 → 使用 def
- 口訣：「一行搞定用 Lambda，複雜邏輯用 def」

#### 困難點 2：map/filter 回傳迭代器

**症狀**：學生看不到 map/filter 的結果

**錯誤示範**：
```python
numbers = [1, 2, 3]
result = map(lambda x: x ** 2, numbers)
print(result)  # <map object at 0x...> 困惑！
```

**解決方法**：
```python
# 方法 1：轉換為 list
result = list(map(lambda x: x ** 2, numbers))
print(result)  # [1, 4, 9]

# 方法 2：使用 for 迴圈迭代
for item in map(lambda x: x ** 2, numbers):
    print(item)
```

**教學重點**：
- Python 3 的 map/filter 回傳迭代器（惰性求值）
- 需要時才轉換為 list
- 解釋迭代器的優勢（記憶體效率）

#### 困難點 3：裝飾器的執行時機

**症狀**：不理解裝飾器何時執行

**教學示範**：
```python
def decorator(func):
    print("Decorator is running")  # 何時執行？
    def wrapper():
        print("Wrapper is running")
        func()
    return wrapper

@decorator
def say_hello():  # 這裡 decorator 就執行了（定義時）
    print("Hello!")

# 輸出：Decorator is running（立即執行）

say_hello()  # 呼叫時才執行 wrapper
# 輸出：
# Wrapper is running
# Hello!
```

**教學重點**：
- 裝飾器在**函式定義時**執行（import 時）
- wrapper 在**函式呼叫時**執行
- 類比：裝飾器是「包裝紙」，定義時就包好了

#### 困難點 4：何時使用高階函式 vs 列表推導式

**症狀**：不知道選擇哪種方式

**對比說明**：
```python
numbers = [1, 2, 3, 4, 5]

# 方法 1：map（函式式）
squares = list(map(lambda x: x ** 2, numbers))

# 方法 2：列表推導式（Pythonic）
squares = [x ** 2 for x in numbers]

# 選擇原則：
# 1. 簡單轉換 → 列表推導式（更清晰）
# 2. 已有函式 → map（避免重複）
#    例如：list(map(str.upper, words))
# 3. 複雜邏輯 → 列表推導式（可讀性佳）
# 4. 函式式風格 → map/filter（鏈式調用）
```

**教學建議**：
- 優先教列表推導式（更 Pythonic）
- map/filter 作為替代方案
- 強調可讀性 > 簡潔性

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**map vs filter vs reduce**：
- **map**：一對一轉換（每個元素都保留，但值改變）
- **filter**：篩選器（部分元素保留，值不變）
- **reduce**：歸約（多個元素合併為一個）

**Lambda 使用時機**：
- **簡短**：一行能寫完
- **一次**：只用一次
- **清晰**：意圖明確（如 `key=lambda x: x[1]`）

**裝飾器原則**：
- 裝飾器 = 高階函式
- @syntax = 語法糖
- 用途：擴展功能不改代碼

### 實作練習建議

1. **Lambda 練習**：
   - 用 Lambda 改寫簡單 def 函式
   - 使用 Lambda 作為 sorted() 的 key
   - 練習判斷何時不應用 Lambda

2. **高階函式練習**：
   - 使用 map/filter 處理資料
   - 對比列表推導式版本
   - 實作自己的 map/filter

3. **裝飾器練習**：
   - 實作計時裝飾器
   - 實作日誌裝飾器
   - 實作參數驗證裝飾器
   - 理解 @wraps 的作用

4. **函式組合練習**：
   - 實作 compose() 函式
   - 建立資料處理管道
   - 使用 partial() 固定參數

### 除錯技巧

```python
# 技巧 1：Lambda 除錯 - 轉換為 def
# ❌ Lambda 難以除錯
result = map(lambda x: x / (x - 2), numbers)  # 可能除以零

# ✅ 轉換為 def 方便除錯
def process(x):
    print(f"Processing {x}")  # 可加 print 除錯
    return x / (x - 2)
result = map(process, numbers)

# 技巧 2：檢視裝飾器行為
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# 技巧 3：檢視 map/filter 結果
result = map(lambda x: x ** 2, [1, 2, 3])
print(list(result))  # 轉為 list 檢視
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools — Higher-order functions](https://docs.python.org/3/library/functools.html)
- [Built-in Functions (map, filter)](https://docs.python.org/3/library/functions.html)

### 推薦閱讀
- Ramalho, L. (2015). *Fluent Python*, Chapter 5: First-Class Functions, Chapter 7: Decorators
- Beazley, D., & Jones, B. K. (2013). *Python Cookbook* (3rd ed.), Chapter 7: Functions
- Real Python: [Python Lambda Functions](https://realpython.com/python-lambda/)
- Real Python: [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化高階函式執行
- [repl.it](https://repl.it/) - 線上練習環境

### 延伸主題（進階學習）
- **Chapter 15**：遞迴（遞迴也是函式式編程的重要技術）
- **進階裝飾器**：帶參數的裝飾器、類別裝飾器
- **itertools 模組**：更多高階函式工具
- **生成器表達式**：惰性求值
- **函式式編程庫**：toolz, fn.py

---

## ❓ 常見問題（FAQ）

**Q1: Lambda 和 def 有什麼區別？何時使用？**

A:
- **Lambda**：
  - 匿名函式（無需命名）
  - 單一運算式（無 return 關鍵字）
  - 適合簡短、一次性使用
  - 常作為高階函式參數

- **def**：
  - 有名稱的函式
  - 可包含多行語句
  - 可寫文檔字串
  - 適合複雜邏輯、重複使用

**使用原則**：
```python
# ✅ 適合 Lambda
sorted(students, key=lambda s: s['grade'])

# ❌ 不適合 Lambda（太複雜）
lambda x: x if x > 0 else -x if x < -10 else 0  # 難讀

# ✅ 應該用 def
def process(x):
    if x > 0:
        return x
    elif x < -10:
        return -x
    else:
        return 0
```

**Q2: map/filter vs 列表推導式，哪個更好？**

A: **大多數情況下優先使用列表推導式**（更 Pythonic）

```python
# 列表推導式（推薦）
squares = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

# map/filter（可選）
squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 例外情況 - 已有現成函式時，map 更簡潔
words = ["hello", "world"]
upper_words = list(map(str.upper, words))  # 簡潔
# vs
upper_words = [w.upper() for w in words]   # 稍冗長
```

**Q3: 裝飾器的 @wraps 是什麼？為什麼需要？**

A: `@wraps` 用於保留原函式的元數據（名稱、文檔字串等）

```python
from functools import wraps

# ❌ 沒有 @wraps
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # wrapper（錯誤！）
print(add.__doc__)   # None（文檔丟失！）

# ✅ 使用 @wraps
def decorator(func):
    @wraps(func)  # 保留原函式元數據
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # add（正確）
print(add.__doc__)   # Add two numbers.（正確）
```

**Q4: reduce() 為什麼不是內建函式？**

A: Python 3 將 reduce() 移到 functools 模組，因為：
1. **可讀性**：列表推導式和 for 迴圈更清晰
2. **少用**：大多數情況有更好的替代方案（sum, any, all）
3. **爭議**：Guido van Rossum 認為 reduce 不夠 Pythonic

```python
# ❌ 使用 reduce（不推薦）
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)

# ✅ 使用內建函式（推薦）
total = sum(numbers)
```

**Q5: 裝飾器可以帶參數嗎？**

A: 可以，但需要三層嵌套（本章暫不深入，Ch14 進階內容）

```python
# 帶參數的裝飾器（簡化版）
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# 輸出：
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12**：函式設計基礎（高階函式建立在函式概念上）
- **Chapter 13**：作用域與生命週期（閉包、裝飾器需要理解作用域）
- **Chapter 7-11**：資料結構（map/filter 處理這些型態）

### 後續章節
- **Chapter 15**：遞迴（函式式編程的另一重要技術）
- **Chapter 23-26**：檔案處理（函式式編程風格處理資料）
- **進階主題**：生成器、迭代器、上下文管理器

### 對應的 Milestone 專案
- **Milestone 4: 文字處理工具箱**（整合 Ch12-15 的函式設計技巧）
  - 使用高階函式建立處理管道
  - 裝飾器實作功能擴展
  - Lambda 簡化代碼

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-07): 初版發布，基於教科書標準結構，完整涵蓋高階函式、Lambda、裝飾器
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 75 分）
- ✅ 能向他人解釋高階函式的概念與用途
- ✅ 能在 10 分鐘內撰寫實用的裝飾器
- ✅ 能判斷何時使用 Lambda vs def
- ✅ 能使用 map/filter/reduce 處理資料轉換
- ✅ 能在實際專案中應用函式式編程思維

---

**學習提醒**：高階函式是 Python 進階開發的重要基礎，掌握它將提升您的代碼抽象能力與設計水平！請透過大量練習建立扎實基礎。
