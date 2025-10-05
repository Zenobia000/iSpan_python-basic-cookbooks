# Jupyter Notebook 安裝與設定指南

**最後更新**：2025-10-05
**適用版本**：Python 3.8+, Jupyter Notebook 6.5+

---

## 📋 目錄

1. [什麼是 Jupyter Notebook](#什麼是-jupyter-notebook)
2. [安裝 Jupyter](#安裝-jupyter)
3. [啟動 Jupyter](#啟動-jupyter)
4. [基本操作](#基本操作)
5. [常用快捷鍵](#常用快捷鍵)
6. [進階設定](#進階設定)
7. [常見問題](#常見問題)

---

## 什麼是 Jupyter Notebook？

**Jupyter Notebook** 是一個互動式的網頁應用程式，讓你可以：
- 編寫並執行 Python 程式碼
- 撰寫說明文字（支援 Markdown）
- 視覺化資料與結果
- 將程式碼、文字、圖表整合在同一文件

**為什麼本課程使用 Jupyter？**
- ✅ 適合學習：可以逐段執行程式碼
- ✅ 即時回饋：立即看到執行結果
- ✅ 筆記整合：程式碼與說明並存
- ✅ 易於分享：.ipynb 檔案可直接開啟

---

## 安裝 Jupyter

### 方法 1：使用 pip（推薦）

**步驟 1：確認 Python 已安裝**
```bash
python --version
# 應顯示：Python 3.8.x 或更高版本
```

**步驟 2：安裝 Jupyter**
```bash
pip install jupyter
```

**步驟 3：驗證安裝**
```bash
jupyter --version
# 應顯示版本號，如：jupyter core: 5.3.0
```

---

### 方法 2：使用 Anaconda（適合初學者）

**Anaconda** 是 Python 的完整發行版，已包含 Jupyter。

**步驟 1：下載 Anaconda**
- 前往 [https://www.anaconda.com/download](https://www.anaconda.com/download)
- 選擇對應作業系統的版本
- 下載並執行安裝程式

**步驟 2：驗證安裝**
- 開啟 Anaconda Navigator
- 點擊 Jupyter Notebook 的「Launch」按鈕

---

## 啟動 Jupyter

### Windows

**方法 1：命令提示字元**
```cmd
# 1. 開啟命令提示字元（Win + R → 輸入 cmd）
# 2. 切換到專案目錄
cd D:\python_workspace\github\iSpan_python-basic-cookbooks

# 3. 啟動 Jupyter
jupyter notebook
```

**方法 2：Anaconda Navigator**
- 開啟 Anaconda Navigator
- 點擊 Jupyter Notebook 的「Launch」

---

### macOS / Linux

```bash
# 1. 開啟終端機（Terminal）
# 2. 切換到專案目錄
cd ~/iSpan_python-basic-cookbooks

# 3. 啟動 Jupyter
jupyter notebook
```

---

### 啟動後會發生什麼？

1. **瀏覽器自動開啟**，顯示檔案管理介面
2. **預設網址**：`http://localhost:8888`
3. **命令列持續執行**（不要關閉）

**畫面示意**：
```
[I 10:30:00.123 NotebookApp] Serving notebooks from local directory: /path/to/project
[I 10:30:00.123 NotebookApp] Jupyter Notebook is running at:
[I 10:30:00.123 NotebookApp] http://localhost:8888/?token=abc123...
[I 10:30:00.123 NotebookApp] Use Control-C to stop this server
```

---

## 基本操作

### 1. 建立新 Notebook

1. 點擊右上角「New」
2. 選擇「Python 3」
3. 新 Notebook 自動開啟

### 2. Cell 的類型

**Code Cell（程式碼）**：
- 預設類型
- 可執行 Python 程式碼
- 按 `Shift + Enter` 執行

**Markdown Cell（文字說明）**：
- 用於撰寫說明文字
- 支援 Markdown 語法
- 按 `Shift + Enter` 渲染

### 3. 執行 Cell

| 操作 | 快捷鍵 | 說明 |
|:-----|:-------|:-----|
| 執行並移到下一個 | `Shift + Enter` | 最常用 |
| 執行並停留 | `Ctrl + Enter` | 調試用 |
| 執行並插入下方 | `Alt + Enter` | 連續執行 |

### 4. 儲存與匯出

**儲存**：
- 快捷鍵：`Ctrl + S`（Mac: `Cmd + S`）
- 自動儲存：每 120 秒

**匯出**：
- File → Download as → Python (.py)
- File → Download as → PDF via LaTeX
- File → Download as → HTML

---

## 常用快捷鍵

### 編輯模式（Edit Mode）- 綠色框

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Esc` | 切換到命令模式 |
| `Ctrl + /` | 註解/取消註解 |
| `Tab` | 自動完成 |
| `Shift + Tab` | 顯示函式說明 |

### 命令模式（Command Mode）- 藍色框

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Enter` | 進入編輯模式 |
| `A` | 在上方插入 Cell |
| `B` | 在下方插入 Cell |
| `D, D` | 刪除 Cell（按兩次 D） |
| `M` | 轉為 Markdown Cell |
| `Y` | 轉為 Code Cell |
| `C` | 複製 Cell |
| `V` | 貼上 Cell |
| `Z` | 復原刪除 |

### 通用快捷鍵

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Shift + Enter` | 執行 Cell 並移到下一個 |
| `Ctrl + Enter` | 執行 Cell 並停留 |
| `Alt + Enter` | 執行 Cell 並在下方插入新 Cell |
| `Ctrl + S` | 儲存 |

---

## 進階設定

### 1. 修改預設工作目錄

**Windows**：
```bash
# 生成設定檔
jupyter notebook --generate-config

# 編輯設定檔（位於 C:\Users\你的使用者名稱\.jupyter\）
# 找到並修改這行：
# c.NotebookApp.notebook_dir = 'D:/python_workspace'
```

**macOS/Linux**：
```bash
# 生成設定檔
jupyter notebook --generate-config

# 編輯 ~/.jupyter/jupyter_notebook_config.py
# c.NotebookApp.notebook_dir = '/Users/你的使用者名稱/projects'
```

---

### 2. 安裝實用擴充套件

```bash
# 安裝 nbextensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# 安裝 nbextensions configurator
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```

**推薦擴充**：
- **Table of Contents**：自動產生目錄
- **Code prettify**：自動格式化程式碼
- **ExecuteTime**：顯示 Cell 執行時間
- **Variable Inspector**：變數檢視器

---

### 3. 安裝主題（美化介面）

```bash
# 安裝 jupyterthemes
pip install jupyterthemes

# 列出可用主題
jt -l

# 套用主題（推薦 onedork）
jt -t onedork -fs 12 -nfs 12 -tfs 12 -ofs 11

# 恢復預設
jt -r
```

---

## 常見問題（FAQ）

### Q1: 啟動 Jupyter 後瀏覽器沒有自動開啟？

**解決方法**：
1. 查看命令列的輸出，找到 URL（如 `http://localhost:8888/?token=...`）
2. 手動複製 URL 到瀏覽器開啟

---

### Q2: 如何停止 Jupyter？

**方法 1（推薦）**：
- 在命令列按 `Ctrl + C`
- 輸入 `y` 確認

**方法 2**：
- 在瀏覽器中：File → Close and Halt
- 關閉所有 Notebook 後再關閉終端

---

### Q3: Cell 執行卡住無法停止？

**解決方法**：
- 點擊上方工具列的 ⏹️（停止）按鈕
- 或按快捷鍵：`I, I`（按兩次 I）
- 重啟 Kernel：Kernel → Restart

---

### Q4: 無法找到已安裝的套件？

**原因**：可能安裝在不同的 Python 環境

**解決方法**：
```bash
# 在 Jupyter 的 Cell 中執行
import sys
print(sys.executable)  # 查看使用的 Python 路徑

# 安裝到正確環境
!pip install package_name
```

---

### Q5: 如何在 Jupyter 中使用虛擬環境？

```bash
# 1. 建立虛擬環境
python -m venv myenv

# 2. 啟動虛擬環境
# Windows:
myenv\Scripts\activate
# macOS/Linux:
source myenv/bin/activate

# 3. 安裝 ipykernel
pip install ipykernel

# 4. 將虛擬環境加入 Jupyter
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"

# 5. 啟動 Jupyter，在 Kernel 選單中選擇 "Python (myenv)"
```

---

## 🎯 Jupyter 使用技巧

### 1. Magic Commands

```python
# 查看所有 magic commands
%lsmagic

# 常用 magic commands
%time code           # 測量執行時間
%timeit code         # 多次執行取平均
%who                 # 列出所有變數
%whos                # 詳細變數資訊
%reset               # 清除所有變數
%load filename.py    # 載入 Python 檔案
!ls                  # 執行系統命令
```

---

### 2. 顯示多個輸出

```python
# 預設只顯示最後一個運算式
3 + 5
2 * 4  # 只會顯示這個

# 方法 1：使用 print()
print(3 + 5)
print(2 * 4)

# 方法 2：使用 IPython.display
from IPython.display import display
display(3 + 5)
display(2 * 4)
```

---

### 3. 在 Markdown Cell 中顯示數學公式

使用 LaTeX 語法：

```markdown
行內公式：$E = mc^2$

區塊公式：
$$
f(x) = \int_{-\infty}^{\infty} e^{-x^2} dx
$$
```

---

## 🚀 最佳實踐

### 1. Notebook 組織

```
my_notebook.ipynb
├── Title Cell (Markdown)
├── Import Cell (Code)
├── Section 1 (Markdown)
│   ├── Code Cell 1
│   ├── Code Cell 2
│   └── Results Cell
├── Section 2 (Markdown)
│   └── ...
└── Summary (Markdown)
```

### 2. 命名規範

- ✅ 有意義的檔名：`01-lecture.ipynb`
- ✅ 使用小寫與連字號：`data-analysis.ipynb`
- ❌ 避免空格：`my notebook.ipynb`（改為 `my-notebook.ipynb`）

### 3. Cell 的粒度

- ✅ 每個 Cell 做一件事
- ✅ 相關程式碼放在同一 Cell
- ❌ 避免單一 Cell 過長（建議 < 50 行）

---

## 📚 學習資源

### 官方文件
- [Jupyter 官方網站](https://jupyter.org/)
- [Jupyter Notebook 文件](https://jupyter-notebook.readthedocs.io/)

### 推薦教學
- [Jupyter Notebook Tutorial (Dataquest)](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [Jupyter Notebook 快速入門](https://realpython.com/jupyter-notebook-introduction/)

### 替代工具
- **JupyterLab**：Jupyter 的下一代介面
  ```bash
  pip install jupyterlab
  jupyter lab
  ```
- **VS Code Jupyter 擴充**：在 VS Code 中使用 Jupyter
- **Google Colab**：線上 Jupyter 環境（免安裝）

---

## ⚠️ 注意事項

### 1. Kernel 狀態

- **實心圓（●）**：Kernel 忙碌中
- **空心圓（○）**：Kernel 閒置
- 長時間未回應？重啟 Kernel

### 2. 執行順序

```python
# Cell [1]
x = 10

# Cell [3] (先執行)
y = x + 5

# Cell [2] (後執行)
x = 20

# 此時 y 的值是？
```

**重要**：Cell 的執行順序由執行時間決定，不是由上到下！

**建議**：養成「由上而下」執行的習慣，或定期 Restart & Run All

---

### 3. 自動儲存

- Jupyter 每 120 秒自動儲存
- 重要變更後手動儲存（`Ctrl + S`）
- 定期備份 .ipynb 檔案

---

## 🎓 給教師的建議

### 課堂使用

1. **投影設定**：
   - 增大字體：設定 → 字體大小
   - 使用 RISE 擴充做簡報

2. **學生示範**：
   - 使用 Jupyter 即時 live coding
   - 讓學生能看到思考過程

3. **作業收繳**：
   - 學生上傳 .ipynb 檔案
   - 使用 nbgrader 自動評分

---

## 🆚 Jupyter vs 傳統 IDE

| 特性 | Jupyter | VS Code/PyCharm |
|:-----|:--------|:----------------|
| **學習曲線** | 低 | 中 |
| **互動性** | 高 | 低 |
| **適合場景** | 學習、實驗、資料分析 | 開發大型專案 |
| **除錯工具** | 基本 | 強大 |
| **版本控制** | 較困難 | 容易 |

**建議**：
- 學習階段：使用 Jupyter
- 專案開發：使用 VS Code（可整合 Jupyter）

---

## ✅ 檢核清單

安裝完成後，請確認：

- [ ] Python 3.8+ 已安裝
- [ ] Jupyter Notebook 已安裝
- [ ] 能成功啟動 Jupyter
- [ ] 能建立並執行新 Notebook
- [ ] 能執行 Code Cell 和 Markdown Cell
- [ ] 理解 Kernel 的概念
- [ ] 知道如何儲存與關閉 Notebook

---

## 🔗 相關文件

- [VS Code 設定指南](./vscode-setup.md) - VS Code Python 環境配置
- [虛擬環境設定](./environment-setup.md) - Python 虛擬環境管理
- [Git 設定指南](./git-setup.md) - Git 版本控制設定

---

**提示**：完成設定後，請開啟 `fundamentals/ch01-variables-and-types/01-lecture.ipynb` 開始學習！
