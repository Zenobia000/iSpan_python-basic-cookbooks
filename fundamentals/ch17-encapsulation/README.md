# Chapter 17: 封裝與資訊隱藏 | Encapsulation and Information Hiding

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (3/5) |
| **先備知識** | Chapter 16（類別與物件）|
| **相關章節** | Chapter 18（繼承與多型）、Chapter 19（特殊方法） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的存取控制約定（public, protected, private）
- **定義** 封裝、資訊隱藏、name mangling 的概念
- **說明** @property 裝飾器的作用與語法

### 理解面（Comprehension）
- **解釋** 為什麼需要封裝（資料保護、介面設計）
- **比較** 公開屬性、保護屬性、私有屬性的差異
- **歸納** property 與直接存取屬性的優缺點

### 應用面（Application）
- **運用** 私有屬性保護類別內部狀態
- **實作** 使用 @property 建立受控的屬性存取
- **解決** 需要驗證與計算的屬性設計問題

### 分析面（Analysis）
- **分析** 何時應該將屬性設為私有
- **診斷** 封裝設計的常見錯誤（過度封裝、錯誤的存取級別）
- **選擇** 適當的封裝策略（直接存取 vs getter/setter vs property）

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
封裝與資訊隱藏
├── 為什麼需要封裝？
│   ├── 保護資料完整性
│   ├── 控制存取方式
│   ├── 隱藏實作細節
│   └── 維護不變式（invariants）
│
├── Python 的存取控制約定
│   ├── Public（公開）- name
│   ├── Protected（保護）- _name
│   └── Private（私有）- __name
│
├── Name Mangling（名稱修飾）
│   ├── __name → _ClassName__name
│   ├── 避免子類別覆寫
│   └── 非真正的私有化
│
├── Property 裝飾器
│   ├── @property（getter）
│   ├── @name.setter（setter）
│   ├── @name.deleter（deleter）
│   └── 讓方法看起來像屬性
│
└── 封裝設計模式
    ├── Read-only properties（唯讀屬性）
    ├── Computed properties（計算屬性）
    ├── Validated properties（驗證屬性）
    └── Lazy properties（延遲計算）
```

### First Principles 解析

#### 為什麼需要封裝？

**根本問題**：如何防止外部代碼直接修改物件內部狀態，導致物件進入無效狀態？

**情境演示**：
```python
# 沒有封裝：銀行帳戶餘額可以被隨意修改
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # 公開屬性

account = BankAccount(1000)
account.balance = -500  # ❌ 可以設定為負數！這不合理
print(account.balance)  # -500
```

**使用封裝解決**：
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有屬性

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
# account.__balance = -500  # ❌ AttributeError（無法直接存取）
account.withdraw(200)  # ✅ 透過受控的方法操作
print(account.get_balance())  # 800
```

**推導過程**：
1. 直接存取屬性 → 可能違反業務規則
2. 隱藏內部實作 → 使用私有屬性（`__name`）
3. 提供受控介面 → 設計公開方法控制存取
4. 保持資料一致性 → 在方法中加入驗證邏輯

---

#### 為什麼需要 Property？

**根本問題**：如何在保持簡潔語法的同時，加入驗證與計算邏輯？

**演化過程**：
```python
# 階段 1：直接存取（無驗證）
class Person:
    def __init__(self, age):
        self.age = age

p = Person(25)
p.age = -10  # ❌ 可以設定為負數

# 階段 2：使用 getter/setter（語法繁瑣）
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value >= 0:
            self.__age = value

p = Person(25)
p.set_age(30)  # 語法不直觀
print(p.get_age())

# 階段 3：使用 @property（語法優雅 + 有驗證）
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("年齡不能為負數")

p = Person(25)
p.age = 30  # ✅ 像屬性一樣使用，但有驗證
print(p.age)  # 30
# p.age = -10  # ValueError
```

---

#### Name Mangling 的運作原理

**根本問題**：如何真正阻止屬性被外部存取？

**Python 的實作**：
```python
class MyClass:
    def __init__(self):
        self.__private = "secret"  # 私有屬性

obj = MyClass()
# print(obj.__private)  # AttributeError

# 實際上 Python 將 __private 改名為 _MyClass__private
print(obj._MyClass__private)  # "secret"（仍可存取，但不鼓勵）
```

**重要認知**：
- Python 沒有真正的私有化（與 Java/C++ 不同）
- `__name` 只是命名慣例 + name mangling
- 目的是防止意外存取，而非強制限制
- 「We're all consenting adults here」原則

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 封裝 | Encapsulation | 將資料與操作資料的方法綁定在一起，隱藏內部實作細節 |
| 資訊隱藏 | Information Hiding | 隱藏物件內部狀態，只透過公開介面存取 |
| 公開屬性 | Public Attribute | 無前綴，可自由存取的屬性（`name`） |
| 保護屬性 | Protected Attribute | 單底線前綴，約定為內部使用（`_name`） |
| 私有屬性 | Private Attribute | 雙底線前綴，觸發 name mangling（`__name`） |
| 名稱修飾 | Name Mangling | Python 自動將 `__name` 改為 `_ClassName__name` |
| 屬性裝飾器 | Property Decorator | 使方法像屬性一樣存取（`@property`） |
| Getter | Getter | 取得屬性值的方法 |
| Setter | Setter | 設定屬性值的方法 |
| Deleter | Deleter | 刪除屬性的方法 |
| 唯讀屬性 | Read-only Property | 只有 getter，無 setter 的屬性 |
| 計算屬性 | Computed Property | 每次存取時重新計算的屬性 |
| 驗證屬性 | Validated Property | 設定時進行驗證的屬性 |
| 不變式 | Invariant | 物件必須始終滿足的條件 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（8 個範例） | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（10 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（15 題） | 60 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（25 題） | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（20 min）：閱讀本 README，理解封裝的必要性
2. **上課**（90 min）：
   - 講義學習（60 min）：`01-lecture.ipynb`
   - 範例演練（30 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（60 min）：
   - 完成習題（45 min）：`04-exercises.ipynb`
   - 對照解答（15 min）：`05-solutions.ipynb`
5. **自我測驗**（20 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能區分 public、protected、private 屬性的命名慣例
- [ ] 能使用 `__name` 建立私有屬性
- [ ] 能使用 `@property` 建立 getter
- [ ] 能使用 `@name.setter` 建立 setter

### 進階能力
- [ ] 能理解 name mangling 的運作機制
- [ ] 能設計唯讀屬性（只有 getter）
- [ ] 能設計計算屬性（動態計算值）
- [ ] 能在 setter 中加入驗證邏輯
- [ ] 能使用 `@property` 重構現有類別

### 應用能力
- [ ] 能判斷哪些屬性應該設為私有
- [ ] 能設計合理的類別封裝介面
- [ ] 能在實際專案中運用封裝原則
- [ ] 能解釋封裝帶來的維護性優勢
- [ ] 能避免過度封裝與過度暴露

---

## 📝 理論重點（Key Theoretical Points）

### 1. Python 的存取控制約定

| 慣例 | 語法 | 意義 | 存取方式 |
|:-----|:-----|:-----|:---------|
| **Public** | `name` | 公開屬性，自由存取 | `obj.name` |
| **Protected** | `_name` | 保護屬性，約定為內部使用 | `obj._name`（不建議） |
| **Private** | `__name` | 私有屬性，觸發 name mangling | `obj._ClassName__name`（極不建議） |

**重要提醒**：
- Python 沒有真正的私有化（與 Java/C++ 不同）
- 這些是**命名慣例**，依賴開發者自律
- 「We're all consenting adults here」哲學

---

### 2. Property 裝飾器語法

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """Getter：取得值"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter：設定值（可加驗證）"""
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("值不能為負數")

    @value.deleter
    def value(self):
        """Deleter：刪除屬性"""
        del self._value
```

**使用方式**：
```python
obj = MyClass(10)
print(obj.value)  # 呼叫 getter
obj.value = 20    # 呼叫 setter
del obj.value     # 呼叫 deleter
```

---

### 3. 封裝的四種常見模式

#### 模式 1：唯讀屬性（Read-only）
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        """唯讀屬性：面積（沒有 setter）"""
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.53975
# c.area = 100  # AttributeError（無法設定）
```

#### 模式 2：計算屬性（Computed）
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        """每次存取時重新計算"""
        return self._width * self._height

r = Rectangle(4, 5)
print(r.area)  # 20
r._width = 6
print(r.area)  # 30（自動更新）
```

#### 模式 3：驗證屬性（Validated）
```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """設定時驗證"""
        if not isinstance(value, int):
            raise TypeError("年齡必須是整數")
        if value < 0 or value > 150:
            raise ValueError("年齡必須在 0-150 之間")
        self._age = value
```

#### 模式 4：延遲計算（Lazy）
```python
class DataProcessor:
    def __init__(self, data):
        self._data = data
        self._result = None

    @property
    def result(self):
        """第一次存取時才計算"""
        if self._result is None:
            print("計算中...")
            self._result = sum(self._data)  # 昂貴的計算
        return self._result
```

---

### 4. Name Mangling 詳解

```python
class Parent:
    def __init__(self):
        self.__private = "parent secret"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = "child secret"  # 不會覆寫父類別的 __private

c = Child()
print(c._Parent__private)  # "parent secret"
print(c._Child__private)   # "child secret"
```

**運作機制**：
- `__private` → `_ClassName__private`
- 避免子類別意外覆寫父類別的私有屬性
- 仍可透過修飾後的名稱存取（但不應該這麼做）

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從實際問題切入**：
   - 先展示無封裝的問題（銀行帳戶餘額被隨意修改）
   - 再介紹封裝如何解決問題
   - 強調「保護資料完整性」的重要性

2. **逐步演化教學法**：
   - 第一階段：公開屬性的風險
   - 第二階段：私有屬性 + getter/setter
   - 第三階段：@property 的優雅語法
   - 第四階段：進階模式（唯讀、計算、驗證）

3. **對比其他語言**：
   - Python vs Java/C++（真正的 private）
   - 強調 Python 的「成人哲學」
   - 說明慣例的重要性（`_name`, `__name`）

4. **實際案例演示**：
   - BankAccount（餘額驗證）
   - User（密碼加密）
   - Temperature（單位轉換）
   - Rectangle（計算面積）

---

### 常見學生困難點

#### 困難點 1：不理解為何需要封裝

**症狀**：認為「直接存取屬性更簡單」

**解決方法**：
- 展示無驗證導致的錯誤資料
- 說明未來需求變更時的維護成本
- 舉例：如果年齡欄位改為「出生日期」，有封裝的類別只需修改內部實作

**實例對比**：
```python
# 無封裝：未來需求變更時，所有使用處都要改
person.age = 25

# 有封裝：只需修改 property 內部邏輯
@property
def age(self):
    # 可以從出生日期計算
    return datetime.now().year - self._birth_year
```

---

#### 困難點 2：混淆 `_name` 與 `__name`

**症狀**：不知何時用單底線、何時用雙底線

**解決方法**：
- **單底線 `_name`**：約定為內部使用，但可存取（建議用於「不希望外部直接用，但也不強制阻止」）
- **雙底線 `__name`**：觸發 name mangling，避免子類別覆寫（建議用於「真正需要隔離的屬性」）

**建議規則**：
- 預設使用 `_name`（90% 的情況）
- 只在需要避免繼承衝突時使用 `__name`

---

#### 困難點 3：Property 裝飾器語法混淆

**症狀**：不理解為何 setter 用 `@name.setter` 而非 `@setter`

**教學策略**：
```python
# 第一步：定義 getter（創建 property 物件）
@property
def age(self):
    return self._age

# 第二步：在同一個 property 物件上定義 setter
@age.setter  # 使用 age 這個 property 物件的 setter 方法
def age(self, value):
    self._age = value
```

**記憶口訣**：「先用 `@property` 建立屬性，再用 `@屬性名.setter` 擴充功能」

---

#### 困難點 4：過度封裝

**症狀**：將所有屬性都設為私有，即使不需要驗證

**解決方法**：
- 強調「Pythonic」哲學：預設公開，必要時才封裝
- 規則：如果屬性需要驗證、計算、或隱藏實作，才使用 property
- 範例：簡單的 `Point` 類別的 x, y 座標不需要封裝

**良好設計**：
```python
# ✅ 簡單資料類別：公開屬性
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ✅ 需要驗證：使用 property
class BankAccount:
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("餘額不能為負數")
        self._balance = value
```

---

## 💡 學習技巧（Learning Strategies）

### 封裝設計決策樹

```
是否需要對屬性進行控制？
├─ 否 → 使用公開屬性（self.name）
└─ 是
   ├─ 只需驗證/計算？ → 使用 @property
   ├─ 需要隱藏實作？ → 使用 _name + @property
   └─ 需要避免繼承衝突？ → 使用 __name
```

### 命名慣例記憶法

- **無底線**：公開給所有人（Public）
- **單底線**：內部使用，請勿碰（Protected）
- **雙底線**：私有領域，子類別也別碰（Private）

### 實作練習建議

1. **重構練習**：將公開屬性改為 property
2. **驗證練習**：為不同類型屬性加入驗證邏輯
3. **計算屬性練習**：實作衍生屬性（如 BMI、面積、全名）
4. **唯讀屬性練習**：設計只能讀取的屬性

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Property](https://docs.python.org/3/library/functions.html#property)
- [Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [Property Decorators](https://docs.python.org/3/howto/descriptor.html#properties)

### 推薦閱讀
- Lutz, M. (2013). *Learning Python* (5th ed.), Chapter 30: Class Design
- Ramalho, L. (2015). *Fluent Python*, Chapter 19: Dynamic Attributes and Properties
- Phillips, D. (2018). *Python 3 Object-Oriented Programming* (3rd ed.), Chapter 5: When to Use Object-Oriented Programming

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化 name mangling
- [Real Python: Properties](https://realpython.com/python-property/)

### 延伸主題（進階學習）
- **Descriptors**：更底層的屬性控制機制
- **__slots__**：限制屬性，節省記憶體
- **Data Classes**（Python 3.7+）：自動生成特殊方法
- **@cached_property**：快取計算結果

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候應該使用私有屬性？**

A: 遵循以下原則：
- **需要驗證**：確保資料有效性（如年齡 >= 0）
- **需要計算**：屬性值由其他屬性計算而來
- **隱藏實作**：內部實作可能變更，不希望外部依賴
- **維護不變式**：確保物件始終處於有效狀態

**Q2: `_name` 和 `__name` 有什麼區別？**

A:
- **`_name`（單底線）**：約定為內部使用，但可存取
  - 用於：不希望外部直接用，但也不強制限制
  - 範例：`_internal_cache`

- **`__name`（雙底線）**：觸發 name mangling
  - 用於：避免子類別意外覆寫
  - 範例：`__private_key`

**建議**：預設用 `_name`，只在真正需要隔離時用 `__name`

---

**Q3: Property 和直接屬性存取有什麼差別？**

A:
```python
# 直接屬性：簡單但無控制
obj.age = -10  # ❌ 可以設定無效值

# Property：語法簡潔 + 有控制
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value >= 0:
        self._age = value  # ✅ 有驗證

obj.age = 25  # 看起來像屬性，實際呼叫 setter
```

---

**Q4: 為什麼 Python 沒有真正的私有化？**

A: Python 的設計哲學：
- **「We're all consenting adults here」**：相信開發者的自律
- 靈活性優於強制限制
- 如果真需要存取內部屬性，應該允許（但要承擔風險）
- Name mangling 足以防止意外存取

---

**Q5: 何時使用 @property，何時使用 getter/setter 方法？**

A:
- **使用 @property**（建議）：
  - 屬性的取得/設定符合直覺
  - 想要優雅的語法（`obj.age = 25`）
  - 未來可能加入驗證邏輯

- **使用 getter/setter 方法**：
  - 操作比較複雜（如 `account.withdraw(100)`）
  - 語意上是「動作」而非「屬性」
  - 需要多個參數

---

**Q6: 如何重構現有類別，加入封裝？**

A: 步驟：
1. 將公開屬性改為 `_name`
2. 建立 `@property` getter（回傳 `_name`）
3. 建立 `@name.setter`，加入驗證邏輯
4. 測試確保外部使用方式不變

```python
# 重構前
class User:
    def __init__(self, age):
        self.age = age

# 重構後
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("年齡不能為負數")

# 外部使用方式不變
user = User(25)
user.age = 30  # 仍然可用，但現在有驗證
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 16**：類別與物件（封裝的基礎）
- **Chapter 12**：函式設計（方法的基礎）

### 後續章節
- **Chapter 18**：繼承與多型（封裝在繼承中的應用）
- **Chapter 19**：特殊方法與運算子重載（進階類別設計）
- **Chapter 20**：例外處理（在 setter 中拋出例外）

### 對應的 Milestone 專案
- **Milestone 5: 銀行系統**（整合 Ch16-19 的 OOP 技巧）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-06): 初版發布，完整的封裝與資訊隱藏教材

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 20/25）
- ✅ 能向他人解釋封裝的必要性
- ✅ 能在 15 分鐘內為類別加入適當的封裝
- ✅ 能識別並修正過度封裝或封裝不足的設計

---

**學習提醒**：封裝是 OOP 的核心原則之一，掌握封裝能讓您設計出更健壯、易維護的類別！
