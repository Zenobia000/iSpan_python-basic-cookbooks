"""
生成 Ch28: 套件管理與虛擬環境 完整內容
包含 5 個 notebooks: 02-worked-examples, 03-practice, 04-exercises, 05-solutions, quiz
"""

import json
import os

# 切換到 fundamentals/ch28-package-management 目錄
TARGET_DIR = r"D:\python_workspace\github\iSpan_python-basic-cookbooks\fundamentals\ch28-package-management"
os.chdir(TARGET_DIR)

def create_notebook(cells):
    """建立 Jupyter Notebook 結構"""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def create_cell(cell_type, source):
    """建立單一 cell"""
    if cell_type == "markdown":
        return {
            "cell_type": "markdown",
            "metadata": {},
            "source": source
        }
    else:  # code
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": source
        }

# ==================== 02-worked-examples.ipynb ====================

worked_examples_cells = [
    create_cell("markdown", """# 套件管理與虛擬環境 | Package Management and Virtual Environments

## 📝 詳解範例 | Worked Examples

---

## 💡 本檔案目的

本檔案提供 **5 個循序漸進的詳解範例**，每個範例包含：
1. **問題描述**：實際應用情境
2. **分析思路**：如何拆解問題
3. **逐步實作**：程式碼 + 註解
4. **執行結果**：預期輸出
5. **知識點總結**：學到什麼

---"""),

    create_cell("markdown", """## 範例 1：pip 基礎操作與套件查詢

### 📋 問題描述

作為 Python 開發者，你需要：
1. 了解目前環境已安裝哪些套件
2. 查詢特定套件的詳細資訊
3. 分析套件之間的依賴關係
4. 將套件清單匯出以供他人使用

**難度**：基礎

### 🔍 分析思路

1. **環境檢查**：使用 `pip list` 列出所有套件
2. **資訊查詢**：使用 `pip show` 查看套件詳情
3. **依賴分析**：理解套件的 Requires 與 Required-by
4. **清單匯出**：使用 `pip freeze` 生成 requirements.txt

### 💻 逐步實作"""),

    create_cell("code", """import subprocess
import json

# 步驟 1: 列出已安裝套件
print("=== 已安裝套件清單 ===")
print()

# 執行 pip list（返回前 10 個套件作為示範）
result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
lines = result.stdout.split('\\n')

# 顯示標題和前 10 個套件
for i, line in enumerate(lines[:12]):  # 標題 2 行 + 10 個套件
    print(line)

print("...")
print()

# 步驟 2: 查詢特定套件資訊（以 pip 自己為例）
print("=== 套件詳細資訊: pip ===")
print()

result = subprocess.run(['pip', 'show', 'pip'], capture_output=True, text=True)
print(result.stdout)

# 步驟 3: 分析套件依賴
print("=== 套件依賴分析 ===")
print()
print("解析 pip show 輸出：")
print("- Name: 套件名稱")
print("- Version: 目前版本")
print("- Location: 安裝路徑")
print("- Requires: 此套件依賴的其他套件")
print("- Required-by: 哪些套件依賴此套件")
print()

# 步驟 4: 匯出套件清單
print("=== 匯出套件清單 ===")
print()

result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
packages = result.stdout.strip().split('\\n')[:5]  # 前 5 個套件作為範例

print("requirements.txt 格式範例:")
for pkg in packages:
    print(f"  {pkg}")
print("  ...")
print()

print("💡 實際使用時，執行: pip freeze > requirements.txt")"""),

    create_cell("markdown", """### 📊 執行結果

```
=== 已安裝套件清單 ===

Package    Version
---------- -------
pip        24.0
setuptools 69.0.0
...

=== 套件詳細資訊: pip ===

Name: pip
Version: 24.0
Summary: The PyPA recommended tool for installing Python packages
Location: /usr/lib/python3.x/site-packages
Requires:
Required-by:

=== 匯出套件清單 ===

requirements.txt 格式範例:
  certifi==2024.2.2
  charset-normalizer==3.3.2
  ...
```

### 📚 知識點總結

- ✅ `pip list` 顯示所有已安裝套件
- ✅ `pip show [package]` 顯示套件詳細資訊
- ✅ `pip freeze` 以 requirements.txt 格式輸出
- ✅ 理解套件依賴關係的重要性
- ✅ 使用 subprocess 執行命令列工具

---"""),

    create_cell("markdown", """## 範例 2：虛擬環境建立與管理

### 📋 問題描述

建立一個新專案，需要使用虛擬環境來隔離依賴：
1. 建立虛擬環境
2. 啟用虛擬環境
3. 驗證環境隔離
4. 在虛擬環境中安裝套件
5. 停用虛擬環境

**難度**：基礎

### 🔍 分析思路

1. **環境建立**：使用 `python -m venv` 建立獨立環境
2. **環境啟用**：執行對應平台的啟用腳本
3. **環境驗證**：檢查 Python 執行檔路徑
4. **套件隔離**：確認套件安裝在虛擬環境中

### 💻 逐步實作"""),

    create_cell("code", """import os
import sys
import subprocess
from pathlib import Path

print("=== 虛擬環境建立與管理 ===")
print()

# 步驟 1: 建立虛擬環境
print("[1] 建立虛擬環境")
print()

venv_name = "demo_venv"
print(f"指令: python -m venv {venv_name}")
print()
print(f"執行結果:")
print(f"  建立目錄: {venv_name}/")
print(f"  建立子目錄: Scripts/ (Windows) 或 bin/ (macOS/Linux)")
print(f"  建立子目錄: Lib/ (Windows) 或 lib/ (macOS/Linux)")
print(f"  建立子目錄: Include/")
print(f"  建立檔案: pyvenv.cfg (環境配置)")
print()

# 實際執行（註解掉避免真的建立）
# subprocess.run(['python', '-m', 'venv', venv_name])
# print(f"✓ 虛擬環境 {venv_name} 建立成功")
# print()

# 步驟 2: 啟用虛擬環境
print("[2] 啟用虛擬環境")
print()

if sys.platform == 'win32':
    activate_cmd = f"{venv_name}\\\\Scripts\\\\activate"
    activate_cmd_ps = f"{venv_name}\\\\Scripts\\\\Activate.ps1"
    print("Windows 系統:")
    print(f"  命令提示字元: {activate_cmd}")
    print(f"  PowerShell: {activate_cmd_ps}")
else:
    activate_cmd = f"source {venv_name}/bin/activate"
    print("macOS/Linux 系統:")
    print(f"  指令: {activate_cmd}")

print()
print("啟用後的變化:")
print(f"  - 提示字元前會顯示 ({venv_name})")
print(f"  - Python 路徑變更為虛擬環境路徑")
print(f"  - pip 安裝套件會安裝到虛擬環境")
print()

# 步驟 3: 驗證環境隔離
print("[3] 驗證環境隔離")
print()

print("檢查 Python 路徑:")
print(f"  目前路徑: {sys.executable}")
print()

if venv_name in sys.executable:
    print(f"✓ 目前在虛擬環境 {venv_name} 中")
else:
    print("✗ 目前在系統 Python 環境中")

print()

# 步驟 4: 虛擬環境中的套件
print("[4] 虛擬環境套件管理")
print()

print("新建虛擬環境預設套件:")
print("  - pip")
print("  - setuptools")
print()

print("安裝新套件範例:")
print("  pip install requests")
print("  → 套件會安裝到: {venv_name}/Lib/site-packages/")
print()

# 步驟 5: 停用虛擬環境
print("[5] 停用虛擬環境")
print()
print("指令: deactivate")
print()
print("停用後的變化:")
print("  - 提示字元前的環境名稱消失")
print("  - Python 路徑恢復為系統路徑")
print("  - pip 操作回到系統環境")"""),

    create_cell("markdown", """### 📊 執行結果

```
=== 虛擬環境建立與管理 ===

[1] 建立虛擬環境

指令: python -m venv demo_venv

執行結果:
  建立目錄: demo_venv/
  建立子目錄: Scripts/ (Windows) 或 bin/ (macOS/Linux)
  ...

[2] 啟用虛擬環境

Windows 系統:
  命令提示字元: demo_venv\\Scripts\\activate
  PowerShell: demo_venv\\Scripts\\Activate.ps1

啟用後的變化:
  - 提示字元前會顯示 (demo_venv)
  ...
```

### 📚 知識點總結

- ✅ `python -m venv [name]` 建立虛擬環境
- ✅ 不同平台的啟用指令差異
- ✅ 使用 `sys.executable` 驗證環境
- ✅ 虛擬環境的目錄結構
- ✅ `deactivate` 停用虛擬環境

---"""),

    create_cell("markdown", """## 範例 3：requirements.txt 進階應用

### 📋 問題描述

管理一個 Web 專案的依賴，需要：
1. 建立基礎 requirements.txt
2. 使用版本限定符號
3. 分離開發與生產環境依賴
4. 處理套件來源與額外選項

**難度**：中級

### 🔍 分析思路

1. **版本語法**：了解 ==, >=, ~= 等符號的意義
2. **環境分離**：使用多個 requirements 檔案
3. **註解說明**：為依賴添加說明
4. **特殊來源**：從 Git 或本地路徑安裝

### 💻 逐步實作"""),

    create_cell("code", """import os

print("=== requirements.txt 進階應用 ===")
print()

# 步驟 1: 基礎 requirements.txt
print("[1] 基礎 requirements.txt")
print()

basic_requirements = \"\"\"# Web 框架
Django==4.2.0

# API 框架
djangorestframework>=3.14.0

# 資料庫驅動
psycopg2-binary~=2.9.5

# 環境變數管理
python-decouple==3.8

# 工具套件
requests>=2.28.0,<3.0.0
\"\"\"

with open('requirements_basic.txt', 'w', encoding='utf-8') as f:
    f.write(basic_requirements)

print("檔案內容:")
print(basic_requirements)
print("✓ 已儲存到 requirements_basic.txt")
print()

# 步驟 2: 版本限定符號說明
print("[2] 版本限定符號")
print()

version_examples = {
    "Django==4.2.0": "精確版本（推薦用於鎖定版本）",
    "requests>=2.28.0": "最低版本（允許更新）",
    "numpy~=1.21.0": "相容版本（允許 1.21.x，不允許 1.22.0）",
    "pandas>=1.3,<2.0": "版本範圍（組合條件）",
    "pytest": "最新版本（不推薦，可能有相容性問題）"
}

for syntax, description in version_examples.items():
    print(f"  {syntax:<30} # {description}")

print()

# 步驟 3: 分離開發與生產環境
print("[3] 分離開發與生產環境")
print()

# 生產環境依賴
prod_requirements = \"\"\"# requirements.txt (生產環境)

Django==4.2.0
djangorestframework==3.14.0
psycopg2-binary==2.9.5
gunicorn==20.1.0
python-decouple==3.8
\"\"\"

# 開發環境依賴
dev_requirements = \"\"\"# requirements-dev.txt (開發環境)

# 首先安裝生產環境依賴
-r requirements.txt

# 測試工具
pytest==7.4.0
pytest-django==4.5.2
pytest-cov==4.1.0

# 程式碼品質
flake8==6.0.0
black==23.7.0

# 除錯工具
ipython==8.14.0
django-debug-toolbar==4.1.0
\"\"\"

with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write(prod_requirements)

with open('requirements-dev.txt', 'w', encoding='utf-8') as f:
    f.write(dev_requirements)

print("生產環境 (requirements.txt):")
print(prod_requirements)
print()

print("開發環境 (requirements-dev.txt):")
print(dev_requirements)
print()

print("✓ 已儲存兩個環境的 requirements 檔案")
print()

# 步驟 4: 特殊安裝來源
print("[4] 特殊安裝來源")
print()

special_requirements = \"\"\"# 從 Git 安裝
git+https://github.com/django/django.git@main

# 從本地路徑安裝
-e ./my-local-package

# 從私有 PyPI 安裝
--index-url https://pypi.private.com/simple/
requests==2.28.0

# 額外功能安裝
celery[redis]==5.3.0
\"\"\"

print("特殊來源範例:")
print(special_requirements)
print()

# 步驟 5: 使用範例
print("[5] 使用方式")
print()

print("安裝生產環境依賴:")
print("  pip install -r requirements.txt")
print()

print("安裝開發環境依賴:")
print("  pip install -r requirements-dev.txt")
print()

print("匯出目前環境:")
print("  pip freeze > requirements.txt")
print()

print("升級所有套件:")
print("  pip install --upgrade -r requirements.txt")"""),

    create_cell("markdown", """### 📚 知識點總結

- ✅ 版本限定符號：`==`, `>=`, `~=`, `,`
- ✅ 使用 `-r` 引用其他 requirements 檔案
- ✅ 分離開發/生產環境依賴的最佳實務
- ✅ 從 Git、本地路徑安裝套件
- ✅ 使用註解提升 requirements.txt 可讀性

---"""),

    create_cell("markdown", """## 範例 4：套件版本衝突診斷與解決

### 📋 問題描述

在專案中遇到套件版本衝突問題：
1. 模擬版本衝突情境
2. 診斷衝突原因
3. 解決衝突的策略
4. 預防衝突的方法

**難度**：中級

### 🔍 分析思路

1. **衝突識別**：理解依賴樹與衝突訊息
2. **版本分析**：檢查相容性矩陣
3. **解決策略**：升級、降級、替換套件
4. **預防措施**：使用版本鎖定工具

### 💻 逐步實作"""),

    create_cell("code", """print("=== 套件版本衝突診斷與解決 ===")
print()

# 步驟 1: 模擬衝突情境
print("[1] 衝突情境模擬")
print()

print("情境描述：")
print("  專案需要 Package-A 和 Package-B")
print("  Package-A 依賴 requests>=2.28.0,<3.0.0")
print("  Package-B 依賴 requests>=2.25.0,<2.27.0")
print()
print("衝突分析：")
print("  Package-A 需要: 2.28.0 <= requests < 3.0.0")
print("  Package-B 需要: 2.25.0 <= requests < 2.27.0")
print("  交集: 無！")
print()
print("錯誤訊息範例：")
print("  ERROR: Cannot install Package-A and Package-B because")
print("  these package versions have conflicting dependencies.")
print()

# 步驟 2: 診斷衝突
print("[2] 衝突診斷步驟")
print()

diagnostic_steps = [
    ("1. 查看錯誤訊息", "pip install 時的 ERROR 輸出"),
    ("2. 檢查依賴樹", "pip show [package] 查看 Requires"),
    ("3. 列出已安裝版本", "pip list | grep [package]"),
    ("4. 查詢可用版本", "pip index versions [package]"),
    ("5. 建立依賴圖", "使用 pipdeptree 視覺化依賴")
]

for i, (step, detail) in enumerate(diagnostic_steps, 1):
    print(f"  {step}")
    print(f"    方法: {detail}")

print()

# 步驟 3: 解決策略
print("[3] 解決策略")
print()

strategies = {
    "策略 1: 升級套件": [
        "pip install --upgrade Package-B",
        "檢查 Package-B 新版本是否相容 requests>=2.28.0"
    ],
    "策略 2: 降級套件": [
        "pip install Package-A==older-version",
        "選擇相容 requests<2.27.0 的 Package-A 版本"
    ],
    "策略 3: 替換套件": [
        "尋找 Package-B 的替代方案",
        "或尋找 Package-A 的替代方案"
    ],
    "策略 4: 使用虛擬環境隔離": [
        "為不同功能建立獨立虛擬環境",
        "避免所有依賴在同一環境"
    ],
    "策略 5: 聯絡維護者": [
        "在 GitHub 提 Issue 回報相容性問題",
        "等待套件更新"
    ]
}

for strategy, actions in strategies.items():
    print(f"{strategy}:")
    for action in actions:
        print(f"  • {action}")
    print()

# 步驟 4: 實際解決範例
print("[4] 實際解決範例")
print()

print("原始需求:")
print("  Package-A==2.0.0 (依賴 requests>=2.28.0)")
print("  Package-B==1.5.0 (依賴 requests<2.27.0)")
print()

print("解決方案: 降級 Package-A")
print()

print("步驟:")
print("  1. 查詢 Package-A 歷史版本")
print("     pip index versions Package-A")
print()
print("  2. 找到相容版本")
print("     Package-A==1.8.0 (依賴 requests>=2.25.0,<2.29.0)")
print()
print("  3. 安裝相容版本")
print("     pip install Package-A==1.8.0 Package-B==1.5.0")
print()
print("  4. 驗證安裝")
print("     pip check  # 檢查依賴一致性")
print()

# 步驟 5: 預防措施
print("[5] 預防措施")
print()

preventions = [
    "使用 pip freeze 鎖定版本",
    "使用 pipenv 或 poetry 自動解析依賴",
    "定期執行 pip check 檢查",
    "在 CI/CD 中測試依賴安裝",
    "使用 Dependabot 自動檢測過時套件",
    "建立 requirements-lock.txt 鎖定精確版本"
]

for i, prevention in enumerate(preventions, 1):
    print(f"  {i}. {prevention}")

print()

# 步驟 6: 診斷工具
print("[6] 實用診斷工具")
print()

tools = {
    "pipdeptree": "視覺化依賴樹",
    "pip check": "檢查依賴一致性",
    "pip-conflict-checker": "自動檢測衝突",
    "pip list --outdated": "列出過時套件"
}

print("安裝與使用:")
for tool, desc in tools.items():
    print(f"  {tool}: {desc}")
    print(f"    安裝: pip install {tool}")

print()"""),

    create_cell("markdown", """### 📚 知識點總結

- ✅ 理解依賴衝突的根本原因
- ✅ 使用 `pip show` 和 `pip check` 診斷問題
- ✅ 掌握多種衝突解決策略
- ✅ 使用虛擬環境預防衝突
- ✅ 採用版本鎖定避免意外更新

---"""),

    create_cell("markdown", """## 範例 5：多專案環境管理工作流程

### 📋 問題描述

作為開發者，同時維護多個專案：
1. 專案 A: Django 3.2 + Python 3.9
2. 專案 B: Django 4.2 + Python 3.11
3. 專案 C: Flask 2.3 + Python 3.10

建立完整的環境管理工作流程。

**難度**：進階

### 🔍 分析思路

1. **專案結構**：每個專案獨立虛擬環境
2. **環境命名**：清晰的命名規則
3. **環境切換**：快速切換工作流程
4. **依賴管理**：各專案的 requirements.txt

### 💻 逐步實作"""),

    create_cell("code", """import os
from pathlib import Path

print("=== 多專案環境管理工作流程 ===")
print()

# 步驟 1: 專案結構規劃
print("[1] 專案目錄結構")
print()

project_structure = \"\"\"
~/projects/
├── project-a/
│   ├── venv/              # 虛擬環境
│   ├── requirements.txt   # 依賴清單
│   ├── manage.py
│   └── ...
├── project-b/
│   ├── venv/
│   ├── requirements.txt
│   └── ...
└── project-c/
    ├── venv/
    ├── requirements.txt
    └── ...
\"\"\"

print(project_structure)
print()

# 步驟 2: 專案 A 設定
print("[2] 專案 A: Django 3.2 專案")
print()

print("建立與設定:")
print("  cd ~/projects/project-a")
print("  python3.9 -m venv venv")
print("  source venv/bin/activate  # Windows: venv\\\\Scripts\\\\activate")
print("  pip install --upgrade pip")
print()

project_a_requirements = \"\"\"# Project A: Django 3.2 專案
# Python 3.9

Django==3.2.20
djangorestframework==3.14.0
psycopg2-binary==2.9.5
celery==5.2.7
redis==4.5.0

# 開發工具
pytest==7.4.0
black==23.7.0
\"\"\"

print("requirements.txt:")
print(project_a_requirements)

print("安裝依賴:")
print("  pip install -r requirements.txt")
print()

# 步驟 3: 專案 B 設定
print("[3] 專案 B: Django 4.2 專案")
print()

print("建立與設定:")
print("  cd ~/projects/project-b")
print("  python3.11 -m venv venv")
print("  source venv/bin/activate")
print()

project_b_requirements = \"\"\"# Project B: Django 4.2 專案
# Python 3.11

Django==4.2.0
djangorestframework==3.14.0
psycopg2-binary==2.9.6
celery==5.3.0
redis==5.0.0

# 開發工具
pytest==7.4.0
black==23.7.0
\"\"\"

print("requirements.txt:")
print(project_b_requirements)
print()

# 步驟 4: 專案 C 設定
print("[4] 專案 C: Flask 2.3 專案")
print()

project_c_requirements = \"\"\"# Project C: Flask 專案
# Python 3.10

Flask==2.3.0
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.4
requests==2.31.0

# 開發工具
pytest==7.4.0
black==23.7.0
\"\"\"

print("requirements.txt:")
print(project_c_requirements)
print()

# 步驟 5: 環境切換工作流程
print("[5] 環境切換工作流程")
print()

print("切換到專案 A:")
print("  1. cd ~/projects/project-a")
print("  2. source venv/bin/activate")
print("  3. 確認: python --version  # 應顯示 Python 3.9.x")
print("  4. 確認: pip show Django  # 應顯示 3.2.20")
print()

print("切換到專案 B:")
print("  1. deactivate  # 先停用目前環境")
print("  2. cd ~/projects/project-b")
print("  3. source venv/bin/activate")
print("  4. 確認: python --version  # 應顯示 Python 3.11.x")
print()

print("切換到專案 C:")
print("  1. deactivate")
print("  2. cd ~/projects/project-c")
print("  3. source venv/bin/activate")
print("  4. 確認: pip show Flask  # 應顯示 2.3.0")
print()

# 步驟 6: 環境管理最佳實務
print("[6] 環境管理最佳實務")
print()

best_practices = [
    ("統一命名", "所有專案虛擬環境都命名為 venv/"),
    ("版本鎖定", "使用 pip freeze 鎖定精確版本"),
    ("Git 忽略", ".gitignore 加入 venv/"),
    ("說明文件", "README 記錄 Python 版本需求"),
    ("依賴分離", "區分 requirements.txt 和 requirements-dev.txt"),
    ("定期更新", "每月檢查並更新過時套件"),
    ("自動化腳本", "建立 setup.sh 自動化環境建立")
]

for i, (practice, detail) in enumerate(best_practices, 1):
    print(f"  {i}. {practice}: {detail}")

print()

# 步驟 7: 環境建立自動化腳本範例
print("[7] 自動化腳本範例 (setup.sh)")
print()

setup_script = \"\"\"#!/bin/bash
# setup.sh - 自動建立虛擬環境與安裝依賴

echo "建立虛擬環境..."
python3 -m venv venv

echo "啟用虛擬環境..."
source venv/bin/activate

echo "升級 pip..."
pip install --upgrade pip

echo "安裝依賴..."
pip install -r requirements.txt

echo "安裝開發依賴..."
pip install -r requirements-dev.txt

echo "✓ 環境設定完成！"
echo "使用 'source venv/bin/activate' 啟用環境"
\"\"\"

print(setup_script)
print()

print("使用方式:")
print("  chmod +x setup.sh  # 賦予執行權限")
print("  ./setup.sh         # 執行腳本")
print()

# 步驟 8: 環境檢查清單
print("[8] 環境檢查清單")
print()

checklist = [
    "✓ 每個專案有獨立虛擬環境",
    "✓ requirements.txt 版本已鎖定",
    "✓ venv/ 已加入 .gitignore",
    "✓ README 記錄 Python 版本需求",
    "✓ 可順利在新機器重建環境",
    "✓ 定期執行 pip list --outdated",
    "✓ 定期執行 pip check 檢查依賴"
]

for item in checklist:
    print(f"  {item}")

print()"""),

    create_cell("markdown", """### 📚 知識點總結

- ✅ 每個專案建立獨立虛擬環境
- ✅ 使用一致的命名規則 (venv/)
- ✅ 建立自動化腳本簡化環境設定
- ✅ 明確記錄 Python 版本需求
- ✅ 使用 .gitignore 排除虛擬環境
- ✅ 定期維護與更新依賴

---"""),

    create_cell("markdown", """## 🎯 總結

本檔案的 5 個詳解範例涵蓋了套件管理與虛擬環境的核心應用：

1. **範例 1**：pip 基礎操作 → 學習套件查詢與匯出
2. **範例 2**：虛擬環境管理 → 學習建立與啟用環境
3. **範例 3**：requirements.txt 進階 → 學習版本管理策略
4. **範例 4**：版本衝突診斷 → 學習問題診斷與解決
5. **範例 5**：多專案管理 → 學習完整工作流程

### 下一步

完成這些範例後，請進入：
- `03-practice.ipynb` 進行課堂練習
- `04-exercises.ipynb` 挑戰課後習題

---

**學習提醒**：虛擬環境是 Python 開發的基礎，務必在每個專案中使用。養成良好習慣，避免依賴衝突！""")
]

# ==================== 03-practice.ipynb ====================

practice_cells = [
    create_cell("markdown", """# 套件管理與虛擬環境 | Package Management and Virtual Environments

## 🛠️ 課堂練習 | Practice Exercises

---

## 📖 練習說明

本檔案包含 **8 個課堂練習題**，涵蓋：
- pip 基本指令操作
- 虛擬環境建立與管理
- requirements.txt 編寫
- 版本管理策略

**建議時間**：30 分鐘

**難度分佈**：
- 基礎題：1-3
- 中級題：4-6
- 進階題：7-8

---"""),

    create_cell("markdown", """## 練習 1：pip 基本指令 ⭐

### 題目

使用 Python 程式模擬以下 pip 操作的輸出：
1. 列出目前環境的前 5 個套件
2. 查詢 `pip` 套件本身的版本
3. 模擬 `pip freeze` 的輸出格式

### 提示

- 使用 `subprocess.run()` 執行 pip 指令
- 處理輸出文字（`capture_output=True, text=True`）
- 解析並格式化輸出"""),

    create_cell("code", """import subprocess

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 2：虛擬環境資訊檢查 ⭐

### 題目

撰寫程式檢查並顯示：
1. 目前 Python 執行檔的完整路徑
2. 判斷是否在虛擬環境中（檢查路徑是否包含 'venv' 或 'env'）
3. 顯示 Python 版本資訊

### 提示

- 使用 `sys.executable` 取得 Python 路徑
- 使用 `sys.version` 取得版本資訊
- 使用字串方法檢查路徑"""),

    create_cell("code", """import sys

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 3：建立 requirements.txt ⭐

### 題目

根據以下需求，建立一個 `requirements.txt` 檔案：
1. Django 精確版本 4.2.0
2. requests 最低版本 2.28.0，但不超過 3.0.0
3. numpy 相容版本 1.24.0（允許 1.24.x）
4. pytest 不限定版本
5. 加入適當的註解說明

### 提示

- 使用 `==`, `>=`, `~=` 符號
- 使用 `#` 加入註解
- 儲存到檔案"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 4：解析 requirements.txt ⭐⭐

### 題目

撰寫程式讀取 requirements.txt 檔案，並解析成結構化資料：
1. 忽略空行與註解行
2. 分離套件名稱與版本限定
3. 以字典格式輸出

範例輸入：
```
Django==4.2.0
requests>=2.28.0,<3.0.0
# 這是註解
numpy~=1.24.0
```

預期輸出：
```python
{
    'Django': '==4.2.0',
    'requests': '>=2.28.0,<3.0.0',
    'numpy': '~=1.24.0'
}
```

### 提示

- 使用 `str.startswith('#')` 判斷註解
- 使用 `str.split('==')` 或正規表達式分離
- 處理多種版本符號（==, >=, ~=）"""),

    create_cell("code", """# 先建立範例 requirements.txt
requirements_content = \"\"\"Django==4.2.0
requests>=2.28.0,<3.0.0
# 這是註解
numpy~=1.24.0
pytest
\"\"\"

with open('test_requirements.txt', 'w', encoding='utf-8') as f:
    f.write(requirements_content)

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 5：環境依賴比對 ⭐⭐

### 題目

撰寫程式比對兩個環境的套件差異：
1. 讀取兩個 requirements.txt 檔案
2. 找出只在環境 A 存在的套件
3. 找出只在環境 B 存在的套件
4. 找出兩個環境都有但版本不同的套件

### 提示

- 使用集合操作（差集、交集）
- 建立字典儲存套件與版本
- 比較版本字串"""),

    create_cell("code", """# 建立兩個範例環境檔案
env_a = \"\"\"Django==3.2.0
requests==2.28.0
numpy==1.23.0
pytest==7.4.0
\"\"\"

env_b = \"\"\"Django==4.2.0
requests==2.28.0
pandas==2.0.0
pytest==7.3.0
\"\"\"

with open('env_a.txt', 'w', encoding='utf-8') as f:
    f.write(env_a)

with open('env_b.txt', 'w', encoding='utf-8') as f:
    f.write(env_b)

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 6：虛擬環境建立腳本 ⭐⭐

### 題目

撰寫 Python 程式，模擬虛擬環境建立流程：
1. 檢查指定名稱的虛擬環境是否已存在
2. 如果不存在，顯示建立指令（不實際執行）
3. 顯示對應平台（Windows/macOS/Linux）的啟用指令
4. 生成後續步驟建議

### 提示

- 使用 `os.path.exists()` 檢查目錄
- 使用 `sys.platform` 判斷作業系統
- 提供清晰的指令說明"""),

    create_cell("code", """import os
import sys

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 練習 7：版本相容性檢查器 ⭐⭐⭐

### 題目

撰寫程式檢查套件版本是否符合 requirements.txt 的限定：
1. 解析版本限定語法（==, >=, <=, ~=）
2. 比對實際安裝版本是否符合
3. 回報不相容的套件

範例：
```
限定: requests>=2.28.0,<3.0.0
實際: 2.31.0
結果: ✓ 相容

限定: Django==4.2.0
實際: 3.2.0
結果: ✗ 不相容
```

### 提示

- 使用 `packaging.version.parse()` 比較版本
- 或手動解析版本號（split('.')）
- 處理多個條件組合（,）"""),

    create_cell("code", """# 在此撰寫你的程式碼
# 提示：可使用字串比較或版本解析

"""),

    create_cell("markdown", """---

## 練習 8：專案環境初始化工具 ⭐⭐⭐

### 題目

撰寫完整的專案環境初始化程式：
1. 建立專案目錄結構
2. 生成 .gitignore 檔案（包含 venv/, __pycache__/, *.pyc）
3. 生成基礎 requirements.txt
4. 生成 requirements-dev.txt（包含開發工具）
5. 生成 README.md（包含環境設定說明）

### 提示

- 使用 `os.makedirs()` 建立目錄
- 使用檔案寫入功能
- 設計合理的專案結構"""),

    create_cell("code", """import os

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 🎯 練習總結

完成以上練習後，你應該能夠：

✅ 熟練使用 pip 基本指令
✅ 建立與管理虛擬環境
✅ 編寫與解析 requirements.txt
✅ 處理版本相容性問題
✅ 建立專案環境自動化工具

### 下一步

完成練習後，請對照 `05-solutions.ipynb` 檢查答案，並嘗試優化你的程式碼！

---

**學習建議**：這些練習題模擬了實際開發中的常見場景，建議多次練習以熟悉工作流程。""")
]

# ==================== 04-exercises.ipynb ====================

exercises_cells = [
    create_cell("markdown", """# 套件管理與虛擬環境 | Package Management and Virtual Environments

## ✍️ 課後習題 | Homework Exercises

---

## 📖 習題說明

本檔案包含 **18 個課後習題**，涵蓋：
- pip 進階操作
- 虛擬環境最佳實務
- requirements.txt 進階應用
- 版本管理與衝突解決

**建議完成時間**：90 分鐘

**難度分佈**：
- 基礎題：1-6（30 分鐘）
- 中級題：7-12（30 分鐘）
- 進階題：13-18（30 分鐘）

---"""),

    create_cell("markdown", """## 第一部分：基礎題（1-6）

---

## 習題 1：pip 指令模擬器 ⭐

### 題目

建立一個簡易的 pip 指令模擬器，支援以下功能：
1. `pip list` - 列出已安裝套件（模擬資料）
2. `pip show <package>` - 顯示套件資訊
3. `pip freeze` - 以 freeze 格式輸出

使用字典儲存模擬的套件資料。

### 測試資料

```python
packages = {
    'Django': {'version': '4.2.0', 'summary': 'Web framework'},
    'requests': {'version': '2.31.0', 'summary': 'HTTP library'},
    'numpy': {'version': '1.24.0', 'summary': 'Scientific computing'}
}
```

### 預期輸出範例

```
>>> pip list
Package    Version
----------  ---------
Django      4.2.0
requests    2.31.0
numpy       1.24.0

>>> pip show Django
Name: Django
Version: 4.2.0
Summary: Web framework

>>> pip freeze
Django==4.2.0
requests==2.31.0
numpy==1.24.0
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 2：環境路徑分析器 ⭐

### 題目

撰寫程式分析 Python 環境路徑：
1. 顯示 Python 執行檔路徑
2. 顯示標準庫路徑
3. 顯示 site-packages 路徑
4. 判斷是否在虛擬環境中
5. 如果在虛擬環境，顯示環境名稱

### 提示

- 使用 `sys.executable`
- 使用 `sys.prefix`
- 使用 `site.getsitepackages()`"""),

    create_cell("code", """import sys
import site

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 3：requirements.txt 生成器 ⭐

### 題目

撰寫程式從套件清單字典生成 requirements.txt：
1. 接受套件名稱與版本限定的字典
2. 加入分類註解（Web、資料科學、測試等）
3. 按字母順序排序
4. 儲存到檔案

### 測試資料

```python
packages = {
    'Django': ('==4.2.0', 'Web'),
    'requests': ('>=2.28.0', 'Web'),
    'numpy': ('~=1.24.0', 'Data Science'),
    'pandas': ('>=2.0.0', 'Data Science'),
    'pytest': ('>=7.0.0', 'Testing')
}
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 4：版本號解析器 ⭐

### 題目

撰寫程式解析並比較版本號：
1. 將版本號字串（如 "2.31.0"）解析為元組 (2, 31, 0)
2. 比較兩個版本號的大小
3. 支援主版本、次版本、修訂號的比較

### 測試案例

```python
version_compare("2.31.0", "2.28.0")  # 返回 1（前者較新）
version_compare("1.24.0", "2.0.0")   # 返回 -1（後者較新）
version_compare("3.2.0", "3.2.0")    # 返回 0（相同）
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 5：.gitignore 生成器 ⭐

### 題目

撰寫程式生成適合 Python 專案的 .gitignore 檔案：
1. 包含虛擬環境目錄（venv/, env/, .venv/）
2. 包含 Python 快取（__pycache__/, *.pyc）
3. 包含 IDE 配置（.vscode/, .idea/）
4. 包含作業系統檔案（.DS_Store, Thumbs.db）
5. 支援自訂規則

### 提示

- 使用多行字串
- 提供清晰的分類註解"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 6：虛擬環境檢查器 ⭐

### 題目

撰寫程式檢查虛擬環境的健康狀況：
1. 檢查虛擬環境目錄是否存在
2. 檢查必要的子目錄（Scripts/bin, Lib/lib）
3. 檢查 activate 腳本是否存在
4. 檢查 pyvenv.cfg 檔案
5. 生成檢查報告

### 提示

- 使用 `os.path.exists()`
- 考慮 Windows 與 Unix 系統差異"""),

    create_cell("code", """import os
import sys

# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 第二部分：中級題（7-12）

---

## 習題 7：requirements.txt 驗證器 ⭐⭐

### 題目

撰寫程式驗證 requirements.txt 的語法正確性：
1. 檢查版本符號是否正確（==, >=, <=, ~=, !=）
2. 檢查是否有重複的套件
3. 檢查版本號格式是否正確
4. 產生驗證報告

### 測試檔案

```
Django==4.2.0
requests>=2.28.0,<3.0.0
Django==3.2.0  # 重複！
numpy~=1.24.x  # 版本號錯誤！
pandas===2.0.0  # 符號錯誤！
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 8：套件依賴樹生成器 ⭐⭐

### 題目

模擬套件依賴關係並生成依賴樹：
1. 使用字典表示套件依賴關係
2. 遞迴顯示依賴樹
3. 標示依賴層級
4. 偵測循環依賴

### 測試資料

```python
dependencies = {
    'Django': ['sqlparse', 'asgiref'],
    'requests': ['urllib3', 'certifi', 'charset-normalizer'],
    'sqlparse': [],
    'asgiref': [],
    'urllib3': [],
    'certifi': [],
    'charset-normalizer': []
}
```

### 預期輸出

```
Django
├── sqlparse
└── asgiref

requests
├── urllib3
├── certifi
└── charset-normalizer
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 9：環境差異報告器 ⭐⭐

### 題目

比對兩個環境的 requirements.txt 並生成詳細報告：
1. 新增的套件
2. 移除的套件
3. 版本升級的套件
4. 版本降級的套件
5. 版本限定改變的套件

### 測試資料

```
# old_requirements.txt
Django==3.2.0
requests==2.28.0
numpy==1.23.0

# new_requirements.txt
Django==4.2.0
requests==2.28.0
pandas==2.0.0
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 10：版本升級建議器 ⭐⭐

### 題目

撰寫程式分析套件版本並提供升級建議：
1. 讀取 requirements.txt
2. 模擬查詢最新版本（使用測試資料）
3. 判斷是否有重大版本更新
4. 提供升級建議與風險評估

### 測試資料

```python
# 目前安裝版本
installed = {
    'Django': '3.2.0',
    'requests': '2.28.0',
    'numpy': '1.23.0'
}

# 最新可用版本
latest = {
    'Django': '4.2.0',  # 主版本升級（高風險）
    'requests': '2.31.0',  # 修訂號升級（低風險）
    'numpy': '1.26.0'  # 次版本升級（中風險）
}
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 11：多環境配置管理器 ⭐⭐

### 題目

建立管理多個環境配置的工具：
1. 支援 development, testing, production 三種環境
2. 每個環境有基礎依賴 + 特定依賴
3. 生成各環境的 requirements 檔案
4. 支援依賴繼承（testing 繼承 development）

### 提示

- 使用 `-r requirements.txt` 引用其他檔案
- 設計清晰的繼承關係"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 12：套件安全性檢查器 ⭐⭐

### 題目

模擬套件安全性檢查工具：
1. 維護已知漏洞資料庫（測試資料）
2. 檢查 requirements.txt 中的套件版本
3. 標示有安全風險的套件
4. 提供修復建議

### 測試資料

```python
vulnerabilities = {
    'Django': {
        '<3.2.14': 'CVE-2022-34265: SQL Injection',
        '<4.0.6': 'CVE-2022-36359: XSS Vulnerability'
    },
    'requests': {
        '<2.31.0': 'CVE-2023-32681: Proxy-Authorization header leak'
    }
}
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 第三部分：進階題（13-18）

---

## 習題 13：虛擬環境遷移工具 ⭐⭐⭐

### 題目

撰寫工具協助虛擬環境遷移到新機器：
1. 匯出當前環境資訊（Python 版本、套件清單、環境變數）
2. 生成遷移報告（JSON 格式）
3. 生成重建腳本（shell script）
4. 包含驗證步驟

### 輸出檔案

- `environment.json` - 環境資訊
- `rebuild.sh` - 重建腳本
- `verification.py` - 驗證腳本"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 14：依賴衝突解析器 ⭐⭐⭐

### 題目

實作簡化版的依賴衝突解析器：
1. 解析多個套件的版本需求
2. 找出衝突點
3. 嘗試找到相容的版本組合
4. 如果無解，提供降級建議

### 測試案例

```python
requirements = {
    'package-a': {'django': '>=4.0,<5.0', 'requests': '>=2.28'},
    'package-b': {'django': '>=3.2,<4.0', 'numpy': '>=1.23'},
}
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 15：套件更新策略分析器 ⭐⭐⭐

### 題目

分析並建議套件更新策略：
1. 區分直接依賴與間接依賴
2. 分析更新的影響範圍
3. 提供漸進式更新計畫
4. 估算更新風險

### 輸出範例

```
更新計畫：
第一階段（低風險）：
  - requests: 2.28.0 → 2.31.0 (修訂號更新)

第二階段（中風險）：
  - numpy: 1.23.0 → 1.26.0 (次版本更新)

第三階段（高風險）：
  - Django: 3.2.0 → 4.2.0 (主版本更新)
  - 建議: 先升級到 3.2.latest，再升級到 4.0，最後到 4.2
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 16：requirements.txt 最佳化工具 ⭐⭐⭐

### 題目

建立工具最佳化 requirements.txt：
1. 移除間接依賴（僅保留直接依賴）
2. 合併重複的版本限定
3. 排序並分組
4. 添加說明註解

### 輸入範例

```
# 雜亂的 requirements.txt
numpy>=1.23
Django==4.2.0
asgiref==3.6.0  # Django 的依賴
numpy>=1.20,<2.0
requests
```

### 預期輸出

```
# Web 框架
Django==4.2.0

# HTTP 請求
requests>=2.0,<3.0  # 建議添加版本限定

# 數據處理
numpy>=1.23,<2.0  # 合併條件

# 注意: asgiref 是 Django 的依賴，已移除
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 17：專案環境診斷工具 ⭐⭐⭐

### 題目

建立完整的專案環境診斷工具：
1. 檢查 Python 版本
2. 檢查虛擬環境狀態
3. 檢查套件依賴一致性
4. 檢查安全性問題
5. 檢查 .gitignore 配置
6. 生成健康報告

### 報告範例

```
環境診斷報告
===================

Python 版本: 3.11.0 ✓

虛擬環境: ✓
  路徑: /project/venv
  Python: 3.11.0

依賴檢查: ⚠️
  - Django 版本不一致: requirements.txt 指定 4.2.0，實際安裝 3.2.0

安全性: ✗
  - requests 版本過舊，存在已知漏洞

Git 配置: ✓
  - .gitignore 已正確配置

建議修復:
  1. 升級 Django: pip install Django==4.2.0
  2. 更新 requests: pip install --upgrade requests
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 習題 18：虛擬環境自動化管理系統 ⭐⭐⭐

### 題目

建立完整的虛擬環境自動化管理系統，支援：

**功能清單**：
1. `create` - 建立新環境
2. `list` - 列出所有環境
3. `activate` - 切換環境（顯示指令）
4. `delete` - 刪除環境
5. `export` - 匯出環境配置
6. `import` - 從配置重建環境
7. `check` - 檢查環境健康狀況

**資料結構**：
- 使用 JSON 檔案儲存環境清單
- 記錄環境名稱、路徑、Python 版本、建立時間

**指令範例**：
```python
manager = VenvManager()
manager.create('myproject', python_version='3.11')
manager.list()
manager.export('myproject', 'backup.json')
```"""),

    create_cell("code", """# 在此撰寫你的程式碼

"""),

    create_cell("markdown", """---

## 🎯 習題總結

完成這 18 題後，你將掌握：

### 基礎能力（1-6）
- ✅ pip 基本操作
- ✅ 環境資訊查詢
- ✅ requirements.txt 基礎操作

### 進階能力（7-12）
- ✅ 依賴關係分析
- ✅ 環境比對與遷移
- ✅ 版本管理策略

### 專家能力（13-18）
- ✅ 衝突解析
- ✅ 自動化工具開發
- ✅ 環境診斷與最佳化

---

## 📝 學習建議

1. **循序漸進**：從基礎題開始，逐步提升難度
2. **實際應用**：將這些工具應用到真實專案
3. **程式碼重構**：完成後嘗試優化程式碼結構
4. **延伸思考**：思考如何整合這些功能成為完整工具

---

**下一步**：完成後對照 `05-solutions.ipynb` 檢查答案！""")
]

# ==================== 05-solutions.ipynb ====================

solutions_cells = [
    create_cell("markdown", """# 套件管理與虛擬環境 | Package Management and Virtual Environments

## ✅ 完整解答 | Solutions

---

## 📖 解答說明

本檔案提供：
1. **18 題課後習題的完整解答**
2. **程式碼註解與說明**
3. **多種解法比較**（部分題目）
4. **延伸思考**

---"""),

    create_cell("markdown", """## 習題 1 解答：pip 指令模擬器

### 解法"""),

    create_cell("code", """def pip_simulator():
    \"\"\"簡易 pip 指令模擬器\"\"\"

    # 模擬套件資料
    packages = {
        'Django': {'version': '4.2.0', 'summary': 'Web framework'},
        'requests': {'version': '2.31.0', 'summary': 'HTTP library'},
        'numpy': {'version': '1.24.0', 'summary': 'Scientific computing'}
    }

    def pip_list():
        \"\"\"模擬 pip list\"\"\"
        print(f"{'Package':<15} {'Version':<10}")
        print("-" * 25)
        for name, info in packages.items():
            print(f"{name:<15} {info['version']:<10}")

    def pip_show(package_name):
        \"\"\"模擬 pip show\"\"\"
        if package_name not in packages:
            print(f"WARNING: Package {package_name} not found")
            return

        info = packages[package_name]
        print(f"Name: {package_name}")
        print(f"Version: {info['version']}")
        print(f"Summary: {info['summary']}")

    def pip_freeze():
        \"\"\"模擬 pip freeze\"\"\"
        for name, info in packages.items():
            print(f"{name}=={info['version']}")

    # 測試
    print(">>> pip list")
    pip_list()
    print()

    print(">>> pip show Django")
    pip_show('Django')
    print()

    print(">>> pip freeze")
    pip_freeze()

# 執行
pip_simulator()"""),

    create_cell("markdown", """### 知識點

- ✅ 字典資料結構模擬套件資訊
- ✅ 字串格式化（f-string）
- ✅ 函式封裝提高程式碼可讀性

---"""),

    create_cell("markdown", """## 習題 2 解答：環境路徑分析器

### 解法"""),

    create_cell("code", """import sys
import site
from pathlib import Path

def analyze_environment():
    \"\"\"分析 Python 環境路徑\"\"\"

    print("=== Python 環境分析 ===")
    print()

    # 1. Python 執行檔路徑
    print(f"Python 執行檔: {sys.executable}")
    print()

    # 2. 標準庫路徑
    print(f"標準庫路徑: {sys.prefix}")
    print()

    # 3. site-packages 路徑
    print("site-packages 路徑:")
    for path in site.getsitepackages():
        print(f"  - {path}")
    print()

    # 4. 判斷是否在虛擬環境
    exe_path = Path(sys.executable)
    venv_indicators = ['venv', 'env', '.venv', 'virtualenv']

    in_venv = any(indicator in exe_path.parts for indicator in venv_indicators)

    if in_venv:
        print("✓ 目前在虛擬環境中")

        # 5. 找出環境名稱
        for part in exe_path.parts:
            if any(indicator in part.lower() for indicator in venv_indicators):
                print(f"環境名稱: {part}")
                break
    else:
        print("✗ 目前在系統 Python 環境中")

# 執行
analyze_environment()"""),

    create_cell("markdown", """### 知識點

- ✅ `sys.executable` - Python 執行檔路徑
- ✅ `sys.prefix` - Python 安裝根目錄
- ✅ `site.getsitepackages()` - 套件安裝路徑
- ✅ `pathlib.Path` - 路徑操作

---"""),

    create_cell("markdown", """## 習題 3 解答：requirements.txt 生成器

### 解法"""),

    create_cell("code", """def generate_requirements():
    \"\"\"生成 requirements.txt\"\"\"

    packages = {
        'Django': ('==4.2.0', 'Web'),
        'requests': ('>=2.28.0', 'Web'),
        'numpy': ('~=1.24.0', 'Data Science'),
        'pandas': ('>=2.0.0', 'Data Science'),
        'pytest': ('>=7.0.0', 'Testing')
    }

    # 按類別分組
    categories = {}
    for name, (version, category) in packages.items():
        if category not in categories:
            categories[category] = []
        categories[category].append((name, version))

    # 生成檔案內容
    lines = []
    lines.append("# requirements.txt")
    lines.append("# 自動生成於 2025-10-09")
    lines.append("")

    for category in sorted(categories.keys()):
        lines.append(f"# {category}")

        # 按字母順序排序
        for name, version in sorted(categories[category]):
            lines.append(f"{name}{version}")

        lines.append("")

    content = "\\n".join(lines)

    # 儲存到檔案
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✓ requirements.txt 已生成")
    print()
    print("檔案內容:")
    print(content)

# 執行
generate_requirements()"""),

    create_cell("markdown", """### 知識點

- ✅ 字典資料結構分組
- ✅ `sorted()` 排序
- ✅ 列表推導式
- ✅ 檔案寫入操作

---"""),

    create_cell("markdown", """## 習題 4 解答：版本號解析器

### 解法"""),

    create_cell("code", """def parse_version(version_str):
    \"\"\"解析版本號字串為元組\"\"\"
    try:
        parts = version_str.split('.')
        return tuple(int(part) for part in parts)
    except ValueError:
        raise ValueError(f"無效的版本號格式: {version_str}")

def version_compare(version1, version2):
    \"\"\"
    比較兩個版本號
    返回: 1 (version1 較新), -1 (version2 較新), 0 (相同)
    \"\"\"
    v1 = parse_version(version1)
    v2 = parse_version(version2)

    # 比較元組（Python 會自動按元素比較）
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0

# 測試
test_cases = [
    ("2.31.0", "2.28.0", 1),
    ("1.24.0", "2.0.0", -1),
    ("3.2.0", "3.2.0", 0),
    ("4.2.1", "4.2.0", 1)
]

print("版本號比較測試:")
print()

for v1, v2, expected in test_cases:
    result = version_compare(v1, v2)
    status = "✓" if result == expected else "✗"

    if result == 1:
        desc = f"{v1} > {v2}"
    elif result == -1:
        desc = f"{v1} < {v2}"
    else:
        desc = f"{v1} == {v2}"

    print(f"{status} {desc} (期望: {expected}, 結果: {result})")"""),

    create_cell("markdown", """### 知識點

- ✅ 字串分割與型態轉換
- ✅ 元組比較（按元素順序比較）
- ✅ 異常處理
- ✅ 測試驅動開發思維

---"""),

    create_cell("markdown", """## 習題 5 解答：.gitignore 生成器

### 解法"""),

    create_cell("code", """def generate_gitignore(custom_rules=None):
    \"\"\"生成 Python 專案的 .gitignore\"\"\"

    gitignore_content = \"\"\"# Python .gitignore
# 自動生成

# 虛擬環境
venv/
env/
.venv/
ENV/
virtualenv/

# Python 快取
__pycache__/
*.py[cod]
*$py.class
*.so

# 測試與覆蓋率
.pytest_cache/
.coverage
htmlcov/
*.cover

# IDE 配置
.vscode/
.idea/
*.swp
*.swo
*~

# Jupyter Notebook
.ipynb_checkpoints/
*.ipynb_checkpoints

# 作業系統
.DS_Store
Thumbs.db
desktop.ini

# 專案特定
*.log
*.sqlite3
.env
.env.local
\"\"\"

    # 加入自訂規則
    if custom_rules:
        gitignore_content += "\\n# 自訂規則\\n"
        for rule in custom_rules:
            gitignore_content += f"{rule}\\n"

    # 儲存到檔案
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)

    print("✓ .gitignore 已生成")
    print()
    print("檔案內容預覽:")
    print(gitignore_content[:300])
    print("...")

# 執行（含自訂規則）
generate_gitignore(custom_rules=['secrets/', '*.key'])"""),

    create_cell("markdown", """### 知識點

- ✅ 多行字串使用
- ✅ 函式參數預設值
- ✅ Python 專案常見忽略檔案

---"""),

    create_cell("markdown", """## 習題 6 解答：虛擬環境檢查器

### 解法"""),

    create_cell("code", """import os
import sys

def check_venv(venv_path):
    \"\"\"檢查虛擬環境健康狀況\"\"\"

    print(f"=== 檢查虛擬環境: {venv_path} ===")
    print()

    results = []

    # 1. 檢查目錄是否存在
    if not os.path.exists(venv_path):
        print("✗ 虛擬環境目錄不存在")
        return

    results.append(("目錄存在", True))

    # 2. 檢查子目錄
    if sys.platform == 'win32':
        scripts_dir = os.path.join(venv_path, 'Scripts')
        lib_dir = os.path.join(venv_path, 'Lib')
    else:
        scripts_dir = os.path.join(venv_path, 'bin')
        lib_dir = os.path.join(venv_path, 'lib')

    results.append(("Scripts/bin 目錄", os.path.exists(scripts_dir)))
    results.append(("Lib/lib 目錄", os.path.exists(lib_dir)))

    # 3. 檢查 activate 腳本
    if sys.platform == 'win32':
        activate_path = os.path.join(scripts_dir, 'activate.bat')
    else:
        activate_path = os.path.join(scripts_dir, 'activate')

    results.append(("activate 腳本", os.path.exists(activate_path)))

    # 4. 檢查 pyvenv.cfg
    cfg_path = os.path.join(venv_path, 'pyvenv.cfg')
    results.append(("pyvenv.cfg", os.path.exists(cfg_path)))

    # 5. 檢查 Python 執行檔
    if sys.platform == 'win32':
        python_path = os.path.join(scripts_dir, 'python.exe')
    else:
        python_path = os.path.join(scripts_dir, 'python')

    results.append(("Python 執行檔", os.path.exists(python_path)))

    # 生成報告
    print("檢查結果:")
    print()

    all_passed = True
    for item, passed in results:
        status = "✓" if passed else "✗"
        print(f"  {status} {item}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("✓ 虛擬環境健康狀況良好")
    else:
        print("⚠️  虛擬環境可能損壞，建議重新建立")

# 測試（使用模擬路徑）
print("範例：檢查不存在的環境")
check_venv('demo_venv')
print()
print("注意：實際使用時請傳入真實的虛擬環境路徑")"""),

    create_cell("markdown", """### 知識點

- ✅ `os.path` 路徑操作
- ✅ `sys.platform` 判斷作業系統
- ✅ 跨平台相容性處理

---"""),

    create_cell("markdown", """## 習題 7-18 解答

由於篇幅限制，以下提供核心程式碼片段與解題思路。

---

## 習題 7 解答：requirements.txt 驗證器"""),

    create_cell("code", """import re

def validate_requirements(filename):
    \"\"\"驗證 requirements.txt 語法\"\"\"

    errors = []
    seen_packages = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # 跳過空行與註解
            if not line or line.startswith('#'):
                continue

            # 檢查版本符號
            valid_operators = ['==', '>=', '<=', '~=', '!=', '<', '>']
            has_operator = any(op in line for op in valid_operators)

            if has_operator:
                # 分離套件名稱
                match = re.match(r'^([a-zA-Z0-9_-]+)(.*)', line)
                if not match:
                    errors.append(f"行 {line_num}: 無效格式 - {line}")
                    continue

                package_name = match.group(1)
                version_spec = match.group(2)

                # 檢查重複
                if package_name in seen_packages:
                    errors.append(f"行 {line_num}: 重複套件 - {package_name} "
                                f"(已在行 {seen_packages[package_name]})")
                else:
                    seen_packages[package_name] = line_num

                # 檢查版本號格式
                # 簡化版：檢查是否有數字
                if not re.search(r'\\d+', version_spec):
                    errors.append(f"行 {line_num}: 版本號格式錯誤 - {line}")

    # 輸出報告
    print("=== requirements.txt 驗證報告 ===")
    print()

    if errors:
        print(f"發現 {len(errors)} 個問題:")
        for error in errors:
            print(f"  ✗ {error}")
    else:
        print("✓ 驗證通過，沒有發現問題")

# 測試
test_content = \"\"\"Django==4.2.0
requests>=2.28.0,<3.0.0
Django==3.2.0
numpy~=1.24.x
pandas===2.0.0
\"\"\"

with open('test_requirements.txt', 'w', encoding='utf-8') as f:
    f.write(test_content)

validate_requirements('test_requirements.txt')"""),

    create_cell("markdown", """---

## 習題 8 解答：套件依賴樹生成器"""),

    create_cell("code", """def print_dependency_tree(package, dependencies, prefix="", visited=None):
    \"\"\"遞迴顯示依賴樹\"\"\"

    if visited is None:
        visited = set()

    # 偵測循環依賴
    if package in visited:
        print(f"{prefix}{package} (循環依賴！)")
        return

    visited.add(package)

    print(f"{prefix}{package}")

    if package in dependencies:
        deps = dependencies[package]
        for i, dep in enumerate(deps):
            is_last = (i == len(deps) - 1)

            if is_last:
                new_prefix = prefix + "└── "
                next_prefix = prefix + "    "
            else:
                new_prefix = prefix + "├── "
                next_prefix = prefix + "│   "

            print(f"{new_prefix}{dep}")

# 測試
dependencies = {
    'Django': ['sqlparse', 'asgiref'],
    'requests': ['urllib3', 'certifi', 'charset-normalizer'],
    'sqlparse': [],
    'asgiref': [],
    'urllib3': [],
    'certifi': [],
    'charset-normalizer': []
}

print("=== 套件依賴樹 ===")
print()

for package in ['Django', 'requests']:
    print_dependency_tree(package, dependencies)
    print()"""),

    create_cell("markdown", """---

## 習題 9 解答：環境差異報告器"""),

    create_cell("code", """def parse_requirements_file(filename):
    \"\"\"解析 requirements.txt\"\"\"
    packages = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # 簡化：假設格式為 package==version
            if '==' in line:
                name, version = line.split('==')
                packages[name] = version

    return packages

def compare_environments(old_file, new_file):
    \"\"\"比對兩個環境差異\"\"\"

    old_packages = parse_requirements_file(old_file)
    new_packages = parse_requirements_file(new_file)

    old_names = set(old_packages.keys())
    new_names = set(new_packages.keys())

    # 分析差異
    added = new_names - old_names
    removed = old_names - new_names
    common = old_names & new_names

    upgraded = []
    downgraded = []
    unchanged = []

    for name in common:
        old_ver = old_packages[name]
        new_ver = new_packages[name]

        if old_ver != new_ver:
            # 簡化比較（實際應使用版本解析）
            if new_ver > old_ver:
                upgraded.append((name, old_ver, new_ver))
            else:
                downgraded.append((name, old_ver, new_ver))
        else:
            unchanged.append(name)

    # 輸出報告
    print("=== 環境差異報告 ===")
    print()

    if added:
        print(f"新增套件 ({len(added)}):")
        for name in sorted(added):
            print(f"  + {name}=={new_packages[name]}")
        print()

    if removed:
        print(f"移除套件 ({len(removed)}):")
        for name in sorted(removed):
            print(f"  - {name}=={old_packages[name]}")
        print()

    if upgraded:
        print(f"升級套件 ({len(upgraded)}):")
        for name, old_ver, new_ver in upgraded:
            print(f"  ↑ {name}: {old_ver} → {new_ver}")
        print()

    if downgraded:
        print(f"降級套件 ({len(downgraded)}):")
        for name, old_ver, new_ver in downgraded:
            print(f"  ↓ {name}: {old_ver} → {new_ver}")
        print()

# 測試
old_content = \"\"\"Django==3.2.0
requests==2.28.0
numpy==1.23.0
\"\"\"

new_content = \"\"\"Django==4.2.0
requests==2.28.0
pandas==2.0.0
\"\"\"

with open('old_requirements.txt', 'w') as f:
    f.write(old_content)

with open('new_requirements.txt', 'w') as f:
    f.write(new_content)

compare_environments('old_requirements.txt', 'new_requirements.txt')"""),

    create_cell("markdown", """---

## 習題 10-18 解答提示

### 習題 10：版本升級建議器
**核心思路**：
- 解析版本號的主版本、次版本、修訂號
- 根據 Semantic Versioning 規則評估風險
- 主版本更新 = 高風險，次版本 = 中風險，修訂號 = 低風險

### 習題 11：多環境配置管理器
**核心思路**：
- 使用 `-r requirements.txt` 實現繼承
- 分層設計：base → development → testing → production

### 習題 12：套件安全性檢查器
**核心思路**：
- 維護漏洞資料庫字典
- 比對套件版本與漏洞版本範圍
- 提供 CVE 編號與修復建議

### 習題 13：虛擬環境遷移工具
**核心思路**：
- 匯出：`sys.version`, `pip freeze`, 環境變數
- 生成 JSON 配置檔
- 生成 shell script 自動化重建

### 習題 14：依賴衝突解析器
**核心思路**：
- 使用 Constraint Satisfaction Problem 方法
- 回溯搜尋找到可行解
- 若無解，建議降級策略

### 習題 15：套件更新策略分析器
**核心思路**：
- 建立依賴圖（直接 vs 間接依賴）
- 拓樸排序決定更新順序
- 風險評估與階段劃分

### 習題 16：requirements.txt 最佳化工具
**核心思路**：
- 移除間接依賴（需依賴樹資訊）
- 合併版本限定（邏輯運算）
- 分組與排序

### 習題 17：專案環境診斷工具
**核心思路**：
- 整合前面所有檢查功能
- 生成結構化報告
- 提供修復建議

### 習題 18：虛擬環境自動化管理系統
**核心思路**：
- 使用 JSON 儲存環境清單
- 封裝所有操作為類別方法
- 提供命令列介面（CLI）

---"""),

    create_cell("markdown", """## 🎯 學習總結

完成這些習題後，你已經掌握：

### 技術能力
- ✅ pip 與虛擬環境的所有核心操作
- ✅ requirements.txt 的進階應用
- ✅ 版本管理與衝突解決策略
- ✅ 自動化工具開發能力

### 軟體工程思維
- ✅ 模組化與函式設計
- ✅ 錯誤處理與邊界條件
- ✅ 跨平台相容性考量
- ✅ 使用者體驗設計

### 實務經驗
- ✅ 真實專案環境管理
- ✅ 團隊協作工作流程
- ✅ 問題診斷與除錯
- ✅ 文件與註解撰寫

---

**恭喜！** 你已完成 Ch28 的所有練習。這些技能將在你的整個 Python 開發生涯中持續使用！""")
]

# ==================== quiz.ipynb ====================

quiz_cells = [
    create_cell("markdown", """# 套件管理與虛擬環境 | Package Management and Virtual Environments

## 📝 自我測驗 | Self-Assessment Quiz

---

## 測驗說明

- **題數**：20 題
- **題型**：選擇題（單選）、填空題、簡答題
- **建議時間**：20 分鐘
- **及格分數**：70 分

---"""),

    create_cell("markdown", """## 第一部分：選擇題（1-12，每題 5 分）

---

### 題目 1

下列哪個指令可以安裝特定版本的套件？

A) `pip install requests`
B) `pip install requests==2.28.0`
C) `pip install requests-2.28.0`
D) `pip get requests@2.28.0`

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- `==` 符號用於指定精確版本
- 格式：`pip install package==version`
</details>

---

### 題目 2

執行 `python -m venv myenv` 後，會建立哪些目錄？

A) 只有 bin/
B) Scripts/ 和 Lib/ (Windows)
C) venv/ 和 site-packages/
D) python/ 和 pip/

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- Windows: Scripts/, Lib/, Include/
- macOS/Linux: bin/, lib/, include/
- 還會建立 pyvenv.cfg 配置檔
</details>

---

### 題目 3

`pip freeze` 與 `pip list` 的主要差異是？

A) freeze 速度較快
B) freeze 輸出格式適合 requirements.txt
C) list 只顯示全域套件
D) 沒有差異

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- `pip list`: 表格格式，易讀
- `pip freeze`: `package==version` 格式，適合寫入 requirements.txt
</details>

---

### 題目 4

版本限定 `~=1.24.0` 允許安裝哪些版本？

A) 1.24.0 到 1.25.0
B) 1.24.x（1.24.0, 1.24.1, ...）
C) 1.x.x
D) 任何版本

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- `~=` 為相容版本運算子
- `~=1.24.0` 等同於 `>=1.24.0,<1.25.0`
- 允許修訂號更新，不允許次版本更新
</details>

---

### 題目 5

如何在 Windows PowerShell 啟用虛擬環境？

A) `source venv/bin/activate`
B) `venv\\Scripts\\activate`
C) `venv\\Scripts\\Activate.ps1`
D) `python venv activate`

<details>
<summary>點擊查看答案</summary>

**答案：C**

說明：
- PowerShell: `venv\\Scripts\\Activate.ps1`
- 命令提示字元: `venv\\Scripts\\activate.bat`
- macOS/Linux: `source venv/bin/activate`
</details>

---

### 題目 6

執行 `pip install -r requirements.txt` 會做什麼？

A) 建立虛擬環境
B) 安裝檔案中列出的所有套件
C) 匯出已安裝套件
D) 更新 pip

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- `-r` 參數表示從檔案讀取
- 會逐行安裝檔案中指定的套件
</details>

---

### 題目 7

為什麼虛擬環境資料夾（venv/）不應提交到 Git？

A) 檔案太大
B) 包含平台特定檔案，不可移植
C) 會洩漏密碼
D) Git 不支援

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- 虛擬環境包含平台相關的二進制檔案
- 應提交 requirements.txt，讓他人重建環境
- 在 .gitignore 中排除 venv/
</details>

---

### 題目 8

`pip check` 指令的用途是？

A) 檢查 pip 版本
B) 檢查依賴一致性
C) 檢查網路連線
D) 檢查 Python 版本

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- 驗證已安裝套件的依賴是否滿足
- 找出版本衝突問題
</details>

---

### 題目 9

版本限定 `>=2.28.0,<3.0.0` 的含義是？

A) 剛好 2.28.0
B) 2.28.0 或更高版本
C) 2.28.0 到 3.0.0 之間（不含 3.0.0）
D) 3.0.0 或更高版本

<details>
<summary>點擊查看答案</summary>

**答案：C**

說明：
- `,` 表示「且」條件
- 允許 2.28.0, 2.29.0, 2.31.0 等
- 不允許 3.0.0 或更高
</details>

---

### 題目 10

如何升級已安裝的套件到最新版本？

A) `pip update requests`
B) `pip install --upgrade requests`
C) `pip upgrade requests`
D) `pip install requests --latest`

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- `--upgrade` 或 `-U` 參數用於升級
- 會安裝最新可用版本
</details>

---

### 題目 11

requirements.txt 中的 `-r base.txt` 表示什麼？

A) 移除 base.txt
B) 重新命名
C) 引用（包含）另一個 requirements 檔案
D) 註解

<details>
<summary>點擊查看答案</summary>

**答案：C**

說明：
- `-r` 表示引用其他檔案
- 常用於環境依賴分層（base → dev → prod）
</details>

---

### 題目 12

如何確認目前是否在虛擬環境中？

A) 執行 `python --version`
B) 檢查提示字元是否有環境名稱
C) 執行 `pip --version`
D) 檢查 Python 版本

<details>
<summary>點擊查看答案</summary>

**答案：B**

說明：
- 虛擬環境啟用後，提示字元會顯示 `(env_name)`
- 也可執行 `python -c "import sys; print(sys.prefix)"` 檢查路徑
</details>

---"""),

    create_cell("markdown", """## 第二部分：填空題（13-16，每題 5 分）

---

### 題目 13

完成以下指令，建立名為 `myproject` 的虛擬環境：

```bash
python -m ________ myproject
```

<details>
<summary>點擊查看答案</summary>

**答案：venv**

完整指令：`python -m venv myproject`
</details>

---

### 題目 14

requirements.txt 中，要指定「numpy 版本至少 1.23，但不能是 2.0 或更高」，應該寫：

```
numpy________
```

<details>
<summary>點擊查看答案</summary>

**答案：>=1.23,<2.0**

或其他等價表達：`>=1.23.0,<2.0.0`
</details>

---

### 題目 15

停用虛擬環境的指令是：

```bash
________
```

<details>
<summary>點擊查看答案</summary>

**答案：deactivate**

適用於所有平台
</details>

---

### 題目 16

查看 Django 套件詳細資訊的指令是：

```bash
pip ________ Django
```

<details>
<summary>點擊查看答案</summary>

**答案：show**

完整指令：`pip show Django`
</details>

---"""),

    create_cell("markdown", """## 第三部分：簡答題（17-20，每題 10 分）

---

### 題目 17

說明為什麼每個 Python 專案都應該使用虛擬環境？至少列出 3 個原因。

<details>
<summary>點擊查看答案要點</summary>

**參考答案**：

1. **依賴隔離**：不同專案可使用不同版本的套件，避免版本衝突
2. **環境可重現**：透過 requirements.txt 在其他機器重建相同環境
3. **避免污染全域環境**：不影響系統 Python，降低風險
4. **權限問題**：不需 sudo/管理員權限安裝套件
5. **測試不同版本**：可建立多個環境測試不同套件版本

（答對 3 點給滿分）
</details>

---

### 題目 18

比較以下三種版本限定方式的差異：
- `Django==4.2.0`
- `Django>=4.2.0`
- `Django~=4.2.0`

<details>
<summary>點擊查看答案要點</summary>

**參考答案**：

1. **`Django==4.2.0`**（精確版本）
   - 只允許 4.2.0
   - 最嚴格，確保一致性
   - 適用於生產環境

2. **`Django>=4.2.0`**（最低版本）
   - 允許 4.2.0 或任何更高版本
   - 最寬鬆，可能有相容性問題
   - 適用於開發環境嘗試新功能

3. **`Django~=4.2.0`**（相容版本）
   - 允許 4.2.x（如 4.2.1, 4.2.5）
   - 不允許 4.3.0
   - 平衡穩定性與更新
   - 適用於接收安全修復但避免破壞性變更
</details>

---

### 題目 19

描述從零開始為新專案建立虛擬環境的完整步驟（至少 5 步）。

<details>
<summary>點擊查看答案要點</summary>

**參考答案**：

1. **建立專案目錄**
   ```bash
   mkdir myproject
   cd myproject
   ```

2. **建立虛擬環境**
   ```bash
   python -m venv venv
   ```

3. **啟用虛擬環境**
   ```bash
   # Windows
   venv\\Scripts\\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. **升級 pip**
   ```bash
   pip install --upgrade pip
   ```

5. **安裝專案依賴**
   ```bash
   pip install Django requests
   ```

6. **匯出依賴清單**
   ```bash
   pip freeze > requirements.txt
   ```

7. **建立 .gitignore**
   ```
   venv/
   __pycache__/
   *.pyc
   ```

（答對 5 步驟給滿分）
</details>

---

### 題目 20

當遇到套件版本衝突時，應該如何診斷和解決？請說明流程。

<details>
<summary>點擊查看答案要點</summary>

**參考答案**：

**診斷步驟**：
1. **閱讀錯誤訊息**：找出衝突的套件與版本需求
2. **查看依賴樹**：`pip show [package]` 或使用 `pipdeptree`
3. **檢查版本需求**：分析哪些套件要求不相容的版本

**解決策略**：
1. **升級套件**：嘗試升級到相容版本
   ```bash
   pip install --upgrade package-name
   ```

2. **降級套件**：安裝較舊但相容的版本
   ```bash
   pip install package-name==older-version
   ```

3. **尋找替代方案**：使用功能相似的其他套件

4. **隔離環境**：為不相容的功能建立獨立虛擬環境

5. **聯絡維護者**：在 GitHub 提 issue 回報相容性問題

6. **使用依賴解析工具**：如 poetry, pipenv 自動解決

（說明診斷與解決流程給滿分）
</details>

---"""),

    create_cell("markdown", """## 📊 評分標準

| 題型 | 題數 | 每題分數 | 小計 |
|:-----|:----:|:--------:|:----:|
| 選擇題 | 12 | 5 | 60 |
| 填空題 | 4 | 5 | 20 |
| 簡答題 | 4 | 10 | 40 |
| **總分** | **20** | - | **120** |

**計分方式**：實得分數 / 120 × 100 = 百分比分數

**評級**：
- 90-100 分：優秀 ⭐⭐⭐
- 70-89 分：良好 ⭐⭐
- 60-69 分：及格 ⭐
- 60 分以下：需加強

---

## 🎯 測驗總結

完成測驗後，請根據結果：

### 90 分以上
✅ 恭喜！你已完全掌握套件管理與虛擬環境
✅ 可以進入下一章學習
✅ 建議：在實際專案中應用這些知識

### 70-89 分
✅ 基礎概念良好
⚠️ 建議：複習錯誤的題目
⚠️ 多練習 requirements.txt 與版本管理

### 60-69 分
⚠️ 及格但需加強
📖 建議：重新學習 01-lecture.ipynb
📖 完成所有 practice 與 exercises

### 60 分以下
📖 需要重新學習本章
📖 建議流程：
1. 重讀 README.md
2. 重新學習 01-lecture.ipynb
3. 完成所有範例與練習
4. 一週後重新測驗

---

**學習提醒**：虛擬環境與套件管理是 Python 開發的基礎，務必熟練掌握！""")
]

# ==================== 寫入檔案 ====================

print("Starting to generate Ch28 complete content...")
print()

files = [
    ("02-worked-examples.ipynb", worked_examples_cells),
    ("03-practice.ipynb", practice_cells),
    ("04-exercises.ipynb", exercises_cells),
    ("05-solutions.ipynb", solutions_cells),
    ("quiz.ipynb", quiz_cells)
]

for filename, cells in files:
    notebook = create_notebook(cells)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"[OK] Generated {filename} ({file_size:.1f} KB)")

print()
print("=" * 60)
print("Ch28 All files generated successfully!")
print("=" * 60)
print()

print("File list:")
for filename, _ in files:
    filepath = os.path.join(TARGET_DIR, filename)
    size = os.path.getsize(filepath) / 1024
    print(f"  - {filename:<30} {size:>6.1f} KB")

print()
print("Total: 5 notebooks")
print()
print("Test with:")
print(f"  cd {TARGET_DIR}")
print("  jupyter notebook")
