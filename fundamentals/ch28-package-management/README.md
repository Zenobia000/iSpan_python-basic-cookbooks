# Chapter 28: 套件管理與虛擬環境 | Package Management and Virtual Environments

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Chapter 27 (自訂模組與套件), 基本命令列操作 |
| **相關章節** | Chapter 23 (檔案操作), Chapter 27 (模組與套件) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠:

### 知識面（Knowledge）
- **列出** pip 的基本指令與用途
- **定義** 虛擬環境的概念與必要性
- **說明** requirements.txt 的格式與作用

### 理解面（Comprehension）
- **解釋** 為什麼需要虛擬環境隔離專案
- **比較** pip, conda, poetry 等套件管理工具
- **歸納** 套件版本衝突的成因與解法

### 應用面（Application）
- **運用** pip 安裝、升級、移除套件
- **實作** 虛擬環境的建立與啟用
- **解決** 套件依賴問題（dependency resolution）

### 分析面（Analysis）
- **分析** requirements.txt 中的版本限制策略
- **診斷** 套件安裝失敗的常見原因
- **選擇** 適合專案的套件管理方案

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
套件管理與虛擬環境
├── pip 套件管理器
│   ├── 安裝套件（pip install）
│   ├── 列出套件（pip list/freeze）
│   ├── 移除套件（pip uninstall）
│   └── 搜尋套件（pip search - 已棄用）
│
├── 虛擬環境（venv）
│   ├── 建立環境（python -m venv）
│   ├── 啟用環境（activate）
│   ├── 停用環境（deactivate）
│   └── 環境隔離原理
│
├── requirements.txt
│   ├── 匯出依賴（pip freeze）
│   ├── 安裝依賴（pip install -r）
│   └── 版本指定語法
│
└── 最佳實務
    ├── 一專案一環境
    ├── 版本鎖定策略
    └── .gitignore 忽略 venv/
```

### First Principles 解析

#### 為什麼需要套件管理器？
**根本問題**: 如何安裝與管理第三方程式庫？

**最小實作**:
```bash
# 手動下載、解壓、安裝（過時方式）
python setup.py install

# pip 自動化流程
pip install requests
```

**推導過程**:
1. Python 標準庫不足以應對所有需求 → 需要第三方套件
2. 手動管理套件繁瑣易錯 → 需要自動化工具
3. 不同專案需要不同版本 → 需要隔離機制（虛擬環境）

#### 為什麼需要虛擬環境？
**根本問題**: 不同專案依賴相同套件的不同版本

**實例說明**:
```
專案 A 需要 Django 3.2
專案 B 需要 Django 4.0
系統 Python 只能安裝一個版本！

解決方案: 虛擬環境（每個專案獨立的 Python 環境）
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 套件管理器 | Package Manager | 自動化安裝、升級、移除套件的工具（如 pip） |
| 虛擬環境 | Virtual Environment | 隔離的 Python 環境,避免套件版本衝突 |
| 依賴 | Dependency | 專案所需的第三方套件 |
| 依賴解析 | Dependency Resolution | 自動找出並安裝所有相依套件 |
| 鎖定檔案 | Lock File | 記錄精確版本的檔案（如 requirements.txt） |
| PyPI | Python Package Index | Python 官方套件倉庫 |
| Wheel | Wheel | Python 套件的預編譯格式（.whl） |
| 版本語義 | Semantic Versioning | 版本號規則（主版本.次版本.修訂號） |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（5 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（3-5 題） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習 | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（10 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗 | 20 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）: 閱讀本 README,了解套件管理概念
2. **上課**（120 min）:
   - 講義學習（80 min）: `01-lecture.ipynb`
   - 範例演練（40 min）: `02-worked-examples.ipynb`
3. **課堂練習**（30 min）: 完成 `03-practice.ipynb`
4. **課後複習**（90 min）:
   - 完成習題（60 min）: `04-exercises.ipynb`
   - 對照解答（30 min）: `05-solutions.ipynb`
5. **自我測驗**（20 min）: `quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後,請確認您能夠:

### 基本能力
- [ ] 能使用 pip install 安裝套件
- [ ] 能使用 pip list 查看已安裝套件
- [ ] 能建立虛擬環境（python -m venv）
- [ ] 能啟用與停用虛擬環境

### 進階能力
- [ ] 能使用 requirements.txt 管理依賴
- [ ] 能理解版本指定語法（==, >=, ~=）
- [ ] 能診斷套件安裝錯誤
- [ ] 能升級與降級套件版本

### 應用能力
- [ ] 能為新專案設定完整的虛擬環境
- [ ] 能匯出並分享專案依賴
- [ ] 能處理套件版本衝突
- [ ] 能在不同環境間切換（開發/測試/生產）

---

## 📝 理論重點（Key Theoretical Points）

### 1. pip 基本指令
```bash
# 安裝套件
pip install requests
pip install requests==2.28.0      # 指定版本
pip install requests>=2.0,<3.0    # 版本範圍

# 升級套件
pip install --upgrade requests

# 移除套件
pip uninstall requests

# 查看已安裝套件
pip list                          # 列表格式
pip freeze                        # requirements.txt 格式

# 查看套件資訊
pip show requests
```

### 2. 虛擬環境操作
```bash
# 建立虛擬環境
python -m venv myenv

# 啟用虛擬環境
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# 停用虛擬環境
deactivate
```

### 3. requirements.txt 格式
```
# requirements.txt 範例
requests==2.28.0        # 精確版本
django>=3.2,<4.0       # 版本範圍
numpy~=1.21.0          # 相容版本（1.21.x）
pytest                 # 最新版本
```

```bash
# 匯出當前環境依賴
pip freeze > requirements.txt

# 安裝依賴
pip install -r requirements.txt
```

### 4. 版本指定語法
| 語法 | 範例 | 說明 |
|:-----|:-----|:-----|
| `==` | `requests==2.28.0` | 精確版本 |
| `>=` | `django>=3.2` | 大於等於 |
| `<=` | `numpy<=1.21` | 小於等於 |
| `~=` | `flask~=2.0.0` | 相容版本（2.0.x） |
| `,` | `pandas>=1.0,<2.0` | 組合條件 |

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **實際操作演示**:
   - 先不用虛擬環境安裝套件,展示全域污染問題
   - 再用虛擬環境示範隔離效果

2. **版本衝突情境**:
   - 建立兩個專案,刻意使用不同版本的同一套件
   - 讓學生體驗沒有虛擬環境的困擾

3. **命令列練習**:
   - 確保學生熟悉終端機/命令提示字元
   - Windows 學生注意路徑差異（反斜線 vs 斜線）

### 常見學生困難點

#### 困難點 1: 虛擬環境啟用失敗
**症狀**: Windows 執行 `activate` 報錯

**解決方法**:
```bash
# PowerShell 執行政策錯誤
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 或改用 cmd
myenv\Scripts\activate.bat
```

#### 困難點 2: pip 指令找不到
**症狀**: `'pip' is not recognized`

**解決方法**:
```bash
# 使用 python -m pip 代替 pip
python -m pip install requests

# 或將 Python Scripts 加入 PATH
```

#### 困難點 3: 不確定是否在虛擬環境中
**症狀**: 分不清是全域環境還是虛擬環境

**檢查方法**:
```bash
# 方法 1: 提示字元會顯示 (venv_name)
(myenv) C:\project>

# 方法 2: 查看 Python 路徑
python -c "import sys; print(sys.executable)"
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **虛擬環境三步驟**: Create → Activate → Install
- **pip 三要角**: install, list, uninstall
- **requirements.txt 雙向流**: freeze 匯出, install -r 匯入

### 實作練習建議
1. **環境練習**: 建立 3 個虛擬環境,安裝不同版本的同一套件
2. **依賴練習**: 從 GitHub 克隆開源專案,練習安裝依賴
3. **版本練習**: 嘗試升級/降級套件,觀察相依性變化

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [PyPI - Python Package Index](https://pypi.org/)

### 推薦閱讀
- Real Python: [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- PEP 405: [Python Virtual Environments](https://peps.python.org/pep-0405/)

### 進階工具
- [Poetry](https://python-poetry.org/) - 現代化套件管理
- [pipenv](https://pipenv.pypa.io/) - pip + venv 整合
- [conda](https://docs.conda.io/) - 跨語言環境管理

### 延伸主題（進階學習）
- pip-tools 鎖定依賴
- Docker 容器化環境
- pyproject.toml 專案配置（PEP 518）
- 私有 PyPI 伺服器架設

---

## ❓ 常見問題（FAQ）

**Q1: venv 和 virtualenv 有什麼區別?**
A: venv 是 Python 3.3+ 內建模組,virtualenv 是第三方工具。現在建議使用 venv。

**Q2: requirements.txt 應該提交到 Git 嗎?**
A: 應該！但虛擬環境資料夾（venv/）不應提交,加入 .gitignore。

**Q3: 如何更新 requirements.txt 中所有套件?**
A:
```bash
pip list --outdated  # 查看過時套件
pip install --upgrade -r requirements.txt  # 升級全部
pip freeze > requirements.txt  # 更新檔案
```

**Q4: 安裝套件時出現權限錯誤怎麼辦?**
A: 1) 使用虛擬環境（推薦） 2) `pip install --user` 安裝到使用者目錄 3) 避免使用 sudo（Linux/macOS）

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 23（檔案操作）**: 理解 requirements.txt 檔案格式
- **Chapter 27（模組與套件）**: 理解套件的組織結構

### 後續章節
- **Chapter 30（版本控制）**: Git 管理專案時需要 .gitignore venv/

### 對應的 Milestone 專案
- **Milestone 8: 專案重構**（結合 Ch27-30 的知識）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布,基於教科書標準結構

---

## 🎯 成功標準（Success Criteria）

完成本章學習後,您應該能夠:
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能在 5 分鐘內為新專案設定虛擬環境
- ✅ 能解決常見的套件安裝問題

---

**學習提醒**: 虛擬環境是 Python 開發的基本功。每個專案都應該有獨立的虛擬環境！
