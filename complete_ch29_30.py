#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完成 Ch29-30 的 solutions 和 quiz 內容"""
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def mk_cell(cell_type, source):
    """建立 notebook cell"""
    cell = {
        'cell_type': cell_type,
        'metadata': {},
        'source': source
    }
    if cell_type == 'code':
        cell['execution_count'] = None
        cell['outputs'] = []
    return cell

def expand_solutions_quiz(filepath, new_cells):
    """擴充 solutions 或 quiz notebook"""
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 在現有 cells 後加入新內容
    nb['cells'].extend(new_cells)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return Path(filepath).stat().st_size

# ============================================================================
# Ch29: Code Style - Solutions
# ============================================================================

ch29_solutions_cells = [
    mk_cell('markdown', '''## 🟢 習題 7 解答：重構違反 PEP 8 的程式碼

### 修正要點
1. 函式名稱：小寫 + 底線 (`CalculateTotal` → `calculate_total`)
2. 類別名稱：首字大寫 (`user` → `User`)
3. 變數名稱：小寫 + 底線 (`ItemList` → `item_list`)
4. 運算子前後加空格 (`Total=Total+i` → `total = total + i`)
5. 參數加空格 (`__init__(self,Name,Age)` → `__init__(self, name, age)`)'''),

    mk_cell('code', '''# 修正後的程式碼
def calculate_total(item_list):
    """計算項目總和

    Args:
        item_list (list): 數字列表

    Returns:
        int: 總和
    """
    total = 0
    for item in item_list:
        total = total + item
    return total

class User:
    """使用者類別"""

    def __init__(self, name, age):
        """初始化使用者

        Args:
            name (str): 使用者姓名
            age (int): 使用者年齡
        """
        self.name = name
        self.age = age

# 測試
user = User("Alice", 25)
print(f"使用者: {user.name}, 年齡: {user.age}")

items = [10, 20, 30, 40]
total = calculate_total(items)
print(f"總計: {total}")'''),

    mk_cell('markdown', '''---

## 🟢 習題 8 解答：為 API 函式加入完整文件

### 文件要點
1. 使用 Google Style Docstring
2. 說明函式功能
3. 列出所有參數（型態、說明、預設值）
4. 說明回傳值
5. 列出可能的例外
6. 提供使用範例'''),

    mk_cell('code', '''def create_user(username, email, password, age=None):
    """建立新使用者

    建立一個包含使用者資訊的字典。username 和 email 為必填欄位。

    Args:
        username (str): 使用者名稱，不可為空
        email (str): 電子郵件地址，不可為空
        password (str): 密碼
        age (int, optional): 年齡。預設為 None。

    Returns:
        dict: 包含使用者資訊的字典，格式如下：
            {
                'username': str,
                'email': str,
                'age': int or None
            }

    Raises:
        ValueError: 當 username 或 email 為空時

    Examples:
        >>> user = create_user("alice", "alice@example.com", "pass123", age=25)
        >>> print(user['username'])
        alice

        >>> user = create_user("bob", "bob@example.com", "pass456")
        >>> print(user['age'])
        None

    Note:
        密碼應該在實際應用中進行加密處理，此範例為簡化版本。
    """
    if not username or not email:
        raise ValueError("Missing required fields: username 和 email 不可為空")

    user = {
        'username': username,
        'email': email,
        'age': age
    }
    return user

# 測試
user1 = create_user("alice", "alice@example.com", "pass123", age=25)
print(f"✓ 建立使用者: {user1}")

user2 = create_user("bob", "bob@example.com", "pass456")
print(f"✓ 建立使用者: {user2}")

try:
    user3 = create_user("", "test@example.com", "pass")
except ValueError as e:
    print(f"✗ 錯誤: {e}")'''),

    mk_cell('markdown', '''---

## 🟡 習題 15 解答：程式碼審查 (Code Review)

### 發現的問題（共 15 處）

1. ❌ `import sys,os` → 應分行匯入
2. ❌ `from typing import *` → 不應使用 wildcard import
3. ❌ 類別名稱 `DataProcessor` 正確，但缺少 docstring
4. ❌ `__init__(self,data)` → 參數後應有空格
5. ❌ `self.Data` → 屬性名稱應小寫
6. ❌ `self.result=None` → 等號前後應有空格
7. ❌ `def Process(self)` → 方法名稱應小寫底線
8. ❌ `self.result=[]` → 等號前後應有空格
9. ❌ `for i in range(len(self.Data))` → 應直接迭代
10. ❌ `x=self.Data[i]` → 等號前後應有空格
11. ❌ `if x>0` → 運算子前後應有空格
12. ❌ `x*2` → 運算子前後應有空格
13. ❌ `def getResult(self): return self.result` → 不應單行
14. ❌ `def calculate(a,b,c)` → 參數應有空格，且缺少 docstring
15. ❌ 所有函式和類別都缺少型別提示'''),

    mk_cell('code', '''# 完整修正版本
import os
import sys
from typing import List, Optional

class DataProcessor:
    """資料處理器

    處理數值列表，過濾並轉換資料。
    """

    def __init__(self, data: List[int]) -> None:
        """初始化處理器

        Args:
            data (List[int]): 待處理的整數列表
        """
        self.data = data
        self.result: Optional[List[int]] = None

    def process(self) -> List[int]:
        """處理資料

        過濾出正數並乘以 2。

        Returns:
            List[int]: 處理後的結果列表
        """
        self.result = []
        for value in self.data:
            if value > 0:
                self.result.append(value * 2)
        return self.result

    def get_result(self) -> Optional[List[int]]:
        """取得處理結果

        Returns:
            Optional[List[int]]: 處理結果，若尚未處理則為 None
        """
        return self.result

def calculate(a: int, b: int, c: int) -> int:
    """計算三數之和

    Args:
        a (int): 第一個數
        b (int): 第二個數
        c (int): 第三個數

    Returns:
        int: 三數總和
    """
    return a + b + c

# 測試程式碼
if __name__ == "__main__":
    data = [1, -2, 3, -4, 5]
    processor = DataProcessor(data)
    result = processor.process()
    print(f"處理結果: {result}")

    total = calculate(10, 20, 30)
    print(f"計算結果: {total}")'''),

    mk_cell('markdown', '''### 改善總結
1. ✅ 所有 import 分行並正確排序
2. ✅ 移除 wildcard import
3. ✅ 所有類別、函式加入 docstring
4. ✅ 所有函式加入型別提示
5. ✅ 修正命名規範（小寫底線）
6. ✅ 所有運算子前後加空格
7. ✅ 函式不使用單行寫法
8. ✅ 迴圈直接迭代，不使用索引
9. ✅ 加入 `if __name__ == "__main__"` 保護
10. ✅ 符合 PEP 8 所有規範'''),
]

# ============================================================================
# Ch29: Code Style - Quiz
# ============================================================================

ch29_quiz_cells = [
    mk_cell('markdown', '''## 📝 問題 11-15：PEP 8 進階規範

### 問題 11
以下哪一個 import 順序是正確的？

A)
```python
import json
from typing import List
import os
from datetime import datetime
```

B)
```python
import os
import json
from datetime import datetime
from typing import List
```

C)
```python
from datetime import datetime
from typing import List
import json
import os
```

D)
```python
import json
import os

from datetime import datetime
from typing import List
```'''),

    mk_cell('markdown', '''### 問題 12
以下哪一個類別定義符合 PEP 8？

A) `class MyClass`
B) `class my_class`
C) `class MYCLASS`
D) `class myClass`'''),

    mk_cell('markdown', '''### 問題 13
以下哪一個常數命名是正確的？

A) `maxSize = 100`
B) `MAX_SIZE = 100`
C) `Max_Size = 100`
D) `MaxSize = 100`'''),

    mk_cell('markdown', '''### 問題 14
Docstring 應該使用什麼符號？

A) `# 單行註解`
B) `''' 三個單引號 '''`
C) `""" 三個雙引號 """`
D) B 和 C 都可以'''),

    mk_cell('markdown', '''### 問題 15
以下哪一個函式定義需要改進？

A)
```python
def get_user_name(user_id: int) -> str:
    pass
```

B)
```python
def getUserName(userId):
    pass
```

C)
```python
def get_username(user_id):
    pass
```

D)
```python
def get_name(id: int) -> str:
    pass
```'''),

    mk_cell('markdown', '''---

## 💻 編程題 6-10

### 編程題 6
建立一個符合 PEP 8 規範的計算機類別，包含四則運算方法。'''),

    mk_cell('code', '''# 你的程式碼
'''),

    mk_cell('markdown', '''### 編程題 7
為以下函式加入完整的 Google Style docstring：

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```'''),

    mk_cell('code', '''# 你的程式碼
'''),

    mk_cell('markdown', '''### 編程題 8
使用 type hints 改寫以下函式：

```python
def filter_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
```'''),

    mk_cell('code', '''# 你的程式碼
'''),

    mk_cell('markdown', '''### 編程題 9
建立一個資料類別 `Student`，包含姓名、年齡、成績，使用 `@property` 裝飾器保護屬性。'''),

    mk_cell('code', '''# 你的程式碼
'''),

    mk_cell('markdown', '''### 編程題 10
撰寫一個裝飾器 `timing_decorator`，計算函式執行時間，並加入完整的型別提示。'''),

    mk_cell('code', '''# 你的程式碼
'''),

    mk_cell('markdown', '''---

## 📊 解答

### 選擇題解答
1. B - 先標準庫，再第三方庫，最後自己的模組
2. C - list, append(), 負索引
3. B - MAX_SIZE (常數用大寫底線)
4. A - class MyClass (大駝峰命名法)
5. A - 變數用小寫底線
6. D - 避免在迴圈內使用 +=
7. A - 三個雙引號
8. C - `python -m flake8`
9. B - black 會自動格式化
10. A - 使用 4 個空格縮排

### 選擇題解答 (11-15)
11. B - 標準庫分組，每組間空一行
12. A - class MyClass (大駝峰)
13. B - MAX_SIZE (常數大寫底線)
14. D - 三單引號或三雙引號都可以，但建議三雙引號
15. B - camelCase 不符合 Python 規範

### 評分標準
- 選擇題: 每題 5 分 (共 75 分)
- 編程題: 每題 5 分 (共 25 分)
- **總分**: 100 分
- **及格標準**: 70 分'''),
]

# ============================================================================
# Ch30: Version Control - Solutions
# ============================================================================

ch30_solutions_cells = [
    mk_cell('markdown', '''## 🟢 習題 7 解答：Git 基本操作練習

### 完整操作步驟'''),

    mk_cell('markdown', '''```bash
# 1. 建立專案資料夾
mkdir git-practice
cd git-practice

# 2. 初始化 Git 倉庫
git init

# 3. 建立 README.md
echo "# Git Practice Project" > README.md

# 4. 查看狀態
git status
# 輸出: Untracked files: README.md

# 5. 將檔案加入暫存區
git add README.md

# 6. 查看狀態
git status
# 輸出: Changes to be committed: new file: README.md

# 7. 提交變更
git commit -m "docs: 新增 README.md"

# 8. 查看提交歷史
git log --oneline
# 輸出: abc1234 docs: 新增 README.md

# 9. 修改 README.md
echo "\n## Introduction\nThis is a Git practice project." >> README.md

# 10. 查看變更
git diff

# 11. 提交修改
git add README.md
git commit -m "docs: 更新 README 說明"

# 12. 查看完整歷史
git log --oneline --graph
```'''),

    mk_cell('markdown', '''### 知識點回顧
- ✅ `git init` 初始化倉庫
- ✅ `git status` 查看狀態
- ✅ `git add` 加入暫存區
- ✅ `git commit` 提交變更
- ✅ `git log` 查看歷史
- ✅ `git diff` 查看差異

---'''),

    mk_cell('markdown', '''## 🟢 習題 8 解答：.gitignore 設定

### .gitignore 完整內容'''),

    mk_cell('markdown', '''```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# 作業系統
.DS_Store
Thumbs.db
desktop.ini

# 日誌檔案
*.log
logs/

# 資料庫
*.db
*.sqlite3

# 環境變數
.env
.env.local
config/secrets.py

# 測試
.coverage
htmlcov/
.pytest_cache/

# 建置產物
dist/
build/
*.egg-info/

# 文件
docs/_build/

# 備份檔案
*.bak
*.tmp
```'''),

    mk_cell('markdown', '''### 測試 .gitignore

```bash
# 建立測試檔案
mkdir __pycache__
echo "test" > __pycache__/test.pyc
echo "test" > test.py
echo "secret" > .env

# 查看 git 狀態
git status

# 應該只看到 test.py，其他被忽略
```

### 知識點回顧
- ✅ 使用 `#` 註解
- ✅ `*` 萬用字元
- ✅ `/` 目錄結尾
- ✅ `!` 例外規則（不忽略）

---'''),

    mk_cell('markdown', '''## 🟡 習題 15 解答：Git Branching Strategy

### 完整的分支策略文件'''),

    mk_cell('markdown', '''# Git Branching Strategy

## 主要分支

### 1. main (主分支)
- **用途**: 穩定的生產環境程式碼
- **保護**: 禁止直接 push，只能透過 PR 合併
- **觸發**: 自動部署到 production

### 2. develop (開發分支)
- **用途**: 下一版本的開發主線
- **來源**: 從 main 分支建立
- **合併**: feature 分支合併到此

### 3. release/x.x.x (發布分支)
- **用途**: 準備新版本發布
- **來源**: 從 develop 分支建立
- **命名**: `release/1.2.0`
- **合併**: 同時合併到 main 和 develop

## 支援分支

### 4. feature/* (功能分支)
- **用途**: 開發新功能
- **來源**: 從 develop 分支建立
- **命名**: `feature/user-login`, `feature/payment-module`
- **生命週期**: 開發完成後刪除
- **合併方式**: PR → develop (使用 squash merge)

### 5. bugfix/* (錯誤修正分支)
- **用途**: 修正非緊急 bug
- **來源**: 從 develop 分支建立
- **命名**: `bugfix/fix-login-error`
- **合併**: PR → develop

### 6. hotfix/* (緊急修正分支)
- **用途**: 修正生產環境緊急問題
- **來源**: 從 main 分支建立
- **命名**: `hotfix/critical-security-fix`
- **合併**: 同時合併到 main 和 develop

## 分支命名規範

```
feature/功能描述   (小寫，使用連字號)
bugfix/問題描述
hotfix/緊急問題
release/版本號
```

## Commit Message 規範 (Conventional Commits)

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Type 類型
- `feat`: 新功能
- `fix`: 錯誤修正
- `docs`: 文件更新
- `style`: 程式碼格式（不影響功能）
- `refactor`: 重構
- `test`: 測試相關
- `chore`: 維護任務

### 範例
```
feat(auth): add user login functionality

Implement JWT-based authentication system with refresh tokens.

Closes #123
```

## Pull Request 流程

1. **建立 PR**
   - 填寫完整的描述
   - 連結相關 Issue
   - 指派 Reviewer

2. **Code Review 檢查清單**
   - [ ] 程式碼符合風格規範
   - [ ] 有足夠的測試覆蓋率
   - [ ] 文件已更新
   - [ ] 無安全性問題
   - [ ] 效能影響已評估

3. **CI/CD 檢查**
   - [ ] Lint 通過
   - [ ] Tests 通過
   - [ ] Build 成功

4. **合併規則**
   - feature → develop: Squash merge
   - develop → main: Merge commit
   - hotfix → main: Merge commit

## Tag 規範

使用語意化版本 (Semantic Versioning):

```
v主版本.次版本.修訂號

v1.0.0  # 第一個正式版本
v1.1.0  # 新增功能
v1.1.1  # 錯誤修正
v2.0.0  # 重大更新（不向下相容）
```

## 緊急 Hotfix 流程

```bash
# 1. 從 main 建立 hotfix 分支
git checkout main
git pull origin main
git checkout -b hotfix/security-patch

# 2. 修正問題
git add .
git commit -m "fix(security): patch XSS vulnerability"

# 3. 合併到 main
git checkout main
git merge --no-ff hotfix/security-patch
git tag v1.0.1
git push origin main --tags

# 4. 同步到 develop
git checkout develop
git merge --no-ff hotfix/security-patch
git push origin develop

# 5. 刪除 hotfix 分支
git branch -d hotfix/security-patch
```

## 工具整合

### Pre-commit Hooks
```bash
#!/bin/sh
# .git/hooks/pre-commit
flake8 src/
black --check src/
pytest
```

### GitHub Branch Protection Rules
- Require PR reviews (至少 1 人)
- Require status checks to pass
- Require branches to be up to date
- Include administrators

## 參考資料
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
'''),

    mk_cell('markdown', '''---'''),
]

# ============================================================================
# Ch30: Version Control - Quiz
# ============================================================================

ch30_quiz_cells = [
    mk_cell('markdown', '''## 📝 問題 11-15：Git 進階操作

### 問題 11
要撤銷最後一次 commit（但保留變更），應該使用？

A) `git reset --soft HEAD~1`
B) `git reset --hard HEAD~1`
C) `git revert HEAD`
D) `git checkout HEAD~1`'''),

    mk_cell('markdown', '''### 問題 12
以下哪個命令可以查看某個檔案的修改歷史？

A) `git log <file>`
B) `git history <file>`
C) `git show <file>`
D) `git track <file>`'''),

    mk_cell('markdown', '''### 問題 13
Git merge 和 Git rebase 的主要差別是？

A) merge 保留完整歷史，rebase 重寫歷史
B) merge 更快，rebase 更慢
C) merge 用於本地，rebase 用於遠端
D) 沒有差別'''),

    mk_cell('markdown', '''### 問題 14
.gitignore 中的 `*.log` 表示？

A) 忽略名為 *.log 的檔案
B) 忽略所有 .log 結尾的檔案
C) 忽略 log 資料夾
D) 忽略包含 log 的檔案'''),

    mk_cell('markdown', '''### 問題 15
GitHub Pull Request 的主要目的是？

A) 下載程式碼
B) 提交程式碼審查請求
C) 刪除分支
D) 備份程式碼'''),

    mk_cell('markdown', '''---

## 💻 編程題 6-10

### 編程題 6
撰寫一個 shell script，自動化以下 Git 流程：
1. 拉取最新程式碼
2. 建立 feature 分支
3. 提交變更
4. 推送到遠端'''),

    mk_cell('code', '''#!/bin/bash
# 你的 shell script
'''),

    mk_cell('markdown', '''### 編程題 7
撰寫一個 pre-commit hook，檢查：
1. Python 檔案是否符合 PEP 8
2. Commit message 是否符合 Conventional Commits 格式'''),

    mk_cell('code', '''#!/bin/sh
# 你的 pre-commit hook
'''),

    mk_cell('markdown', '''### 編程題 8
建立一個 .gitignore 檔案，適用於 Django + React 專案。'''),

    mk_cell('code', '''# 你的 .gitignore
'''),

    mk_cell('markdown', '''### 編程題 9
撰寫一個 Python 腳本，解析 git log 輸出，統計每位作者的提交次數。'''),

    mk_cell('code', '''# 你的 Python 腳本
'''),

    mk_cell('markdown', '''### 編程題 10
設計一個 GitHub Actions workflow，在 PR 時執行以下檢查：
- Lint (flake8)
- Tests (pytest)
- Security scan (bandit)'''),

    mk_cell('code', '''# .github/workflows/pr-check.yml
# 你的 workflow
'''),

    mk_cell('markdown', '''---

## 📊 解答

### 選擇題解答
1. B - git init
2. A - git add .
3. C - git commit -m "message"
4. A - git status
5. B - git log
6. C - git checkout -b feature-branch
7. A - git merge feature-branch
8. C - git push origin main
9. B - git pull origin main
10. A - git clone <url>

### 選擇題解答 (11-15)
11. A - git reset --soft HEAD~1 (撤銷commit保留變更)
12. A - git log <file>
13. A - merge保留歷史，rebase重寫歷史
14. B - 忽略所有 .log 結尾的檔案
15. B - 提交程式碼審查請求

### 評分標準
- 選擇題: 每題 5 分 (共 75 分)
- 編程題: 每題 5 分 (共 25 分)
- **總分**: 100 分
- **及格標準**: 70 分'''),
]

# ============================================================================
# 執行補充
# ============================================================================

def main():
    print("="*70)
    print("補充 Ch29-30 Solutions 和 Quiz")
    print("="*70)

    base = Path("fundamentals")

    # Ch29
    print("\n[Ch29: Code Style]")
    ch29_base = base / "ch29-code-style"

    size = expand_solutions_quiz(ch29_base / "05-solutions.ipynb", ch29_solutions_cells)
    print(f"  05-solutions.ipynb: {size:,} bytes ({size/1024:.1f} KB)")

    size = expand_solutions_quiz(ch29_base / "quiz.ipynb", ch29_quiz_cells)
    print(f"  quiz.ipynb: {size:,} bytes ({size/1024:.1f} KB)")

    # Ch30
    print("\n[Ch30: Version Control]")
    ch30_base = base / "ch30-version-control"

    size = expand_solutions_quiz(ch30_base / "05-solutions.ipynb", ch30_solutions_cells)
    print(f"  05-solutions.ipynb: {size:,} bytes ({size/1024:.1f} KB)")

    size = expand_solutions_quiz(ch30_base / "quiz.ipynb", ch30_quiz_cells)
    print(f"  quiz.ipynb: {size:,} bytes ({size/1024:.1f} KB)")

    print("\n" + "="*70)
    print("✓ 完成！")
    print("="*70)

    # 顯示最終大小
    print("\n=== 最終大小統計 ===")
    for ch_name in ['ch29-code-style', 'ch30-version-control']:
        ch_path = base / ch_name
        files = ['02-worked-examples.ipynb', '03-practice.ipynb', '04-exercises.ipynb', '05-solutions.ipynb', 'quiz.ipynb']
        total = sum((ch_path / f).stat().st_size for f in files)
        print(f"{ch_name:30s}: {total:7,} bytes ({total/1024:5.1f} KB)")

if __name__ == "__main__":
    main()
