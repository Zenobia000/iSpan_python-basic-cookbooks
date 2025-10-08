# Ch25: CSV Data Processing | CSV 資料處理

## 章節資訊 | Chapter Information

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時 (講課 2 小時 + 實作 2 小時) |
| **難度等級** | ★★★☆☆ (中級) |
| **先備知識** | Ch23 (File I/O), Ch24 (JSON), Ch09 (Dictionaries), Ch07 (Lists) |
| **學習目標** | 掌握 CSV 格式讀寫、資料處理與分析技能 |
| **應用場景** | 資料匯入匯出、報表生成、資料分析、ETL 處理 |
| **Python 版本** | 3.8+ |
| **標準庫模組** | `csv`, `pathlib`, `json` |

---

## 學習目標 | Learning Objectives

依據 Bloom's Taxonomy 設計的四層次學習目標:

### 1. 知識 | Knowledge (記憶與理解)
- [ ] 理解 CSV 格式的結構與特性
- [ ] 認識 `csv` 模組的核心類別與函式
- [ ] 理解 reader/writer 與 DictReader/DictWriter 的差異
- [ ] 了解分隔符號、引號字元、換行符號的處理
- [ ] 掌握 CSV 編碼問題與解決方案

### 2. 理解 | Comprehension (解釋與分類)
- [ ] 解釋為什麼 CSV 是常見的資料交換格式
- [ ] 說明何時使用 reader 何時使用 DictReader
- [ ] 比較 CSV 與 JSON 的優缺點
- [ ] 理解 CSV 資料驗證的重要性
- [ ] 分析大型 CSV 檔案的處理策略

### 3. 應用 | Application (實作與操作)
- [ ] 使用 csv.reader() 讀取 CSV 檔案
- [ ] 使用 csv.writer() 寫入 CSV 檔案
- [ ] 使用 DictReader 進行結構化讀取
- [ ] 使用 DictWriter 進行結構化寫入
- [ ] 處理不同編碼的 CSV 檔案
- [ ] 實作資料清理與驗證邏輯
- [ ] 進行 CSV 與 JSON 格式轉換

### 4. 分析 | Analysis (設計與整合)
- [ ] 設計健壯的 CSV 讀寫工具
- [ ] 建立資料處理管道 (pipeline)
- [ ] 實作完整的資料分析流程
- [ ] 開發批次資料處理系統
- [ ] 設計錯誤處理與資料驗證機制

---

## 核心概念 | Key Concepts

### 概念地圖 | Concept Map

```
CSV 資料處理 (CSV Data Processing)
│
├─ CSV 格式基礎 (CSV Format Basics)
│  ├─ 結構 (Structure)
│  │  ├─ 標題列 (Header Row)
│  │  ├─ 資料列 (Data Rows)
│  │  └─ 欄位 (Fields)
│  ├─ 分隔符號 (Delimiters)
│  │  ├─ 逗號 (Comma)
│  │  ├─ Tab (Tab)
│  │  └─ 其他 (Others)
│  └─ 特殊處理 (Special Handling)
│     ├─ 引號 (Quotes)
│     ├─ 換行符號 (Newlines)
│     └─ 跳脫字元 (Escape Chars)
│
├─ 讀取方法 (Reading Methods)
│  ├─ csv.reader()
│  │  ├─ 基本讀取 (Basic Reading)
│  │  ├─ 逐列處理 (Row-by-Row)
│  │  └─ 列表資料 (List Data)
│  └─ csv.DictReader()
│     ├─ 字典讀取 (Dict Reading)
│     ├─ 欄位名稱 (Field Names)
│     └─ 結構化資料 (Structured Data)
│
├─ 寫入方法 (Writing Methods)
│  ├─ csv.writer()
│  │  ├─ 基本寫入 (Basic Writing)
│  │  ├─ writerow() (Single Row)
│  │  └─ writerows() (Multiple Rows)
│  └─ csv.DictWriter()
│     ├─ 字典寫入 (Dict Writing)
│     ├─ 欄位定義 (Field Definition)
│     └─ 結構化輸出 (Structured Output)
│
├─ 進階處理 (Advanced Processing)
│  ├─ 編碼處理 (Encoding)
│  │  ├─ UTF-8
│  │  ├─ Big5/GBK
│  │  └─ 自動偵測 (Auto-Detect)
│  ├─ 資料清理 (Data Cleaning)
│  │  ├─ 空值處理 (Null Handling)
│  │  ├─ 格式驗證 (Format Validation)
│  │  └─ 重複移除 (Deduplication)
│  └─ 效能優化 (Performance)
│     ├─ 串流處理 (Streaming)
│     ├─ 批次讀取 (Batch Reading)
│     └─ 記憶體管理 (Memory Management)
│
└─ 實務應用 (Practical Applications)
   ├─ 資料匯入匯出 (Import/Export)
   ├─ 報表生成 (Report Generation)
   ├─ 資料轉換 (Data Transformation)
   └─ ETL 流程 (ETL Pipeline)
```

---

## First Principles 解析 | First Principles Analysis

### 為什麼 CSV 格式存在？ | Why Does CSV Format Exist?

#### 問題根源 | Root Problem
在電腦發展早期,不同系統、不同軟體之間需要交換表格資料 (tabular data),但缺乏統一的標準格式。

#### CSV 的解決方案 | CSV Solution
CSV (Comma-Separated Values) 提供了一個**簡單、通用、人類可讀**的文字格式:

```
姓名,年齡,城市
張三,25,台北
李四,30,高雄
```

#### 設計原則 | Design Principles

**1. 簡單性 (Simplicity)**
```
原則: 最簡結構 = 文字 + 分隔符號
實現: 每列一筆資料,欄位用逗號分隔
```

**2. 通用性 (Universality)**
```
原則: 純文字格式,任何系統都能讀寫
實現: ASCII/UTF-8 編碼,無專屬格式
```

**3. 可讀性 (Readability)**
```
原則: 人類可直接閱讀與編輯
實現: 文字編輯器即可開啟修改
```

### Python csv 模組的設計哲學

#### 1. 讀取方式的二元性 | Duality of Reading

**csv.reader() - 列表導向 (List-Oriented)**
```python
# 原理: 每列 → 列表
['張三', '25', '台北']
['李四', '30', '高雄']

# 優點: 簡單直接,適合順序處理
# 缺點: 需手動管理索引,易出錯
```

**csv.DictReader() - 字典導向 (Dict-Oriented)**
```python
# 原理: 每列 → 字典
{'姓名': '張三', '年齡': '25', '城市': '台北'}
{'姓名': '李四', '年齡': '30', '城市': '高雄'}

# 優點: 自我描述,欄位名稱存取
# 缺點: 稍微複雜,記憶體稍高
```

#### 2. 分隔符號的靈活性 | Delimiter Flexibility

**為什麼需要不同分隔符號？**

```python
# 問題: 資料中包含逗號
"張三,PhD",25,台北  # ← 姓名中的逗號會導致解析錯誤

# 解決方案 1: 使用引號
"張三,PhD",25,台北  # ← csv 模組自動處理

# 解決方案 2: 使用不同分隔符號
張三,PhD|25|台北    # ← delimiter='|'
張三,PhD	25	台北   # ← delimiter='\t' (Tab)
```

#### 3. 編碼問題 | Encoding Issues

**為什麼編碼很重要？**

```python
# 問題: 中文資料在不同系統間交換

# Windows (Big5)
姓名,年齡
±i¤T,25  # ← Big5 編碼

# Mac/Linux (UTF-8)
姓名,年齡
張三,25   # ← UTF-8 編碼

# 解決: 明確指定編碼
with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
```

---

## 核心術語對照 | Terminology

| 中文 | English | 說明 | 範例 |
|:-----|:--------|:-----|:-----|
| **CSV 格式** | CSV Format | Comma-Separated Values 逗號分隔值格式 | `name,age,city` |
| **分隔符號** | Delimiter | 用於分隔欄位的字元 | `,` `;` `\t` `|` |
| **引號字元** | Quote Character | 用於包裹含特殊字元的欄位 | `"` `'` |
| **跳脫字元** | Escape Character | 用於跳脫特殊字元 | `\` |
| **標題列** | Header Row | CSV 的第一列,包含欄位名稱 | `name,age,city` |
| **資料列** | Data Row | 包含實際資料的列 | `張三,25,台北` |
| **欄位** | Field | CSV 的一個儲存格 | `張三` |
| **讀取器** | Reader | 用於讀取 CSV 的物件 | `csv.reader()` |
| **寫入器** | Writer | 用於寫入 CSV 的物件 | `csv.writer()` |
| **字典讀取器** | DictReader | 將每列讀取為字典 | `csv.DictReader()` |
| **字典寫入器** | DictWriter | 將字典寫入為 CSV 列 | `csv.DictWriter()` |
| **方言** | Dialect | CSV 格式的變體設定 | `excel`, `unix` |
| **換行符號** | Line Terminator | 用於分隔列的字元 | `\n` `\r\n` |
| **編碼** | Encoding | 字元編碼方式 | `utf-8`, `big5` |
| **資料清理** | Data Cleaning | 移除或修正錯誤資料 | 移除空列、驗證格式 |
| **資料驗證** | Data Validation | 確認資料符合規則 | 檢查型別、範圍 |
| **串流處理** | Stream Processing | 逐列處理不載入全部 | 處理大型檔案 |
| **批次處理** | Batch Processing | 分批讀取與處理 | 每次處理 1000 列 |
| **ETL** | Extract-Transform-Load | 擷取-轉換-載入流程 | 資料倉儲處理 |

---

## 課程教材 | Course Materials

### 檔案列表 | File List

| 檔案名稱 | 說明 | 大小 | 預估時間 |
|:---------|:-----|:-----|:---------|
| `README.md` | 本章節說明文件 | ~20KB | 15 分鐘 |
| `01-lecture.ipynb` | 主要講義 (12 個範例) | ~35KB | 90 分鐘 |
| `02-worked-examples.ipynb` | 詳解範例 (5 個案例) | ~25KB | 45 分鐘 |
| `03-practice.ipynb` | 課堂練習 (12 題) | ~18KB | 30 分鐘 |
| `04-exercises.ipynb` | 課後習題 (18 題) | ~25KB | 60 分鐘 |
| `05-solutions.ipynb` | 完整解答 | ~40KB | 參考用 |
| `quiz.ipynb` | 自我測驗 (25 題) | ~25KB | 30 分鐘 |

### 學習路徑建議 | Learning Path

```
第 1 階段 (90 分鐘): 理論學習
├─ 閱讀 README.md (15 分鐘)
└─ 學習 01-lecture.ipynb (75 分鐘)
   ├─ Part I: CSV 格式基礎 (15 分鐘)
   ├─ Part II: 讀取與寫入 (30 分鐘)
   └─ Part III: 進階處理 (30 分鐘)

第 2 階段 (45 分鐘): 案例研究
└─ 實作 02-worked-examples.ipynb (45 分鐘)
   ├─ 學生成績系統 (10 分鐘)
   ├─ 銷售資料分析 (10 分鐘)
   ├─ CSV 轉 JSON 工具 (10 分鐘)
   ├─ 資料清理管道 (10 分鐘)
   └─ 批次資料處理 (5 分鐘)

第 3 階段 (30 分鐘): 課堂練習
└─ 完成 03-practice.ipynb (30 分鐘)

第 4 階段 (60 分鐘): 課後習題
└─ 完成 04-exercises.ipynb (60 分鐘)

第 5 階段 (30 分鐘): 自我評估
└─ 完成 quiz.ipynb (30 分鐘)
```

**總學習時數: 4 小時**

---

## 能力檢核 | Competency Checklist

完成本章後,你應該能夠:

### 基礎能力 (必須全部達成)
- [ ] 使用 csv.reader() 讀取 CSV 檔案
- [ ] 使用 csv.writer() 寫入 CSV 檔案
- [ ] 理解 CSV 標題列的處理方式
- [ ] 處理基本的編碼問題 (UTF-8)
- [ ] 進行簡單的資料過濾與轉換
- [ ] 使用 DictReader 進行結構化讀取
- [ ] 使用 DictWriter 進行結構化寫入

### 進階能力 (至少達成 80%)
- [ ] 處理不同分隔符號的 CSV 檔案
- [ ] 處理多種編碼格式 (Big5, GBK)
- [ ] 實作資料驗證邏輯
- [ ] 實作資料清理功能
- [ ] 處理含特殊字元的 CSV 資料
- [ ] 進行 CSV 與 JSON 格式轉換
- [ ] 設計錯誤處理機制
- [ ] 處理大型 CSV 檔案 (串流處理)

### 專家能力 (選修,至少達成 50%)
- [ ] 設計通用的 CSV 處理類別
- [ ] 建立完整的資料處理管道
- [ ] 實作自動編碼偵測
- [ ] 開發批次資料處理系統
- [ ] 實作資料統計與分析功能
- [ ] 整合多個 CSV 檔案
- [ ] 設計效能優化策略

---

## 授課要點 | Teaching Tips

### 教學重點 | Key Teaching Points

#### 1. 從實際問題出發
```python
# 不好的開場
"今天要學 csv 模組,它有 reader 和 writer..."

# 好的開場
"假設老師要匯出全班成績到 Excel,最簡單的方式是什麼？"
→ 引導學生理解 CSV 是通用的資料交換格式
```

#### 2. 對比 reader 與 DictReader
```python
# 先展示 reader 的問題
row = ['張三', '25', '台北']
name = row[0]  # 需要記住索引
age = row[1]   # 易錯

# 再展示 DictReader 的優勢
row = {'姓名': '張三', '年齡': '25', '城市': '台北'}
name = row['姓名']  # 清楚明確
age = row['年齡']   # 不易錯
```

#### 3. 強調編碼重要性
```python
# 展示編碼錯誤的實際後果
# Windows Excel 匯出 (Big5) → Mac 開啟 (UTF-8) → 亂碼

# 教導正確做法
with open('data.csv', encoding='utf-8-sig') as f:  # ← BOM for Excel
    reader = csv.DictReader(f)
```

#### 4. 實作中學習資料清理
```python
# 不要只講理論,直接展示髒資料
姓名,年齡,城市
張三,25,台北
,30,    # ← 缺失資料
李四,abc,高雄  # ← 錯誤格式
王五,28,台南

# 帶學生一步步清理
```

### 常見困難與解決 | Common Difficulties

#### 困難 1: 編碼問題混淆
**現象**: 學生不知何時用 UTF-8, 何時用 Big5
```python
# 解決策略: 提供決策樹
if 資料來源 == "Excel (Windows)":
    encoding = 'big5' 或 'utf-8-sig'
elif 資料來源 == "網路下載" 或 "Python 產生":
    encoding = 'utf-8'
else:
    # 試錯法
    try:
        with open(file, encoding='utf-8') as f:
            f.read()
    except UnicodeDecodeError:
        with open(file, encoding='big5') as f:
            f.read()
```

#### 困難 2: 分隔符號搞混
**現象**: 學生不知道自己的 CSV 用什麼分隔符號
```python
# 解決策略: 教導檢查方法
# 1. 用文字編輯器開啟查看
# 2. 讀取第一列檢查

with open('data.csv') as f:
    first_line = f.readline()
    print(repr(first_line))  # ← 顯示實際字元
    # 輸出: '姓名\t年齡\t城市\n' → Tab 分隔
```

#### 困難 3: reader vs DictReader 選擇
**現象**: 學生不知何時該用哪個
```python
# 解決策略: 提供選擇指南

用 reader 的時機:
✓ CSV 沒有標題列
✓ 只需要順序處理,不在乎欄位名稱
✓ 需要最高效能

用 DictReader 的時機:
✓ CSV 有標題列 (最常見)
✓ 需要透過欄位名稱存取資料
✓ 可讀性與維護性優先
```

#### 困難 4: 處理大型檔案
**現象**: 學生用 list() 讀取整個大檔案,記憶體不足
```python
# ❌ 錯誤做法
with open('huge.csv') as f:
    reader = csv.reader(f)
    all_data = list(reader)  # ← 載入全部到記憶體

# ✅ 正確做法
with open('huge.csv') as f:
    reader = csv.reader(f)
    for row in reader:  # ← 逐列處理
        process(row)
```

#### 困難 5: 空值與缺失值處理
**現象**: 學生不知如何處理 CSV 中的空欄位
```python
# 展示問題
張三,25,台北
李四,,高雄    # ← 年齡是空字串 ''

# 教導處理策略
row = {'姓名': '李四', '年齡': '', '城市': '高雄'}

# 方法 1: 預設值
age = int(row['年齡']) if row['年齡'] else 0

# 方法 2: 跳過
if not row['年齡']:
    continue

# 方法 3: None
age = int(row['年齡']) if row['年齡'] else None
```

### 教學流程建議 | Suggested Teaching Flow

**第 1 小時: CSV 基礎與讀取**
- 00-15 分: CSV 格式介紹與應用場景
- 15-30 分: csv.reader() 基本讀取
- 30-45 分: csv.DictReader() 結構化讀取
- 45-60 分: 編碼問題與處理

**第 2 小時: 寫入與進階處理**
- 00-15 分: csv.writer() 基本寫入
- 15-30 分: csv.DictWriter() 結構化寫入
- 30-45 分: 資料清理與驗證
- 45-60 分: 實戰案例 (學生成績管理)

**第 3-4 小時: 實作練習**
- 課堂練習 (30 分鐘)
- 課後習題 (60 分鐘)
- 自我測驗 (30 分鐘)

---

## 延伸學習 | Further Learning

### 進階主題 | Advanced Topics

1. **pandas 庫的 CSV 處理**
   - DataFrame.read_csv()
   - DataFrame.to_csv()
   - 更強大的資料分析功能

2. **CSV 格式變體**
   - TSV (Tab-Separated Values)
   - PSV (Pipe-Separated Values)
   - 自訂分隔符號

3. **資料驗證框架**
   - pydantic 資料驗證
   - cerberus 規則驗證
   - 自動型別轉換

4. **大數據處理**
   - Dask 平行處理
   - Vaex 記憶體映射
   - Polars 高效能處理

### 學習資源 | Learning Resources

**官方文件**
- Python csv 模組: https://docs.python.org/3/library/csv.html
- CSV RFC 4180: https://tools.ietf.org/html/rfc4180

**推薦閱讀**
- Real Python - Reading and Writing CSV Files in Python
- Python Cookbook - Chapter on Data Encoding and Processing

**實用工具**
- csvkit - CSV 命令列工具
- pandas - 資料分析庫
- Tabulate - 表格美化輸出

### 實務專案建議 | Project Ideas

1. **學生成績管理系統**
   - CSV 匯入匯出
   - 成績統計分析
   - 報表生成

2. **銷售資料分析器**
   - 多個 CSV 合併
   - 資料清理與驗證
   - 統計圖表生成

3. **資料轉換工具**
   - CSV ↔ JSON
   - CSV ↔ Excel
   - CSV ↔ 資料庫

4. **日誌分析系統**
   - 大型 CSV 串流處理
   - 錯誤偵測與報告
   - 效能優化

---

## 與其他章節的關聯 | Connections

### 前置章節 | Prerequisites
- **Ch23 (File I/O)**: 檔案讀寫基礎、路徑處理、編碼
- **Ch24 (JSON)**: 結構化資料處理、格式轉換
- **Ch09 (Dictionaries)**: DictReader/DictWriter 基礎
- **Ch07 (Lists)**: 資料處理與轉換

### 後續章節 | Next Steps
- **Ch26 (Path Handling)**: 進階路徑處理、檔案管理
- **Ch27-30 (工程實務)**: 專案中的資料處理應用

### 整合應用 | Integration
- **Milestone 7 (待辦事項管理)**: CSV 作為資料儲存格式
- **資料分析專案**: CSV 作為資料來源
- **Web 應用**: CSV 匯入匯出功能

---

## 總結 | Summary

CSV 資料處理是 Python 開發者必備技能,無論是資料分析、系統整合、報表生成,都會用到 CSV 格式。本章從 First Principles 出發,系統性地介紹 CSV 格式、讀寫方法、進階處理,以及實務應用。

**核心要點**:
1. **理解 CSV 格式**: 簡單、通用、人類可讀的表格資料格式
2. **掌握讀寫方法**: reader/writer (列表) vs DictReader/DictWriter (字典)
3. **處理編碼問題**: UTF-8, Big5, 自動偵測
4. **資料清理驗證**: 空值處理、格式驗證、錯誤處理
5. **效能優化**: 串流處理、批次讀取、記憶體管理

完成本章學習後,你將能夠自信地處理各種 CSV 資料任務,並為後續的資料處理與分析打下堅實基礎。

---

**準備好了嗎？讓我們開始學習 CSV 資料處理！**
