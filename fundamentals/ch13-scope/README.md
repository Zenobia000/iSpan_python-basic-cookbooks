# Chapter 13: 作用域與生命週期 | Scope and Lifetime

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (3/5) |
| **先備知識** | Chapter 12（函式設計基礎） |
| **相關章節** | Chapter 14（高階函式）、Chapter 15（遞迴）、Chapter 16（類別與封裝） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的四種作用域：Local、Enclosing、Global、Built-in
- **定義** 變數的生命週期（lifetime）與作用域（scope）的差異
- **說明** LEGB 規則的查找順序與優先權

### 理解面（Comprehension）
- **解釋** 為什麼需要作用域機制（避免名稱衝突、記憶體管理）
- **比較** 區域變數與全域變數的使用時機
- **歸納** global 和 nonlocal 關鍵字的適用場景

### 應用面（Application）
- **運用** LEGB 規則預測變數的查找結果
- **實作** 閉包（closure）函式並理解其應用
- **解決** 變數作用域相關的常見錯誤

### 分析面（Analysis）
- **分析** 函式內外變數的可見性與生命週期
- **診斷** UnboundLocalError 的成因並修正
- **選擇** 何時應避免使用 global（遵循良好設計原則）

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
作用域與生命週期
├── 作用域（Scope）
│   ├── Local（區域作用域）
│   │   ├── 函式內部定義的變數
│   │   └── 參數也是區域變數
│   ├── Enclosing（封閉作用域）
│   │   ├── 外層函式的作用域
│   │   └── 閉包的基礎
│   ├── Global（全域作用域）
│   │   ├── 模組層級的變數
│   │   └── global 關鍵字
│   └── Built-in（內建作用域）
│       ├── Python 內建函式與常數
│       └── 最低優先權
│
├── LEGB 規則
│   ├── 查找順序：Local → Enclosing → Global → Built-in
│   ├── 由內而外的搜索
│   └── 找到後立即停止
│
├── 變數生命週期
│   ├── 創建時機（賦值時）
│   ├── 銷毀時機（作用域結束時）
│   └── 與作用域的關係
│
├── global 和 nonlocal 關鍵字
│   ├── global：修改全域變數
│   ├── nonlocal：修改外層函式變數
│   └── 使用時機與陷阱
│
└── 閉包（Closure）
    ├── 內層函式捕獲外層變數
    ├── 保持狀態的機制
    └── 實際應用場景
```

### First Principles 解析

#### 為什麼需要作用域？

**根本問題**：如果所有變數都是全域的，會發生什麼問題？

**問題演示**：
```python
# 假設所有變數都是全域的（不良設計）
count = 0  # 全域變數

def add_numbers(a, b):
    result = a + b  # 如果是全域，會與其他地方的 result 衝突
    return result

def multiply_numbers(x, y):
    result = x * y  # 名稱衝突！覆蓋了上面的 result
    return result

# 問題：
# 1. 名稱衝突：不同函式可能使用相同變數名
# 2. 難以追蹤：無法確定變數在哪裡被修改
# 3. 記憶體浪費：所有變數永久存在
```

**作用域的解決方案**：
```python
# 使用作用域機制
def add_numbers(a, b):
    result = a + b  # result 是區域變數，只存在於此函式
    return result

def multiply_numbers(x, y):
    result = x * y  # 這是另一個獨立的 result
    return result

# 優點：
# 1. 無名稱衝突：每個函式有自己的命名空間
# 2. 易於追蹤：變數的影響範圍受限
# 3. 記憶體效率：函式執行完畢後，區域變數自動銷毀
```

**推導過程**：
1. **隔離性**：每個函式需要獨立的變數空間 → 引入區域作用域
2. **層次性**：程式有模組、函式、內層函式的層次 → 引入多層作用域
3. **可訪問性**：內層需要訪問外層的變數 → 引入作用域鏈（LEGB）
4. **修改控制**：明確指定是否修改外層變數 → 引入 global/nonlocal

#### 為什麼需要 LEGB 規則？

**根本問題**：當多個作用域有同名變數時，Python 如何決定使用哪一個？

**LEGB 查找順序**：
```python
x = "global"  # Global

def outer():
    x = "enclosing"  # Enclosing

    def inner():
        x = "local"  # Local
        print(x)  # 輸出 "local"（最內層優先）

    inner()

outer()

# 查找順序：
# 1. Local（區域）：先找 inner 內部的 x
# 2. Enclosing（封閉）：如果沒有，找 outer 的 x
# 3. Global（全域）：如果沒有，找模組層級的 x
# 4. Built-in（內建）：如果沒有，找 Python 內建名稱
```

**為什麼是 L → E → G → B 順序？**
- **最近原則**：最接近的變數最相關（減少意外修改）
- **安全性**：優先使用區域變數（避免全域污染）
- **直覺性**：符合人類「由內而外」的思考方式

#### 為什麼需要閉包（Closure）？

**根本問題**：如何讓函式「記住」某些狀態？

**最小實作**：
```python
# 問題：如何創建一個計數器？
# 方法 1：使用全域變數（不良設計）
counter = 0

def increment():
    global counter
    counter += 1
    return counter

# 問題：全域變數可被任何地方修改，不安全

# 方法 2：使用閉包（優雅設計）
def make_counter():
    count = 0  # 封閉變數

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# 使用
counter1 = make_counter()
counter2 = make_counter()  # 獨立的計數器

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1（獨立）
```

**閉包的優勢**：
1. **封裝性**：狀態被封裝在函式內，外部無法直接訪問
2. **獨立性**：每次呼叫 `make_counter()` 創建獨立的計數器
3. **持久性**：即使外層函式執行完畢，內層函式仍保有對變數的引用

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 作用域 | Scope | 變數名稱的可見範圍 |
| 生命週期 | Lifetime | 變數從創建到銷毀的時間段 |
| 區域作用域 | Local Scope | 函式內部定義的變數所在的作用域 |
| 全域作用域 | Global Scope | 模組層級定義的變數所在的作用域 |
| 封閉作用域 | Enclosing Scope | 外層函式的作用域（巢狀函式） |
| 內建作用域 | Built-in Scope | Python 內建名稱所在的作用域（如 `len`, `print`） |
| LEGB 規則 | LEGB Rule | Local → Enclosing → Global → Built-in 的查找順序 |
| 閉包 | Closure | 內層函式捕獲外層變數的機制 |
| global 關鍵字 | global Keyword | 在函式內宣告使用全域變數 |
| nonlocal 關鍵字 | nonlocal Keyword | 在內層函式宣告使用外層函式變數 |
| 命名空間 | Namespace | 名稱到物件的映射（字典形式） |
| 自由變數 | Free Variable | 閉包中捕獲的外層變數 |
| UnboundLocalError | UnboundLocalError | 在賦值前使用區域變數的錯誤 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（10 個範例） | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（15 題） | 60 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（22 題） | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（20 min）：閱讀本 README，理解作用域的必要性
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
- [ ] 能識別變數屬於哪種作用域（Local/Enclosing/Global/Built-in）
- [ ] 能使用 LEGB 規則預測變數查找結果
- [ ] 能理解變數的生命週期（何時創建、何時銷毀）
- [ ] 能解釋區域變數與全域變數的差異

### 進階能力
- [ ] 能正確使用 `global` 關鍵字修改全域變數
- [ ] 能正確使用 `nonlocal` 關鍵字修改外層函式變數
- [ ] 能診斷並修正 UnboundLocalError
- [ ] 能實作簡單的閉包函式
- [ ] 能理解閉包捕獲變數的機制

### 應用能力
- [ ] 能設計函式時合理規劃變數作用域
- [ ] 能避免不必要的全域變數使用
- [ ] 能使用閉包實作狀態保持（如計數器、累加器）
- [ ] 能在除錯時快速定位作用域相關問題
- [ ] 能評估何時使用閉包 vs 類別

---

## 📝 理論重點（Key Theoretical Points）

### 1. LEGB 規則詳解

```python
x = "global x"  # Global

def outer():
    x = "enclosing x"  # Enclosing

    def inner():
        x = "local x"  # Local
        print(x)  # 輸出：local x

    inner()

outer()

# 查找順序：
# L (Local)     → 先找 inner() 內的 x
# E (Enclosing) → 如果沒找到，找 outer() 的 x
# G (Global)    → 如果沒找到,找模組層級的 x
# B (Built-in)  → 如果沒找到，找 Python 內建名稱
```

### 2. global 關鍵字

```python
count = 0  # 全域變數

def increment():
    global count  # 宣告使用全域變數
    count += 1
    return count

print(increment())  # 1
print(increment())  # 2
print(count)        # 2（全域變數被修改）

# 注意事項：
# 1. 必須在使用前宣告 global
# 2. 僅當需要「修改」全域變數時才需要 global
# 3. 只是「讀取」全域變數不需要 global
```

### 3. nonlocal 關鍵字

```python
def outer():
    count = 0  # 外層函式變數

    def inner():
        nonlocal count  # 宣告使用外層變數
        count += 1
        return count

    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
```

### 4. 閉包的三個條件

```python
# 閉包必須滿足：
# 1. 有巢狀函式（inner function）
# 2. 內層函式引用外層函式的變數（自由變數）
# 3. 外層函式回傳內層函式

def make_multiplier(n):  # 外層函式
    def multiplier(x):   # 內層函式
        return x * n     # 引用外層變數 n
    return multiplier    # 回傳內層函式

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### 5. 常見陷阱：UnboundLocalError

```python
# ❌ 錯誤：先讀取後賦值
x = 10

def func():
    print(x)  # UnboundLocalError!
    x = 20    # Python 看到這行，判定 x 是區域變數

# ✅ 正確方法 1：只讀取
def func():
    print(x)  # 10（讀取全域變數，不需要 global）

# ✅ 正確方法 2：宣告 global
def func():
    global x
    print(x)  # 10
    x = 20    # 修改全域變數
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從問題切入**：
   - 先展示沒有作用域的混亂（所有變數全域）
   - 引出作用域的必要性（隔離、安全、記憶體管理）

2. **視覺化教學**：
   - 使用圖示展示作用域的層次結構
   - 使用 [Python Tutor](http://pythontutor.com/) 視覺化變數查找過程
   - 繪制 LEGB 查找路徑圖

3. **對比教學法**：
   - 對比區域變數 vs 全域變數
   - 對比 global vs nonlocal
   - 對比閉包 vs 類別（狀態保持）

4. **漸進式教學**：
   - 先講解單層函式的作用域
   - 再引入巢狀函式與 Enclosing 作用域
   - 最後講解閉包的應用

### 常見學生困難點

#### 困難點 1：UnboundLocalError 的理解

**症狀**：學生不理解為什麼會報錯

**錯誤示範**：
```python
x = 10

def add_to_x():
    print(x)  # UnboundLocalError!
    x = x + 5
    return x
```

**解決方法**：
- 解釋 Python 的「編譯時決策」：看到 `x = ...` 就判定 x 是區域變數
- 強調規則：在函式內賦值的變數，整個函式內都是區域變數
- 提供修正方案（使用 global 或改用不同變數名）

#### 困難點 2：global 和 nonlocal 的混淆

**症狀**：不知道何時用 global，何時用 nonlocal

**教學策略**：
```python
# global：修改「模組層級」的變數
x = 10  # 模組層級
def func():
    global x  # 使用 global
    x = 20

# nonlocal：修改「外層函式」的變數
def outer():
    x = 10  # 外層函式
    def inner():
        nonlocal x  # 使用 nonlocal
        x = 20
```

**記憶口訣**：
- **global**：跨越到「模組的全域」
- **nonlocal**：只到「上一層（非本地）」

#### 困難點 3：閉包的概念

**症狀**：不理解為什麼內層函式可以「記住」外層變數

**教學重點**：
```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c1 = make_counter()
c2 = make_counter()

print(c1())  # 1
print(c1())  # 2
print(c2())  # 1（為什麼是 1？）

# 解釋：
# 1. 每次呼叫 make_counter() 都創建新的 count 變數
# 2. increment 函式「捕獲」了對 count 的引用
# 3. 即使 make_counter() 執行完畢，count 仍存在（被引用）
```

**類比說明**：
- 閉包 = 函式 + 「背包」（裝著外層變數）
- 每個閉包都有自己的背包（獨立）

#### 困難點 4：何時應避免 global

**症狀**：學生過度使用 global

**教學原則**：
```python
# ❌ 不良設計：過度使用 global
total = 0

def add(x):
    global total
    total += x

# ✅ 良好設計：使用回傳值
def add(x, total):
    return total + x

total = 0
total = add(5, total)
```

**原則**：
1. 優先使用參數與回傳值
2. 只在必要時使用 global（如配置常數）
3. 考慮使用類別封裝狀態

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**LEGB 規則**：
- **L**ocal（本地優先）
- **E**nclosing（向外一層）
- **G**lobal（全域次之）
- **B**uilt-in（內建墊底）

**global vs nonlocal**：
- **global**：我要用「全球的」（模組層級）
- **nonlocal**：我要用「非本地的」（上一層函式）

### 實作練習建議

1. **預測輸出練習**：給定代碼，預測變數查找結果
2. **除錯練習**：修正 UnboundLocalError
3. **閉包實作練習**：實作計數器、累加器、記憶化函式
4. **代碼重構練習**：消除不必要的 global 變數

### 除錯技巧

```python
# 技巧 1：使用 locals() 和 globals() 檢視變數
def func():
    x = 10
    print(locals())   # 查看區域變數
    print(globals())  # 查看全域變數

# 技巧 2：使用 __closure__ 檢視閉包捕獲的變數
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter.__closure__)  # 查看閉包捕獲的變數
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Programming FAQ: What are the rules for local and global variables?](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)

### 推薦閱讀
- Beazley, D., & Jones, B. K. (2013). *Python Cookbook* (3rd ed.), Chapter 7: Functions
- Ramalho, L. (2015). *Fluent Python*, Chapter 7: Function Decorators and Closures
- Real Python: [Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化作用域與變數生命週期
- [Python Scope Visualizer](https://pythontutor.com/visualize.html)

### 延伸主題（進階學習）
- **Chapter 14**：高階函式與裝飾器（Decorators）
- **Chapter 15**：遞迴與作用域
- **Chapter 16**：類別的命名空間與屬性查找
- 裝飾器的閉包應用
- 生成器與作用域

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候需要使用 global？**

A: 僅在以下情況：
1. 需要在函式內**修改**模組層級的變數
2. 配置常數需要在初始化函式中設定
3. 注意：只是**讀取**全域變數不需要 global

**Q2: global 和 nonlocal 有什麼區別？**

A:
- **global**：宣告使用模組層級的全域變數
- **nonlocal**：宣告使用外層函式的變數（不包括全域）

```python
x = "global"

def outer():
    x = "enclosing"

    def inner1():
        global x  # 使用模組層級的 x
        print(x)  # global

    def inner2():
        nonlocal x  # 使用 outer 的 x
        print(x)  # enclosing
```

**Q3: 為什麼會發生 UnboundLocalError？**

A: Python 在函式編譯時，看到 `x = ...` 就判定 x 是區域變數。如果在賦值前嘗試讀取，就會報錯。

```python
x = 10

def func():
    print(x)  # 錯誤！Python 認為 x 是區域變數，但尚未賦值
    x = 20

# 解決方法：
def func():
    global x  # 明確宣告使用全域變數
    print(x)
    x = 20
```

**Q4: 閉包有什麼實際用途？**

A: 閉包的主要用途：
1. **數據隱藏**：封裝私有狀態
2. **工廠函式**：創建具有不同配置的函式
3. **裝飾器**：修改函式行為
4. **回調函式**：保持上下文狀態

**Q5: 如何判斷一個變數是區域還是全域？**

A: 規則：
1. 在函式內**賦值**的變數 → 區域變數
2. 只**讀取**的變數 → 按 LEGB 規則查找
3. 使用 `global` 或 `nonlocal` 宣告 → 依宣告決定

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12**：函式設計基礎（本章的函式知識基礎）
- **Chapter 7-11**：資料結構（閉包中常處理這些型態）

### 後續章節
- **Chapter 14**：高階函式（理解裝飾器需要作用域知識）
- **Chapter 15**：遞迴（遞迴中的作用域管理）
- **Chapter 16**：類別與封裝（類別的命名空間與作用域）

### 對應的 Milestone 專案
- **Milestone 4: 文字處理工具箱**（整合 Ch12-15 的函式設計技巧）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-06): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 75 分）
- ✅ 能向他人解釋 LEGB 規則
- ✅ 能在 10 分鐘內實作一個實用的閉包函式
- ✅ 能診斷並修正作用域相關錯誤

---

**學習提醒**：作用域是 Python 的核心機制，理解它將幫助您避免大量常見錯誤！請透過大量練習建立扎實基礎。
