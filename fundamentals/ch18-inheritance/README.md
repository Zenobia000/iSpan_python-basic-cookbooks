# Chapter 18: 繼承與多型 | Inheritance and Polymorphism

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3.5 小時（2 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Chapter 16 (類別基礎), Chapter 17 (封裝) |
| **相關章節** | 參見 Chapter 19 (特殊方法), Chapter 21 (自訂例外) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 繼承的三種類型：單一繼承、多重繼承、多層繼承
- **定義** 父類（Parent Class）、子類（Child Class）、super() 的用途
- **說明** 方法解析順序（MRO）與抽象基類（ABC）的概念

### 理解面（Comprehension）
- **解釋** 為什麼需要繼承機制（程式碼重用、建立類別階層）
- **比較** 繼承（is-a）與組合（has-a）的差異
- **歸納** 多型（Polymorphism）的實現方式與優勢

### 應用面（Application）
- **運用** 單一繼承建立基本的類別階層
- **實作** 方法覆寫（Method Overriding）與 super() 調用
- **解決** 需要多重繼承的實際問題

### 分析面（Analysis）
- **分析** MRO 在複雜繼承中的解析順序
- **診斷** 繼承相關的常見錯誤（如鑽石問題）
- **選擇** 何時使用繼承 vs 組合的設計決策

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
繼承與多型
├── 繼承（Inheritance）
│   ├── 單一繼承（Single Inheritance）
│   ├── 多重繼承（Multiple Inheritance）
│   ├── 多層繼承（Multilevel Inheritance）
│   └── super() 函式
│
├── 方法覆寫（Method Overriding）
│   ├── 覆寫父類方法
│   ├── 擴展父類方法
│   └── 方法解析順序（MRO）
│
├── 多型（Polymorphism）
│   ├── 方法多型
│   ├── 運算子多型
│   └── 鴨子型別（Duck Typing）
│
└── 抽象基類（Abstract Base Class）
    ├── abc 模組
    ├── @abstractmethod 裝飾器
    └── 介面設計
```

### First Principles 解析

#### 為什麼需要繼承？
**根本問題**：程式中經常出現「具有共同特性的類別」，需要避免重複程式碼

**最小實作**：
```python
# 沒有繼承：程式碼重複
class Dog:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"

class Cat:
    def __init__(self, name):
        self.name = name
    def eat(self):  # 重複的程式碼！
        return f"{self.name} is eating"

# 使用繼承：程式碼重用
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    pass  # 自動繼承 __init__ 和 eat

class Cat(Animal):
    pass  # 自動繼承 __init__ 和 eat
```

**推導過程**：
1. 多個類別有共同屬性/方法 → 需要避免重複
2. 提取共同部分到父類 → 繼承機制
3. 子類自動獲得父類功能 → is-a 關係（Dog is-a Animal）

#### 繼承的本質是什麼？
**核心概念**：建立「is-a」關係的類別階層

```python
# is-a 關係（使用繼承）
class Manager(Employee):  # Manager is-a Employee ✓
    pass

# has-a 關係（使用組合）
class Department:
    def __init__(self):
        self.manager = Manager()  # Department has-a Manager ✓
```

#### 多型如何實現？
**根本問題**：同一個操作在不同類別上有不同的行為

**實例說明**：
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # 覆寫父類方法
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # 覆寫父類方法
        return 3.14 * self.radius ** 2

# 多型：同樣呼叫 area()，但行為不同
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())  # 自動呼叫對應的 area() 方法
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 繼承 | Inheritance | 子類自動獲得父類屬性與方法的機制 |
| 父類/基類 | Parent/Base Class | 被繼承的類別 |
| 子類/衍生類 | Child/Derived Class | 繼承其他類別的類別 |
| 方法覆寫 | Method Overriding | 子類重新定義父類的方法 |
| super() | super() | 用於調用父類方法的內建函式 |
| 多型 | Polymorphism | 同一介面有多種實作形式 |
| MRO | Method Resolution Order | 方法解析順序（多重繼承時的查找順序） |
| 抽象基類 | Abstract Base Class (ABC) | 定義介面但不實作的類別 |
| 抽象方法 | Abstract Method | 必須由子類實作的方法 |
| 鴨子型別 | Duck Typing | 「如果它走起來像鴨子，叫起來像鴨子，那它就是鴨子」|

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（6 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（4 個完整專案） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（8 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（15 選擇 + 5 程式） | 30 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，理解繼承的核心概念
2. **上課**（120 min）：
   - 講義學習（80 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（90 min）：
   - 完成習題（60 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（30 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能建立單一繼承的類別階層
- [ ] 能使用 `isinstance()` 和 `issubclass()` 檢查繼承關係
- [ ] 能正確覆寫父類的方法
- [ ] 能使用 `super()` 呼叫父類的建構子

### 進階能力
- [ ] 能理解並實作多重繼承
- [ ] 能使用 `__mro__` 或 `.mro()` 查看方法解析順序
- [ ] 能區分方法覆寫與方法擴展的差異
- [ ] 能使用 ABC 模組建立抽象基類

### 應用能力
- [ ] 能設計合理的類別階層（3 層以上）
- [ ] 能判斷何時使用繼承 vs 組合
- [ ] 能重構重複程式碼為繼承結構
- [ ] 能使用多型簡化程式碼邏輯

---

## 📝 理論重點（Key Theoretical Points）

### 1. 繼承的語法與類型

#### 單一繼承
```python
class Parent:
    def method(self):
        return "Parent method"

class Child(Parent):  # 單一繼承
    pass

c = Child()
print(c.method())  # "Parent method"（繼承來的）
```

#### 多重繼承
```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):  # 多重繼承
    pass

d = Duck()
print(d.fly())   # "Flying"
print(d.swim())  # "Swimming"
```

### 2. super() 的使用

| 使用情境 | 範例 | 說明 |
|:---------|:-----|:-----|
| 呼叫父類建構子 | `super().__init__(name)` | 初始化父類屬性 |
| 擴展父類方法 | `super().method()` | 保留父類行為並添加新功能 |
| 多重繼承 | `super().__init__()` | 依據 MRO 順序呼叫 |

**完整範例**：
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 呼叫父類建構子
        self.breed = breed

    def speak(self):
        parent_msg = super().speak()  # 擴展父類方法
        return f"{parent_msg} - Woof!"
```

### 3. 方法解析順序（MRO）

**鑽石問題（Diamond Problem）**：
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # 鑽石繼承
    pass

d = D()
print(d.method())      # "B"
print(D.__mro__)       # 查看 MRO: D -> B -> C -> A -> object
```

**MRO 規則**（C3 線性化演算法）：
1. 子類優先於父類
2. 多個父類按照繼承順序（從左到右）
3. 保持每個類別只出現一次

### 4. 抽象基類（ABC）

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):  # 抽象基類
    @abstractmethod
    def process_payment(self, amount):
        """子類必須實作此方法"""
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):  # 必須實作
        return f"Processing ${amount} via Credit Card"

# payment = PaymentMethod()  # TypeError: 無法實例化抽象類別
card = CreditCard()  # ✓ 可以實例化
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **從現實類比切入**：
   - 生物分類學：動物 → 哺乳類 → 犬科 → 狗
   - 交通工具：車輛 → 汽車/飛機/船

2. **強調 is-a vs has-a**：
   - ✓ Car is-a Vehicle（繼承）
   - ✓ Car has-a Engine（組合）
   - ✗ Car is-a Engine（錯誤的繼承）

3. **視覺化工具**：
   - 使用 UML 類圖展示繼承關係
   - 畫出 MRO 的查找路徑

### 常見學生困難點

#### 困難點 1：super() 的迷思
**症狀**：不理解為什麼要用 `super()` 而不是直接呼叫父類

**解決方法**：
```python
# ❌ 不建議：直接呼叫父類名稱
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # 多重繼承時會出問題

# ✅ 建議：使用 super()
class Child(Parent):
    def __init__(self):
        super().__init__()  # 遵循 MRO，支援多重繼承
```

**關鍵說明**：
- `super()` 依據 MRO 自動找到正確的父類
- 在多重繼承中，直接呼叫父類名稱可能跳過某些類別
- `super()` 是 Python 推薦的最佳實踐

#### 困難點 2：何時覆寫 vs 何時擴展
**症狀**：混淆「完全覆寫」與「擴展父類方法」

**解決方法**：
```python
# 完全覆寫（不呼叫 super）
class Dog(Animal):
    def speak(self):
        return "Woof!"  # 完全取代父類行為

# 擴展父類方法（呼叫 super）
class Dog(Animal):
    def speak(self):
        parent_msg = super().speak()  # 保留父類行為
        return f"{parent_msg} - Woof!"  # 添加新行為
```

#### 困難點 3：過度使用繼承
**症狀**：所有關係都用繼承，導致類別階層過深

**建議**：
- **優先考慮組合**：「has-a」關係用組合
- **繼承深度 ≤ 3 層**：過深的階層難以維護
- **使用抽象基類**：定義介面而非實作

**範例**：
```python
# ❌ 錯誤：過度繼承
class Engine:
    pass

class Car(Engine):  # 錯誤！Car 不是 Engine
    pass

# ✅ 正確：使用組合
class Car:
    def __init__(self):
        self.engine = Engine()  # Car has-a Engine
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **is-a → 繼承**：狗 is-a 動物（Dog is-a Animal）
- **has-a → 組合**：車 has-a 引擎（Car has-a Engine）
- **MRO 規則**：**左**邊優先，**深度**優先（Left-first, Depth-first）

### 實作練習建議
1. **繪製 UML 圖**：視覺化類別關係
2. **重構練習**：找出重複程式碼，提取為父類
3. **MRO 實驗**：建立複雜繼承，觀察 `__mro__`

### 除錯技巧
```python
# 檢查繼承關係
isinstance(dog, Animal)      # True
issubclass(Dog, Animal)      # True

# 查看 MRO
print(Dog.__mro__)
print(Dog.mro())

# 檢查屬性來源
print(dog.__class__.__name__)  # 'Dog'
print(type(dog))               # <class 'Dog'>
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Classes - Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Method Resolution Order (MRO)](https://www.python.org/download/releases/2.3/mro/)

### 推薦閱讀
- Gamma, E. et al. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*
- Lutz, M. (2013). *Learning Python* (5th ed.), Chapter 31-32
- Ramalho, L. (2015). *Fluent Python*, Chapter 12

### 互動式工具
- [Python Tutor - 視覺化繼承](http://pythontutor.com/)
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)

### 延伸主題（進階學習）
- **Mixin 類別**：提供額外功能的小類別
- **合成優於繼承**（Composition over Inheritance）原則
- **協定（Protocols）**：PEP 544 結構型子型別（Structural Subtyping）
- **元類別（Metaclasses）**：控制類別建立的類別

---

## ❓ 常見問題（FAQ）

**Q1: 繼承與組合該如何選擇？**
A: 使用 **is-a 測試**：
- "Dog is-a Animal" ✓ → 繼承
- "Car is-a Engine" ✗ → 組合（Car has-a Engine）
- 經驗法則：**優先使用組合**，只有明確的 is-a 關係才用繼承

**Q2: 為什麼 Python 允許多重繼承？**
A: Python 設計哲學強調靈活性。雖然多重繼承可能造成複雜性（如鑽石問題），但 MRO 機制能妥善處理。現代 Python 更推薦使用 Mixin 模式。

**Q3: `super()` 在多重繼承中如何運作？**
A: `super()` 依據 **MRO（Method Resolution Order）** 順序呼叫下一個類別，不是「父類」而是「MRO 中的下一個類別」。

**Q4: 什麼時候應該使用抽象基類？**
A: 當你需要：
1. 定義介面（強制子類實作某些方法）
2. 建立可插拔的架構（如支付系統、資料庫驅動）
3. 文件化期望的 API

**Q5: Python 的鴨子型別與繼承有何關係？**
A: 鴨子型別不要求繼承關係，只要物件有相同方法即可。這是 Python 的動態特性，與靜態語言（如 Java）的嚴格繼承不同。

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 16（類別基礎）**：理解類別與物件
- **Chapter 17（封裝）**：掌握屬性與方法的封裝

### 後續章節
- **Chapter 19（特殊方法）**：自訂運算子行為（多型的進階應用）
- **Chapter 21（自訂例外）**：繼承 Exception 類別

### 對應的 Milestone 專案
- **Milestone 5: 銀行系統**（結合 Ch16-19，實作帳戶類別階層）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能設計一個 3 層的類別階層（如：Shape → 2D/3D → Rectangle/Circle/Cube）
- ✅ 能解釋 MRO 在複雜繼承中的運作原理
- ✅ 能在 10 分鐘內實作一個抽象基類及其兩個子類

---

**學習提醒**：繼承是物件導向程式設計的核心概念，但「能用不代表應該用」。現代軟體工程更強調「組合優於繼承」，請確實理解兩者的適用時機！
