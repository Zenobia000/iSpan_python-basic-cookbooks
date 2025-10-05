# Chapter 3: 輸入輸出與格式化 | Input/Output and Formatting

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐☆☆☆☆ (入門) |
| **先備知識** | Chapter 1（變數與資料型態）, Chapter 2（運算子） |
| **相關章節** | Chapter 4 (條件判斷), Milestone 1 (計算機) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 的輸出函式：print() 及其參數
- **列出** Python 的輸入函式：input() 及其特性
- **識別** 三種字串格式化方法：%, .format(), f-string

### 理解面（Comprehension）
- **解釋** 為什麼 input() 總是回傳字串
- **比較** 三種格式化方法的優缺點
- **歸納** 格式化規範的語法規則

### 應用面（Application）
- **運用** print() 輸出各種格式的資料
- **實作** 從使用者獲取輸入並進行型態轉換
- **解決** 需要與使用者互動的簡單問題

### 分析面（Analysis）
- **分析** 輸入驗證的必要性
- **診斷** 輸入型態錯誤的原因
- **評估** 不同格式化方法的適用情境

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
輸入輸出與格式化
├── 輸出（Output）
│   ├── print() 函式
│   │   ├── 基本輸出
│   │   ├── 多個參數
│   │   └── sep/end 參數
│   └── 格式化輸出
│       ├── f-string（推薦）
│       ├── .format() 方法
│       └── % 格式化（舊式）
│
└── 輸入（Input）
    ├── input() 函式
    ├── 回傳值（永遠是 str）
    └── 型態轉換（str → int/float）
```

### First Principles 解析

#### 為什麼需要輸入輸出？
**根本問題**：程式需要與使用者（或外部系統）交換資訊

**最小實作**：
```python
print("Hello")     # 輸出：將資料顯示給使用者
name = input()     # 輸入：從使用者獲取資料
```

**推導過程**：
1. 程式需要顯示結果 → 需要輸出功能（print）
2. 程式需要動態資料 → 需要輸入功能（input）
3. 資料需要易讀格式 → 需要格式化功能（f-string）

#### 為什麼 input() 總是回傳字串？
**根本問題**：鍵盤輸入的是「文字」，不是「數字」

**實例說明**：
```python
# 使用者輸入 "25"
age = input()      # 得到的是字串 "25"，不是整數 25
age_int = int(age) # 需要手動轉換為整數
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 輸出 | Output | 將資料顯示給使用者 |
| 輸入 | Input | 從使用者獲取資料 |
| 格式化 | Formatting | 控制資料的顯示格式 |
| 佔位符 | Placeholder | 格式化字串中待填入的位置 |
| 對齊 | Alignment | 控制文字左右對齊方式 |
| 精度 | Precision | 浮點數保留的小數位數 |
| 填充 | Padding | 填充空白字元至指定寬度 |
| 分隔符 | Separator | 多個輸出值之間的分隔字元 |

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
1. **預習**（30 min）：閱讀本 README，了解 I/O 概念
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
- [ ] 能使用 print() 輸出各種型態的資料
- [ ] 能使用 input() 獲取使用者輸入
- [ ] 能將 input() 的結果轉換為適當型態
- [ ] 能使用 f-string 進行基本格式化

### 進階能力
- [ ] 能控制 print() 的 sep 和 end 參數
- [ ] 能使用格式化規範控制輸出格式
- [ ] 能處理多行輸入
- [ ] 能驗證使用者輸入的合法性

### 應用能力
- [ ] 能撰寫完整的互動式程式
- [ ] 能格式化輸出表格資料
- [ ] 能處理輸入錯誤（try-except）
- [ ] 能建立使用者友善的介面

---

## 📝 理論重點（Key Theoretical Points）

### 1. print() 函式詳解

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

**參數說明**：
- `*objects`: 要輸出的物件（可多個）
- `sep`: 分隔符（預設空格）
- `end`: 結尾字元（預設換行）
- `file`: 輸出目標（預設標準輸出）
- `flush`: 是否立即輸出（預設 False）

### 2. input() 函式特性

```python
user_input = input(prompt)
```

**重要特性**：
- 回傳值**永遠**是 `str` 型態
- 可選的提示訊息（prompt）
- 會等待使用者輸入並按 Enter

**常見模式**：
```python
# 獲取整數
age = int(input("請輸入年齡："))

# 獲取浮點數
height = float(input("請輸入身高(cm)："))

# 獲取字串（不需轉換）
name = input("請輸入姓名：")
```

### 3. f-string 格式化語法

```python
f"{變數:格式規範}"
```

**常用格式規範**：

| 規範 | 說明 | 範例 | 輸出 |
|:-----|:-----|:-----|:-----|
| `:d` | 整數 | `f"{42:d}"` | `42` |
| `:.2f` | 浮點數（2 位小數）| `f"{3.14159:.2f}"` | `3.14` |
| `:10` | 寬度 10 | `f"{42:10}"` | `       42` |
| `:>10` | 右對齊寬度 10 | `f"{42:>10}"` | `        42` |
| `:<10` | 左對齊寬度 10 | `f"{42:<10}"` | `42        ` |
| `:^10` | 置中寬度 10 | `f"{42:^10}"` | `    42    ` |
| `:05d` | 寬度 5 補零 | `f"{42:05d}"` | `00042` |
| `:,` | 千分位 | `f"{1000000:,}"` | `1,000,000` |
| `:.2%` | 百分比 | `f"{0.856:.2%}"` | `85.60%` |

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從對話類比切入**：
   - print() = 說話（輸出給別人）
   - input() = 聆聽（接收別人的輸入）
   - 格式化 = 說話的方式（禮貌、清楚）

2. **強調型態轉換**：
```python
# 常見錯誤
age = input("年齡：")      # "25" (str)
next_year = age + 1         # TypeError!

# 正確做法
age = int(input("年齡："))  # 25 (int)
next_year = age + 1         # 26
```

3. **實際演示格式化**：
```python
# 展示不同格式化的差異
pi = 3.14159
print(f"預設: {pi}")        # 3.14159
print(f"2位小數: {pi:.2f}") # 3.14
print(f"6位小數: {pi:.6f}") # 3.141590
```

### 常見學生困難點

#### 困難點 1：input() 回傳字串
**症狀**：以為 `input()` 會自動判斷型態

**解決方法**：
```python
# 學生常犯的錯誤
num1 = input("數字1：")  # 輸入 "5"
num2 = input("數字2：")  # 輸入 "3"
result = num1 + num2     # "53" (字串串接，不是 8)

# 正確做法
num1 = int(input("數字1："))
num2 = int(input("數字2："))
result = num1 + num2     # 8 (數字相加)
```

#### 困難點 2：格式化語法混淆
**症狀**：混用不同格式化方法

**解決方法**：
- **初學階段統一使用 f-string**
- 只在必要時介紹其他方法

#### 困難點 3：input() 的錯誤處理
**症狀**：使用者輸入非數字時程式崩潰

**解決方法**（進階，Ch20 會詳細說明）：
```python
try:
    age = int(input("年齡："))
except ValueError:
    print("請輸入有效的數字")
    age = 0  # 預設值
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣

**print() 參數**：
- **sep**（分隔）：多個值之間
- **end**（結尾）：輸出最後

**f-string 格式**：
- **冒號前**：變數名
- **冒號後**：格式規範

### 實作練習建議

1. **互動實驗**：
```python
# 嘗試不同的 print() 參數
print("A", "B", "C")              # A B C
print("A", "B", "C", sep="-")     # A-B-C
print("A", "B", "C", end="!\n")   # A B C!
```

2. **格式化實驗**：
```python
# 測試各種格式化規範
num = 42
print(f"{num}")      # 42
print(f"{num:5}")    # "   42"
print(f"{num:05}")   # "00042"
print(f"{num:>10}")  # "        42"
```

3. **輸入練習**：
```python
# 建立簡單的對話程式
name = input("你的名字：")
age = int(input("你的年齡："))
print(f"你好，{name}！你今年 {age} 歲。")
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
- [printf-style Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 2.3
- [Real Python: Python String Formatting](https://realpython.com/python-f-strings/)
- [PyFormat](https://pyformat.info/) - 格式化語法參考

### 互動式工具
- [Python Format String Tester](https://pyformat.info/)
- 線上 Python 解釋器練習 I/O

### 延伸主題（進階學習）
- 檔案輸出：print() 的 file 參數
- 格式化規範進階：對齊、填充、正負號
- 從命令列獲取參數：sys.argv
- Rich text 輸出（使用 rich 套件）

---

## ❓ 常見問題（FAQ）

**Q1: 為什麼 input() 總是回傳字串？**
A: 因為鍵盤輸入本質上就是文字。Python 無法自動判斷使用者想輸入整數還是小數，所以統一回傳字串，由程式設計師決定如何轉換。

**Q2: f-string、.format()、% 該用哪一個？**
A: **推薦使用 f-string**（Python 3.6+）：
- 簡潔易讀
- 執行效率高
- 支援表達式

**Q3: 如何讓 print() 不換行？**
A: 設定 `end` 參數：`print("Hello", end=" ")`

**Q4: 如何一次輸入多個值？**
A: 使用 `split()` 分割：
```python
# 輸入：10 20 30
numbers = input().split()  # ['10', '20', '30']
a, b, c = map(int, numbers)  # 轉成整數
```

**Q5: 格式化時如何對齊小數點？**
A: 使用寬度和精度：`f"{value:8.2f}"`（總寬度 8，小數 2 位）

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 1（變數）**：提供要輸出的資料
- **Chapter 2（運算子）**：計算要輸出的結果

### 後續章節
- **Chapter 4（條件判斷）**：根據輸入做決策
- **Chapter 12（函式）**：input/output 作為函式參數/回傳值
- **Chapter 23（檔案）**：從檔案讀取/寫入資料

### 對應的 Milestone 專案
- **Milestone 1: 簡易計算機**（使用 input/output 實作互動式計算）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能建立簡單的對話式程式
- ✅ 能在 5 分鐘內用 f-string 格式化輸出表格

---

## 🎨 格式化範例速查

### 數字格式化
```python
num = 1234.5678

f"{num}"          # 1234.5678 (預設)
f"{num:.2f}"      # 1234.57 (2位小數)
f"{num:,.2f}"     # 1,234.57 (千分位)
f"{num:10.2f}"    # "   1234.57" (寬度10)
f"{num:>10.2f}"   # "   1234.57" (右對齊)
f"{num:<10.2f}"   # "1234.57   " (左對齊)
f"{num:^10.2f}"   # " 1234.57  " (置中)
f"{num:010.2f}"   # "0001234.57" (補零)
```

### 字串格式化
```python
name = "Alice"

f"{name}"         # Alice
f"{name:10}"      # "Alice     " (寬度10)
f"{name:>10}"     # "     Alice" (右對齊)
f"{name:^10}"     # "  Alice   " (置中)
f"{name:*^10}"    # "**Alice***" (補*置中)
```

### 百分比與特殊格式
```python
ratio = 0.856

f"{ratio:.2%}"    # 85.60% (百分比)
f"{ratio:.1%}"    # 85.6%

# 二進位、八進位、十六進位
num = 42
f"{num:b}"        # 101010 (二進位)
f"{num:o}"        # 52 (八進位)
f"{num:x}"        # 2a (十六進位小寫)
f"{num:X}"        # 2A (十六進位大寫)
```

---

**學習提醒**：輸入輸出是程式與使用者互動的橋樑，務必多加練習！
