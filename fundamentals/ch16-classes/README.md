# Chapter 16: 類別與物件 | Classes and Objects

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (3/5) |
| **先備知識** | Chapter 12-15（函式設計、作用域、高階函式、遞迴） |
| **相關章節** | Chapter 17（封裝）、Chapter 18（繼承）、Chapter 19（特殊方法） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 類別的組成要素：class、__init__、attributes、methods
- **定義** 類別、物件、實例、屬性、方法的概念
- **說明** self 參數的作用與必要性
- **辨識** 類別屬性與實例屬性的差異

### 理解面（Comprehension）
- **解釋** 為什麼需要物件導向程式設計（封裝、繼承、多型）
- **比較** 類別與物件的關係（藍圖 vs 實例）
- **歸納** 類別方法、靜態方法、實例方法的使用時機
- **詮釋** 物件導向如何提升代碼的可維護性

### 應用面（Application）
- **運用** 類別封裝相關的資料與行為
- **實作** 具有建構子的類別
- **設計** 符合單一職責原則的類別
- **解決** 需要物件化的實際問題（如學生管理、銀行帳戶）

### 分析面（Analysis）
- **分析** 何時應該使用類別而非函式
- **診斷** 類別設計的常見錯誤（忘記 self、類別屬性誤用）
- **選擇** 適當的屬性與方法設計策略
- **評估** 類別設計的可重用性與擴展性

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
類別與物件
├── 基本概念
│   ├── 類別（Class）：物件的藍圖
│   ├── 物件（Object）：類別的實例
│   ├── 實例化（Instantiation）：創建物件
│   └── self 參數：指向實例本身
│
├── 屬性（Attributes）
│   ├── 實例屬性：每個物件獨立擁有
│   ├── 類別屬性：所有實例共享
│   └── 屬性存取：obj.attribute
│
├── 方法（Methods）
│   ├── 實例方法：操作實例資料
│   ├── 類別方法（@classmethod）：操作類別資料
│   ├── 靜態方法（@staticmethod）：工具函式
│   └── __init__ 建構子：初始化物件
│
├── 封裝概念
│   ├── 資料與行為綁定
│   ├── 資訊隱藏（命名慣例）
│   └── 介面設計
│
└── OOP 核心原則
    ├── 封裝（Encapsulation）
    ├── 繼承（Inheritance，Ch18）
    └── 多型（Polymorphism，Ch18）
```

### First Principles 解析

#### 為什麼需要類別與物件？

**根本問題**：當程式需要處理複雜的資料結構時，如何組織相關的資料與操作？

**演化過程**：

```python
# 階段 1：使用變數（混亂）
student1_name = "Alice"
student1_age = 20
student1_scores = [85, 90, 88]

student2_name = "Bob"
student2_age = 21
student2_scores = [78, 82, 80]

# 問題：變數分散，難以管理

# 階段 2：使用字典（改善但仍不足）
student1 = {"name": "Alice", "age": 20, "scores": [85, 90, 88]}
student2 = {"name": "Bob", "age": 21, "scores": [78, 82, 80]}

def calculate_average(student):
    return sum(student["scores"]) / len(student["scores"])

# 問題：資料與行為分離，無法保證結構一致

# 階段 3：使用類別（物件導向）
class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

student1 = Student("Alice", 20, [85, 90, 88])
student2 = Student("Bob", 21, [78, 82, 80])

print(student1.calculate_average())  # 資料與行為綁定
```

**優勢**：
1. **封裝性**：資料與操作綁定在一起
2. **可重用性**：類別是可重用的模板
3. **可維護性**：修改類別即可影響所有實例
4. **語意化**：更接近真實世界的建模

#### 為什麼需要 self 參數？

**根本問題**：實例方法如何知道要操作哪個物件的資料？

**解析**：

```python
class Counter:
    def __init__(self):
        self.count = 0  # self 指向當前實例

    def increment(self):
        self.count += 1  # 操作當前實例的 count

# 創建兩個獨立的計數器
c1 = Counter()
c2 = Counter()

c1.increment()  # c1.count = 1
c1.increment()  # c1.count = 2

c2.increment()  # c2.count = 1

# Python 實際的呼叫方式
c1.increment()  # 等同於 Counter.increment(c1)
#                         ^ self 就是 c1
```

**關鍵理解**：
- `self` 是實例方法的第一個參數（慣例名稱）
- 呼叫 `obj.method()` 時，Python 自動傳遞 `obj` 給 `self`
- 透過 `self` 存取實例的屬性與方法

#### 類別屬性 vs 實例屬性

**根本問題**：如何區分「所有實例共享」與「每個實例獨立」的資料？

```python
class Dog:
    species = "Canis familiaris"  # 類別屬性（所有狗都是犬科）

    def __init__(self, name, age):
        self.name = name  # 實例屬性（每隻狗有自己的名字）
        self.age = age    # 實例屬性（每隻狗有自己的年齡）

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.species)  # "Canis familiaris"（共享）
print(dog2.species)  # "Canis familiaris"（共享）

print(dog1.name)  # "Buddy"（獨立）
print(dog2.name)  # "Max"（獨立）

# 修改類別屬性影響所有實例
Dog.species = "Dog"
print(dog1.species)  # "Dog"
print(dog2.species)  # "Dog"
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 類別 | Class | 定義物件的藍圖或模板 |
| 物件 | Object | 類別的實例，具體的資料實體 |
| 實例 | Instance | 與「物件」同義，強調由類別產生 |
| 實例化 | Instantiation | 根據類別創建物件的過程 |
| 屬性 | Attribute | 物件儲存的資料（變數） |
| 方法 | Method | 物件的行為（函式） |
| 建構子 | Constructor | `__init__` 方法，用於初始化物件 |
| self | self | 實例方法的第一個參數，指向實例本身 |
| 實例屬性 | Instance Attribute | 每個實例獨立擁有的屬性 |
| 類別屬性 | Class Attribute | 所有實例共享的屬性 |
| 實例方法 | Instance Method | 操作實例資料的方法（含 self 參數） |
| 類別方法 | Class Method | 操作類別資料的方法（`@classmethod` 裝飾器） |
| 靜態方法 | Static Method | 不依賴實例或類別的方法（`@staticmethod` 裝飾器） |
| 封裝 | Encapsulation | 將資料與操作綁定，隱藏內部實作 |
| 繼承 | Inheritance | 子類別繼承父類別的屬性與方法（Ch18） |
| 多型 | Polymorphism | 不同類別可用相同介面（Ch18） |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（10 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 40 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（18 題） | 100 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（28 題） | 25 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解物件導向的必要性
2. **上課**（120 min）：
   - 講義學習（80 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（40 min）：完成 `03-practice.ipynb`
4. **課後複習**（100 min）：
   - 完成習題（70 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（25 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能使用 `class` 定義類別
- [ ] 能實作 `__init__` 建構子初始化物件
- [ ] 能正確使用 `self` 參數
- [ ] 能定義實例屬性與實例方法
- [ ] 能創建物件並呼叫方法

### 進階能力
- [ ] 能區分類別屬性與實例屬性
- [ ] 能設計具有多個方法的類別
- [ ] 能使用 `@classmethod` 定義類別方法
- [ ] 能使用 `@staticmethod` 定義靜態方法
- [ ] 能實作物件之間的互動

### 應用能力
- [ ] 能根據需求設計適當的類別結構
- [ ] 能遵循單一職責原則設計類別
- [ ] 能撰寫清晰的類別文件
- [ ] 能使用物件導向思維解決實際問題
- [ ] 能在實務專案中合理運用類別

---

## 📝 理論重點（Key Theoretical Points）

### 1. 類別定義的語法結構

```python
class 類別名稱:
    """類別文件字串"""

    # 類別屬性（所有實例共享）
    類別屬性 = 值

    # 建構子（初始化方法）
    def __init__(self, 參數1, 參數2):
        """初始化實例"""
        self.屬性1 = 參數1  # 實例屬性
        self.屬性2 = 參數2

    # 實例方法
    def 方法名稱(self, 參數):
        """方法文件字串"""
        # 使用 self 存取屬性
        return self.屬性1 + 參數
```

**實例**：
```python
class Rectangle:
    """矩形類別"""

    shape_type = "四邊形"  # 類別屬性

    def __init__(self, length, width):
        """初始化矩形"""
        self.length = length  # 實例屬性
        self.width = width

    def area(self):
        """計算面積"""
        return self.length * self.width

    def perimeter(self):
        """計算周長"""
        return 2 * (self.length + self.width)
```

### 2. 物件的創建與使用

| 操作 | 語法 | 說明 |
|:-----|:-----|:-----|
| 創建物件 | `obj = ClassName(args)` | 實例化，呼叫 `__init__` |
| 存取屬性 | `obj.attribute` | 取得屬性值 |
| 修改屬性 | `obj.attribute = value` | 設定屬性值 |
| 呼叫方法 | `obj.method(args)` | 執行方法 |
| 取得類別 | `type(obj)` | 回傳物件的類別 |

**範例**：
```python
# 創建物件
rect = Rectangle(10, 5)

# 存取屬性
print(rect.length)  # 10
print(rect.width)   # 5

# 修改屬性
rect.length = 15

# 呼叫方法
print(rect.area())       # 75
print(rect.perimeter())  # 40

# 取得類別
print(type(rect))  # <class '__main__.Rectangle'>
```

### 3. 類別屬性 vs 實例屬性

| 特性 | 類別屬性 | 實例屬性 |
|:-----|:---------|:---------|
| 定義位置 | 類別內，方法外 | `__init__` 中，使用 `self` |
| 共享性 | 所有實例共享 | 每個實例獨立 |
| 存取方式 | `ClassName.attr` 或 `obj.attr` | `obj.attr` |
| 修改影響 | 影響所有實例 | 只影響單一實例 |
| 記憶體 | 只有一份 | 每個實例一份 |

**重要範例**：
```python
class Counter:
    total_count = 0  # 類別屬性：追蹤總實例數

    def __init__(self, name):
        self.name = name  # 實例屬性
        Counter.total_count += 1  # 修改類別屬性

c1 = Counter("A")
c2 = Counter("B")
c3 = Counter("C")

print(Counter.total_count)  # 3
print(c1.total_count)       # 3（實例也能存取類別屬性）
print(c2.name)              # "B"（實例屬性）
```

### 4. 三種方法類型

```python
class MyClass:
    class_var = "類別變數"

    def __init__(self, value):
        self.instance_var = value

    # 實例方法（Instance Method）
    def instance_method(self):
        """可存取 self.instance_var 和 self.class_var"""
        return f"Instance: {self.instance_var}"

    # 類別方法（Class Method）
    @classmethod
    def class_method(cls):
        """可存取 cls.class_var，但無法存取 instance_var"""
        return f"Class: {cls.class_var}"

    # 靜態方法（Static Method）
    @staticmethod
    def static_method(x, y):
        """獨立的工具函式，無法存取類別或實例資料"""
        return x + y

# 呼叫方式
obj = MyClass("實例值")
print(obj.instance_method())  # "Instance: 實例值"
print(MyClass.class_method()) # "Class: 類別變數"
print(MyClass.static_method(3, 5))  # 8
```

**使用時機**：
- **實例方法**：需要存取或修改實例資料（最常用）
- **類別方法**：需要存取類別資料，或作為替代建構子
- **靜態方法**：邏輯上屬於類別，但不需要存取任何資料

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從現實類比切入**：
   - 類別 = 餅乾模具（Cookie Cutter）
   - 物件 = 實際的餅乾（每片餅乾都是獨立的）
   - 屬性 = 餅乾的特徵（大小、口味、顏色）
   - 方法 = 餅乾的行為（被吃掉、變硬）

2. **強調封裝概念**：
   - 展示字典 vs 類別的差異
   - 說明為何資料與行為應綁定
   - 示範類別如何提升代碼組織

3. **逐步演化教學法**：
   - 從最簡單的空類別開始
   - 逐步加入屬性、方法、建構子
   - 最後講解類別屬性與裝飾器

4. **實際操作演示**：
   - 使用 `type()` 和 `dir()` 檢查物件
   - 使用 Python Tutor 視覺化物件創建
   - 故意製造常見錯誤（忘記 self）

### 常見學生困難點

#### 困難點 1：忘記 self 參數

**症狀**：方法定義時忘記 self，或在方法內存取屬性時忘記 `self.`

**錯誤示範**：
```python
class Person:
    def __init__(self, name):
        name = name  # ❌ 錯誤：應該是 self.name = name

    def greet():  # ❌ 錯誤：缺少 self 參數
        print(f"Hello, {name}")  # ❌ 錯誤：應該是 self.name
```

**解決方法**：
- 強調 `self` 是「當前物件的代名詞」
- 實例方法第一個參數永遠是 `self`
- 存取屬性時一定要用 `self.attribute`

#### 困難點 2：類別 vs 物件的混淆

**症狀**：不理解「類別是模板，物件是實例」

**教學策略**：
```python
# 類別定義（藍圖）
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# 物件創建（實例）
car1 = Car("Toyota", "red")    # 第一輛車
car2 = Car("Honda", "blue")    # 第二輛車

# 每個物件都是獨立的
print(car1.brand)  # "Toyota"
print(car2.brand)  # "Honda"
```

**記憶口訣**：
- **類別**：Cookie Cutter（模具）
- **物件**：Cookies（餅乾）
- 一個模具可以做出很多餅乾

#### 困難點 3：類別屬性與實例屬性的混淆

**症狀**：不知道何時使用類別屬性，何時使用實例屬性

**教學重點**：
```python
class Student:
    school = "iSpan"  # 類別屬性：所有學生都在 iSpan

    def __init__(self, name, age):
        self.name = name  # 實例屬性：每個學生有自己的名字
        self.age = age    # 實例屬性：每個學生有自己的年齡

s1 = Student("Alice", 20)
s2 = Student("Bob", 21)

# 類別屬性共享
print(s1.school)  # "iSpan"
print(s2.school)  # "iSpan"

# 實例屬性獨立
print(s1.name)  # "Alice"
print(s2.name)  # "Bob"
```

**判斷原則**：
- 所有實例共享的資料 → 類別屬性
- 每個實例獨立的資料 → 實例屬性

#### 困難點 4：修改屬性 vs 創建新屬性

**症狀**：誤以為 `obj.attr = value` 會修改類別屬性

**教學重點**：
```python
class MyClass:
    count = 0  # 類別屬性

obj = MyClass()
print(obj.count)  # 0（存取類別屬性）

obj.count = 10  # ❌ 這不會修改類別屬性，而是創建實例屬性！
print(obj.count)       # 10（實例屬性）
print(MyClass.count)   # 0（類別屬性未變）

# 正確修改類別屬性
MyClass.count = 5
print(MyClass.count)  # 5
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**類別定義四要素**：
- **C**lass：類別關鍵字
- **A**ttributes：屬性（資料）
- **M**ethods：方法（行為）
- **I**nit：建構子（初始化）

**self 的三個作用**：
1. 區分實例屬性與區域變數
2. 呼叫同一物件的其他方法
3. 回傳物件本身（鏈式呼叫）

### 實作練習建議

1. **從真實世界建模**：將現實物體轉換為類別（書籍、動物、車輛）
2. **改寫既有代碼**：將使用字典的代碼改寫為類別
3. **設計類別層次**：思考哪些資料應屬於類別，哪些屬於實例
4. **撰寫完整文件**：為類別和方法撰寫清晰的 docstring

### 除錯技巧

```python
# 檢查物件的所有屬性和方法
obj = MyClass()
print(dir(obj))

# 檢查物件的類別
print(type(obj))

# 檢查是否為某類別的實例
print(isinstance(obj, MyClass))

# 檢查屬性是否存在
print(hasattr(obj, 'attribute_name'))

# 取得屬性值（若不存在回傳預設值）
print(getattr(obj, 'attribute_name', 'default'))
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [Data Model - Special Methods](https://docs.python.org/3/reference/datamodel.html)
- [PEP 8 – Class Names](https://peps.python.org/pep-0008/#class-names)

### 推薦閱讀
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 15-17: Classes and Objects
- Matthes, E. (2019). *Python Crash Course* (2nd ed.), Chapter 9: Classes
- Lutz, M. (2013). *Learning Python* (5th ed.), Part VI: Classes and OOP

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化物件創建與方法呼叫
- [Real Python: OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)

### 延伸主題（進階學習）
- **Chapter 17**：封裝與資訊隱藏（私有屬性、getter/setter）
- **Chapter 18**：繼承與多型（父類別、子類別、方法覆寫）
- **Chapter 19**：特殊方法（`__str__`、`__repr__`、`__len__`）
- 屬性裝飾器（@property）
- 多重繼承與 MRO（Method Resolution Order）
- 抽象基類（ABC, Abstract Base Classes）

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候應該使用類別而非函式？**

A: 遵循以下原則：
- **資料與行為相關**：需要將資料與操作綁定時
- **需要狀態管理**：物件需要記住狀態變化
- **需要多個實例**：同一結構需要創建多個獨立實體
- **需要繼承擴展**：未來可能需要建立子類別

**範例**：
- ✅ 使用類別：銀行帳戶（有餘額狀態、存款提款行為）
- ❌ 使用函式：計算圓面積（無狀態、單一運算）

**Q2: self 參數為什麼不需要在呼叫時傳遞？**

A: Python 自動處理：
```python
class MyClass:
    def method(self, x):
        return x * 2

obj = MyClass()
obj.method(5)  # Python 自動轉換為：MyClass.method(obj, 5)
#              ↑ obj 被自動傳給 self
```

**Q3: 類別屬性什麼時候使用？**

A: 適用場景：
- 所有實例共享的常數（如 `PI = 3.14159`）
- 追蹤所有實例的統計（如實例計數器）
- 預設值或配置資料

**不適合**：
- 每個實例獨立的資料（應使用實例屬性）

**Q4: 為什麼類別名稱使用 PascalCase？**

A: 這是 Python 的命名慣例（PEP 8）：
- **類別名稱**：`PascalCase`（每個單字首字母大寫）
- **函式/方法名稱**：`snake_case`（小寫加底線）
- **常數**：`UPPER_CASE`（全大寫加底線）

```python
class StudentManager:  # ✅ 類別：PascalCase
    def add_student(self):  # ✅ 方法：snake_case
        pass

MAX_STUDENTS = 100  # ✅ 常數：UPPER_CASE
```

**Q5: __init__ 和一般方法有什麼不同？**

A:
- **`__init__`**：建構子，創建物件時自動呼叫，用於初始化
- **一般方法**：需要明確呼叫，用於執行特定操作

```python
class Person:
    def __init__(self, name):
        self.name = name  # 創建物件時自動執行

    def greet(self):
        print(f"Hello, {self.name}")  # 需要明確呼叫

p = Person("Alice")  # __init__ 自動呼叫
p.greet()            # 需要明確呼叫
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12**：函式設計（方法本質上是函式）
- **Chapter 13**：作用域（類別有自己的命名空間）
- **Chapter 7-11**：資料結構（類別封裝這些結構）

### 後續章節
- **Chapter 17**：封裝與資訊隱藏（私有屬性、getter/setter）
- **Chapter 18**：繼承與多型（類別的延伸）
- **Chapter 19**：特殊方法與運算子重載（魔術方法）

### 對應的 Milestone 專案
- **Milestone 5: 銀行系統**（整合 Ch16-19 的物件導向設計）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-06): 初版發布，基於教科書標準結構

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 75 分）
- ✅ 能向他人解釋類別與物件的概念
- ✅ 能在 10 分鐘內設計並實作一個實用類別
- ✅ 能識別何時應使用物件導向而非程序式設計

---

**學習提醒**：物件導向程式設計是現代軟體開發的核心範式，掌握類別與物件是成為專業開發者的必經之路！
