# Chapter 5: 迴圈控制 | Loops

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3-4 小時 |
| **難度等級** | ⭐⭐⭐ (中等) |
| **先備知識** | Ch01 變數與資料型態、Ch02 運算子、Ch03 輸入輸出、Ch04 條件判斷 |
| **學習目標** | 掌握 Python 迴圈控制結構，能使用 for/while 解決重複性任務 |

## 學習目標 | Learning Objectives

### 知識層次 (Knowledge)
- [ ] 理解迴圈的運作原理與執行流程
- [ ] 認識 for 迴圈與 while 迴圈的差異
- [ ] 理解 range() 函式的三種用法
- [ ] 了解 break、continue、else 在迴圈中的作用

### 理解層次 (Comprehension)
- [ ] 能夠說明何時使用 for 迴圈，何時使用 while 迴圈
- [ ] 能夠解釋巢狀迴圈的執行順序
- [ ] 能夠識別無窮迴圈的成因與預防方法
- [ ] 能夠分析迴圈的迭代次數

### 應用層次 (Application)
- [ ] 能夠使用 for 迴圈遍歷序列資料
- [ ] 能夠使用 while 迴圈處理未知次數的重複
- [ ] 能夠使用 break/continue 控制迴圈流程
- [ ] 能夠使用巢狀迴圈解決二維問題

### 分析層次 (Analysis)
- [ ] 能夠選擇適當的迴圈類型解決問題
- [ ] 能夠優化迴圈效率與可讀性
- [ ] 能夠除錯常見的迴圈錯誤
- [ ] 能夠設計防護機制避免無窮迴圈

## 核心概念 | Key Concepts

### 概念地圖

```
迴圈控制 (Loops)
├── for 迴圈
│   ├── 基本語法
│   ├── range() 函式
│   │   ├── range(stop)
│   │   ├── range(start, stop)
│   │   └── range(start, stop, step)
│   └── 遍歷可迭代物件
│       ├── 字串
│       ├── 列表
│       └── 其他序列
├── while 迴圈
│   ├── 基本語法
│   ├── 條件控制
│   └── 無窮迴圈防護
├── 迴圈控制語句
│   ├── break (中斷迴圈)
│   ├── continue (跳過本次)
│   └── else (正常結束執行)
├── 巢狀迴圈
│   ├── 雙層迴圈
│   └── 多層迴圈
└── 常見模式
    ├── 累加器 (Accumulator)
    ├── 計數器 (Counter)
    ├── 旗標變數 (Flag)
    └── 哨兵值 (Sentinel)
```

### First Principles 解析

#### 1. 為什麼需要迴圈？

**問題**：如果要印出 1 到 100 的數字，該怎麼做？

**原始方法**（沒有迴圈）：
```python
print(1)
print(2)
print(3)
# ... 重複 100 次？
```
這種方法有三個問題：
- **冗長**：需要寫 100 行重複的程式碼
- **難以維護**：如果要改成 1000，需要重寫
- **容易出錯**：手動複製容易遺漏或打錯

**迴圈方法**：
```python
for i in range(1, 101):
    print(i)
```

**First Principle**：迴圈是「自動化重複」的抽象概念。它將「做某事 N 次」這個需求，用一個簡潔的控制結構表達。

#### 2. for 迴圈 vs while 迴圈：何時用哪個？

**核心差異**：

| 特性 | for 迴圈 | while 迴圈 |
|:-----|:---------|:-----------|
| **用途** | 已知迭代次數或範圍 | 未知迭代次數，基於條件 |
| **語法重點** | 遍歷可迭代物件 | 檢查布林條件 |
| **典型場景** | 遍歷資料、固定次數 | 等待輸入、條件滿足 |
| **例子** | 處理列表的每個元素 | 猜數字直到猜對 |

**First Principle**：
- **for** = "對每個東西做某事" (iteration over collection)
- **while** = "只要條件成立就做某事" (conditional repetition)

#### 3. break 與 continue 的本質

**問題**：如何在迴圈中間提前結束或跳過？

**break**：立即跳出整個迴圈
```python
for i in range(10):
    if i == 5:
        break  # 找到 5 就停止
    print(i)
# 輸出：0 1 2 3 4
```

**continue**：跳過本次迭代，繼續下一次
```python
for i in range(10):
    if i % 2 == 0:
        continue  # 跳過偶數
    print(i)
# 輸出：1 3 5 7 9
```

**First Principle**：break 和 continue 提供「提前決策」的能力，讓迴圈不必完整執行所有迭代，增加效率和邏輯彈性。

#### 4. 迴圈中的 else 子句

Python 獨特設計：迴圈可以有 else 子句
```python
for i in range(5):
    if i == 10:
        break
else:
    print("迴圈正常結束")  # 沒有 break 才執行
```

**First Principle**：else 回答「迴圈是否完整執行完畢？」這個問題。它區分「自然結束」和「被 break 中斷」兩種情況。

#### 5. 無窮迴圈的危險與防護

**危險範例**：
```python
while True:
    print("永遠不會停止")  # 無窮迴圈！
```

**防護機制**：
```python
count = 0
max_iterations = 1000

while True:
    count += 1
    if count > max_iterations:
        print("達到最大迭代次數，強制中斷")
        break
    # 正常邏輯
```

**First Principle**：所有迴圈都應該有「終止條件」(termination condition)。設計迴圈時，必須確保條件最終會變成 False，或有 break 語句提供退出路徑。

## 課程教材 | Course Materials

| 檔案 | 說明 | 預估時間 |
|:-----|:-----|:---------|
| `01-lecture.ipynb` | 主講義：迴圈理論與 10+ 範例 | 90 分鐘 |
| `02-worked-examples.ipynb` | 詳解範例：5 個完整解題流程 | 45 分鐘 |
| `03-practice.ipynb` | 課堂練習：15 題即時演練 | 60 分鐘 |
| `04-exercises.ipynb` | 課後習題：20 題作業 | 90 分鐘 |
| `05-solutions.ipynb` | 完整解答 | 參考用 |
| `quiz.ipynb` | 自我測驗：25 題檢測 | 30 分鐘 |

**總計**：約 3-4 小時核心學習 + 1.5 小時練習

## 能力檢核清單 | Competency Checklist

### 基礎能力
- [ ] 能寫出正確的 for 迴圈語法
- [ ] 能使用 range(n)、range(start, stop)、range(start, stop, step)
- [ ] 能寫出正確的 while 迴圈語法
- [ ] 能使用 break 中斷迴圈
- [ ] 能使用 continue 跳過迭代
- [ ] 能遍歷字串的每個字元

### 進階能力
- [ ] 能在 for 和 while 之間選擇合適的迴圈類型
- [ ] 能使用累加器模式計算總和/乘積
- [ ] 能使用旗標變數控制迴圈狀態
- [ ] 能寫出正確的巢狀迴圈
- [ ] 能使用迴圈的 else 子句
- [ ] 能識別並預防無窮迴圈

### 挑戰能力
- [ ] 能用迴圈實作數學數列（階乘、Fibonacci）
- [ ] 能用巢狀迴圈繪製圖案
- [ ] 能結合條件判斷與迴圈解決複雜問題
- [ ] 能優化迴圈效率（提前 break）
- [ ] 能除錯複雜的迴圈邏輯錯誤

## 教學建議 | Teaching Tips

### 授課要點

1. **從具體到抽象**
   - 先展示「手動重複」的痛苦（印 100 個數字）
   - 再引入迴圈作為解決方案
   - 強調「自動化」的價值

2. **視覺化執行流程**
   - 使用 Python Tutor 展示迴圈執行過程
   - 畫出流程圖說明 for/while 的差異
   - 特別展示 break/continue 的跳躍行為

3. **實作優先**
   - 每個概念講完立即寫範例
   - 鼓勵學生預測輸出再執行
   - 常見錯誤現場演示（無窮迴圈、縮排錯誤）

4. **對比教學**
   - 同一問題用 for 和 while 兩種方式實作
   - 比較有 break 和沒有 break 的差異
   - 展示巢狀迴圈 vs 單層迴圈的適用場景

### 常見學習困難

| 困難點 | 原因 | 解決策略 |
|:-------|:-----|:---------|
| **range() 不直觀** | range(5) 不包含 5 | 強調「到達但不包含」，用數軸圖示 |
| **無窮迴圈** | while 條件永遠為 True | 教授「防護計數器」模式，限制最大迭代次數 |
| **巢狀迴圈困惑** | 搞不清楚哪層先執行 | 用「外層轉一圈，內層轉完整圈」類比時鐘 |
| **break vs continue** | 分不清楚差異 | 用「離開建築物」(break) vs「跳過這層樓」(continue) 比喻 |
| **迭代變數誤用** | 在迴圈內修改 i | 警告：修改迭代變數不會影響迴圈次數（for 的情況） |

### 教學節奏建議

**第一堂課（90 分鐘）**：
- 0-20 分：迴圈的必要性 + for 基本語法
- 20-40 分：range() 詳解 + 5 個範例
- 40-60 分：while 迴圈 + 對比教學
- 60-80 分：break/continue 實作
- 80-90 分：課堂練習（基礎題）

**第二堂課（90 分鐘）**：
- 0-30 分：巢狀迴圈（九九乘法表）
- 30-50 分：累加器與旗標模式
- 50-70 分：複雜範例（質數、Fibonacci）
- 70-90 分：課堂練習（進階題）

## 常見錯誤與除錯 | Common Mistakes

### 1. range() 範圍錯誤
```python
# ❌ 錯誤：想印 1 到 10
for i in range(10):
    print(i)  # 輸出 0-9

# ✅ 正確
for i in range(1, 11):
    print(i)  # 輸出 1-10
```

### 2. 無窮迴圈
```python
# ❌ 錯誤：條件永遠為 True
x = 0
while x < 10:
    print(x)  # 忘記更新 x，無窮迴圈！

# ✅ 正確
x = 0
while x < 10:
    print(x)
    x += 1
```

### 3. 縮排錯誤
```python
# ❌ 錯誤：else 與 if 對齊
for i in range(5):
    if i == 2:
        break
    else:  # 這是 if 的 else，不是 for 的 else！
        print("迴圈結束")

# ✅ 正確
for i in range(5):
    if i == 2:
        break
else:  # 這才是 for 的 else
    print("迴圈正常結束")
```

## 延伸閱讀 | Further Reading

### 官方文件
- [Python Tutorial - for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Tutorial - while Statements](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Built-in Functions - range()](https://docs.python.org/3/library/stdtypes.html#range)

### 推薦資源
- **Python Tutor**：視覺化迴圈執行過程
  - https://pythontutor.com/
- **Real Python - Python "for" Loops**
  - https://realpython.com/python-for-loop/
- **Real Python - Python "while" Loops**
  - https://realpython.com/python-while-loop/

### 進階主題（後續章節）
- Ch07：列表 | Lists（使用迴圈處理列表）
- Ch11：串列推導式 | List Comprehensions（迴圈的簡潔寫法）
- Ch15：遞迴 | Recursion（迴圈的函式式替代方案）

## 學習檢查點 | Learning Checkpoints

完成本章後，你應該能夠：

✅ **理解層面**
- 解釋 for 和 while 的執行流程
- 說明 break/continue/else 的作用
- 識別無窮迴圈的成因

✅ **實作層面**
- 寫出九九乘法表
- 計算階乘和 Fibonacci 數列
- 使用迴圈驗證使用者輸入

✅ **應用層面**
- 選擇適當的迴圈類型解決問題
- 設計防護機制避免無窮迴圈
- 優化迴圈效率（提前 break）

---

**下一章**：[Ch06: 進階迭代技巧 | Advanced Iteration](../ch06-advanced-iteration/)
**上一章**：[Ch04: 條件判斷 | Conditional Statements](../ch04-conditionals/)
**返回目錄**：[Fundamentals 目錄](../README.md)
