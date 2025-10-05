# Chapter 7: 序列資料：列表 | Sequential Data: Lists

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐☆☆☆ (基礎-中級) |
| **先備知識** | Chapter 1-6（變數、運算子、控制結構） |
| **相關章節** | Chapter 8 (元組), Chapter 11 (推導式), Milestone 3 (成績管理) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 列表的基本操作：建立、存取、修改、刪除
- **定義** 列表的可變性（mutability）特徵
- **識別** 常用的列表方法：append, extend, insert, remove, pop, sort

### 理解面（Comprehension）
- **解釋** 為什麼需要列表（儲存多筆資料）
- **比較** 列表與元組的差異
- **歸納** 列表索引與切片的規則

### 應用面（Application）
- **運用** 列表儲存與處理多筆資料
- **實作** 列表的增刪查改（CRUD）操作
- **解決** 涉及資料集合的實際問題

### 分析面（Analysis）
- **分析** 列表方法的時間複雜度
- **診斷** 列表操作常見錯誤（IndexError）
- **評估** 何時使用列表而非其他資料結構

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
列表（Lists）
├── 基本操作
│   ├── 建立列表：[], list()
│   ├── 索引存取：list[i]
│   ├── 切片：list[start:end:step]
│   └── 長度：len(list)
│
├── 修改列表（可變性）
│   ├── 新增：append, insert, extend
│   ├── 刪除：remove, pop, del, clear
│   └── 修改：list[i] = value
│
├── 列表方法
│   ├── 排序：sort, reverse
│   ├── 搜尋：index, count
│   └── 複製：copy
│
└── 進階操作
    ├── 列表推導式
    ├── 巢狀列表
    └── 列表作為堆疊/佇列
```

### First Principles 解析

#### 為什麼需要列表？
**根本問題**：程式需要處理「一組」相關資料，而非單一值

**最小實作**：
```python
scores = [90, 85, 88]  # 將三個分數存在一個容器中
```

**推導過程**：
1. 需要管理多筆資料 → 不可能為每筆資料建立變數
2. 需要有序儲存 → 列表維持插入順序
3. 需要動態修改 → 列表是可變的（mutable）

**實例說明**：
```python
# ❌ 沒有列表（笨拙）
score1 = 90
score2 = 85
score3 = 88
average = (score1 + score2 + score3) / 3

# ✅ 使用列表（優雅）
scores = [90, 85, 88]
average = sum(scores) / len(scores)
```

#### 列表的本質是什麼？
**定義**：列表是一個有序、可變的資料容器

**核心特性**：
1. **有序性（Ordered）**：元素有固定位置，可用索引存取
2. **可變性（Mutable）**：可以修改、新增、刪除元素
3. **異質性（Heterogeneous）**：可存放不同型態的元素

**與變數的差異**：
```python
# 變數：一個名稱對應一個值
x = 10

# 列表：一個名稱對應多個值
numbers = [10, 20, 30, 40, 50]
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 列表 | List | 有序、可變的資料集合 |
| 索引 | Index | 列表中元素的位置（從 0 開始）|
| 切片 | Slice | 取得列表的子集合 |
| 可變 | Mutable | 可以修改內容的特性 |
| 元素 | Element | 列表中的單一項目 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 40 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（15 題） | 120 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（20 題） | 30 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解列表的核心概念
2. **上課**（120 min）：
   - 講義學習（80 min）：`01-lecture.ipynb`
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
- [ ] 能建立列表並初始化元素
- [ ] 能使用正負索引存取列表元素
- [ ] 能使用切片取得子列表
- [ ] 能使用 `len()` 取得列表長度
- [ ] 能使用 `in` 檢查元素是否存在

### 進階能力
- [ ] 能使用 append、extend、insert 新增元素
- [ ] 能使用 remove、pop、del 刪除元素
- [ ] 能使用 sort、reverse 排序列表
- [ ] 能使用 index、count 搜尋元素
- [ ] 能使用 `for` 迴圈遍歷列表
- [ ] 能使用 `enumerate()` 同時取得索引和值

### 應用能力
- [ ] 能處理巢狀列表（二維列表）
- [ ] 能解決成績處理、資料過濾等實際問題
- [ ] 能理解並避免列表的淺拷貝陷阱
- [ ] 能選擇合適的列表方法解決問題

---

## 📝 理論重點（Key Theoretical Points）

### 1. 列表的可變性（Mutability）

```python
# 列表是可變的
numbers = [1, 2, 3]
numbers[0] = 10      # 修改元素
print(numbers)       # [10, 2, 3]

# 與字串的對比（字串不可變）
text = "hello"
# text[0] = "H"      # TypeError: 字串不可變
text = "Hello"       # 只能重新賦值
```

### 2. 索引規則

| 索引方式 | 範例 | 說明 |
|:---------|:-----|:-----|
| 正索引 | `lst[0]` | 從 0 開始，取第一個元素 |
| 負索引 | `lst[-1]` | 從 -1 開始，取最後一個元素 |
| 切片 | `lst[1:4]` | 取索引 1-3 的元素（不含 4） |
| 省略起點 | `lst[:3]` | 從開頭取到索引 2 |
| 省略終點 | `lst[2:]` | 從索引 2 取到結尾 |
| 步長切片 | `lst[::2]` | 每隔一個取一個 |
| 反轉 | `lst[::-1]` | 反向取所有元素 |

### 3. 常用列表方法

| 方法 | 功能 | 修改原列表 | 回傳值 |
|:-----|:-----|:-----------|:-------|
| `append(x)` | 在末尾新增元素 | ✅ | None |
| `extend(lst)` | 合併另一個列表 | ✅ | None |
| `insert(i, x)` | 在指定位置插入 | ✅ | None |
| `remove(x)` | 刪除第一個 x | ✅ | None |
| `pop(i)` | 刪除並回傳元素 | ✅ | 被刪除的元素 |
| `sort()` | 排序列表 | ✅ | None |
| `reverse()` | 反轉列表 | ✅ | None |
| `index(x)` | 找出 x 的索引 | ❌ | 索引值 |
| `count(x)` | 計算 x 的數量 | ❌ | 數量 |
| `copy()` | 複製列表 | ❌ | 新列表 |

**重要提醒**：修改原列表的方法通常回傳 `None`！

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從具體例子切入**：
   - 使用學生熟悉的場景（如班級成績、購物清單）
   - 對比有列表與沒列表的程式碼

2. **強調索引從 0 開始**：
   - 這是初學者最常犯的錯誤
   - 用「樓層」類比：地面樓層是 0 樓

3. **示範可變性的影響**：
   - 展示列表修改後的變化
   - 對比字串的不可變性

4. **漸進式教學**：
   - 先教基本操作（建立、存取、修改）
   - 再教方法（append、remove 等）
   - 最後教進階技巧（切片、巢狀列表）

### 常見學生困難點

#### 困難點 1：索引錯誤（IndexError）

**症狀**：存取超出範圍的索引

**解決方法**：
```python
numbers = [10, 20, 30]
# 錯誤：numbers[3]（只有索引 0, 1, 2）

# 安全做法 1：檢查長度
if len(numbers) > 3:
    print(numbers[3])

# 安全做法 2：使用負索引取最後一個
print(numbers[-1])  # 30
```

#### 困難點 2：方法回傳 None

**症狀**：誤以為 `sort()` 會回傳排序後的列表

**解決方法**：
```python
# 錯誤示範
numbers = [3, 1, 2]
sorted_numbers = numbers.sort()  # sorted_numbers 是 None！

# 正確做法 1：sort() 直接修改原列表
numbers.sort()
print(numbers)  # [1, 2, 3]

# 正確做法 2：使用 sorted() 函式
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)  # 回傳新列表
```

#### 困難點 3：列表淺拷貝陷阱

**症狀**：修改拷貝的列表，原列表也改變

**解決方法**：
```python
# 錯誤：直接賦值（只是建立參考）
list1 = [1, 2, 3]
list2 = list1       # list2 指向同一個列表
list2[0] = 100
print(list1)        # [100, 2, 3]（原列表也改了！）

# 正確做法 1：使用 copy()
list2 = list1.copy()

# 正確做法 2：使用切片
list2 = list1[:]

# 正確做法 3：使用 list()
list2 = list(list1)
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

- **索引從 0 開始**：第一個是 0，第二個是 1
- **負索引從 -1 開始**：最後一個是 -1，倒數第二個是 -2
- **切片不含終點**：`[1:4]` 取索引 1, 2, 3（不含 4）
- **方法多回傳 None**：修改型方法直接改列表，不回傳新列表

### 實作練習建議

1. **索引練習**：對任意列表，快速說出正負索引對應的元素
2. **方法實驗**：每個方法都實際操作一次，觀察效果
3. **切片挑戰**：用切片實現各種取值需求（奇數位、偶數位、反轉）
4. **應用場景**：用列表解決日常問題（待辦清單、成績排名）

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 5.3
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 10

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化列表操作
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)

### 延伸主題（進階學習）
- 列表推導式（List Comprehension）- Chapter 11
- 時間複雜度分析（Big O）
- collections.deque（雙端佇列）
- 深拷貝與淺拷貝（copy vs deepcopy）

---

## ❓ 常見問題（FAQ）

**Q1: 列表和元組（Tuple）有什麼區別？**
A: 列表是可變的（mutable），可以修改、新增、刪除元素；元組是不可變的（immutable），一旦建立就無法改變。詳見 Chapter 8。

**Q2: 為什麼 `numbers.append(4)` 回傳 None？**
A: `append()` 是修改型方法，直接修改原列表，不回傳新列表。這是 Python 的設計哲學：避免混淆「修改」和「回傳」兩種操作。

**Q3: `lst[:]` 和 `lst.copy()` 有什麼區別？**
A: 功能相同，都是淺拷貝。`lst[:]` 是切片語法，`lst.copy()` 更明確表達意圖，建議使用後者。

**Q4: 如何刪除列表中的所有特定元素？**
A: 使用列表推導式：`lst = [x for x in lst if x != target_value]`，或使用 `filter()`。不建議在迴圈中使用 `remove()`（會跳過元素）。

**Q5: 列表可以包含不同型態的元素嗎？**
A: 可以！`mixed = [1, "hello", 3.14, True]` 是合法的。但實務上通常不建議，會造成程式邏輯複雜。

**Q6: 為什麼 `numbers.sort()` 之後 `numbers` 是 None？**
A: 這是誤用！應該這樣：
```python
numbers = [3, 1, 2]
numbers.sort()        # 直接修改 numbers，不要賦值
print(numbers)        # [1, 2, 3]

# 或使用 sorted() 函式
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)  # 回傳新列表
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 1-3**：變數、運算子、輸入輸出（列表元素的操作基礎）
- **Chapter 4-6**：條件判斷、迴圈（用於遍歷列表）

### 後續章節
- **Chapter 8（元組）**：對比列表與元組的差異
- **Chapter 9（字串進階）**：字串與列表的轉換
- **Chapter 10（字典）**：另一種重要的資料結構
- **Chapter 11（推導式）**：列表推導式的優雅語法

### 對應的 Milestone 專案
- **Milestone 3: 成績管理系統**（結合 Ch7-11 的知識）

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：

- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能操作 20+ 元素的列表而不出錯
- ✅ 能在 10 分鐘內實作成績處理程式
- ✅ 能向他人解釋列表的可變性與索引規則

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

**學習提醒**：列表是 Python 最重要的資料結構之一，務必熟練掌握！所有後續章節都會頻繁使用列表。
