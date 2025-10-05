# Chapter 18: 繼承與多型 | Inheritance and Polymorphism

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐⭐☆ (進階) |
| **先備知識** | Chapter 16 (類別基礎), Chapter 17 (封裝) |
| **相關章節** | Chapter 19 (特殊方法), Chapter 21 (自訂例外) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 繼承的三種主要類型：單一繼承、多重繼承、多層繼承
- **定義** 多型（Polymorphism）的概念與應用
- **說明** MRO（Method Resolution Order）的運作機制

### 理解面（Comprehension）
- **解釋** 為什麼繼承能提升程式碼重用性
- **比較** 繼承與組合（Composition）的優缺點
- **歸納** `super()` 函式在繼承中的角色

### 應用面（Application）
- **運用** 繼承建立類別階層關係
- **實作** 方法覆寫（Method Overriding）
- **解決** 使用多型處理不同類別的物件

### 分析面（Analysis）
- **分析** 菱形繼承問題（Diamond Problem）
- **診斷** 繼承鏈中的方法呼叫順序
- **選擇** 何時使用繼承、何時使用組合

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
繼承與多型
├── 繼承（Inheritance）
│   ├── 單一繼承（Single Inheritance）
│   ├── 多重繼承（Multiple Inheritance）
│   ├── 多層繼承（Multilevel Inheritance）
│   ├── super() 函式
│   └── MRO（Method Resolution Order）
│
├── 多型（Polymorphism）
│   ├── 方法覆寫（Method Overriding）
│   ├── Duck Typing
│   └── 抽象基類概念（ABC）
│
└── 設計原則
    ├── is-a 關係
    ├── 里氏替換原則（LSP）
    └── 繼承 vs 組合
```

### First Principles 解析

#### 為什麼需要繼承？
**根本問題**：多個類別有共同屬性和行為，如何避免重複程式碼？

**最小實作**：
```python
# 不使用繼承 - 程式碼重複
class Dog:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Cat:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

# 使用繼承 - 程式碼重用
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass  # 繼承 Animal 的所有功能

class Cat(Animal):
    pass
```

**推導過程**：
1. 發現共同特徵 → 提取基類（Base Class）
2. 定義差異化特徵 → 在子類（Subclass）中擴展
3. 建立 is-a 關係 → Dog is an Animal

#### 為什麼需要多型？
**根本問題**：如何用同一個介面處理不同類型的物件？

**實例說明**：
```python
# 多型的威力
def make_sound(animal):
    animal.speak()  # 不需知道具體是哪種動物

dog = Dog("Buddy")
cat = Cat("Whiskers")

make_sound(dog)  # Woof!
make_sound(cat)  # Meow!
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 繼承 | Inheritance | 子類別從父類別獲取屬性與方法的機制 |
| 父類別 | Base/Parent Class | 被繼承的類別（也稱超類別 Superclass） |
| 子類別 | Derived/Child Class | 繼承其他類別的類別（也稱衍生類別） |
| 多型 | Polymorphism | 同一介面可操作不同類型物件的能力 |
| 方法覆寫 | Method Overriding | 子類別重新定義父類別的方法 |
| super() | super() | 呼叫父類別方法的函式 |
| MRO | Method Resolution Order | 方法解析順序，決定多重繼承的查找路徑 |
| 抽象基類 | Abstract Base Class (ABC) | 定義介面規範的類別，不能直接實例化 |
| Duck Typing | Duck Typing | "如果它走路像鴨子、叫聲像鴨子，那它就是鴨子" |
| 菱形繼承 | Diamond Inheritance | 多重繼承導致的菱形結構問題 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 90 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 40 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 120 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 30 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，理解繼承的必要性
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
- [ ] 能建立單一繼承關係
- [ ] 能使用 `super()` 呼叫父類別方法
- [ ] 能覆寫父類別的方法
- [ ] 能使用 `isinstance()` 和 `issubclass()` 檢查繼承關係

### 進階能力
- [ ] 能實作多重繼承並理解 MRO
- [ ] 能解釋 `super()` 在多重繼承中的行為
- [ ] 能運用多型設計彈性的系統
- [ ] 能分辨何時該用繼承、何時該用組合

### 應用能力
- [ ] 能設計合理的類別階層架構
- [ ] 能處理菱形繼承問題
- [ ] 能使用抽象基類（ABC）定義介面
- [ ] 能重構重複的程式碼為繼承結構

---

## 📝 理論重點（Key Theoretical Points）

### 1. 單一繼承 vs 多重繼承

**單一繼承**（推薦，簡單清晰）：
```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):  # Dog 只繼承 Animal
    def bark(self):
        print("Woof!")
```

**多重繼承**（強大但複雜）：
```python
class Flyable:
    def fly(self):
        print("Flying...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class Duck(Flyable, Swimmable):  # Duck 繼承兩個類別
    pass
```

### 2. MRO（Method Resolution Order）

Python 使用 C3 線性化算法決定方法查找順序：

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):  # 多重繼承
    pass

print(D.mro())  # [D, B, C, A, object]
d = D()
d.method()  # 輸出 "B"（依照 MRO 順序）
```

### 3. super() 的正確用法

| 情境 | 用法 | 說明 |
|:-----|:-----|:-----|
| 單一繼承 | `super().__init__()` | 呼叫父類別建構子 |
| 覆寫方法 | `super().method()` | 在擴展前先執行父類別邏輯 |
| 多重繼承 | `super()` 依照 MRO | 確保所有父類別被正確初始化 |

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **從現實類比切入**：
   - 動物分類（動物 → 哺乳類 → 犬科 → 狗）
   - 交通工具階層（車輛 → 汽車 → 電動車）

2. **先教單一繼承，再引入多重繼承**：
   - 單一繼承佔 90% 的實際應用
   - 多重繼承需謹慎使用

3. **強調 is-a vs has-a 關係**：
   - is-a → 使用繼承（Dog is an Animal）
   - has-a → 使用組合（Car has an Engine）

4. **實際操作演示**：
   - 用 `.mro()` 可視化繼承鏈
   - 逐步展示方法覆寫的效果

### 常見學生困難點

#### 困難點 1：忘記呼叫 super().__init__()
**症狀**：子類別覆寫 `__init__` 後，父類別的初始化沒有執行

**解決方法**：
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 必須呼叫！
        self.breed = breed
```

#### 困難點 2：混淆方法覆寫與方法重載
**症狀**：誤以為 Python 支援方法重載（Overloading）

**說明**：
- Python **不支援**傳統的方法重載（同名不同參數）
- 只支援方法覆寫（Overriding，同名同參數）
- 可用 `*args` 或預設參數模擬重載

#### 困難點 3：多重繼承的 MRO 混亂
**症狀**：不理解為什麼某個方法被呼叫

**解決方法**：
```python
# 隨時檢查 MRO
print(MyClass.mro())
print(MyClass.__mro__)

# 或使用 help()
help(MyClass)
```

#### 困難點 4：過度使用繼承
**症狀**：為了重用程式碼而建立不合理的繼承關係

**建議**：
- 遵循里氏替換原則（LSP）
- 優先考慮組合（Composition over Inheritance）
- 繼承應表達 is-a 關係，不只是程式碼重用

---

## 💡 設計原則（Design Principles）

### 1. 里氏替換原則（Liskov Substitution Principle, LSP）
> 子類別物件應該能替換父類別物件，而不影響程式正確性

**良好範例**：
```python
def process_animal(animal: Animal):
    animal.eat()  # 任何 Animal 子類別都能正確運作

dog = Dog("Buddy")
cat = Cat("Whiskers")
process_animal(dog)  # ✅ 正確
process_animal(cat)  # ✅ 正確
```

### 2. 組合優於繼承（Composition Over Inheritance）

**何時使用繼承**：
- is-a 關係明確（Dog is an Animal）
- 需要多型行為
- 共享核心邏輯

**何時使用組合**：
- has-a 關係（Car has an Engine）
- 需要動態改變行為
- 避免複雜的繼承鏈

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Classes - Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [super() built-in function](https://docs.python.org/3/library/functions.html#super)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### 推薦閱讀
- Martin, R. C. (2017). *Clean Architecture*, Chapter 9 (LSP)
- Gamma, E. et al. (1994). *Design Patterns*, Chapter 1 (Inheritance vs Composition)
- Ramalho, L. (2022). *Fluent Python* (2nd ed.), Chapter 14

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化繼承關係
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)

### 延伸主題（進階學習）
- Mixin 類別的應用
- 元類別（Metaclass）與繼承
- 協定（Protocol, PEP 544）作為 Duck Typing 的型態提示

---

## ❓ 常見問題（FAQ）

**Q1: Python 的多重繼承與 C++ 有何不同？**
A: Python 使用 MRO（C3 線性化算法）確保每個類別只被初始化一次，避免 C++ 的虛繼承問題。

**Q2: 什麼時候該用抽象基類（ABC）？**
A: 當你需要定義「介面規範」而非「實作細節」時。例如：定義所有形狀都必須有 `area()` 方法。

**Q3: super() 在多重繼承中如何運作？**
A: `super()` 不是呼叫「父類別」，而是呼叫 MRO 中的「下一個類別」。這確保協作式繼承（cooperative inheritance）。

**Q4: 如何避免菱形繼承問題？**
A:
1. 優先使用單一繼承
2. 使用 Mixin（只提供方法，不儲存狀態）
3. 確保所有類別都使用 `super()`

**Q5: isinstance() 和 type() 的區別？**
A:
- `isinstance(obj, Class)` - 考慮繼承關係（推薦）
- `type(obj) == Class` - 只檢查確切類別（過於嚴格）

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 16（類別基礎）**：定義類別與物件
- **Chapter 17（封裝）**：理解屬性的存取控制

### 後續章節
- **Chapter 19（特殊方法）**：透過繼承擴展運算子功能
- **Chapter 21（自訂例外）**：繼承 Exception 類別

### 對應的 Milestone 專案
- **Milestone 5: 銀行系統**（使用繼承建立不同帳戶類型）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 75%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能設計包含 3 層以上的繼承架構
- ✅ 能解釋 MRO 並預測方法呼叫結果
- ✅ 能判斷何時該用繼承、何時該用組合

---

**學習提醒**：繼承是強大的工具，但過度使用會導致耦合度過高。請謹慎設計類別階層！
