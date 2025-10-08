#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""快速擴充 Ch29-30 內容（直接修改 notebook，不產生 .py 檔案）"""
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def expand_notebook(filepath, additional_cells):
    """擴充 notebook 檔案"""
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 在最後加入額外的 cells
    nb['cells'].extend(additional_cells)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    size = Path(filepath).stat().st_size
    return size

# ============================================================================
# Ch29 補充內容
# ============================================================================

ch29_02_extra = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 範例 4: 使用 type hints 提升程式碼品質\n\n**問題描述**: 為一個學生管理系統加入完整的型別提示。\n\n**解題思路**: 使用 typing 模組的 List, Dict, Optional, Union 等型別。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "from typing import List, Dict, Optional, Union\n\nclass Student:\n    \"\"\"學生類別\"\"\"\n    def __init__(self, name: str, age: int, grades: List[float]) -> None:\n        self.name = name\n        self.age = age\n        self.grades = grades\n    \n    def average_grade(self) -> float:\n        \"\"\"計算平均成績\"\"\"\n        if not self.grades:\n            return 0.0\n        return sum(self.grades) / len(self.grades)\n    \n    def get_info(self) -> Dict[str, Union[str, int, float]]:\n        \"\"\"取得學生資訊\"\"\"\n        return {\n            'name': self.name,\n            'age': self.age,\n            'average': self.average_grade()\n        }\n\nclass ClassRoom:\n    \"\"\"教室類別\"\"\"\n    def __init__(self, name: str) -> None:\n        self.name = name\n        self.students: List[Student] = []\n    \n    def add_student(self, student: Student) -> None:\n        \"\"\"新增學生\"\"\"\n        self.students.append(student)\n    \n    def find_student(self, name: str) -> Optional[Student]:\n        \"\"\"尋找學生\"\"\"\n        for student in self.students:\n            if student.name == name:\n                return student\n        return None\n    \n    def get_top_students(self, n: int = 3) -> List[Student]:\n        \"\"\"取得前 N 名學生\"\"\"\n        sorted_students = sorted(\n            self.students,\n            key=lambda s: s.average_grade(),\n            reverse=True\n        )\n        return sorted_students[:n]\n\n# 測試\nclassroom = ClassRoom(\"Python 班\")\nclassroom.add_student(Student(\"小明\", 20, [85, 90, 88]))\nclassroom.add_student(Student(\"小華\", 21, [92, 95, 89]))\nclassroom.add_student(Student(\"小美\", 20, [78, 82, 85]))\n\ntop_student = classroom.get_top_students(1)[0]\nprint(f\"第一名: {top_student.name}, 平均: {top_student.average_grade():.2f}\")\n\nfound = classroom.find_student(\"小明\")\nif found:\n    print(f\"找到學生: {found.get_info()}\")"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 範例 5: 整合 flake8 與 black 進行程式碼檢查\n\n**問題描述**: 設定專案的程式碼風格檢查工具鏈。\n\n**解題思路**: 建立設定檔，整合多種工具。"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 建立 .flake8 設定檔\n\n```ini\n[flake8]\nmax-line-length = 88\nextend-ignore = E203, W503\nexclude = \n    .git,\n    __pycache__,\n    venv,\n    .venv\nmax-complexity = 10\n```\n\n#### 建立 pyproject.toml (black 設定)\n\n```toml\n[tool.black]\nline-length = 88\ntarget-version = ['py38']\ninclude = '\\.pyi?$'\nexclude = '''\n/(\n    \\.git\n  | \\.venv\n  | __pycache__\n)/\n'''\n```\n\n#### 執行檢查\n\n```bash\n# 檢查程式碼風格\nflake8 src/\n\n# 自動格式化\nblack src/\n\n# 檢查但不修改\nblack --check src/\n\n# 排序 import\nisort src/\n```\n\n#### 建立 Makefile 自動化\n\n```makefile\n.PHONY: lint format check\n\nlint:\n\tflake8 src/\n\nformat:\n\tblack src/\n\tisort src/\n\ncheck:\n\tblack --check src/\n\tflake8 src/\n```"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 示範: 使用 flake8 檢查程式碼（需先安裝 flake8）\n# !pip install flake8 black isort\n\n# 建立測試檔案\ntest_code = '''\ndef bad_function( x,y ):\n    z=x+y\n    return z\n\ndef good_function(x, y):\n    \"\"\"良好的函式範例\"\"\"\n    result = x + y\n    return result\n'''\n\nwith open('test_style.py', 'w', encoding='utf-8') as f:\n    f.write(test_code)\n\nprint(\"已建立 test_style.py，可執行:\")\nprint(\"  flake8 test_style.py\")\nprint(\"  black test_style.py\")"
    }
]

ch29_03_extra = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 練習 7: 重構違反 PEP 8 的程式碼\n\n將下列程式碼重構為符合 PEP 8 規範:\n\n```python\ndef CalculateTotal(ItemList):\n    Total=0\n    for i in ItemList:\n        Total=Total+i\n    return Total\n\nclass user:\n    def __init__(self,Name,Age):\n        self.Name=Name\n        self.Age=Age\n```"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 練習 8: 為 API 函式加入完整文件\n\n為以下 REST API 函式加入 docstring（使用 Google style）:\n\n```python\ndef create_user(username, email, password, age=None):\n    if not username or not email:\n        raise ValueError(\"Missing required fields\")\n    user = {\n        'username': username,\n        'email': email,\n        'age': age\n    }\n    return user\n```"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    }
]

ch29_04_extra = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 15: 程式碼審查 (Code Review)\n\n以下程式碼有多處風格問題，請找出並修正（至少 10 處）:\n\n```python\nimport sys,os\nfrom typing import *\n\nclass DataProcessor:\n    def __init__(self,data):\n        self.Data=data\n        self.result=None\n    \n    def Process(self):\n        self.result=[]\n        for i in range(len(self.Data)):\n            x=self.Data[i]\n            if x>0:\n                self.result.append(x*2)\n        return self.result\n    \n    def getResult(self): return self.result\n\ndef calculate(a,b,c):\n    return a+b+c\n\ndata=[1,-2,3,-4,5]\nprocessor=DataProcessor(data)\nresult=processor.Process()\nprint(result)\n```\n\n**要求**:\n1. 列出所有違反 PEP 8 的地方\n2. 提供修正後的完整程式碼\n3. 加入適當的 docstring\n4. 加入型別提示"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 16: 建立專案的程式碼風格檢查流程\n\n為一個 Python 專案建立完整的程式碼風格檢查流程:\n\n**要求**:\n1. 建立 `.flake8` 設定檔\n2. 建立 `pyproject.toml` (black 設定)\n3. 建立 `.isort.cfg` (isort 設定)\n4. 建立 `Makefile` 包含 lint, format, check 指令\n5. 撰寫 README 說明如何使用這些工具"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 17: 型別提示進階應用\n\n為一個快取裝飾器加入完整的型別提示:\n\n```python\ndef memoize(func):\n    cache = {}\n    def wrapper(*args, **kwargs):\n        key = str(args) + str(kwargs)\n        if key not in cache:\n            cache[key] = func(*args, **kwargs)\n        return cache[key]\n    return wrapper\n```\n\n**要求**:\n1. 使用 `typing.Callable`\n2. 使用 `typing.TypeVar`\n3. 使用 `functools.wraps`\n4. 加入完整的 docstring"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 18: 設計程式碼風格指南文件\n\n為你的團隊撰寫一份程式碼風格指南文件 (Style Guide):\n\n**要求**:\n1. 命名規範（變數、函式、類別、常數、私有成員）\n2. 程式碼排版（縮排、空白、空行）\n3. Import 順序與分組\n4. Docstring 格式（使用哪種 style）\n5. 型別提示使用原則\n6. 註解撰寫原則\n7. 檔案組織結構\n8. 工具鏈設定（flake8, black, mypy）\n9. Git commit message 格式\n10. Code review 檢查清單\n\n以 Markdown 格式撰寫，至少 200 行。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案 (可以使用 %%writefile style_guide.md)\n"
    }
]

# ============================================================================
# Ch30 補充內容
# ============================================================================

ch30_02_extra = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 範例 4: Git 分支策略與合併衝突解決\n\n**問題描述**: 模擬團隊開發中的分支管理與衝突解決流程。\n\n**解題思路**: 建立 feature branch, 製造衝突, 解決衝突。"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 步驟 1: 初始化專案\n\n```bash\n# 建立新專案\nmkdir git-demo\ncd git-demo\ngit init\n\n# 建立初始檔案\necho \"# My Project\" > README.md\necho \"print('Hello World')\" > main.py\n\ngit add .\ngit commit -m \"feat: 初始化專案\"\n```"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 步驟 2: 建立 feature 分支\n\n```bash\n# 建立並切換到 feature 分支\ngit checkout -b feature/user-login\n\n# 修改檔案\necho \"def login(username, password):\" >> main.py\necho \"    return True\" >> main.py\n\ngit add main.py\ngit commit -m \"feat: 新增登入功能\"\n```"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 步驟 3: 同時在 main 分支修改（模擬衝突）\n\n```bash\n# 切回 main\ngit checkout main\n\n# 修改同一檔案\necho \"def logout():\" >> main.py\necho \"    return True\" >> main.py\n\ngit add main.py\ngit commit -m \"feat: 新增登出功能\"\n```"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 步驟 4: 合併並解決衝突\n\n```bash\n# 嘗試合併 feature 分支\ngit merge feature/user-login\n\n# 衝突訊息:\n# Auto-merging main.py\n# CONFLICT (content): Merge conflict in main.py\n# Automatic merge failed; fix conflicts and then commit the result.\n\n# 檢視衝突\ngit status\n\n# main.py 內容會變成:\n# print('Hello World')\n# <<<<<<< HEAD\n# def logout():\n#     return True\n# =======\n# def login(username, password):\n#     return True\n# >>>>>>> feature/user-login\n\n# 手動編輯解決衝突，改成:\n# print('Hello World')\n# def login(username, password):\n#     return True\n# def logout():\n#     return True\n\n# 標記為已解決\ngit add main.py\ngit commit -m \"merge: 合併 feature/user-login，保留兩個功能\"\n```"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 步驟 5: 查看分支圖\n\n```bash\n# 美化的分支歷史\ngit log --oneline --graph --all\n\n# 輸出類似:\n# *   a1b2c3d (HEAD -> main) merge: 合併 feature/user-login\n# |\\  \n# | * d4e5f6g (feature/user-login) feat: 新增登入功能\n# * | g6h7i8j feat: 新增登出功能\n# |/  \n# * j8k9l0m feat: 初始化專案\n```"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 範例 5: GitHub 協作工作流程\n\n**問題描述**: 模擬 GitHub 的 Fork-Pull Request 工作流程。\n\n**解題思路**: Fork -> Clone -> Branch -> Commit -> Push -> Pull Request。"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "#### 完整的 GitHub 協作流程\n\n```bash\n# 1. Fork 專案（在 GitHub 網站上點擊 Fork 按鈕）\n\n# 2. Clone 你的 fork\ngit clone https://github.com/YOUR_USERNAME/project.git\ncd project\n\n# 3. 新增上游倉庫\ngit remote add upstream https://github.com/ORIGINAL_OWNER/project.git\n\n# 4. 建立 feature 分支\ngit checkout -b feature/new-feature\n\n# 5. 開發功能\necho \"新功能\" > new_feature.py\ngit add new_feature.py\ngit commit -m \"feat: 新增新功能\"\n\n# 6. 同步上游變更（避免衝突）\ngit fetch upstream\ngit rebase upstream/main\n\n# 7. 推送到你的 fork\ngit push origin feature/new-feature\n\n# 8. 在 GitHub 上建立 Pull Request\n#    - 前往你的 GitHub fork\n#    - 點擊 \"Compare & pull request\"\n#    - 填寫 PR 標題與描述\n#    - 點擊 \"Create pull request\"\n\n# 9. Code Review 後如需修改\necho \"修正\" >> new_feature.py\ngit add new_feature.py\ngit commit -m \"fix: 根據 review 修正\"\ngit push origin feature/new-feature\n\n# 10. PR 被合併後，更新本地\ngit checkout main\ngit pull upstream main\ngit push origin main\n\n# 11. 刪除 feature 分支\ngit branch -d feature/new-feature\ngit push origin --delete feature/new-feature\n```"
    }
]

ch30_04_extra = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 15: 設計 Git Branching Strategy\n\n為一個中型團隊（10 人）設計完整的 Git 分支策略:\n\n**要求**:\n1. 定義主要分支（main, develop, release 等）\n2. 定義支援分支（feature, bugfix, hotfix）\n3. 分支命名規範\n4. 合併規則（何時用 merge, 何時用 rebase）\n5. Tag 規範（版本號格式）\n6. Commit message 規範（使用 Conventional Commits）\n7. Pull Request 流程\n8. Code Review 檢查清單\n9. CI/CD 整合點\n10. 緊急 hotfix 流程\n\n以 Markdown 格式撰寫完整文件。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案 (可以使用 %%writefile git_workflow.md)\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 16: Git Hooks 自動化\n\n建立 Git Hooks 來自動化開發流程:\n\n**要求**:\n1. **pre-commit hook**: 檢查程式碼風格（flake8, black）\n2. **commit-msg hook**: 驗證 commit message 格式\n3. **pre-push hook**: 執行測試\n4. **post-merge hook**: 自動安裝依賴（requirements.txt 變更時）\n\n撰寫完整的 shell script 並說明如何安裝。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 17: 修復 Git 歷史記錄\n\n處理以下 Git 歷史問題:\n\n**問題 1**: 最後一次 commit message 寫錯了\n```bash\n# 如何修正？\n```\n\n**問題 2**: 不小心 commit 了敏感檔案（如 .env）\n```bash\n# 如何從歷史中完全移除？\n```\n\n**問題 3**: 想要合併最近 3 個 commit\n```bash\n# 如何使用 interactive rebase？\n```\n\n**問題 4**: 不小心 commit 到錯誤的分支\n```bash\n# 如何將 commit 移到正確的分支？\n```\n\n撰寫完整的命令與解釋。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案\n"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "### 習題 18: GitHub Actions CI/CD Pipeline\n\n為 Python 專案建立 GitHub Actions workflow:\n\n**要求**:\n1. 在 PR 時執行:\n   - Lint (flake8, black check)\n   - Type check (mypy)\n   - Tests (pytest)\n   - Coverage report\n2. 在 merge 到 main 時:\n   - 建立 Docker image\n   - 推送到 Docker Hub\n   - 部署到 staging 環境\n3. 在建立 tag 時:\n   - 建立 GitHub Release\n   - 上傳 artifacts\n   - 部署到 production\n\n撰寫完整的 `.github/workflows/ci.yml` 檔案。"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# 你的答案 (可以使用 %%writefile .github/workflows/ci.yml)\n"
    }
]

# ============================================================================
# 執行擴充
# ============================================================================

def main():
    print("="*70)
    print("擴充 Ch29-30 內容")
    print("="*70)

    base = Path("fundamentals")

    # Ch29
    print("\n[Ch29: Code Style]")
    ch29_base = base / "ch29-code-style"

    size = expand_notebook(ch29_base / "02-worked-examples.ipynb", ch29_02_extra)
    print(f"  02-worked-examples.ipynb: {size:,} bytes")

    size = expand_notebook(ch29_base / "03-practice.ipynb", ch29_03_extra)
    print(f"  03-practice.ipynb: {size:,} bytes")

    size = expand_notebook(ch29_base / "04-exercises.ipynb", ch29_04_extra)
    print(f"  04-exercises.ipynb: {size:,} bytes")

    # Ch30
    print("\n[Ch30: Version Control]")
    ch30_base = base / "ch30-version-control"

    size = expand_notebook(ch30_base / "02-worked-examples.ipynb", ch30_02_extra)
    print(f"  02-worked-examples.ipynb: {size:,} bytes")

    size = expand_notebook(ch30_base / "04-exercises.ipynb", ch30_04_extra)
    print(f"  04-exercises.ipynb: {size:,} bytes")

    print("\n" + "="*70)
    print("✓ 完成！")
    print("="*70)

if __name__ == "__main__":
    main()
