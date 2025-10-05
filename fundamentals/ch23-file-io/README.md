# Chapter 23: 檔案操作基礎 | File I/O Basics

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中級) |
| **先備知識** | Chapter 20-22 (異常處理), Chapter 7 (字串) |
| **相關章節** | Chapter 24 (JSON), Chapter 25 (CSV), Chapter 26 (路徑) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 檔案操作的基本模式：讀取、寫入、附加
- **定義** 文字檔與二進位檔的差異
- **說明** `with` 語句的作用與優點

### 理解面（Comprehension）
- **解釋** 為什麼需要關閉檔案（資源管理）
- **比較** `read()`, `readline()`, `readlines()` 的差異
- **歸納** 檔案編碼（UTF-8, Big5）的重要性

### 應用面（Application）
- **運用** `open()` 函式進行檔案讀寫
- **實作** 使用 `with` 語句自動管理檔案資源
- **解決** 檔案不存在、權限錯誤等常見問題

### 分析面（Analysis）
- **分析** 檔案操作中的異常處理策略
- **診斷** 編碼錯誤（UnicodeDecodeError）的原因
- **選擇** 適合特定情境的讀寫模式

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
檔案操作基礎
├── 檔案開啟與關閉
│   ├── open() 函式
│   ├── close() 方法
│   └── with 語句（context manager）
│
├── 讀取模式
│   ├── read() - 一次讀取全部
│   ├── readline() - 逐行讀取
│   └── readlines() - 讀取為列表
│
├── 寫入模式
│   ├── write() - 寫入字串
│   ├── writelines() - 寫入列表
│   └── 模式：'w' (覆蓋), 'a' (附加)
│
└── 檔案類型
    ├── 文字檔（text mode）
    └── 二進位檔（binary mode）
```

### First Principles 解析

#### 為什麼需要檔案操作？
**根本問題**：程式執行結束後，記憶體中的資料會消失，需要永久儲存

**最小實作**：
```python
# 寫入檔案
f = open("data.txt", "w")
f.write("Hello, World!")
f.close()

# 讀取檔案
f = open("data.txt", "r")
content = f.read()
f.close()
```

**推導過程**：
1. 資料需要持久化 → 需要儲存裝置（硬碟）
2. 儲存需要組織 → 需要檔案系統
3. 存取需要介面 → 需要檔案操作函式（open, read, write）
4. 資源有限 → 需要關閉檔案（釋放資源）

#### 為什麼需要 with 語句？
**根本問題**：手動管理檔案關閉容易遺忘，造成資源洩漏

**對比**：
```python
# 傳統方式：需要手動關閉
f = open("file.txt", "r")
content = f.read()
f.close()  # ❌ 容易遺忘！

# with 語句：自動關閉
with open("file.txt", "r") as f:
    content = f.read()
# ✅ 離開區塊時自動關閉
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 檔案操作 | File I/O | 讀取或寫入檔案資料的操作 |
| 檔案句柄 | File Handle | open() 返回的檔案物件，用於後續操作 |
| 讀取模式 | Read Mode | 'r' - 以唯讀方式開啟檔案 |
| 寫入模式 | Write Mode | 'w' - 以覆蓋方式寫入（會刪除原內容） |
| 附加模式 | Append Mode | 'a' - 在檔案末端追加內容 |
| 上下文管理器 | Context Manager | 使用 `with` 語句自動管理資源 |
| 文字模式 | Text Mode | 預設模式，處理字串資料 |
| 二進位模式 | Binary Mode | 'b' - 處理位元組資料（如圖片） |
| 編碼 | Encoding | 字元與位元組的轉換方式（如 UTF-8） |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 90 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 120 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 25 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解檔案操作的重要性
2. **上課**（130 min）：
   - 講義學習（90 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（120 min）：
   - 完成習題（90 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（25 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能使用 `open()` 開啟檔案並指定模式（'r', 'w', 'a'）
- [ ] 能使用 `read()` 讀取檔案全部內容
- [ ] 能使用 `write()` 寫入文字到檔案
- [ ] 能使用 `with` 語句自動管理檔案資源

### 進階能力
- [ ] 能使用 `readline()` 和 `readlines()` 逐行處理大檔案
- [ ] 能正確處理檔案編碼（指定 `encoding='utf-8'`）
- [ ] 能區分覆蓋模式（'w'）與附加模式（'a'）
- [ ] 能處理檔案操作相關異常（FileNotFoundError, PermissionError）

### 應用能力
- [ ] 能撰寫程式批次處理多個文字檔
- [ ] 能實作簡單的日誌（log）記錄功能
- [ ] 能除錯編碼錯誤（UnicodeDecodeError）
- [ ] 能設計安全的檔案寫入流程（避免資料遺失）

---

## 📝 理論重點（Key Theoretical Points）

### 1. 檔案操作的基本流程
```python
# 標準流程（三步驟）
# 1. 開啟檔案
file = open("example.txt", "r")

# 2. 操作檔案
content = file.read()

# 3. 關閉檔案
file.close()

# ✅ 推薦：使用 with 語句
with open("example.txt", "r") as file:
    content = file.read()
# 自動關閉，即使發生異常也會正確關閉
```

### 2. 檔案開啟模式對照表

| 模式 | 說明 | 檔案不存在 | 檔案已存在 | 常見用途 |
|:-----|:-----|:-----------|:-----------|:---------|
| `'r'` | 唯讀 | ❌ 報錯 | ✅ 讀取原內容 | 讀取設定檔 |
| `'w'` | 寫入（覆蓋） | ✅ 建立新檔 | ⚠️ 刪除原內容 | 產生報表 |
| `'a'` | 附加 | ✅ 建立新檔 | ✅ 保留原內容 | 日誌記錄 |
| `'r+'` | 讀寫 | ❌ 報錯 | ✅ 可讀可寫 | 更新檔案 |
| `'w+'` | 讀寫（覆蓋） | ✅ 建立新檔 | ⚠️ 刪除原內容 | 暫存檔 |
| `'rb'` | 二進位讀取 | ❌ 報錯 | ✅ 讀取原內容 | 讀取圖片 |
| `'wb'` | 二進位寫入 | ✅ 建立新檔 | ⚠️ 刪除原內容 | 儲存圖片 |

### 3. 讀取方法比較

| 方法 | 返回型態 | 適用情境 | 記憶體使用 |
|:-----|:---------|:---------|:-----------|
| `read()` | str（全部內容） | 小檔案 | 高（一次載入） |
| `readline()` | str（一行） | 逐行處理 | 低（逐行載入） |
| `readlines()` | list（所有行） | 需要列表操作 | 高（全部載入） |
| `for line in file` | 迭代器 | 大檔案逐行 | 低（串流處理） |

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從實際需求切入**：
   - 範例：為什麼遊戲需要存檔？為什麼應用程式需要設定檔？
   - 強調檔案操作是資料持久化的基礎

2. **強調 with 語句的重要性**：
   - 演示忘記 `close()` 的後果（資源洩漏）
   - 展示異常發生時，with 仍會正確關閉檔案

3. **實際操作演示**：
   - 在 Jupyter 中建立實際檔案，讓學生看到檔案系統的變化
   - 使用 `!cat` (Linux/Mac) 或 `!type` (Windows) 顯示檔案內容

4. **編碼問題的處理**：
   - 示範 Big5 與 UTF-8 的差異（使用繁體中文範例）
   - 說明 `encoding='utf-8'` 的必要性

### 常見學生困難點

#### 困難點 1：忘記關閉檔案
**症狀**：程式執行後檔案被鎖定，無法刪除或修改

**解決方法**：
```python
# ❌ 錯誤：忘記關閉
file = open("test.txt", "w")
file.write("data")
# 檔案未關閉，資源未釋放

# ✅ 正確：使用 with
with open("test.txt", "w") as file:
    file.write("data")
# 自動關閉
```

#### 困難點 2：寫入模式混淆
**症狀**：使用 'w' 模式誤刪原有資料

**解決方法**：
```python
# ❌ 危險：'w' 會刪除原內容
with open("important.txt", "w") as f:
    f.write("new data")  # 原有資料消失！

# ✅ 安全：先讀取，再決定
with open("important.txt", "a") as f:  # 使用 'a' 附加
    f.write("\nnew data")  # 保留原資料
```

#### 困難點 3：編碼錯誤
**症狀**：`UnicodeDecodeError: 'utf-8' codec can't decode`

**解決方法**：
```python
# ❌ 錯誤：使用錯誤編碼
with open("big5_file.txt", "r") as f:  # 預設 UTF-8
    content = f.read()  # 可能報錯

# ✅ 正確：指定正確編碼
with open("big5_file.txt", "r", encoding="big5") as f:
    content = f.read()

# 或轉換編碼
with open("big5_file.txt", "r", encoding="big5") as f:
    content = f.read()
with open("utf8_file.txt", "w", encoding="utf-8") as f:
    f.write(content)
```

#### 困難點 4：檔案路徑錯誤
**症狀**：`FileNotFoundError: No such file or directory`

**解決方法**：
```python
import os

# 檢查檔案是否存在
if os.path.exists("file.txt"):
    with open("file.txt", "r") as f:
        content = f.read()
else:
    print("檔案不存在！")

# 或使用異常處理
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("找不到檔案，請檢查路徑")
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **R**ead（讀取）：**R**etrieve 取回資料
- **W**rite（寫入）：**W**ipe 清空重寫
- **A**ppend（附加）：**A**dd 追加到尾端

### 實作練習建議
1. **建立測試檔案**：手動建立 `.txt` 檔案，練習讀取
2. **觀察檔案變化**：每次寫入後，用文字編輯器檢查結果
3. **故意製造錯誤**：嘗試讀取不存在的檔案，觀察錯誤訊息
4. **編碼實驗**：建立包含中文的檔案，測試不同編碼

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Built-in Functions: open()](https://docs.python.org/3/library/functions.html#open)
- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Context Managers (with statement)](https://docs.python.org/3/reference/compound_stmts.html#with)

### 推薦閱讀
- Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.), Chapter 4.2
- Downey, A. B. (2015). *Think Python* (2nd ed.), Chapter 14

### 互動式工具
- [Real Python: Reading and Writing Files](https://realpython.com/read-write-files-python/)
- [Python File Handling Cheatsheet](https://www.pythoncheatsheet.org/cheatsheet/file-handling)

### 延伸主題（進階學習）
- `os` 模組：檔案系統操作（Chapter 26）
- `pathlib` 模組：現代化路徑處理（Chapter 26）
- `json` 模組：結構化資料儲存（Chapter 24）
- `csv` 模組：試算表資料處理（Chapter 25）

---

## ❓ 常見問題（FAQ）

**Q1: 什麼時候該用 'w'，什麼時候該用 'a'？**
A: 如果要**完全重寫**檔案（如產生報表），用 'w'；如果要**保留原資料並追加**（如日誌），用 'a'。

**Q2: 為什麼我的中文字會變成亂碼？**
A: 可能是編碼不一致。建議統一使用 UTF-8：`open(file, encoding='utf-8')`

**Q3: read() 和 readlines() 有什麼差別？**
A: `read()` 返回整個檔案的字串；`readlines()` 返回每行為元素的列表。大檔案建議用 `for line in file` 逐行處理。

**Q4: 如何確保檔案一定會被關閉？**
A: 使用 `with` 語句，即使程式發生異常，檔案也會被正確關閉。

**Q5: 'r+' 和 'w+' 有什麼區別？**
A: 'r+' 要求檔案必須存在，且不會刪除原內容；'w+' 會建立新檔或清空現有檔案。

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 20-22（異常處理）**：處理檔案操作錯誤
- **Chapter 7（字串）**：處理檔案內容

### 後續章節
- **Chapter 24（JSON）**：結構化資料的讀寫
- **Chapter 25（CSV）**：試算表資料的處理
- **Chapter 26（路徑）**：跨平台檔案路徑管理

### 對應的 Milestone 專案
- **Milestone 7: 待辦事項應用**（結合 Ch23-26 的知識）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能撰寫一個簡單的日誌記錄程式
- ✅ 能正確處理檔案不存在、編碼錯誤等常見問題

---

**學習提醒**：檔案操作是資料持久化的基礎，務必透過大量實作熟悉！建議在電腦上建立測試資料夾，實際操作每個範例。
