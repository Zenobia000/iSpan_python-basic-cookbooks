# Chapter 10: 集合資料 | Sets

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 2-3 小時 |
| **難度等級** | ⭐⭐ (中階) |
| **先備知識** | Ch01-09 (變數、運算子、流程控制、列表、元組、字串、字典) |
| **學習類型** | 資料結構、集合論應用 |

## 學習目標 | Learning Objectives

### 知識 (Knowledge)
- 理解集合的定義與特性(無序、唯一、可變)
- 認識集合與列表、字典的差異
- 理解集合運算的數學意義
- 了解 frozenset 的用途

### 理解 (Comprehension)
- 解釋為什麼需要集合資料結構
- 說明集合運算的實際應用場景
- 比較集合符號與方法的差異
- 理解集合的效能優勢

### 應用 (Application)
- 使用集合進行資料去重
- 運用集合運算解決實際問題
- 實作集合推導式
- 選擇適當的集合操作方法

### 分析 (Analysis)
- 分析何時使用集合比列表更適合
- 評估集合運算的效率
- 比較不同集合操作的複雜度

## 核心概念 | Key Concepts

### 概念地圖 | Concept Map

```
集合 (Sets)
├── 特性 (Characteristics)
│   ├── 無序性 (Unordered)
│   ├── 唯一性 (Unique Elements)
│   └── 可變性 (Mutable)
│
├── 創建方式 (Creation)
│   ├── 花括號 {1, 2, 3}
│   ├── set() 函數
│   └── 集合推導式 {x for x in ...}
│
├── 基本操作 (Basic Operations)
│   ├── 新增: add(), update()
│   ├── 刪除: remove(), discard(), pop(), clear()
│   └── 查詢: in, len(), membership
│
├── 集合運算 (Set Operations)
│   ├── 聯集 (Union): | or union()
│   ├── 交集 (Intersection): & or intersection()
│   ├── 差集 (Difference): - or difference()
│   └── 對稱差集 (Symmetric Difference): ^ or symmetric_difference()
│
├── 集合關係 (Set Relations)
│   ├── 子集 (Subset): <=, issubset()
│   ├── 超集 (Superset): >=, issuperset()
│   └── 互斥 (Disjoint): isdisjoint()
│
└── 進階主題 (Advanced)
    ├── 不可變集合 (frozenset)
    ├── 集合推導式 (Set Comprehension)
    └── 效能考量 (Performance)
```

## First Principles 分析 | First Principles Analysis

### Q1: 為什麼需要集合?

**數學基礎**:
- 集合論是現代數學的基礎
- 程式設計中經常需要處理"唯一元素的集合"
- 集合運算(聯集、交集等)是常見的邏輯操作

**實際問題**:
```python
# 問題: 找出兩個班級的共同學生
class_a = ["Alice", "Bob", "Charlie", "David"]
class_b = ["Bob", "David", "Eve", "Frank"]

# 使用列表 - 複雜且低效
common_students = []
for student in class_a:
    if student in class_b:
        common_students.append(student)
# 結果: ['Bob', 'David']

# 使用集合 - 簡潔高效
common = set(class_a) & set(class_b)
# 結果: {'Bob', 'David'}
```

**核心需求**:
1. **唯一性保證**: 自動去重,無需手動檢查
2. **集合運算**: 直覺的數學操作
3. **高效查詢**: O(1) 的成員檢查
4. **語義清晰**: 表達"集合"概念而非"序列"

### Q2: 集合如何實現唯一性?

**底層機制**:
```python
# 集合使用雜湊表 (Hash Table) 實現
# 每個元素都必須是可雜湊的 (hashable)

# 可以放入集合
valid_set = {1, 2, "text", (1, 2)}  # int, str, tuple 可雜湊

# 無法放入集合
# invalid_set = {[1, 2]}  # TypeError: unhashable type: 'list'
# invalid_set = {{1, 2}}  # TypeError: unhashable type: 'set'
```

**唯一性判定**:
- 使用 `hash()` 函數計算元素的雜湊值
- 使用 `==` 比較元素是否相同
- 相同元素只保留一個

### Q3: 集合 vs 列表 vs 字典?

| 特性 | 集合 (Set) | 列表 (List) | 字典 (Dict) |
|:-----|:-----------|:------------|:------------|
| **順序** | 無序 | 有序 | 3.7+ 有序 |
| **重複** | 不允許 | 允許 | 鍵不重複 |
| **索引** | 不支援 | 支援 | 鍵索引 |
| **可變** | 是 | 是 | 是 |
| **用途** | 去重、集合運算 | 序列儲存 | 鍵值對映 |
| **查詢** | O(1) | O(n) | O(1) |

## 課程教材 | Course Materials

| 檔案 | 說明 | 題數/範例數 |
|:-----|:-----|:------------|
| `01-lecture.ipynb` | 主講義 | 8 個範例 |
| `02-worked-examples.ipynb` | 詳解範例 | 5 題 |
| `03-practice.ipynb` | 課堂練習 | 12 題 |
| `04-exercises.ipynb` | 課後作業 | 15 題 |
| `05-solutions.ipynb` | 完整解答 | 15 題 |
| `quiz.ipynb` | 自我測驗 | 20 題 |

## 能力檢核 | Competency Checklist

完成本章後,你應該能夠:

### 基礎能力 (Basic)
- [ ] 使用三種方式創建集合
- [ ] 新增和刪除集合元素
- [ ] 使用 `in` 檢查成員資格
- [ ] 理解集合的無序性和唯一性
- [ ] 使用 `len()` 取得集合大小

### 進階能力 (Intermediate)
- [ ] 執行四種集合運算(聯集、交集、差集、對稱差集)
- [ ] 使用符號和方法兩種方式進行集合運算
- [ ] 比較集合關係(子集、超集、互斥)
- [ ] 將列表轉換為集合進行去重
- [ ] 使用集合推導式創建集合

### 高階能力 (Advanced)
- [ ] 選擇適當的資料結構(集合 vs 列表 vs 字典)
- [ ] 理解集合的效能優勢
- [ ] 使用 frozenset 作為字典鍵
- [ ] 解決複雜的集合運算問題
- [ ] 優化程式碼使用集合提升效率

## 教學建議 | Teaching Tips

### 授課要點 (Key Points)
1. **先講數學背景**: 用維恩圖解釋集合運算
2. **強調唯一性**: 展示自動去重的效果
3. **對比操作方式**: 符號 vs 方法的差異
4. **實際應用**: 展示集合在實務中的用途

### 常見困難 (Common Difficulties)

**困難 1: 無序性混淆**
```python
# 錯誤認知: 集合有順序
s = {3, 1, 2}
# 學生可能期望: {3, 1, 2}
# 實際輸出: {1, 2, 3} 或其他順序

# 解決方法: 強調集合是數學集合,不是序列
```

**困難 2: 創建空集合**
```python
# 常見錯誤
empty = {}  # 這是空字典,不是空集合!

# 正確方式
empty_set = set()
```

**困難 3: 符號運算限制**
```python
# 符號只能用於集合物件
s1 = {1, 2}
s2 = {2, 3}
result = s1 | s2  # OK

# 方法可以接受任何可迭代物件
result = s1.union([2, 3, 4])  # OK
result = s1 | [2, 3, 4]  # TypeError!
```

**困難 4: 可雜湊性限制**
```python
# 無法將列表加入集合
# s = {[1, 2]}  # TypeError

# 應該使用元組
s = {(1, 2)}  # OK
```

### 教學活動建議 (Activities)
1. **維恩圖練習**: 繪製集合運算的視覺化圖表
2. **去重競賽**: 比較列表和集合去重的程式碼長度
3. **實際應用**: 設計標籤管理系統、學生選課系統

## 延伸閱讀 | Further Reading

### 官方文件
- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [set Built-in Type](https://docs.python.org/3/library/stdtypes.html#set)
- [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)

### 進階主題
- 集合的時間複雜度分析
- 雜湊表原理
- 布隆過濾器 (Bloom Filter)
- 集合論在演算法中的應用

### 實務應用
- 資料去重
- 權限管理系統
- 標籤分類
- 社群網路分析(共同好友)

## 本章總結 | Chapter Summary

集合是 Python 中實現數學集合的資料結構,提供唯一性保證和高效的集合運算。理解集合的特性和適用場景,能讓你的程式碼更簡潔、更高效。

**核心要點**:
1. 集合具有無序性、唯一性、可變性
2. 集合運算提供直覺的數學操作
3. 集合查詢效率為 O(1)
4. 集合元素必須是可雜湊的
5. 使用集合進行去重和成員檢查

下一章我們將學習 **Ch11: 推導式 (Comprehensions)**,整合列表、字典、集合的簡潔創建語法。
