# Ch26: Paths and File System (路徑與檔案系統)

## 章節資訊

- **學習時數**: 3 小時
- **難度**: ⭐⭐⭐ (中階)
- **先備知識**:
  - Ch23: File I/O Fundamentals (檔案輸入輸出基礎)
  - Ch07: Lists (序列資料：列表)
  - Ch09: Dictionaries (映射資料：字典)
  - Ch12: Function Fundamentals (函式設計基礎)

## 學習目標

### 知識層次 (Knowledge)
- 理解檔案系統的基本概念與結構
- 認識絕對路徑與相對路徑的差異
- 了解 `pathlib` 模組的設計理念與優勢
- 掌握跨平台路徑處理的重要性

### 理解層次 (Comprehension)
- 說明 Path 物件導向設計的優點
- 解釋路徑解析與正規化的過程
- 比較 `pathlib` 與 `os.path` 的異同
- 描述 glob 模式匹配的規則

### 應用層次 (Application)
- 使用 Path 物件進行路徑操作
- 實作檔案與目錄的建立、刪除、重新命名
- 應用 glob 模式搜尋檔案
- 遍歷目錄樹並處理檔案

### 分析層次 (Analysis)
- 分析檔案組織結構的優缺點
- 評估不同路徑操作方法的效能
- 診斷路徑相關的常見錯誤
- 設計跨平台相容的檔案處理系統

## 核心概念

### 概念地圖

```
路徑與檔案系統
├── 路徑基礎
│   ├── 絕對路徑 vs 相對路徑
│   ├── Path 物件
│   └── 路徑組合
├── 路徑屬性
│   ├── name, stem, suffix
│   ├── parent, parents
│   └── parts
├── 路徑檢查
│   ├── exists(), is_file(), is_dir()
│   ├── is_absolute(), is_relative_to()
│   └── resolve(), absolute()
├── 檔案操作
│   ├── 建立與刪除
│   ├── 重新命名
│   └── 屬性查詢 (stat)
├── 目錄操作
│   ├── mkdir, rmdir
│   ├── iterdir
│   └── 遍歷目錄樹
└── 進階技巧
    ├── Glob 模式匹配
    ├── 跨平台處理
    └── 檔案組織系統
```

### First Principles 解析

#### 為什麼需要 pathlib？

**問題的本質**: 傳統的 `os.path` 模組使用字串處理路徑，存在以下問題：
1. **不直觀**: 需要記憶大量函式名稱
2. **平台差異**: Windows 使用 `\`，Unix 使用 `/`
3. **錯誤處理**: 字串拼接容易出錯
4. **功能分散**: 路徑操作分散在多個模組

**pathlib 的解決方案**:
```python
# 舊方式 (os.path)
import os
path = os.path.join('data', 'files', 'report.txt')
if os.path.exists(path):
    size = os.path.getsize(path)

# 新方式 (pathlib)
from pathlib import Path
path = Path('data') / 'files' / 'report.txt'
if path.exists():
    size = path.stat().st_size
```

**優勢**:
- **物件導向**: Path 物件封裝所有操作
- **直觀**: 使用 `/` 運算子組合路徑
- **跨平台**: 自動處理平台差異
- **強大**: 整合檔案系統操作

#### 絕對路徑 vs 相對路徑

**絕對路徑 (Absolute Path)**:
- 從檔案系統根目錄開始的完整路徑
- Windows: `C:\Users\user\documents\file.txt`
- Unix: `/home/user/documents/file.txt`
- **優點**: 明確、不受工作目錄影響
- **缺點**: 不可移植、路徑較長

**相對路徑 (Relative Path)**:
- 相對於目前工作目錄的路徑
- `data/file.txt`
- `../config/settings.json`
- **優點**: 可移植、路徑較短
- **缺點**: 依賴工作目錄

#### Path 物件的核心設計

**不可變性 (Immutability)**:
```python
p = Path('data')
p / 'file.txt'  # 創建新 Path 物件
print(p)  # 原物件不變：data
```

**運算子重載**:
- `/`: 路徑組合
- `==`, `!=`: 路徑比較

**懶惰求值 (Lazy Evaluation)**:
```python
# 建立 Path 不會檢查檔案是否存在
p = Path('nonexistent.txt')  # 不會報錯
p.exists()  # 實際檢查時才訪問檔案系統
```

## 重要術語

| 中文 | English | 說明 |
|:-----|:--------|:-----|
| 路徑 | Path | 檔案或目錄在檔案系統中的位置 |
| 絕對路徑 | Absolute Path | 從根目錄開始的完整路徑 |
| 相對路徑 | Relative Path | 相對於目前位置的路徑 |
| 路徑分隔符 | Path Separator | Windows: `\`, Unix: `/` |
| 根目錄 | Root Directory | 檔案系統的最上層目錄 |
| 工作目錄 | Working Directory | 程式執行的目前目錄 (cwd) |
| 父目錄 | Parent Directory | 上一層目錄 |
| 子目錄 | Subdirectory | 下一層目錄 |
| 檔名 | Filename | 檔案的名稱 |
| 副檔名 | File Extension | 檔案類型標識 (如 .txt, .py) |
| 主檔名 | Stem | 不含副檔名的檔名 |
| Glob 模式 | Glob Pattern | 檔案名稱匹配模式 (如 `*.txt`) |
| 遍歷 | Traverse | 逐一訪問目錄中的所有項目 |
| 解析 | Resolve | 將路徑轉換為絕對路徑並消除符號連結 |
| 正規化 | Normalize | 簡化路徑 (如移除 `..` 和 `.`) |

## 課程教材

| 檔案 | 說明 | 大小 |
|:-----|:-----|:-----|
| `01-lecture.ipynb` | 主講義：12 個範例 (Path 基礎、操作、目錄處理、Glob) | ~30-35KB |
| `02-worked-examples.ipynb` | 詳解範例：5 個完整案例 (搜尋、整理、備份) | ~20-25KB |
| `03-practice.ipynb` | 課堂練習：12 題 | ~15-18KB |
| `04-exercises.ipynb` | 課後習題：18 題 (基礎 6 + 進階 6 + 挑戰 6) | ~22-25KB |
| `05-solutions.ipynb` | 完整解答 | ~35-40KB |
| `quiz.ipynb` | 自我測驗：25 題 (選擇 15 + 填空 5 + 程式 5) | ~22-25KB |

## 能力檢核表

完成本章後，你應該能夠：

### Path 物件基礎
- [ ] 建立 Path 物件
- [ ] 使用 `/` 運算子組合路徑
- [ ] 區分絕對路徑與相對路徑
- [ ] 轉換字串與 Path 物件

### 路徑屬性
- [ ] 取得檔名、主檔名、副檔名
- [ ] 取得父目錄、祖先目錄
- [ ] 分解路徑為組成部分
- [ ] 判斷路徑類型

### 路徑檢查與解析
- [ ] 檢查路徑是否存在
- [ ] 判斷是檔案或目錄
- [ ] 解析相對路徑為絕對路徑
- [ ] 檢查路徑關係

### 檔案操作
- [ ] 建立、刪除檔案
- [ ] 重新命名檔案
- [ ] 查詢檔案屬性 (大小、時間)
- [ ] 讀寫檔案內容

### 目錄操作
- [ ] 建立、刪除目錄
- [ ] 列出目錄內容
- [ ] 遍歷目錄樹
- [ ] 使用 glob 搜尋檔案

### 跨平台處理
- [ ] 編寫跨平台相容的程式碼
- [ ] 處理不同平台的路徑分隔符
- [ ] 使用 PurePath 進行純路徑操作
- [ ] 避免硬編碼路徑

## 教學要點

### 重點概念

1. **Path 物件的優勢**
   - 強調物件導向設計的直觀性
   - 示範與 os.path 的對比
   - 展示跨平台相容性

2. **路徑組合**
   - 使用 `/` 運算子的優雅性
   - 避免字串拼接的錯誤
   - 自動處理分隔符

3. **檔案系統操作**
   - 安全的檔案操作流程
   - 錯誤處理 (FileNotFoundError, PermissionError)
   - 資源清理

4. **Glob 模式**
   - `*`: 匹配任意字元
   - `**`: 遞迴匹配
   - `?`: 單一字元
   - `[]`: 字元集合

### 常見困難與解決方案

#### 困難 1: 混淆絕對路徑與相對路徑
**問題**:
```python
p = Path('data/file.txt')
# 不確定這是絕對還是相對路徑
```

**解決**:
```python
# 檢查路徑類型
print(p.is_absolute())  # False

# 轉換為絕對路徑
abs_p = p.resolve()
print(abs_p)  # C:\Users\...\data\file.txt
```

**教學策略**:
- 使用視覺化圖示展示路徑結構
- 演示工作目錄的影響
- 練習路徑轉換

#### 困難 2: 路徑組合錯誤
**問題**:
```python
# 錯誤：字串拼接
path = 'data' + '/' + 'file.txt'  # 平台相依

# 錯誤：使用絕對路徑會覆蓋
base = Path('C:/data')
full = base / 'C:/other/file.txt'  # 結果: C:/other/file.txt
```

**解決**:
```python
# 正確：使用 / 運算子
path = Path('data') / 'file.txt'

# 注意絕對路徑行為
base = Path('C:/data')
full = base / 'subfolder' / 'file.txt'  # 正確
```

**教學策略**:
- 強調 `/` 運算子的規則
- 警告絕對路徑的特殊行為
- 提供反例練習

#### 困難 3: 目錄遍歷效率
**問題**:
```python
# 低效：遞迴搜尋所有檔案
def find_all_files(directory):
    files = []
    for item in directory.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(find_all_files(item))  # 手動遞迴
    return files
```

**解決**:
```python
# 高效：使用 rglob
def find_all_files(directory):
    return list(directory.rglob('*'))
```

**教學策略**:
- 比較 glob 與 rglob
- 展示效能差異
- 討論適用場景

#### 困難 4: 跨平台路徑處理
**問題**:
```python
# Windows 路徑在 Linux 失效
path = Path('C:\\Users\\user\\file.txt')
```

**解決**:
```python
# 使用相對路徑或 Path.home()
path = Path.home() / 'documents' / 'file.txt'

# 或使用環境變數
from os import environ
path = Path(environ.get('USERPROFILE', '~')) / 'documents' / 'file.txt'
```

**教學策略**:
- 避免硬編碼絕對路徑
- 使用 Path.cwd(), Path.home()
- 介紹環境變數

### 教學建議

1. **實作導向**
   - 建立真實的檔案操作專案
   - 練習檔案整理、備份腳本
   - 設計檔案搜尋工具

2. **安全意識**
   - 強調檔案操作的不可逆性
   - 教導備份的重要性
   - 演示錯誤處理

3. **跨平台思維**
   - 在不同系統測試程式碼
   - 討論路徑分隔符差異
   - 使用虛擬環境模擬

4. **效能考量**
   - 比較不同遍歷方法
   - 討論大型目錄的處理
   - 介紹生成器的優勢

## 延伸學習資源

### 官方文件
- [pathlib - Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
- [os.path - Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
- [glob - Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)

### 進階主題
- **符號連結處理**: `resolve(strict=False)`, `readlink()`
- **檔案權限**: `chmod()`, `stat().st_mode`
- **臨時檔案**: `tempfile` 模組
- **檔案監控**: `watchdog` 套件
- **大型目錄處理**: 生成器、迭代器

### 實務應用
- 自動化檔案整理腳本
- 備份系統設計
- 日誌檔案管理
- 專案結構掃描
- 重複檔案偵測

### 相關章節
- **Ch23: File I/O Fundamentals** - 檔案讀寫基礎
- **Ch24: JSON and Serialization** - 結構化資料存儲
- **Ch25: CSV and Data Files** - 表格資料處理
- **Ch27: Modules and Imports** - 模組化設計
- **M07: Todo App** - 整合專案應用

## 學習檢核

完成以下檢核項目，確保掌握本章內容：

### 基礎檢核
- [ ] 能建立並操作 Path 物件
- [ ] 理解絕對路徑與相對路徑
- [ ] 能組合、分解路徑
- [ ] 能檢查檔案與目錄

### 進階檢核
- [ ] 能遍歷目錄並處理檔案
- [ ] 能使用 glob 模式搜尋
- [ ] 能設計檔案組織系統
- [ ] 能處理跨平台路徑

### 實戰檢核
- [ ] 完成所有課堂練習
- [ ] 完成所有課後習題
- [ ] 通過自我測驗 (80% 以上)
- [ ] 能解釋程式碼給他人聽

---

## 本章架構總覽

```
Ch26: 路徑與檔案系統
│
├── Part I: 理論基礎
│   ├── 為什麼需要 pathlib
│   ├── 絕對路徑 vs 相對路徑
│   └── Path 物件設計理念
│
├── Part II: 核心操作
│   ├── Path 物件建立與組合
│   ├── 路徑屬性與解析
│   ├── 檔案與目錄檢查
│   └── 基本檔案操作
│
├── Part III: 進階技巧
│   ├── 目錄遍歷
│   ├── Glob 模式匹配
│   ├── 跨平台處理
│   └── 實戰案例
│
└── Part IV: 整合應用
    ├── 檔案搜尋工具
    ├── 目錄整理器
    ├── 備份系統
    └── 檔案組織最佳實務
```

**學習策略**: 先理解路徑的基本概念，再掌握 Path 物件的操作方法，最後結合實際案例進行練習。重點在於理解物件導向設計的優勢，以及跨平台相容性的重要性。

**下一章預告**: Ch27 將學習模組與套件的組織，建立可重用的程式庫。
