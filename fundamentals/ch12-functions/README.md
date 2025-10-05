# Chapter 12: 函式設計基礎 | Function Fundamentals

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐☆☆☆ (2/5) |
| **先備知識** | Chapter 11（列表推導式），Chapter 7-10（資料結構） |
| **相關章節** | Chapter 13（作用域）、Chapter 14（高階函式）、Chapter 15（遞迴） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 函式的組成要素：def、參數、函式體、return
- **定義** 函式、參數、引數、回傳值的概念
- **說明** 位置參數、關鍵字參數、預設參數的差異

### 理解面（Comprehension）
- **解釋** 為什麼需要函式（代碼重用、模組化、抽象化）
- **比較** 純函式與有副作用的函式
- **歸納** 函式參數傳遞的規則與最佳實踐

### 應用面（Application）
- **運用** 函式封裝重複的代碼邏輯
- **實作** 具有多種參數型態的函式
- **解決** 需要函式化的實際問題（如計算、驗證、轉換）

### 分析面（Analysis）
- **分析** 何時應該將代碼抽取為函式
- **診斷** 函式設計的常見錯誤（忘記 return、可變預設值陷阱）
- **選擇** 適當的參數設計與回傳值策略

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
函式設計基礎
├── 函式定義與呼叫
│   ├── def 關鍵字
│   ├── 函式名稱與命名規範
│   ├── 函式體（縮排）
│   └── 呼叫語法
│
├── 參數與引數
│   ├── 位置參數（Positional Arguments）
│   ├── 關鍵字參數（Keyword Arguments）
│   ├── 預設參數（Default Parameters）
│   └── 參數傳遞機制
│
├── 回傳值
│   ├── return 語句
│   ├── 單一回傳值
│   ├── 多重回傳值（tuple unpacking）
│   └── None 回傳值
│
├── 函式文件
│   ├── Docstring 規範
│   ├── help() 函式
│   └── 註解與文件的區別
│
└── 函式設計原則
    ├── 單一職責原則
    ├── 純函式 vs 副作用
    ├── 輸入驗證
    └── 常見陷阱（可變預設值）
```

### First Principles 解析

#### 為什麼需要函式？

**根本問題**：程式中經常出現重複的代碼邏輯，如何避免複製貼上（DRY 原則：Don't Repeat Yourself）？

**最小實作**：
```python
# 沒有函式：重複代碼
celsius1 = 25
fahrenheit1 = celsius1 * 9/5 + 32
print(f"{celsius1}°C = {fahrenheit1}°F")

celsius2 = 30
fahrenheit2 = celsius2 * 9/5 + 32
print(f"{celsius2}°C = {fahrenheit2}°F")

# 使用函式：代碼重用
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"30°C = {celsius_to_fahrenheit(30)}°F")
```

**推導過程**：
1. 需要重複執行相同邏輯 → 抽取為可呼叫的單元
2. 需要處理不同輸入 → 設計參數接收外部資料
3. 需要返回計算結果 → 使用 return 語句
4. 需要在多處使用 → 賦予有意義的名稱

#### 為什麼需要參數？

**根本問題**：函式需要處理不同的輸入資料，如何靈活接收外部值？

**演化過程**：
```python
# 階段 1：無參數，功能固定
def greet():
    print("Hello, Alice!")  # 只能打招呼給 Alice

# 階段 2：位置參數，增加靈活性
def greet(name):
    print(f"Hello, {name}!")  # 可以打招呼給任何人

# 階段 3：預設參數，提供便利性
def greet(name="Guest"):
    print(f"Hello, {name}!")  # 未指定時使用預設值

greet("Bob")    # Hello, Bob!
greet()         # Hello, Guest!
```

#### 為什麼需要回傳值？

**根本問題**：函式計算的結果需要在外部使用，如何傳遞結果？

**對比說明**：
```python
# 只有副作用（print）：無法進一步使用結果
def add_print(a, b):
    print(a + b)

add_print(3, 5)  # 顯示 8，但無法儲存結果
result = add_print(3, 5)  # result 是 None

# 有回傳值：結果可重用
def add_return(a, b):
    return a + b

result = add_return(3, 5)  # result = 8
total = add_return(3, 5) * 2  # total = 16
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 函式 | Function | 封裝特定功能的可重用代碼塊 |
| 定義 | Definition | 使用 `def` 宣告函式的過程 |
| 呼叫 | Call/Invocation | 執行函式的操作（使用 `()` 語法） |
| 參數 | Parameter | 函式定義中的變數（形式參數） |
| 引數 | Argument | 呼叫函式時傳入的實際值（實際參數） |
| 位置參數 | Positional Argument | 依順序對應的參數 |
| 關鍵字參數 | Keyword Argument | 使用名稱指定的參數 |
| 預設參數 | Default Parameter | 具有預設值的參數 |
| 回傳值 | Return Value | 函式執行後返回的結果 |
| 函式簽名 | Function Signature | 函式名稱與參數列表的組合 |
| 文件字串 | Docstring | 函式的說明文件（`"""..."""`） |
| 純函式 | Pure Function | 無副作用且輸出僅依賴輸入的函式 |
| 副作用 | Side Effect | 函式對外部狀態的修改（如 print、修改全域變數） |
| None | None | Python 的空值，函式未使用 return 時的預設回傳值 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（8 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 40 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（18 題） | 100 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（28 題） | 25 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解函式的必要性
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
- [ ] 能使用 `def` 定義簡單函式
- [ ] 能正確呼叫函式並傳遞參數
- [ ] 能使用 `return` 回傳計算結果
- [ ] 能撰寫函式的 docstring

### 進階能力
- [ ] 能設計具有預設參數的函式
- [ ] 能同時使用位置參數與關鍵字參數
- [ ] 能實作回傳多個值的函式（tuple unpacking）
- [ ] 能區分純函式與有副作用的函式
- [ ] 能避免可變預設值陷阱（mutable default arguments）

### 應用能力
- [ ] 能根據需求設計函式的參數與回傳值
- [ ] 能重構重複代碼為函式
- [ ] 能撰寫清晰的函式文件
- [ ] 能使用 `help()` 查看函式說明
- [ ] 能在實際問題中合理運用函式

---

## 📝 理論重點（Key Theoretical Points）

### 1. 函式定義的語法結構

```python
def 函式名稱(參數1, 參數2, ...):
    """
    函式文件字串（Docstring）
    說明函式的功能、參數、回傳值
    """
    函式體（縮排的代碼）
    return 回傳值
```

**實例**：
```python
def calculate_area(length, width):
    """
    計算矩形面積

    參數:
        length (float): 矩形長度
        width (float): 矩形寬度

    回傳:
        float: 矩形面積
    """
    area = length * width
    return area
```

### 2. 參數傳遞的三種方式

| 方式 | 語法 | 特點 | 範例 |
|:-----|:-----|:-----|:-----|
| 位置參數 | `func(a, b)` | 依順序對應 | `greet("Alice", 25)` |
| 關鍵字參數 | `func(name=value)` | 明確指定參數名 | `greet(name="Alice", age=25)` |
| 混合使用 | 位置參數在前 | 位置參數必須在關鍵字參數之前 | `greet("Alice", age=25)` |

**重要規則**：
```python
# ✅ 正確
def greet(name, age, city="Taipei"):
    print(f"{name}, {age}, {city}")

greet("Alice", 25)                    # 位置參數
greet("Bob", age=30)                  # 混合使用
greet(name="Carol", age=28, city="NY")  # 全部使用關鍵字

# ❌ 錯誤
greet(age=25, "Alice")  # SyntaxError: 位置參數不能在關鍵字參數之後
```

### 3. 回傳值的四種情況

```python
# 情況 1：單一回傳值
def add(a, b):
    return a + b
result = add(3, 5)  # result = 8

# 情況 2：多重回傳值（實際是 tuple）
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder
q, r = divide(10, 3)  # q = 3, r = 1

# 情況 3：條件式回傳
def is_even(n):
    if n % 2 == 0:
        return True
    return False  # 或簡化為: return n % 2 == 0

# 情況 4：無明確 return（回傳 None）
def print_message(msg):
    print(msg)
    # 無 return 語句
result = print_message("Hello")  # result = None
```

### 4. 可變預設值陷阱（重要！）

```python
# ❌ 錯誤：使用可變物件作為預設值
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] ← 預期應該是 ['banana']

# ✅ 正確：使用 None 並在函式內初始化
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana'] ← 正確
```

**原因**：預設參數在函式定義時創建一次，多次呼叫共享同一個物件。

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從現實類比切入**：
   - 函式 = 工廠的生產線（輸入原料、處理、輸出產品）
   - 參數 = 生產線的設定參數
   - 回傳值 = 生產的產品

2. **強調 DRY 原則**：
   - 展示重複代碼的問題（維護困難、容易出錯）
   - 示範如何將重複邏輯抽取為函式

3. **逐步演化教學法**：
   - 從無參數無回傳值的函式開始
   - 逐步加入參數、回傳值、預設值
   - 最後講解進階主題（可變預設值陷阱）

4. **實際操作演示**：
   - 使用 `help()` 查看內建函式的文件
   - 故意製造常見錯誤（忘記 return、參數順序錯誤）
   - 使用 Python Tutor 視覺化函式呼叫過程

### 常見學生困難點

#### 困難點 1：忘記使用 return

**症狀**：函式執行了運算但無法取得結果

**錯誤示範**：
```python
def add(a, b):
    sum = a + b  # 計算了但沒有 return

result = add(3, 5)
print(result)  # None
```

**解決方法**：
- 強調 `print` 和 `return` 的區別
- `print`：顯示資訊（副作用）
- `return`：回傳結果（函式的輸出）

#### 困難點 2：參數與引數的混淆

**症狀**：不理解「定義時是參數，呼叫時是引數」

**教學策略**：
```python
# 定義時：name 和 age 是參數（Parameter）
def greet(name, age):
    print(f"Hello, {name}! You are {age}.")

# 呼叫時："Alice" 和 25 是引數（Argument）
greet("Alice", 25)
```

**記憶口訣**：
- **P**arameter = **P**laceholder（佔位符，在定義時）
- **A**rgument = **A**ctual value（實際值，在呼叫時）

#### 困難點 3：位置參數與關鍵字參數的順序

**症狀**：`greet(age=25, "Alice")` 導致 SyntaxError

**解決方法**：
- 明確規則：位置參數必須在關鍵字參數之前
- 建議初學者優先使用位置參數，除非需要跳過某些參數

#### 困難點 4：可變預設值的行為

**症狀**：多次呼叫函式時，預設列表累積了舊值

**教學重點**：
- 演示問題發生的過程
- 使用 `id()` 函式證明多次呼叫共享同一個列表
- 強調「預設值在定義時創建一次」的特性

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**函式定義四要素**：
- **D**ef：定義關鍵字
- **N**ame：函式名稱
- **P**arameters：參數列表
- **R**eturn：回傳值

**參數設計原則**：
- **必要參數**：無預設值，使用者必須提供
- **可選參數**：有預設值，使用者可省略

### 實作練習建議

1. **函式改寫練習**：將現有的直列代碼改寫為函式
2. **文件撰寫練習**：為每個函式撰寫清晰的 docstring
3. **測試導向練習**：先寫測試案例，再實作函式
4. **重構練習**：識別代碼中的重複部分並抽取為函式

### 除錯技巧

```python
# 使用 print 除錯函式
def calculate(a, b):
    print(f"DEBUG: a={a}, b={b}")  # 檢查參數值
    result = a * 2 + b
    print(f"DEBUG: result={result}")  # 檢查計算結果
    return result

# 使用 type() 檢查參數型態
def safe_divide(a, b):
    print(f"Type of a: {type(a)}, Type of b: {type(b)}")
    return a / b
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)

### 推薦閱讀
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 3: Functions
- Matthes, E. (2019). *Python Crash Course* (2nd ed.), Chapter 8: Functions
- Martin, R. C. (2008). *Clean Code*, Chapter 3: Functions

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化函式呼叫與變數作用域
- [Real Python: Functions](https://realpython.com/defining-your-own-python-function/)

### 延伸主題（進階學習）
- **Chapter 13**：變數作用域（Scope）與 LEGB 規則
- **Chapter 14**：高階函式（Higher-Order Functions）與 lambda
- **Chapter 15**：遞迴（Recursion）
- 函式註解（Function Annotations, PEP 484）
- 裝飾器（Decorators）基礎

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候應該將代碼寫成函式？**

A: 遵循以下原則：
- **重複性**：同樣的邏輯出現 2 次以上
- **獨立性**：代碼塊有明確的單一功能
- **可測試性**：需要單獨測試的邏輯
- **可讀性**：代碼塊過長，需要抽取以提升可讀性

**Q2: `print()` 和 `return` 有什麼區別？**

A:
- `print()`：輸出到螢幕（副作用），函式仍回傳 `None`
- `return`：將結果傳遞給呼叫者，可進一步使用

```python
def func1():
    print(42)  # 顯示 42，但回傳 None

def func2():
    return 42  # 不顯示，但回傳 42

x = func1()  # 螢幕顯示 42，x = None
y = func2()  # 螢幕無顯示，y = 42
```

**Q3: 為什麼要寫 docstring？**

A:
- 提供函式的使用說明（用途、參數、回傳值）
- 支援 `help()` 函式的自動文件生成
- 提升代碼的可維護性與協作效率
- 專業開發的標準實踐

**Q4: 函式可以沒有 return 語句嗎？**

A: 可以。沒有 `return` 的函式會自動回傳 `None`。這類函式通常用於執行副作用（如 print、檔案寫入）。

```python
def log_message(msg):
    print(f"[LOG] {msg}")
    # 無 return，等同於 return None
```

**Q5: 如何決定參數的順序？**

A: 最佳實踐：
1. 必要參數在前，可選參數（有預設值）在後
2. 常用的參數在前，不常用的在後
3. 相關聯的參數放在一起

```python
# 良好設計
def create_user(username, email, age=18, country="Taiwan"):
    pass

# 不佳設計
def create_user(country="Taiwan", username, email, age=18):  # SyntaxError
    pass
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 7-11**：資料結構（列表、字典等），函式常處理這些型態
- **Chapter 4-6**：控制流程，函式內部使用條件與迴圈

### 後續章節
- **Chapter 13**：變數作用域（Scope）與全域/區域變數
- **Chapter 14**：高階函式與 lambda 表達式
- **Chapter 15**：遞迴（函式呼叫自己）
- **Chapter 16**：類別與方法（物件導向的函式）

### 對應的 Milestone 專案
- **Milestone 4: 文字處理工具箱**（整合 Ch12-15 的函式設計技巧）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 75 分）
- ✅ 能向他人解釋函式的運作原理
- ✅ 能在 10 分鐘內設計並實作一個實用函式
- ✅ 能識別並重構重複代碼為函式

---

**學習提醒**：函式是程式設計的核心概念，幾乎所有後續主題都建立在函式之上。請務必透過大量練習建立扎實基礎！
