# VS Code Python 環境設定指南

**最後更新**：2025-10-05
**適用版本**：VS Code 1.80+, Python 3.8+

---

## 📋 目錄

1. [為什麼選擇 VS Code](#為什麼選擇-vs-code)
2. [安裝 VS Code](#安裝-vs-code)
3. [安裝 Python 擴充](#安裝-python-擴充)
4. [Python 環境設定](#python-環境設定)
5. [Jupyter 整合](#jupyter-整合)
6. [推薦擴充套件](#推薦擴充套件)
7. [快捷鍵與技巧](#快捷鍵與技巧)
8. [常見問題](#常見問題)

---

## 為什麼選擇 VS Code？

**VS Code（Visual Studio Code）** 是 Microsoft 開發的免費程式碼編輯器。

### 優點
- ✅ **免費開源**：完全免費
- ✅ **輕量快速**：啟動速度快
- ✅ **擴充豐富**：Python、Jupyter、Git 等
- ✅ **整合 Jupyter**：直接開啟 .ipynb 檔案
- ✅ **強大除錯**：中斷點、變數檢視
- ✅ **跨平台**：Windows、macOS、Linux

### 與其他 IDE 比較

| 特性 | VS Code | PyCharm | Jupyter |
|:-----|:--------|:--------|:--------|
| **免費** | ✅ | 社群版 | ✅ |
| **輕量** | ✅ | ❌ | ✅ |
| **Jupyter 支援** | ✅ | ✅ | ✅ (原生) |
| **適合初學** | ✅ | 中 | ✅ |
| **專案開發** | ✅ | ✅ | ❌ |

---

## 安裝 VS Code

### 步驟 1：下載 VS Code

前往官網下載：[https://code.visualstudio.com/](https://code.visualstudio.com/)

**Windows**：
- 下載 `.exe` 安裝檔
- 執行並依指示安裝
- ✅ 勾選「Add to PATH」

**macOS**：
- 下載 `.dmg` 檔案
- 拖曳到 Applications 資料夾

**Linux**：
```bash
# Ubuntu/Debian
sudo apt install code

# Fedora
sudo dnf install code
```

---

### 步驟 2：啟動 VS Code

**Windows**：
- 開始選單搜尋「VS Code」
- 或命令列輸入：`code`

**macOS**：
- Spotlight 搜尋「Visual Studio Code」
- 或終端機輸入：`code`

---

## 安裝 Python 擴充

### 必裝擴充：Python

**安裝步驟**：
1. 點擊左側「擴充功能」圖示（或按 `Ctrl + Shift + X`）
2. 搜尋「Python」
3. 點擊 Microsoft 官方的「Python」擴充
4. 點擊「Install」

**包含功能**：
- ✅ 語法高亮
- ✅ 智慧提示（IntelliSense）
- ✅ 程式碼格式化（autopep8, black）
- ✅ Linting（pylint, flake8）
- ✅ 除錯工具
- ✅ Jupyter Notebook 支援

---

### 必裝擴充：Jupyter

**安裝步驟**：
1. 搜尋「Jupyter」
2. 安裝 Microsoft 官方的「Jupyter」擴充

**功能**：
- ✅ 在 VS Code 中開啟 .ipynb 檔案
- ✅ 執行 Jupyter Cell
- ✅ 變數檢視器
- ✅ 繪圖支援

---

## Python 環境設定

### 1. 選擇 Python 解釋器

**步驟**：
1. 按 `Ctrl + Shift + P` 開啟命令選擇區
2. 輸入「Python: Select Interpreter」
3. 選擇已安裝的 Python 版本

**驗證**：
- 左下角應顯示 Python 版本（如 `Python 3.11.4`）

---

### 2. 設定工作區（Workspace）

**開啟專案資料夾**：
1. File → Open Folder
2. 選擇 `iSpan_python-basic-cookbooks` 資料夾
3. 點擊「選擇資料夾」

**工作區設定（.vscode/settings.json）**：
```json
{
    "python.defaultInterpreterPath": "python",
    "python.formatting.provider": "autopep8",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000
}
```

---

## Jupyter 整合

### 在 VS Code 中使用 Jupyter

**步驟 1：開啟 Notebook**
- 點擊任意 `.ipynb` 檔案
- VS Code 自動使用 Jupyter 擴充開啟

**步驟 2：執行 Cell**
- 點擊 Cell 左側的 ▶️ 按鈕
- 或按 `Shift + Enter`

**步驟 3：切換 Kernel**
- 點擊右上角的 Kernel 名稱
- 選擇適當的 Python 環境

---

### Jupyter Notebook vs VS Code Jupyter

| 特性 | Jupyter Notebook | VS Code Jupyter |
|:-----|:-----------------|:----------------|
| **介面** | 網頁 | 編輯器 |
| **功能** | 基本 | 強化（變數檢視、除錯） |
| **編輯體驗** | 一般 | 優秀（自動完成） |
| **適合** | 純學習 | 學習 + 開發 |

---

## 推薦擴充套件

### 開發效率

1. **Python Docstring Generator**
   - 自動產生函式說明文件

2. **indent-rainbow**
   - 縮排視覺化（不同顏色）

3. **Bracket Pair Colorizer**
   - 括號配對顏色

4. **autoDocstring**
   - 自動生成 docstring

---

### 程式碼品質

5. **Pylance**
   - 強化型態檢查
   - 更好的自動完成

6. **Error Lens**
   - 行內顯示錯誤訊息

---

### Git 整合

7. **GitLens**
   - 增強 Git 功能
   - 查看每行程式碼的修改歷史

---

## 快捷鍵與技巧

### 編輯快捷鍵

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Ctrl + Space` | 觸發自動完成 |
| `Ctrl + /` | 註解/取消註解 |
| `Alt + ↑/↓` | 移動整行 |
| `Shift + Alt + ↑/↓` | 複製整行 |
| `Ctrl + D` | 選取下一個相同字詞 |
| `Ctrl + F` | 尋找 |
| `Ctrl + H` | 取代 |

---

### Jupyter Cell 快捷鍵

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Shift + Enter` | 執行 Cell 並移到下一個 |
| `Ctrl + Enter` | 執行 Cell 並停留 |
| `Ctrl + Shift + P` | 命令選擇區 |
| `Esc` | 退出 Cell 編輯模式 |

---

### 視窗管理

| 快捷鍵 | 功能 |
|:-------|:-----|
| `Ctrl + B` | 切換側邊欄 |
| `Ctrl + J` | 切換終端機 |
| `Ctrl + \`` | 開啟終端機 |
| `Ctrl + Shift + E` | 檔案總管 |
| `Ctrl + Shift + F` | 全域搜尋 |

---

## 執行 Python 程式

### 方法 1：執行整個檔案

```python
# 方法 1：右鍵選單
# 右鍵點擊 .py 檔案 → Run Python File in Terminal

# 方法 2：快捷鍵
# 開啟 .py 檔案，按 Ctrl + F5

# 方法 3：執行按鈕
# 點擊右上角的 ▶️ 按鈕
```

---

### 方法 2：執行選取的程式碼

1. 選取要執行的程式碼
2. 按 `Shift + Enter`
3. 程式碼在 Python 互動視窗執行

---

### 方法 3：使用除錯器

```python
# 1. 設定中斷點（點擊行號左側）
# 2. 按 F5 啟動除錯
# 3. 使用除錯工具列：
#    - 繼續 (F5)
#    - 單步執行 (F10)
#    - 進入函式 (F11)
#    - 停止 (Shift + F5)
```

---

## 常見問題（FAQ）

### Q1: VS Code 找不到 Python？

**解決方法**：
```bash
# 1. 確認 Python 已安裝
python --version

# 2. 找到 Python 路徑
# Windows:
where python

# macOS/Linux:
which python3

# 3. 在 VS Code 手動設定路徑
# Ctrl + Shift + P → Python: Select Interpreter → Enter interpreter path
```

---

### Q2: 自動完成不工作？

**解決方法**：
1. 確認已安裝 Python 擴充
2. 確認已選擇正確的 Python 解釋器
3. 重新載入視窗：`Ctrl + Shift + P` → Reload Window

---

### Q3: Jupyter Notebook 無法執行？

**解決方法**：
```bash
# 安裝 ipykernel
pip install ipykernel

# 重新啟動 VS Code
```

---

### Q4: 如何在 VS Code 中使用虛擬環境？

**步驟**：
1. 建立虛擬環境（見 [environment-setup.md](./environment-setup.md)）
2. 在 VS Code 選擇該環境：
   - `Ctrl + Shift + P`
   - 輸入「Python: Select Interpreter」
   - 選擇虛擬環境中的 Python

---

## 🎨 主題與外觀設定

### 更換顏色主題

1. `Ctrl + K, Ctrl + T`
2. 選擇喜歡的主題

**推薦主題**：
- **Dark+**（預設深色）
- **Light+**（預設淺色）
- **One Dark Pro**（Atom 風格）
- **Dracula Official**（護眼）

---

### 字體設定

**settings.json**：
```json
{
    "editor.fontSize": 14,
    "editor.fontFamily": "Consolas, 'Courier New', monospace",
    "editor.lineHeight": 1.5,
    "terminal.integrated.fontSize": 13
}
```

---

## 🚀 進階功能

### 1. Code Snippets（程式碼片段）

建立常用程式碼範本：
1. File → Preferences → User Snippets
2. 選擇「python.json」
3. 新增片段：

```json
{
  "Print Statement": {
    "prefix": "prt",
    "body": [
      "print(f\"${1:variable} = {${1:variable}}\")"
    ],
    "description": "Print formatted variable"
  }
}
```

使用：輸入 `prt` 後按 `Tab`

---

### 2. 多游標編輯

- `Alt + Click`：新增游標
- `Ctrl + Alt + ↑/↓`：上下新增游標
- `Ctrl + D`：選取下一個相同字詞

---

### 3. 重構工具

- **重新命名**：`F2`
- **提取變數**：選取程式碼 → 右鍵 → Extract Variable
- **提取函式**：選取程式碼 → 右鍵 → Extract Method

---

## 🎓 給學習者的建議

### 學習階段（Ch01-Ch11）

**推薦工具**：
- **主要**：Jupyter Notebook（互動學習）
- **輔助**：VS Code（編輯 .py 檔案）

---

### 專案階段（Milestone 專案）

**推薦工具**：
- **主要**：VS Code（多檔案管理）
- **輔助**：Jupyter（實驗與測試）

---

## 🔧 推薦的 settings.json 設定

完整設定檔（針對 Python 學習）：

```json
{
  // 編輯器
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.rulers": [79],

  // Python
  "python.defaultInterpreterPath": "python",
  "python.formatting.provider": "autopep8",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.analysis.typeCheckingMode": "basic",

  // Jupyter
  "jupyter.askForKernelRestart": false,
  "jupyter.interactiveWindow.textEditor.executeSelection": true,

  // 檔案
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  },

  // 終端機
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.defaultProfile.windows": "Command Prompt"
}
```

---

## ✅ 檢核清單

設定完成後，請確認：

- [ ] VS Code 已成功安裝
- [ ] Python 擴充已安裝
- [ ] Jupyter 擴充已安裝
- [ ] 能選擇正確的 Python 解釋器
- [ ] 能開啟並執行 .py 檔案
- [ ] 能開啟並執行 .ipynb 檔案
- [ ] 自動完成功能正常
- [ ] 能使用除錯器設定中斷點

---

## 🎯 快速上手測試

### 測試 1：執行 Python 檔案

1. 建立 `test.py`：
```python
print("Hello from VS Code!")
name = input("你的名字：")
print(f"你好，{name}！")
```

2. 按 `F5` 執行
3. 在終端機輸入名字

---

### 測試 2：執行 Jupyter Notebook

1. 開啟 `fundamentals/ch01-variables-and-types/01-lecture.ipynb`
2. 點擊第一個 Cell
3. 按 `Shift + Enter` 執行
4. 觀察輸出結果

---

## 🔗 相關文件

- [Jupyter 設定指南](./jupyter-setup.md) - Jupyter Notebook 安裝
- [虛擬環境設定](./environment-setup.md) - Python 虛擬環境管理
- [Git 設定指南](./git-setup.md) - Git 版本控制設定

---

## 📚 學習資源

### 官方文件
- [VS Code Python 教學](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Jupyter 支援](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### 推薦影片
- [VS Code Python Tutorial (Corey Schafer)](https://www.youtube.com/watch?v=06I63_p-2A4)
- [VS Code Jupyter Notebook Tutorial](https://www.youtube.com/watch?v=DA6ZAHBPF1U)

---

**提示**：VS Code 功能強大，但初學階段不需要全部掌握。先熟悉基本編輯與執行，隨著學習進度逐步探索進階功能！
