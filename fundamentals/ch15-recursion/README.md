# Chapter 15: 遞迴思維 | Recursive Thinking

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 5 小時（3 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐⭐☆ (4/5 - 進階) |
| **先備知識** | Chapter 12 (函式基礎), Chapter 13 (作用域), Chapter 5-6 (迴圈) |
| **相關章節** | Chapter 14 (高階函式), Milestone 4 (文字工具包) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 遞迴的兩個必要要素：基本情況與遞迴情況
- **定義** 遞迴函式的執行流程與呼叫堆疊（Call Stack）
- **識別** 適合使用遞迴解決的問題類型（自相似問題）

### 理解面（Comprehension）
- **解釋** 為什麼需要遞迴（處理自相似、樹狀、分治問題）
- **比較** 遞迴與迭代的優缺點、適用場景
- **歸納** 遞迴函式的設計模式與思維方式

### 應用面（Application）
- **運用** 遞迴解決數學問題（階乘、費氏數列、GCD）
- **實作** 遞迴處理資料結構（列表、樹狀結構、字串）
- **解決** 分治法問題（二分搜尋、快速排序、河內塔）

### 分析面（Analysis）
- **分析** 遞迴的時間與空間複雜度
- **診斷** 遞迴常見錯誤（無限遞迴、堆疊溢位）
- **評估** 何時使用遞迴、何時使用迴圈

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
遞迴（Recursion）
├── 核心要素
│   ├── 基本情況（Base Case）：終止條件
│   ├── 遞迴情況（Recursive Case）：呼叫自己
│   └── 收斂性（Convergence）：逐步趨向基本情況
│
├── 執行機制
│   ├── 呼叫堆疊（Call Stack）
│   ├── 堆疊框架（Stack Frame）
│   └── 回溯（Backtracking）
│
├── 遞迴類型
│   ├── 線性遞迴（Linear Recursion）
│   ├── 樹狀遞迴（Tree Recursion）
│   ├── 尾遞迴（Tail Recursion）
│   └── 相互遞迴（Mutual Recursion）
│
├── 應用領域
│   ├── 數學問題：階乘、費氏數列、GCD
│   ├── 分治法：二分搜尋、合併排序、快速排序
│   ├── 樹狀結構：檔案遍歷、DOM 解析
│   └── 回溯法：排列組合、迷宮問題、N 皇后
│
└── 遞迴 vs 迭代
    ├── 優點：簡潔、自然表達、處理樹狀結構
    ├── 缺點：效能開銷、堆疊溢位風險
    └── 選擇標準：問題性質、效能需求
```

### First Principles 解析

#### 為什麼需要遞迴？

**根本問題**：某些問題具有「自相似性」（Self-Similarity），即問題的解法與子問題的解法相同

**最小實作**：
```python
def countdown(n):
    if n == 0:           # 基本情況：停止條件
        print("發射！")
        return
    print(n)
    countdown(n - 1)     # 遞迴情況：呼叫自己處理更小的問題

countdown(3)
# 輸出：
# 3
# 2
# 1
# 發射！
```

**推導過程**：
1. **觀察自相似性**：倒數 3 = 印出 3 + 倒數 2，倒數 2 = 印出 2 + 倒數 1
2. **找出基本情況**：倒數到 0 時停止
3. **建立遞迴關係**：countdown(n) = print(n) + countdown(n-1)

**實例說明**：
```python
# ❌ 沒有遞迴（笨拙）
print(3)
print(2)
print(1)
print("發射！")

# ✅ 使用遞迴（優雅）
def countdown(n):
    if n == 0:
        print("發射！")
        return
    print(n)
    countdown(n - 1)

countdown(3)
```

#### 遞迴的本質是什麼？

**定義**：遞迴是一種函式直接或間接呼叫自己的程式設計技巧

**核心公式**：
```
遞迴函式 = 基本情況（終止條件）+ 遞迴情況（縮小問題規模）
```

**必要條件**：
1. **基本情況（Base Case）**：最簡單的情況，不需要遞迴即可解決
2. **遞迴情況（Recursive Case）**：將問題分解為更小的子問題
3. **收斂性（Convergence）**：每次遞迴都朝基本情況前進

**經典範例：階乘**
```python
# 數學定義
# 0! = 1              （基本情況）
# n! = n × (n-1)!     （遞迴情況）

def factorial(n):
    if n == 0:               # 基本情況
        return 1
    return n * factorial(n - 1)  # 遞迴情況

# factorial(3) 的執行過程
factorial(3)
  → 3 * factorial(2)
      → 2 * factorial(1)
          → 1 * factorial(0)
              → 1           # 基本情況
          ← 1               # 回傳 1
      ← 2 * 1 = 2          # 回傳 2
  ← 3 * 2 = 6              # 回傳 6
```

#### 呼叫堆疊（Call Stack）原理

**視覺化**：
```
呼叫 factorial(3)

堆疊變化：
Step 1: factorial(3)          | n=3 |
Step 2: factorial(2)          | n=2 |  ← 新增
                              | n=3 |
Step 3: factorial(1)          | n=1 |  ← 新增
                              | n=2 |
                              | n=3 |
Step 4: factorial(0)          | n=0 |  ← 新增（基本情況）
                              | n=1 |
                              | n=2 |
                              | n=3 |
Step 5: 回傳 1                | n=1 |  ← 彈出 n=0
                              | n=2 |
                              | n=3 |
Step 6: 回傳 1                | n=2 |  ← 彈出 n=1
                              | n=3 |
Step 7: 回傳 2                | n=3 |  ← 彈出 n=2
Step 8: 回傳 6                 空     ← 彈出 n=3，完成
```

**記憶體消耗**：
- 每次遞迴呼叫都會在堆疊上建立新的框架（Stack Frame）
- 深度過深會導致 `RecursionError: maximum recursion depth exceeded`
- Python 預設遞迴深度限制：約 1000 層

#### 遞迴 vs 迭代

**遞迴版本**：
```python
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
```

**迭代版本**：
```python
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

**比較表**：

| 特性 | 遞迴 | 迭代 |
|:-----|:-----|:-----|
| **程式碼** | 簡潔、直觀 | 較冗長 |
| **效能** | 較慢（函式呼叫開銷） | 較快 |
| **記憶體** | 較多（堆疊空間） | 較少 |
| **除錯** | 較困難（堆疊追蹤） | 較容易 |
| **適用問題** | 樹狀、分治、自相似 | 線性、簡單迴圈 |

**選擇標準**：
- ✅ **使用遞迴**：樹狀結構、分治法、問題天然遞迴
- ✅ **使用迭代**：簡單迴圈、效能敏感、大規模資料

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 遞迴 | Recursion | 函式直接或間接呼叫自己的技巧 |
| 基本情況 | Base Case | 遞迴的終止條件，不需要進一步遞迴 |
| 遞迴情況 | Recursive Case | 呼叫自己處理更小問題的情況 |
| 呼叫堆疊 | Call Stack | 儲存函式呼叫資訊的記憶體區域 |
| 堆疊框架 | Stack Frame | 單次函式呼叫的資訊（參數、區域變數） |
| 堆疊溢位 | Stack Overflow | 遞迴深度超過限制導致的錯誤 |
| 尾遞迴 | Tail Recursion | 遞迴呼叫是函式的最後一個操作 |
| 回溯 | Backtracking | 遞迴返回時的逐層退出過程 |
| 分治法 | Divide and Conquer | 將問題分解為子問題的演算法策略 |
| 收斂性 | Convergence | 遞迴逐步趨向基本情況的特性 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（10 個範例） | 120 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 50 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 50 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（18 題） | 150 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（28 題） | 40 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（40 min）：閱讀本 README，理解遞迴的核心概念
2. **上課**（170 min）：
   - 講義學習（120 min）：`01-lecture.ipynb`
   - 範例演練（50 min）：`02-worked-examples.ipynb`
3. **課堂練習**（50 min）：完成 `03-practice.ipynb`
4. **課後複習**（150 min）：
   - 完成習題（120 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（40 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能識別遞迴函式的基本情況與遞迴情況
- [ ] 能撰寫簡單的遞迴函式（階乘、總和、次方）
- [ ] 能追蹤遞迴的執行流程（手動模擬堆疊）
- [ ] 能理解遞迴與迴圈的差異
- [ ] 能避免無限遞迴（遺漏基本情況）

### 進階能力
- [ ] 能用遞迴處理列表與字串（反轉、搜尋、過濾）
- [ ] 能實作經典遞迴演算法（費氏數列、GCD、二分搜尋）
- [ ] 能視覺化遞迴的呼叫過程（使用縮排或圖示）
- [ ] 能將簡單遞迴改寫為迴圈（互相轉換）
- [ ] 能理解樹狀遞迴與線性遞迴的差異

### 應用能力
- [ ] 能用遞迴實作分治法演算法（快速排序、合併排序）
- [ ] 能用遞迴處理樹狀結構（檔案遍歷、巢狀資料）
- [ ] 能用遞迴解決回溯問題（全排列、組合、迷宮）
- [ ] 能分析遞迴的時間與空間複雜度
- [ ] 能選擇合適的方法（遞迴 vs 迭代）解決問題

---

## 📝 理論重點（Key Theoretical Points）

### 1. 遞迴的基本結構

```python
def recursive_function(問題):
    # 1. 基本情況（必須！）
    if 問題足夠簡單:
        return 直接解答

    # 2. 遞迴情況
    縮小後的問題 = 將問題分解
    子問題解答 = recursive_function(縮小後的問題)

    # 3. 組合結果
    return 組合(子問題解答)
```

### 2. 遞迴設計的三步驟

**Step 1：找出基本情況**
- 什麼時候問題簡單到可以直接解決？
- 階乘：`n == 0` 時，回傳 1
- 倒數：`n == 0` 時，停止

**Step 2：建立遞迴關係**
- 如何用更小的問題表達當前問題？
- 階乘：`factorial(n) = n * factorial(n-1)`
- 總和：`sum(n) = n + sum(n-1)`

**Step 3：確保收斂性**
- 每次遞迴都讓問題規模縮小
- 最終會到達基本情況

### 3. 常見遞迴模式

**模式 1：累積型遞迴**
```python
def sum_list(lst):
    if not lst:  # 空列表
        return 0
    return lst[0] + sum_list(lst[1:])  # 第一個元素 + 剩餘總和
```

**模式 2：分治型遞迴**
```python
def binary_search(arr, target, left, right):
    if left > right:  # 找不到
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
```

**模式 3：樹狀遞迴**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # 兩次遞迴呼叫
```

### 4. 遞迴的效能分析

**時間複雜度**：
- 線性遞迴：O(n) - 如 `factorial(n)`
- 樹狀遞迴：O(2^n) - 如 `fibonacci(n)`（未優化）
- 分治遞迴：O(n log n) - 如 `merge_sort(n)`

**空間複雜度**：
- 遞迴深度 = 堆疊空間
- `factorial(n)` → O(n) 空間
- `fibonacci(n)` → O(n) 空間（深度）

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從最簡單的例子開始**：
   - 用「倒數計時」作為第一個範例
   - 手動追蹤 `countdown(3)` 的執行過程
   - 強調基本情況的重要性

2. **視覺化呼叫堆疊**：
   - 使用縮排顯示遞迴層級
   - 畫出堆疊的成長與收縮
   - 使用 [Python Tutor](http://pythontutor.com/) 演示

3. **對比遞迴與迴圈**：
   - 同一問題用兩種方法實作
   - 讓學生體會遞迴的簡潔性
   - 討論效能差異

4. **強調常見錯誤**：
   - 忘記基本情況 → 無限遞迴
   - 基本情況永遠不會到達 → 無限遞迴
   - 遞迴深度過深 → 堆疊溢位

5. **漸進式教學**：
   - 第一週：簡單數學遞迴（階乘、總和）
   - 第二週：資料結構遞迴（列表、字串）
   - 第三週：演算法遞迴（搜尋、排序）

### 常見學生困難點

#### 困難點 1：理解遞迴的執行流程

**症狀**：不理解函式如何「呼叫自己」，覺得違反直覺

**解決方法**：
1. 使用具體數字手動追蹤（如 `factorial(3)`）
2. 每一步都寫出堆疊狀態
3. 強調「信任遞迴」：相信子問題會正確解決

```python
# 手動追蹤範例
def factorial(n):
    print(f"呼叫 factorial({n})")
    if n == 0:
        print(f"基本情況：回傳 1")
        return 1
    result = n * factorial(n - 1)
    print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")
    return result

factorial(3)
```

#### 困難點 2：忘記基本情況

**症狀**：遞迴函式導致 `RecursionError`

**解決方法**：
```python
# ❌ 錯誤：沒有基本情況
def bad_countdown(n):
    print(n)
    bad_countdown(n - 1)  # 永遠不會停止！

# ✅ 正確：有基本情況
def good_countdown(n):
    if n == 0:           # 基本情況
        return
    print(n)
    good_countdown(n - 1)
```

**檢查清單**：
- [ ] 是否有 `if` 判斷基本情況？
- [ ] 基本情況是否會回傳值或停止？
- [ ] 遞迴是否朝基本情況前進？

#### 困難點 3：分不清何時用遞迴、何時用迴圈

**症狀**：所有問題都想用遞迴，或完全不敢用遞迴

**解決方法**：
提供決策樹：

```
問題是否天然遞迴？（樹狀、自相似）
├── 是 → 優先考慮遞迴（如：檔案遍歷、全排列）
└── 否 → 問題規模是否很大？
    ├── 是 → 使用迴圈（避免堆疊溢位）
    └── 否 → 選擇更易懂的方式
```

**實例對比**：
- **適合遞迴**：河內塔、全排列、二元樹遍歷
- **適合迴圈**：簡單總和、陣列遍歷、計數

#### 困難點 4：樹狀遞迴效能問題

**症狀**：`fibonacci(40)` 跑很久

**解決方法**：
```python
# ❌ 慢：樹狀遞迴（重複計算）
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)  # O(2^n)

# ✅ 快：記憶化（Memoization）
def fib_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_fast(n-1, memo) + fib_fast(n-2, memo)
    return memo[n]

# ✅ 更快：迭代
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

- **遞迴三要素**：基本情況 + 遞迴情況 + 收斂性
- **設計遞迴**：先寫基本情況，再寫遞迴呼叫
- **除錯遞迴**：加入 `print` 追蹤執行流程
- **信任遞迴**：不要試圖理解每一層，相信子問題會解決

### 實作練習建議

1. **手動追蹤**：用紙筆追蹤 3-5 層遞迴的執行
2. **加入除錯**：在每個遞迴函式加入 `print` 觀察執行
3. **對比實作**：同一問題用遞迴和迴圈實作
4. **漸進複雜**：從階乘 → 費氏 → 排序 → 回溯

### 除錯技巧

```python
# 技巧 1：加入縮排顯示遞迴深度
def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}→ factorial({n})")
    if n == 0:
        print(f"{indent}← 回傳 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}← 回傳 {result}")
    return result

# 技巧 2：使用 Python Tutor 視覺化
# 前往 http://pythontutor.com/

# 技巧 3：設定遞迴深度限制（防止無限遞迴）
import sys
sys.setrecursionlimit(100)  # 設為較小值測試
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Recursion](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [sys.setrecursionlimit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 4.1
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 5-6
- Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.), Chapter 4 (Divide-and-Conquer)

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化遞迴執行
- [VisuAlgo](https://visualgo.net/en/recursion) - 演算法視覺化
- [Recursion Visualizer](https://recursion.vercel.app/) - 遞迴樹視覺化

### 延伸主題（進階學習）
- 動態規劃（Dynamic Programming）
- 記憶化遞迴（Memoization）
- 尾遞迴優化（Tail Call Optimization）
- Lambda Calculus（λ 演算）

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候該用遞迴，什麼時候該用迴圈？**
A:
- **用遞迴**：問題具有自相似性（如樹狀結構、分治法、回溯）
- **用迴圈**：簡單的線性問題、效能敏感的場景
- **兩者皆可**：根據程式碼可讀性選擇

**Q2: 為什麼我的遞迴函式會報 `RecursionError`？**
A: 可能原因：
1. 忘記基本情況
2. 基本情況永遠不會到達（如 `n` 沒有遞減）
3. 遞迴深度超過 Python 限制（約 1000 層）

**Q3: 遞迴一定比迴圈慢嗎？**
A: 通常是的，因為函式呼叫有開銷。但：
- 某些編譯器支援尾遞迴優化（Python 不支援）
- 遞迴的簡潔性有時值得犧牲少許效能
- 對小規模問題，差異可忽略

**Q4: 如何理解「信任遞迴」？**
A: 設計遞迴時，假設 `factorial(n-1)` 已經正確回傳 `(n-1)!`，只需專注於當前層：`n * factorial(n-1)`。不要試圖追蹤每一層的細節。

**Q5: 遞迴函式可以有多個基本情況嗎？**
A: 可以！例如費氏數列有兩個基本情況：
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

**Q6: 什麼是「尾遞迴」？**
A: 遞迴呼叫是函式的最後一個操作，例如：
```python
# 尾遞迴
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, n * acc)  # 最後一步是遞迴

# 非尾遞迴
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # 最後一步是乘法，不是遞迴
```
Python 不支援尾遞迴優化，但某些語言（如 Scheme）會優化為迴圈。

**Q7: 如何避免重複計算（如費氏數列）？**
A: 使用記憶化（Memoization）：
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12（函式基礎）**：函式定義、參數、回傳值
- **Chapter 13（作用域）**：區域變數、堆疊框架
- **Chapter 5-6（迴圈）**：對比遞迴與迭代

### 後續章節
- **Chapter 16（類別基礎）**：遞迴處理物件結構
- **Chapter 23（檔案處理）**：遞迴走訪檔案系統

### 對應的 Milestone 專案
- **Milestone 4: 文字工具包**（結合 Ch12-15 的知識）

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：

- ✅ 獨立完成課後習題（正確率 ≥ 75%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能手動追蹤 5 層遞迴的執行流程
- ✅ 能在 15 分鐘內實作階乘、費氏、GCD
- ✅ 能向他人解釋遞迴的運作原理與適用場景
- ✅ 能判斷何時使用遞迴、何時使用迴圈

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構

---

**學習提醒**：遞迴是程式設計的重要概念，初學時可能覺得抽象，但透過大量練習和視覺化工具，你會逐漸掌握這項強大的技巧！
