# Chapter 9: 映射資料：字典 | Dictionaries

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3-4 小時 |
| **難度等級** | ⭐⭐⭐ (中階) |
| **先備知識** | Ch01-Ch08（特別是 Ch07 列表、Ch08 字串） |
| **學習模式** | 理論講解 40% + 實作練習 60% |
| **核心概念** | 鍵值對映射、雜湊表、字典方法、字典推導式 |

---

## 學習目標 | Learning Objectives

### 知識層次 (Knowledge)
- 理解字典的定義與底層原理（雜湊表）
- 認識字典與列表的本質差異
- 熟悉字典的可變性與鍵的不可變性

### 理解層次 (Comprehension)
- 說明為什麼需要鍵值對資料結構
- 比較 `get()` 與 `[]` 的差異
- 理解字典遍歷的三種方式

### 應用層次 (Application)
- 使用字典進行資料映射與查詢
- 應用字典方法進行 CRUD 操作
- 使用字典推導式簡化程式碼

### 分析層次 (Analysis)
- 分析何時該用字典、何時該用列表
- 設計巢狀字典來表示複雜資料
- 優化字典操作效能

---

## 核心概念 | Key Concepts

### 概念地圖
```
字典 (Dictionaries)
│
├── 基礎概念
│   ├── 鍵值對映射 (Key-Value Mapping)
│   ├── 雜湊表原理 (Hash Table)
│   ├── 鍵的唯一性與不可變性
│   └── 字典的可變性
│
├── 字典創建
│   ├── 字面量語法 {...}
│   ├── dict() 建構子
│   ├── dict.fromkeys()
│   └── 字典推導式
│
├── 字典操作
│   ├── 存取：dict[key], get()
│   ├── 新增：dict[new_key] = value
│   ├── 修改：dict[key] = new_value
│   └── 刪除：del, pop(), popitem(), clear()
│
├── 字典方法
│   ├── 檢視：keys(), values(), items()
│   ├── 查詢：get(), setdefault()
│   ├── 更新：update()
│   └── 複製：copy()
│
├── 字典遍歷
│   ├── 遍歷鍵：for key in dict
│   ├── 遍歷值：for value in dict.values()
│   └── 遍歷鍵值對：for k, v in dict.items()
│
└── 進階應用
    ├── 字典推導式
    ├── 巢狀字典
    ├── defaultdict (collections)
    └── Counter (collections)
```

### First Principles 分析

#### 為什麼需要字典？

**問題根源**：
1. **列表的限制**：
   - 列表使用數字索引（0, 1, 2...）
   - 查詢需要知道位置
   - 語義不明確（`students[0]` 代表什麼？）

2. **真實世界的映射關係**：
   - 學號 → 姓名
   - 身分證字號 → 個人資料
   - 商品代碼 → 價格
   - 英文單字 → 中文翻譯

3. **查詢效能需求**：
   - 列表查詢：O(n) 線性時間
   - 字典查詢：O(1) 常數時間（雜湊表）

**解決方案**：
```python
# 列表方式（不直觀）
students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# 要找 Bob 的分數？需要先找到索引 1

# 字典方式（直觀且高效）
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
# 直接查詢：student_scores["Bob"]  # 92
```

#### 字典 vs 列表：何時用哪個？

| 特性 | 列表 (List) | 字典 (Dict) |
|:-----|:-----------|:-----------|
| **索引** | 數字索引 (0, 1, 2...) | 任意不可變鍵 (字串, 數字, 元組...) |
| **順序** | 有序 (Python 3.7+) | 保留插入順序 (Python 3.7+) |
| **查詢效率** | O(n) | O(1) |
| **用途** | 同類型序列資料 | 鍵值對映射關係 |
| **語義** | "一群東西" | "誰對應什麼" |

**使用時機**：
- **用列表**：購物清單、考試成績序列、待辦事項
- **用字典**：通訊錄、配置設定、資料庫記錄

#### 雜湊表原理（簡化版）

字典的底層是 **雜湊表 (Hash Table)**：

```
鍵 (Key) → 雜湊函數 (Hash Function) → 雜湊值 (Hash) → 儲存位置

例如：
"Alice" → hash("Alice") → 3547698234 → 記憶體位置 X
```

**為什麼鍵必須不可變？**
```python
# 可以作為鍵（不可變）
valid_keys = {
    "name": "Alice",      # 字串 ✓
    123: "number",        # 數字 ✓
    (1, 2): "tuple",      # 元組 ✓
}

# 不能作為鍵（可變）
# invalid_keys = {
#     [1, 2]: "list",    # 列表 ✗ (unhashable type)
#     {"a": 1}: "dict",  # 字典 ✗ (unhashable type)
# }
```

原因：如果鍵可變，雜湊值會改變，導致無法找到原本的值！

---

## 課程教材 | Course Materials

### 檔案說明表

| 檔案 | 說明 | 使用時機 |
|:-----|:-----|:---------|
| `README.md` | 本檔案，章節總覽 | 課前預習 |
| `01-lecture.ipynb` | 主要講義（理論 + 10 個範例） | 課堂教學 |
| `02-worked-examples.ipynb` | 詳解範例（5 個完整應用） | 課堂演示 |
| `03-practice.ipynb` | 課堂練習（15 題） | 課堂實作 |
| `04-exercises.ipynb` | 課後習題（18 題） | 回家作業 |
| `05-solutions.ipynb` | 完整解答 | 課後檢討 |
| `quiz.ipynb` | 自我測驗（25 題） | 課後複習 |

---

## 能力檢核清單 | Competency Checklist

### 基礎能力 (必須掌握)
- [ ] 能說明字典與列表的差異
- [ ] 能使用三種方式創建字典
- [ ] 能使用 `[]` 與 `get()` 存取字典值
- [ ] 能新增、修改、刪除字典元素
- [ ] 能使用 `keys()`, `values()`, `items()` 查看字典內容
- [ ] 能使用三種方式遍歷字典
- [ ] 能判斷鍵是否存在（`in` 運算子）

### 進階能力 (熟練應用)
- [ ] 能使用 `get()` 避免 KeyError
- [ ] 能使用 `setdefault()` 設定預設值
- [ ] 能使用 `update()` 合併字典
- [ ] 能使用 `pop()` / `popitem()` 刪除並取得值
- [ ] 能使用字典推導式創建字典
- [ ] 能設計巢狀字典處理複雜資料

### 挑戰能力 (選修)
- [ ] 能使用 `defaultdict` 簡化計數邏輯
- [ ] 能使用 `Counter` 進行頻率統計
- [ ] 能分析字典操作的時間複雜度
- [ ] 能設計字典來解決實際問題

---

## 教學建議 | Teaching Tips

### 授課要點

#### 1. 開場引導（15 分鐘）
- **問題引入**：「如何儲存學生的成績？」
  - 方法 1：兩個列表（姓名、分數）→ 同步問題
  - 方法 2：字典 → 自然映射
- **類比說明**：字典就像「通訊錄」或「目錄索引」

#### 2. 核心觀念（30 分鐘）
- **重點 1**：鍵的唯一性與不可變性
  ```python
  # 示範鍵重複的行為
  d = {"a": 1, "a": 2}  # 後者覆蓋前者
  print(d)  # {"a": 2}
  ```

- **重點 2**：`get()` vs `[]`
  ```python
  d = {"name": "Alice"}

  # [] 方式：鍵不存在會報錯
  # print(d["age"])  # KeyError

  # get() 方式：可設定預設值
  print(d.get("age", 0))  # 0
  ```

- **重點 3**：三種遍歷方式
  ```python
  for key in student_scores:           # 遍歷鍵
  for value in student_scores.values():  # 遍歷值
  for k, v in student_scores.items():    # 遍歷鍵值對
  ```

#### 3. 實作練習（45 分鐘）
- 從 `03-practice.ipynb` 選擇 8-10 題
- 建議順序：基礎 → 方法應用 → 巢狀字典
- 鼓勵學生「先想再寫」

#### 4. 進階主題（30 分鐘，選教）
- 字典推導式：`{k: v for k, v in ...}`
- `collections.defaultdict`：自動初始化
- `collections.Counter`：計數器

### 常見困難與解決方案

| 困難點 | 學生誤區 | 解決方法 |
|:-------|:---------|:---------|
| **鍵的類型** | 以為列表可以當鍵 | 示範 TypeError，強調「不可變」規則 |
| **KeyError** | 直接用 `[]` 存取不存在的鍵 | 教 `get()` 與 `in` 運算子 |
| **字典遍歷** | 不知道何時用 `items()` | 對比三種遍歷方式的使用場景 |
| **修改 vs 新增** | 不清楚賦值語法的雙重作用 | 示範：存在則修改，不存在則新增 |
| **巢狀字典存取** | 多層索引寫錯 | 分步示範：`data["students"]["Alice"]["score"]` |

### 教學節奏建議

**2 小時課程**：
- 0:00-0:20：理論 + 範例 1-3
- 0:20-0:40：範例 4-6 + 練習 1-5
- 0:40-1:00：範例 7-8 + 練習 6-10
- 1:00-1:20：範例 9-10 + 練習 11-15
- 1:20-2:00：綜合應用 + Q&A

**4 小時課程**：
- 前 2 小時：同上
- 2:00-3:00：`02-worked-examples.ipynb` 詳解範例 1-3
- 3:00-4:00：`04-exercises.ipynb` 習題 1-10

---

## 延伸閱讀 | Further Reading

### 官方文件
- [Python Tutorial: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [dict - Python Documentation](https://docs.python.org/3/library/stdtypes.html#dict)
- [collections — Container datatypes](https://docs.python.org/3/library/collections.html)

### 進階主題
- **雜湊表原理**：[Hash Tables Explained](https://www.youtube.com/watch?v=KyUTuwz_b7Q)
- **字典效能分析**：[Time Complexity of Python Data Structures](https://wiki.python.org/moin/TimeComplexity)
- **字典推導式**：[Dictionary Comprehensions in Python](https://realpython.com/lessons/dictionary-comprehensions/)

### 實用資源
- **速查表**：`resources/dict-methods-cheatsheet.md`（字典方法速查）
- **視覺化工具**：[Python Tutor](http://pythontutor.com/) 觀察字典操作過程
- **練習平台**：[LeetCode Hash Table Problems](https://leetcode.com/tag/hash-table/)

### 下一步學習
- **Ch10: 唯一集合：集合 (Sets)**：學習無序不重複集合
- **Ch11: 列表推導式 (List Comprehensions)**：簡化資料處理
- **Module: 資料處理專案**：綜合應用字典與列表

---

## 學習檢核 | Self-Assessment

完成本章後，你應該能夠：

✅ **基礎檢核**
- 用字典儲存學生成績並查詢
- 用 `get()` 安全存取字典值
- 遍歷字典並列印所有鍵值對
- 新增、修改、刪除字典元素

✅ **進階檢核**
- 用字典推導式轉換資料格式
- 設計巢狀字典儲存複雜資料
- 用 `update()` 合併多個字典
- 用字典實作簡單的資料庫

✅ **應用檢核**
- 完成通訊錄管理系統
- 完成字元頻率統計器
- 完成投票統計程式
- 完成商品庫存管理系統

---

## 重點提醒 | Key Takeaways

1. **字典 = 鍵值對映射**：用有意義的鍵取代數字索引
2. **鍵必須不可變**：字串、數字、元組 ✓；列表、字典 ✗
3. **`get()` 比 `[]` 安全**：避免 KeyError
4. **三種遍歷方式**：
   - `for key in dict`：遍歷鍵
   - `for value in dict.values()`：遍歷值
   - `for k, v in dict.items()`：遍歷鍵值對
5. **字典是可變的**：可以新增、修改、刪除元素
6. **效能優勢**：查詢、插入、刪除都是 O(1)

---

**Happy Coding!** 🐍
