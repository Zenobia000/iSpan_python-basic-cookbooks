# Chapter 1: 變數與資料型態 | Variables and Data Types

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐☆☆☆☆ (入門) |
| **先備知識** | 無（本課程起點） |
| **相關章節** | 參見 Chapter 2 (運算子), Chapter 7 (資料結構) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的四種基本資料型態：int, float, str, bool
- **定義** 變數的概念與命名規則
- **說明** 動態型態（dynamic typing）的特性

### 理解面（Comprehension）
- **解釋** 為什麼程式需要不同的資料型態
- **比較** int 與 float 的差異與應用情境
- **歸納** 型態轉換的規則與限制

### 應用面（Application）
- **運用** 變數儲存與操作不同型態的資料
- **實作** 基本的型態檢查與轉換
- **解決** 涉及多種資料型態的簡單問題

### 分析面（Analysis）
- **分析** 型態錯誤（TypeError）的成因
- **診斷** 變數命名不當導致的問題
- **選擇** 適合特定情境的資料型態

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
變數與資料型態
├── 變數（Variables）
│   ├── 變數宣告與賦值
│   ├── 變數命名規則
│   └── 變數的可變性（mutability）
│
└── 資料型態（Data Types）
    ├── 數值型態
    │   ├── 整數（int）
    │   └── 浮點數（float）
    ├── 布林值（bool）
    └── 字串（str）
```

### First Principles 解析

#### 為什麼需要變數？
**根本問題**：程式需要在記憶體中儲存資料，並在後續使用

**最小實作**：
```python
x = 10  # 將數值 10 儲存在名為 x 的記憶體位置
```

**推導過程**：
1. 資料需要儲存 → 需要記憶體空間
2. 空間需要識別 → 需要名稱（變數名）
3. 名稱與資料綁定 → 賦值運算（=）

#### 為什麼需要型態？
**根本問題**：不同資料需要不同的儲存方式與操作規則

**實例說明**：
- `3 + 5` → 數學加法 = 8
- `"3" + "5"` → 字串串接 = "35"
- `3 + "5"` → TypeError（型態衝突）

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 變數 | Variable | 用於儲存資料值的命名容器 |
| 賦值 | Assignment | 將值綁定到變數的操作（使用 `=`） |
| 資料型態 | Data Type | 定義資料的類別與可執行的操作 |
| 整數 | Integer (int) | 不含小數點的數值 |
| 浮點數 | Floating-point (float) | 含小數點的數值 |
| 布林值 | Boolean (bool) | True 或 False 的邏輯值 |
| 字串 | String (str) | 文字資料的序列 |
| 型態轉換 | Type Casting | 將資料從一種型態轉換為另一種 |
| 動態型態 | Dynamic Typing | 變數型態在執行時期決定，可改變 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（10 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解學習目標
2. **上課**（90 min）：
   - 講義學習（60 min）：`01-lecture.ipynb`
   - 範例演練（30 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（90 min）：
   - 完成習題（60 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（20 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能宣告變數並賦予初值
- [ ] 能使用 `type()` 檢查變數型態
- [ ] 能正確命名變數（遵循 PEP 8）
- [ ] 能區分 int、float、str、bool 四種型態

### 進階能力
- [ ] 能進行型態轉換：int(), float(), str(), bool()
- [ ] 能理解隱式轉換（implicit conversion）與顯式轉換（explicit conversion）
- [ ] 能解釋動態型態的優缺點
- [ ] 能預測型態不匹配導致的錯誤

### 應用能力
- [ ] 能根據需求選擇合適的資料型態
- [ ] 能除錯型態相關的錯誤（TypeError）
- [ ] 能撰寫涉及多種型態的簡單程式（如單位轉換器）

---

## 📝 理論重點（Key Theoretical Points）

### 1. Python 的動態型態系統
```python
# Python 是動態型態語言
x = 10        # x 是 int
x = "hello"   # x 變成 str（允許改變型態）
x = 3.14      # x 變成 float

# 與靜態型態語言（如 C++）對比：
# int x = 10;      // x 永遠是 int
# x = "hello";     // 編譯錯誤！
```

### 2. 型態轉換規則
| 轉換 | 範例 | 結果 | 注意事項 |
|:-----|:-----|:-----|:---------|
| int → float | `float(10)` | `10.0` | 安全轉換 |
| float → int | `int(3.9)` | `3` | 會截斷小數（不是四捨五入） |
| str → int | `int("42")` | `42` | 字串必須是數字格式 |
| int → str | `str(42)` | `"42"` | 安全轉換 |
| bool → int | `int(True)` | `1` | True=1, False=0 |
| 任意 → bool | `bool(0)`, `bool("")` | `False` | 0、空字串、None 為 False |

### 3. 變數命名規範（PEP 8）
✅ **良好命名**：
```python
student_name = "Alice"       # 蛇形命名法（snake_case）
total_score = 95
is_passed = True             # 布林值以 is_/has_ 開頭
```

❌ **不良命名**：
```python
s = "Alice"                  # 過於簡短，語意不明
studentName = "Alice"        # 駝峰式（camelCase）不符合 Python 慣例
2nd_score = 80               # 不能以數字開頭
class = "A"                  # 不能使用保留字
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **從現實類比切入**：
   - 變數 = 貼有標籤的盒子
   - 型態 = 盒子裡東西的類別

2. **強調動態型態的雙面性**：
   - 優點：靈活、易上手
   - 缺點：執行時期才發現型態錯誤

3. **實際操作演示**：
   - 使用 Python REPL 即時展示 `type()` 的結果
   - 故意製造 TypeError 讓學生觀察錯誤訊息

### 常見學生困難點

#### 困難點 1：int 與 float 的混淆
**症狀**：不理解 `3` 與 `3.0` 的區別

**解決方法**：
```python
print(3 / 2)     # 1.5 (float)
print(3 // 2)    # 1 (int，整數除法)
print(type(3 / 2))   # <class 'float'>
```

#### 困難點 2：型態轉換的陷阱
**症狀**：`int("3.14")` 會報錯，但 `int(3.14)` 不會

**解決方法**：
```python
# 錯誤示範
int("3.14")  # ValueError

# 正確做法
int(float("3.14"))  # 3

# 或直接處理字串
float("3.14")  # 3.14
```

#### 困難點 3：動態型態的誤用
**症狀**：在同一個變數中存放不同型態，造成混亂

**建議**：
- 初學階段避免變數重新賦值為不同型態
- 使用有意義的變數名，暗示型態（如 `count` 暗示 int）

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **I**nt：整數無小數（**I**nteger）
- **F**loat：浮動有小數（**F**loating）
- **S**tr：字串加引號（**S**tring）
- **B**ool：True/False 布林值（**B**oolean）

### 實作練習建議
1. **型態探索**：對各種值使用 `type()`，建立直覺
2. **轉換實驗**：嘗試所有可能的型態轉換組合
3. **錯誤收集**：記錄遇到的 TypeError，分析原因

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 命名規範](https://peps.python.org/pep-0008/#naming-conventions)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 2.1
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 2

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化變數與型態
- [Real Python: Variables](https://realpython.com/python-variables/)

### 延伸主題（進階學習）
- 複數型態（complex）
- None 型態的特殊性
- 型態提示（Type Hints, PEP 484）

---

## ❓ 常見問題（FAQ）

**Q1: Python 的動態型態與 JavaScript 有何不同？**
A: Python 是強型態（strong typing），不允許隱式的型態轉換（如 `"3" + 5` 會報錯）；JavaScript 是弱型態，會自動轉換（結果為 `"35"`）。

**Q2: 為什麼 `int(3.9)` 是 3 而不是 4？**
A: `int()` 執行的是截斷（truncation），不是四捨五入。如需四捨五入，使用 `round(3.9)`。

**Q3: 變數名稱可以使用中文嗎？**
A: 技術上可以（Python 3 支援 Unicode），但不建議。國際協作時會造成困擾，應使用英文命名。

**Q4: `=` 和 `==` 有什麼區別？**
A: `=` 是賦值運算子（assignment），`==` 是比較運算子（comparison）。這會在 Chapter 2 詳細說明。

---

## 📊 本章與課程架構的關係

### 前置章節
- 無（本章是課程起點）

### 後續章節
- **Chapter 2（運算子）**：使用變數進行運算
- **Chapter 7（列表）**：多個變數的集合管理
- **Chapter 12（函式）**：變數作為函式參數

### 對應的 Milestone 專案
- **Milestone 1: 簡易計算機**（結合 Ch1-3 的知識）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能向他人解釋變數與型態的概念
- ✅ 能在 5 分鐘內寫出一個簡單的型態轉換程式

---

**學習提醒**：程式設計是一門需要大量練習的技能。請確保完成所有練習題，不要只是閱讀解答！
