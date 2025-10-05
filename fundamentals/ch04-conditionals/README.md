# Chapter 4: 條件判斷 | Conditionals

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 2-3 小時 |
| **難度等級** | ⭐⭐ (基礎進階) |
| **先備知識** | Ch01 變數與資料型態、Ch02 運算子與表達式、Ch03 輸入輸出 |
| **對應里程碑** | Milestone 2: 猜數字遊戲 |

---

## 學習目標 | Learning Objectives

### 知識層次 (Knowledge)
- 理解條件判斷在程式邏輯中的角色
- 掌握 if/elif/else 的語法結構
- 認識比較運算子與邏輯運算子
- 了解 Python 縮排的重要性

### 理解層次 (Comprehension)
- 解釋布林值與條件表達式的關係
- 說明邏輯運算子的優先順序
- 區分巢狀條件與多重條件的差異
- 理解三元運算子的應用時機

### 應用層次 (Application)
- 使用 if 語句實作單一條件判斷
- 應用 elif/else 處理多重選擇邏輯
- 組合邏輯運算子解決複雜問題
- 實作巢狀條件處理層級邏輯

### 分析層次 (Analysis)
- 分析問題的決策流程
- 優化條件判斷的邏輯順序
- 辨識可簡化的條件結構
- 除錯常見的條件判斷錯誤

---

## 核心概念 | Key Concepts

### 概念地圖 | Concept Map

```
條件判斷 (Conditionals)
│
├─ 基本語法
│  ├─ if 語句 (單一條件)
│  ├─ if-else 語句 (二選一)
│  └─ if-elif-else 語句 (多選一)
│
├─ 條件表達式
│  ├─ 比較運算子 (>, <, >=, <=, ==, !=)
│  ├─ 邏輯運算子 (and, or, not)
│  ├─ 成員運算子 (in, not in)
│  └─ 身份運算子 (is, is not)
│
├─ 進階技巧
│  ├─ 巢狀條件 (Nested Conditionals)
│  ├─ 三元運算子 (Ternary Operator)
│  └─ 短路求值 (Short-circuit Evaluation)
│
└─ 最佳實踐
   ├─ 正確的縮排
   ├─ 可讀性優化
   └─ 邏輯簡化
```

### First Principles 解析

#### 1. 為什麼需要條件判斷？ | Why Do We Need Conditionals?

**第一原理**：程式需要根據不同情況做出不同決策。

**現實類比**：
```
如果下雨 → 帶雨傘
否則 → 不帶雨傘
```

**程式實現**：
```python
is_raining = True

if is_raining:
    print("帶雨傘")
else:
    print("不帶雨傘")
```

**本質**：條件判斷是程式的「決策機制」，讓程式具備智能行為。

#### 2. if 語句的最小實作 | Minimal Implementation of if

**語法結構**：
```python
if 條件表達式:
    執行區塊
```

**三個要素**：
1. `if` 關鍵字
2. 條件表達式（結果為 True/False）
3. 縮排的程式碼區塊

**範例**：
```python
age = 18

if age >= 18:
    print("已成年")
```

#### 3. elif 和 else 的設計哲學 | Design Philosophy

**問題**：如何處理多種情況？

**解決方案**：
- `else`：處理「其他所有情況」
- `elif`：處理「多個互斥條件」

```python
score = 85

if score >= 90:
    print("優秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

**邏輯流程**：從上到下依序檢查，找到第一個為真的條件就執行，其餘跳過。

#### 4. 縮排的重要性 | The Importance of Indentation

**Python 的設計理念**：使用縮排定義程式碼區塊（而非大括號）。

**正確**：
```python
if age >= 18:
    print("已成年")
    print("可以投票")
```

**錯誤**：
```python
if age >= 18:
print("已成年")  # IndentationError
```

**原則**：同一區塊的程式碼必須有相同的縮排層級（通常 4 個空格）。

---

## 課程教材 | Course Materials

### 檔案說明表 | File Descriptions

| 檔案名稱 | 用途 | 建議使用時機 |
|:---------|:-----|:-------------|
| `01-lecture.ipynb` | 主要教學內容，包含理論與範例 | 課前預習、課堂講解 |
| `02-worked-examples.ipynb` | 5 個詳解範例，逐步拆解 | 課堂示範、自學參考 |
| `03-practice.ipynb` | 15 題課堂練習 | 課堂實作、即時練習 |
| `04-exercises.ipynb` | 20 題課後作業 | 課後複習、自我挑戰 |
| `05-solutions.ipynb` | 完整解答 | 對照檢查、學習參考 |
| `quiz.ipynb` | 25 題自我測驗 | 章節結束後自我評估 |
| `README.md` | 本文件，章節總覽 | 了解學習路徑與目標 |

---

## 能力檢核清單 | Competency Checklist

完成本章後，你應該能夠：

### 基礎能力
- [ ] 正確使用 if 語句進行單一條件判斷
- [ ] 使用 if-else 實作二選一邏輯
- [ ] 使用 if-elif-else 實作多選一邏輯
- [ ] 正確使用 6 種比較運算子
- [ ] 理解並應用 and, or, not 邏輯運算子
- [ ] 寫出正確縮排的條件語句

### 進階能力
- [ ] 組合多個邏輯運算子解決複雜問題
- [ ] 實作巢狀條件處理層級邏輯
- [ ] 使用三元運算子簡化簡單判斷
- [ ] 理解短路求值的運作機制
- [ ] 優化條件判斷的執行順序

### 應用能力
- [ ] 分析現實問題並設計條件邏輯
- [ ] 除錯常見的條件判斷錯誤
- [ ] 實作成績系統、年齡分級等實際應用
- [ ] 整合前三章知識解決綜合問題

---

## 授課要點 | Teaching Tips

### 1. 教學流程建議

#### 第一節課（60 分鐘）
1. **引入動機（10 分鐘）**
   - 提問：「程式如何做決策？」
   - 現實案例：紅綠燈、ATM 提款

2. **基本語法（20 分鐘）**
   - if 單一條件
   - if-else 二選一
   - 比較運算子

3. **實作練習（20 分鐘）**
   - `03-practice.ipynb` 基礎題 1-6

4. **總結與預告（10 分鐘）**

#### 第二節課（60 分鐘）
1. **複習（10 分鐘）**
   - 快速回顧 if/else

2. **進階語法（25 分鐘）**
   - if-elif-else 多選一
   - 邏輯運算子
   - 巢狀條件

3. **綜合應用（20 分鐘）**
   - `02-worked-examples.ipynb` 範例 3, 4

4. **作業說明（5 分鐘）**

### 2. 常見困難與對策

| 困難點 | 學生表現 | 教學對策 |
|:-------|:---------|:---------|
| **縮排錯誤** | IndentationError 頻繁出現 | 強調 Tab vs 空格，示範正確縮排，使用編輯器顯示空白字元 |
| **邏輯運算子混淆** | and/or 用錯，條件判斷錯誤 | 真值表教學，多舉實例，設計對比練習 |
| **等號誤用** | 用 = 而非 == | 強調「賦值」vs「比較」，刻意製造錯誤示範 |
| **條件順序錯誤** | elif 順序不當導致邏輯錯誤 | 畫流程圖，說明「第一個為真就執行」原則 |
| **過度巢狀** | 巢狀過深，可讀性差 | 示範邏輯簡化技巧，提早 return/continue |

### 3. 教學技巧

#### 使用流程圖
```
開始
 ↓
輸入分數
 ↓
分數 >= 90? ─Yes→ 顯示「優秀」
 ↓ No
分數 >= 80? ─Yes→ 顯示「良好」
 ↓ No
分數 >= 60? ─Yes→ 顯示「及格」
 ↓ No
顯示「不及格」
 ↓
結束
```

#### 真值表教學
```
A     B     A and B    A or B
True  True     True      True
True  False    False     True
False True     False     True
False False    False     False
```

#### 現實案例類比
- 登入系統：帳號密碼都正確才能登入（and）
- 會員資格：VIP 或累積消費 > 10000 可享優惠（or）
- 門禁系統：非工作時間不能進入（not）

---

## 常見錯誤示範 | Common Mistakes

### 1. 縮排錯誤
```python
# ❌ 錯誤
if age >= 18:
print("已成年")  # IndentationError

# ✅ 正確
if age >= 18:
    print("已成年")
```

### 2. 等號誤用
```python
# ❌ 錯誤（賦值而非比較）
if age = 18:
    print("18 歲")

# ✅ 正確
if age == 18:
    print("18 歲")
```

### 3. 邏輯運算子誤用
```python
# ❌ 錯誤（語法錯誤）
if age >= 18 and <= 65:
    print("勞動人口")

# ✅ 正確
if age >= 18 and age <= 65:
    print("勞動人口")

# 🌟 更好（範圍比較）
if 18 <= age <= 65:
    print("勞動人口")
```

### 4. 條件順序錯誤
```python
# ❌ 錯誤（永遠不會執行 90+ 的情況）
if score >= 60:
    print("及格")
elif score >= 90:
    print("優秀")

# ✅ 正確（從大到小判斷）
if score >= 90:
    print("優秀")
elif score >= 60:
    print("及格")
```

---

## 延伸閱讀 | Further Reading

### 官方文件
- [Python Tutorial - More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [PEP 8 - Style Guide for Python Code (Indentation)](https://www.python.org/dev/peps/pep-0008/#indentation)

### 進階主題
- **短路求值 (Short-circuit Evaluation)**：`and` 和 `or` 的提前終止機制
- **海象運算子 (Walrus Operator, :=)**：Python 3.8+ 的條件賦值
- **模式匹配 (Pattern Matching)**：Python 3.10+ 的 `match-case` 語法

### 實戰應用
- 表單驗證邏輯
- 遊戲規則判斷
- 權限控制系統
- 數據過濾與分類

### 相關章節
- **Ch02 運算子與表達式**：深入理解比較與邏輯運算子
- **Ch05 迴圈 (Loops)**：條件判斷與迴圈的組合
- **Ch20 例外處理**：另一種處理異常情況的方式

---

## 學習資源 | Learning Resources

### 線上練習平台
- [LeetCode Easy Problems](https://leetcode.com/problemset/all/?difficulty=Easy)
- [HackerRank - Conditionals](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-conditionals)

### 視覺化工具
- [Python Tutor](http://pythontutor.com/)：視覺化程式執行流程

### 中文資源
- [菜鳥教程 - Python 條件語句](https://www.runoob.com/python3/python3-conditional-statements.html)

---

## 本章關鍵字 | Keywords

- 條件判斷 | Conditionals
- if 語句 | if Statement
- elif 語句 | elif Statement
- else 語句 | else Statement
- 比較運算子 | Comparison Operators
- 邏輯運算子 | Logical Operators
- 布林值 | Boolean
- 縮排 | Indentation
- 巢狀條件 | Nested Conditionals
- 三元運算子 | Ternary Operator
- 短路求值 | Short-circuit Evaluation
- 真值表 | Truth Table

---

**上一章**: [Ch03 輸入輸出與格式化](../ch03-input-output-and-formatting/)
**下一章**: [Ch05 迴圈基礎](../ch05-loops/)
**對應專案**: [Milestone 2: 猜數字遊戲](../../milestones/milestone02-guessing-game/)
