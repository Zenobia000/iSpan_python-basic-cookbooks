# Chapter 2: 運算子與表達式 | Operators and Expressions

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐☆☆☆☆ (入門) |
| **先備知識** | Chapter 1（變數與資料型態） |
| **相關章節** | Chapter 3 (輸入輸出), Chapter 4 (條件判斷) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的三大運算子類別：算術、比較、邏輯運算子
- **定義** 表達式（expression）與陳述式（statement）的差異
- **識別** 運算子的優先順序（precedence）

### 理解面（Comprehension）
- **解釋** 為什麼需要不同類型的運算子
- **比較** `//`（整數除法）與 `/`（浮點除法）的差異
- **歸納** 短路求值（short-circuit evaluation）的原理

### 應用面（Application）
- **運用** 算術運算子進行數值計算
- **實作** 使用比較與邏輯運算子構建條件表達式
- **解決** 涉及多種運算子的複雜運算問題

### 分析面（Analysis）
- **分析** 運算子優先順序導致的計算結果
- **診斷** 型態不匹配導致的運算錯誤
- **評估** 何時需要使用括號改變運算順序

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
運算子與表達式
├── 運算子（Operators）
│   ├── 算術運算子（Arithmetic）
│   │   ├── 基本運算：+, -, *, /
│   │   ├── 進階運算：//, %, **
│   │   └── 一元運算：+x, -x
│   ├── 比較運算子（Comparison）
│   │   ├── 相等性：==, !=
│   │   └── 大小關係：<, >, <=, >=
│   └── 邏輯運算子（Logical）
│       ├── and（且）
│       ├── or（或）
│       └── not（非）
│
└── 表達式（Expressions）
    ├── 簡單表達式：3 + 5
    ├── 複合表達式：(3 + 5) * 2
    └── 布林表達式：age >= 18 and has_license
```

### First Principles 解析

#### 為什麼需要運算子？
**根本問題**：程式需要對資料進行計算與比較

**最小實作**：
```python
3 + 5  # 加法運算，結果為 8
```

**推導過程**：
1. 資料需要處理 → 需要運算規則
2. 運算規則需要符號 → 運算子誕生
3. 運算需要優先順序 → 括號與優先級

#### 為什麼需要表達式？
**根本問題**：複雜計算需要組合多個運算

**實例說明**：
```python
# 計算圓面積：π × r²
import math
radius = 5
area = math.pi * radius ** 2  # 表達式：組合 *, ** 運算子
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 運算子 | Operator | 執行特定運算的符號（如 +, -, *） |
| 運算元 | Operand | 參與運算的值或變數 |
| 表達式 | Expression | 可求值的程式碼片段 |
| 陳述式 | Statement | 執行特定動作的程式碼 |
| 優先順序 | Precedence | 運算子的執行先後次序 |
| 結合律 | Associativity | 相同優先級運算子的運算方向 |
| 短路求值 | Short-circuit Evaluation | and/or 在確定結果後即停止運算 |
| 整數除法 | Integer Division | 除法後取整數部分（// 運算子） |
| 取模 | Modulo | 除法後取餘數（% 運算子） |
| 指數 | Exponentiation | 次方運算（** 運算子） |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解運算子分類
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
- [ ] 能使用六種算術運算子：+, -, *, /, //, %
- [ ] 能使用六種比較運算子：==, !=, <, >, <=, >=
- [ ] 能使用三種邏輯運算子：and, or, not
- [ ] 能正確使用括號改變運算順序

### 進階能力
- [ ] 能計算包含 ** 的指數運算
- [ ] 能理解整數除法 // 與取模 % 的應用
- [ ] 能組合多個邏輯運算子構建複雜條件
- [ ] 能預測運算子優先順序的影響

### 應用能力
- [ ] 能撰寫數學公式（如BMI計算、溫度轉換）
- [ ] 能構建布林表達式進行條件判斷
- [ ] 能除錯運算順序錯誤
- [ ] 能優化運算表達式（利用短路求值）

---

## 📝 理論重點（Key Theoretical Points）

### 1. 運算子優先順序（由高到低）

| 優先級 | 運算子 | 說明 | 範例 |
|:-------|:-------|:-----|:-----|
| 1 | `**` | 指數 | `2 ** 3` → 8 |
| 2 | `+x`, `-x` | 一元正負 | `-5` |
| 3 | `*`, `/`, `//`, `%` | 乘除運算 | `10 / 2` → 5.0 |
| 4 | `+`, `-` | 加減運算 | `3 + 5` → 8 |
| 5 | `<`, `<=`, `>`, `>=`, `==`, `!=` | 比較 | `5 > 3` → True |
| 6 | `not` | 邏輯非 | `not True` → False |
| 7 | `and` | 邏輯且 | `True and False` → False |
| 8 | `or` | 邏輯或 | `True or False` → True |

**記憶口訣**：**括**號 **指**數 **乘除** **加減** **比** 邏輯（**not** → **and** → **or**）

### 2. 算術運算子詳解

```python
# 基本四則運算
print(10 + 3)   # 13  加法
print(10 - 3)   # 7   減法
print(10 * 3)   # 30  乘法
print(10 / 3)   # 3.333... 浮點除法（結果為 float）

# 進階運算
print(10 // 3)  # 3   整數除法（取商）
print(10 % 3)   # 1   取模（取餘數）
print(2 ** 3)   # 8   指數（2的3次方）

# 應用範例：判斷奇偶數
number = 17
is_even = (number % 2 == 0)  # False（奇數）
```

### 3. 比較運算子特性

```python
# 比較運算子回傳 bool 型態
print(5 > 3)       # True
print(5 == 5.0)    # True（不同型態可比較）
print("a" < "b")   # True（字串按字典序比較）

# 連鎖比較（Python 特有）
age = 25
print(18 <= age < 65)  # True
# 等同於：(18 <= age) and (age < 65)
```

### 4. 邏輯運算子與短路求值

```python
# and：兩者皆真才為真
print(True and True)    # True
print(True and False)   # False

# or：一者為真即為真
print(True or False)    # True
print(False or False)   # False

# not：取反
print(not True)         # False

# 短路求值（Short-circuit）
x = 10
print(x > 5 and x < 20)  # 若 x > 5 為 False，不會檢查 x < 20
print(x < 5 or x > 0)    # 若 x < 5 為 True，不會檢查 x > 0
```

### 5. 運算子的型態限制

✅ **允許的運算**：
```python
3 + 5          # int + int → int
3.0 + 5        # float + int → float
"hello" + "world"  # str + str → str（串接）
```

❌ **不允許的運算**：
```python
"3" + 5        # TypeError: 不能將 str 與 int 相加
True + "hello" # TypeError: 不能將 bool 與 str 相加
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從計算機類比切入**：
   - 運算子 = 計算機按鍵
   - 表達式 = 完整的計算式
   - 優先順序 = 按鍵順序規則

2. **視覺化運算順序**：
```python
# 使用括號拆解運算步驟
result = 2 + 3 * 4
# Step 1: 3 * 4 = 12
# Step 2: 2 + 12 = 14

# 錯誤理解（從左到右）
# Step 1: 2 + 3 = 5
# Step 2: 5 * 4 = 20  ❌ 錯誤！
```

3. **實際演示短路求值**：
```python
# 範例：避免除以零錯誤
x = 0
# 安全寫法（短路求值）
if x != 0 and 10 / x > 2:
    print("條件成立")
```

### 常見學生困難點

#### 困難點 1：整數除法 // 與取模 % 的理解
**症狀**：不理解 `10 // 3` 和 `10 % 3` 的用途

**解決方法**：
```python
# 現實情境：分配問題
total_cookies = 10
children = 3

cookies_per_child = total_cookies // 3  # 3 個（每人分到的）
leftover = total_cookies % 3            # 1 個（剩餘的）

print(f"每人分到 {cookies_per_child} 個，剩下 {leftover} 個")
```

#### 困難點 2：運算子優先順序混淆
**症狀**：`2 + 3 * 4` 誤算為 20

**解決方法**：
- **黃金法則**：**不確定時，加括號！**
```python
# 不確定優先級？
result = 2 + 3 * 4        # 能算對嗎？

# 明確寫出意圖
result = 2 + (3 * 4)      # 14（先乘後加）
result = (2 + 3) * 4      # 20（先加後乘）
```

#### 困難點 3：比較運算的型態陷阱
**症狀**：`"10" > "9"` 的結果出乎意料

**解決方法**：
```python
# 字串比較是字典序（lexicographic）
print("10" > "9")   # False（"1" < "9"）
print(10 > 9)       # True（數值比較）

# 教訓：比較前確保型態一致
print(int("10") > int("9"))  # True
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**算術運算子**（從基礎到進階）：
- **加減乘除** 最基本
- **整除取模** 分配問題
- **指數乘方** 科學計算

**邏輯運算子**（AND/OR/NOT）：
- **AND** 要求高：全真才真（嚴格）
- **OR** 很寬容：一真即真（寬鬆）
- **NOT** 很叛逆：真假顛倒（反轉）

### 實作練習建議

1. **運算實驗**：
```python
# 測試所有運算子組合
print(10 + 5, 10 - 5, 10 * 5, 10 / 5, 10 // 5, 10 % 5, 10 ** 2)
```

2. **優先順序測試**：
```python
# 預測結果，再執行驗證
print(2 + 3 * 4)        # 猜測 → 驗證
print(10 - 5 - 2)       # 猜測 → 驗證
print(2 ** 3 ** 2)      # 猜測 → 驗證
```

3. **真值表練習**：
```python
# 製作 AND/OR 真值表
for a in [True, False]:
    for b in [True, False]:
        print(f"{a} and {b} = {a and b}")
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Built-in Operators](https://docs.python.org/3/library/operator.html)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 2.2
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 5

### 互動式工具
- [Python Operator Precedence Table](https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html)
- [Real Python: Operators and Expressions](https://realpython.com/python-operators-expressions/)

### 延伸主題（進階學習）
- 位元運算子（Bitwise Operators）：&, |, ^, ~, <<, >>
- 賦值運算子（Assignment Operators）：+=, -=, *=, /=
- 身份運算子（Identity Operators）：is, is not
- 成員運算子（Membership Operators）：in, not in

---

## ❓ 常見問題（FAQ）

**Q1: 為什麼 `5 / 2` 結果是 2.5 而不是 2？**
A: Python 3 的 `/` 永遠執行浮點除法。若要整數除法，使用 `//`：`5 // 2` → 2。

**Q2: `-2 ** 2` 的結果是多少？**
A: 結果是 -4，因為 `**` 優先級高於 `-`，運算順序為 `-(2 ** 2)` = -4。若要 `(-2) ** 2` = 4，需加括號。

**Q3: `and` 和 `or` 可以用 `&` 和 `|` 取代嗎？**
A: 不建議。`&` 和 `|` 是位元運算子，語意不同。邏輯運算請用 `and`/`or`。

**Q4: 為什麼 `10 % 3` 是 1？**
A: `%` 是取餘數運算子。10 ÷ 3 = 3 餘 1，所以 `10 % 3` → 1。

**Q5: 如何記憶運算子優先順序？**
A: 與數學相同：括號 > 指數 > 乘除 > 加減。邏輯運算最後處理。**不確定時，加括號！**

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 1（變數與資料型態）**：提供運算的基本資料

### 後續章節
- **Chapter 3（輸入輸出）**：用表達式處理使用者輸入
- **Chapter 4（條件判斷）**：用布林表達式控制流程
- **Chapter 12（函式）**：用表達式計算回傳值

### 對應的 Milestone 專案
- **Milestone 1: 簡易計算機**（使用算術運算子實作四則運算）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能正確預測任意表達式的運算結果
- ✅ 能在 5 分鐘內寫出 BMI 計算程式

---

## 🧮 實用範例速查

### 單位換算
```python
# 溫度轉換：攝氏 → 華氏
celsius = 25
fahrenheit = celsius * 9 / 5 + 32  # 77.0

# 距離轉換：公里 → 英里
kilometers = 10
miles = kilometers * 0.621371  # 6.21371
```

### 數學計算
```python
# BMI 計算
weight_kg = 70
height_m = 1.75
bmi = weight_kg / (height_m ** 2)  # 22.86

# 圓面積
import math
radius = 5
area = math.pi * radius ** 2  # 78.54
```

### 條件判斷
```python
# 範圍檢查
age = 25
is_adult = age >= 18  # True
is_senior = age >= 65  # False

# 複合條件
score = 85
is_pass = score >= 60 and score <= 100  # True
```

---

**學習提醒**：運算子是程式設計的基本積木，請透過大量練習培養直覺！
