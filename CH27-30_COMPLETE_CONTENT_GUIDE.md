# Ch27-30 完整內容開發指南
# Complete Content Development Guide for Chapters 27-30

**文件目的**: 本文件提供 Ch27-Ch30 所有檔案的完整內容大綱與範例程式碼,確保品質達到 Ch01 標準。

**使用方式**: 按照本指南依序建立各章節的 7 個檔案（README + 6 notebooks）。

---

## 📋 總覽 (Overview)

### 檔案清單 (File Checklist)

每章需要的 7 個檔案:
- [ ] README.md - 章節導讀
- [ ] 01-lecture.ipynb - 完整講義（至少 5 個範例）
- [ ] 02-worked-examples.ipynb - 詳解範例（3-5 題）
- [ ] 03-practice.ipynb - 課堂練習
- [ ] 04-exercises.ipynb - 課後習題（至少 10 題）
- [ ] 05-solutions.ipynb - 習題解答
- [ ] quiz.ipynb - 自我測驗

### 完成狀態 (Completion Status)

**Ch27: 自訂模組與套件**
- [x] README.md - 已完成
- [ ] 01-lecture.ipynb
- [ ] 02-worked-examples.ipynb
- [ ] 03-practice.ipynb
- [ ] 04-exercises.ipynb
- [ ] 05-solutions.ipynb
- [ ] quiz.ipynb

**Ch28: 套件管理與虛擬環境**
- [x] README.md - 已完成
- [ ] 01-lecture.ipynb
- [ ] 02-worked-examples.ipynb
- [ ] 03-practice.ipynb
- [ ] 04-exercises.ipynb
- [ ] 05-solutions.ipynb
- [ ] quiz.ipynb

**Ch29: 程式碼風格與文件**
- [x] README_FULL.md - 已完成（需重新命名為 README.md）
- [ ] 01-lecture.ipynb
- [ ] 02-worked-examples.ipynb
- [ ] 03-practice.ipynb
- [ ] 04-exercises.ipynb
- [ ] 05-solutions.ipynb
- [ ] quiz.ipynb

**Ch30: 版本控制基礎**
- [ ] README.md
- [ ] 01-lecture.ipynb
- [ ] 02-worked-examples.ipynb
- [ ] 03-practice.ipynb
- [ ] 04-exercises.ipynb
- [ ] 05-solutions.ipynb
- [ ] quiz.ipynb

---

## 📚 Ch27: 自訂模組與套件 (Custom Modules and Packages)

### README.md ✅ 已完成

### 01-lecture.ipynb 內容大綱

**Part I: 理論基礎**
- 章節概覽（學習目標、先備知識、時長）
- 核心概念（模組 vs 套件、First Principles）

**Part II: 實作演練（5 個範例）**

**範例 1: 建立第一個模組**
```python
# math_utils.py
PI = 3.14159

def add(a, b):
    return a + b

def circle_area(radius):
    return PI * radius ** 2

if __name__ == "__main__":
    print("Testing...")
```

匯入方式:
```python
import math_utils
from math_utils import circle_area
import math_utils as mu
```

**範例 2: 套件結構**
```
mypackage/
├── __init__.py
├── math_ops.py
└── string_ops.py
```

```python
# __init__.py
__version__ = "1.0.0"
__all__ = ['math_ops', 'string_ops']

# math_ops.py
def square(x):
    return x ** 2

# string_ops.py
def reverse(s):
    return s[::-1]
```

**範例 3: `__name__` 特殊變數**
```python
# demo.py
print(f"__name__ = {__name__}")

def greet():
    print("Hello!")

if __name__ == "__main__":
    print("直接執行")
    greet()
else:
    print("被匯入")
```

**範例 4: 模組搜尋路徑（sys.path）**
```python
import sys

# 查看模組搜尋路徑
for path in sys.path:
    print(path)

# 手動加入路徑
sys.path.append('/my/custom/path')
```

**範例 5: 絕對匯入 vs 相對匯入**
```python
# 絕對匯入（在套件外部）
from mypackage.subpackage import module

# 相對匯入（在套件內部）
from . import sibling_module      # 同層級
from .. import parent_module       # 上層級
from .subpkg import child_module   # 子套件
```

**Part III: 本章總結**
- 知識回顧
- 常見誤區
- 自我檢核
- 延伸閱讀

### 02-worked-examples.ipynb 內容

**範例 1: 建立計算機模組**
```python
# 問題：建立一個 calculator.py 模組,包含四則運算

# 步驟 1: 建立模組
%%writefile calculator.py
def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """減法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除數不能為零")
    return a / b

if __name__ == "__main__":
    # 測試
    assert add(3, 5) == 8
    assert subtract(10, 3) == 7
    print("所有測試通過!")

# 步驟 2: 匯入並使用
import calculator
print(calculator.add(10, 20))      # 30
print(calculator.divide(10, 2))    # 5.0
```

**範例 2: 建立工具套件**
```python
# 問題：建立 myutils 套件,包含 file_ops 和 text_ops 兩個模組

# 步驟 1: 建立套件結構
import os
os.makedirs('myutils', exist_ok=True)

# 步驟 2: __init__.py
%%writefile myutils/__init__.py
"""My Utilities Package"""
__version__ = "0.1.0"
__all__ = ['file_ops', 'text_ops']

from .file_ops import read_file, write_file
from .text_ops import word_count

# 步驟 3: file_ops.py
%%writefile myutils/file_ops.py
def read_file(filepath):
    """讀取檔案內容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """寫入檔案"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 步驟 4: text_ops.py
%%writefile myutils/text_ops.py
def word_count(text):
    """計算字數"""
    return len(text.split())

# 步驟 5: 使用套件
from myutils import read_file, word_count
# 或
import myutils
print(myutils.__version__)
```

**範例 3: 解決循環匯入問題**
```python
# 問題：模組 A 匯入模組 B,模組 B 又匯入模組 A（循環匯入）

# 錯誤示範
# module_a.py
from module_b import func_b
def func_a():
    return func_b()

# module_b.py
from module_a import func_a  # 循環匯入!
def func_b():
    return func_a()

# 解決方案 1: 延遲匯入
# module_a.py
def func_a():
    from module_b import func_b  # 在函式內部匯入
    return func_b()

# 解決方案 2: 重構程式碼
# 將共同依賴抽取到第三個模組
# common.py
def shared_function():
    pass

# module_a.py
from common import shared_function
# module_b.py
from common import shared_function
```

### 03-practice.ipynb 內容

**練習 1**: 建立溫度轉換模組（temperature.py）
- celsius_to_fahrenheit()
- fahrenheit_to_celsius()
- 加入 `if __name__ == "__main__":` 測試

**練習 2**: 建立字串工具套件（stringtools/）
- 包含 case.py（大小寫轉換）
- 包含 validate.py（驗證函式）
- 撰寫 `__init__.py`

**練習 3**: 修正以下模組的問題
```python
# 提供有問題的程式碼,讓學生找出並修正
```

### 04-exercises.ipynb 內容（10 題）

**基礎題（1-5）**
1. 建立 math_helper.py 模組,包含 is_prime(), is_even(), is_odd()
2. 建立 list_utils.py,包含 flatten(), unique(), reverse()
3. 為上述模組加入 `if __name__ == "__main__":` 測試碼
4. 使用三種不同方式匯入 math_helper 模組
5. 建立套件結構 mytools/,包含兩個子模組

**中級題（6-8）**
6. 建立檔案操作套件 file_handler/,包含 reader.py 和 writer.py
7. 使用相對匯入在套件內部組織模組
8. 處理模組匯入錯誤（ModuleNotFoundError）

**挑戰題（9-10）**
9. 建立多層套件結構 myproject/core/utils/
10. 實作動態匯入（使用 `importlib`）

### 05-solutions.ipynb 內容
提供上述 10 題的完整解答,包含:
- 程式碼
- 執行結果
- 詳細註解
- 延伸說明

### quiz.ipynb 內容

**選擇題（10 題）**
1. 以下何者是模組？
   A) .py 檔案
   B) 資料夾
   C) 函式
   D) 變數

2. `__name__` 在模組被匯入時的值是？
   A) `"__main__"`
   B) 模組名稱
   C) `None`
   D) 空字串

3. 套件必須包含哪個檔案？
   A) `__main__.py`
   B) `__init__.py`
   C) `setup.py`
   D) 不需要特殊檔案

**簡答題（3 題）**
1. 解釋 `if __name__ == "__main__":` 的用途
2. 說明絕對匯入與相對匯入的差異
3. 如何解決循環匯入問題？

**程式題（2 題）**
1. 建立一個模組,包含三個函式,並示範三種匯入方式
2. 建立簡單的套件結構並匯入使用

---

## 📦 Ch28: 套件管理與虛擬環境

### README.md ✅ 已完成

### 01-lecture.ipynb 內容大綱

**Part I: 理論基礎**
- pip 套件管理器的用途
- 虛擬環境的必要性
- requirements.txt 的作用

**Part II: 實作演練（5 個範例）**

**範例 1: pip 基本操作**
```bash
# 安裝套件
pip install requests

# 安裝特定版本
pip install requests==2.28.0

# 升級套件
pip install --upgrade requests

# 移除套件
pip uninstall requests

# 列出已安裝套件
pip list
pip freeze

# 查看套件資訊
pip show requests
```

**範例 2: 建立虛擬環境**
```bash
# 建立虛擬環境
python -m venv myenv

# 啟用虛擬環境
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# 確認在虛擬環境中
python -c "import sys; print(sys.executable)"

# 停用虛擬環境
deactivate
```

**範例 3: requirements.txt**
```bash
# requirements.txt 範例
requests==2.28.0
flask>=2.0,<3.0
numpy~=1.21.0
pytest

# 匯出當前環境依賴
pip freeze > requirements.txt

# 安裝依賴
pip install -r requirements.txt
```

**範例 4: 版本指定語法**
```
# requirements.txt 詳細範例
# 精確版本
Django==4.0.0

# 版本範圍
pandas>=1.0,<2.0

# 相容版本（1.21.x）
numpy~=1.21.0

# 大於等於
requests>=2.0

# 從 Git 安裝
git+https://github.com/user/repo.git

# 本地套件
-e ./local_package
```

**範例 5: 專案環境設定流程**
```bash
# 步驟 1: 建立專案資料夾
mkdir myproject
cd myproject

# 步驟 2: 建立虛擬環境
python -m venv venv

# 步驟 3: 啟用虛擬環境
venv\Scripts\activate  # Windows

# 步驟 4: 升級 pip
python -m pip install --upgrade pip

# 步驟 5: 安裝套件
pip install flask requests

# 步驟 6: 匯出依賴
pip freeze > requirements.txt

# 步驟 7: 建立 .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

### 02-worked-examples.ipynb 內容

**範例 1: 為新專案設定環境**
```bash
# 完整流程示範
# 1. 建立專案
mkdir flask_app
cd flask_app

# 2. 建立虛擬環境
python -m venv venv

# 3. 啟用環境
venv\Scripts\activate

# 4. 安裝套件
pip install flask flask-sqlalchemy

# 5. 建立 requirements.txt
pip freeze > requirements.txt

# 6. 驗證
cat requirements.txt
pip list
```

**範例 2: 克隆專案並安裝依賴**
```bash
# 情境：從 GitHub 克隆專案

# 1. 克隆專案
git clone https://github.com/user/project.git
cd project

# 2. 建立虛擬環境
python -m venv venv

# 3. 啟用環境
source venv/bin/activate  # macOS/Linux

# 4. 安裝依賴
pip install -r requirements.txt

# 5. 驗證安裝
pip list
python -c "import flask; print(flask.__version__)"
```

**範例 3: 處理版本衝突**
```bash
# 問題：兩個套件依賴不同版本的 numpy

# requirements.txt
scikit-learn==0.24.0  # 需要 numpy>=1.13
tensorflow==2.4.0     # 需要 numpy<1.20

# 解決方案 1: 找到相容版本
numpy==1.19.5  # 滿足兩者需求

# 解決方案 2: 使用不同虛擬環境
# 專案 A 環境
python -m venv venv_sklearn
# 專案 B 環境
python -m venv venv_tensorflow
```

### 03-practice.ipynb 內容

**練習 1**: 建立虛擬環境並安裝 requests
**練習 2**: 建立 requirements.txt 並在新環境中安裝
**練習 3**: 處理 pip 安裝錯誤

### 04-exercises.ipynb 內容（10 題）

**基礎題（1-5）**
1. 使用 pip 安裝 requests 套件
2. 查看 requests 的版本與資訊
3. 建立名為 testenv 的虛擬環境
4. 在虛擬環境中安裝 3 個套件
5. 匯出 requirements.txt

**中級題（6-8）**
6. 建立包含版本限制的 requirements.txt
7. 在新環境中從 requirements.txt 安裝
8. 診斷並修正套件安裝錯誤

**挑戰題（9-10）**
9. 為 Web 專案設定完整環境（Flask + DB）
10. 建立開發/測試/生產三個環境配置

### 05-solutions.ipynb 內容
完整解答所有習題

### quiz.ipynb 內容

**選擇題（10 題）**
關於 pip, venv, requirements.txt

**簡答題（3 題）**
1. 為什麼需要虛擬環境？
2. requirements.txt 中 `~=` 的含義？
3. 如何確認當前在虛擬環境中？

**實作題（2 題）**
1. 建立虛擬環境並安裝 5 個套件
2. 處理版本衝突問題

---

## 🎨 Ch29: 程式碼風格與文件

### README.md ✅ 已完成（README_FULL.md 需重新命名）

### 01-lecture.ipynb 內容大綱

**Part I: 理論基礎**
- PEP 8 風格指南介紹
- docstring 與 type hints
- 程式碼品質的重要性

**Part II: 實作演練（5 個範例）**

**範例 1: PEP 8 縮排與格式**
```python
# ❌ 不符合 PEP 8
def my_function(x,y,z):
  if x>0:
        return x+y+z

# ✅ 符合 PEP 8
def my_function(x, y, z):
    """計算三個數的和"""
    if x > 0:
        return x + y + z
    return 0
```

**範例 2: 命名規範**
```python
# ✅ 正確命名
class StudentGrade:  # PascalCase
    MAX_SCORE = 100  # 常數 UPPER_CASE

    def __init__(self, student_name):  # snake_case
        self.student_name = student_name
        self._score = 0  # 私有變數 _leading

    def calculate_average(self):  # snake_case
        pass

# ❌ 錯誤命名
class student_grade:  # 應該 PascalCase
    maxScore = 100    # 應該 UPPER_CASE

    def __init__(self, StudentName):  # 應該 snake_case
        self.StudentName = StudentName

    def CalculateAverage(self):  # 應該 snake_case
        pass
```

**範例 3: Docstring 撰寫**
```python
# 單行 docstring
def square(n):
    """計算平方"""
    return n ** 2

# 多行 docstring (Google Style)
def calculate_bmi(weight, height):
    """計算 BMI 指數

    Args:
        weight (float): 體重（公斤）
        height (float): 身高（公尺）

    Returns:
        float: BMI 指數

    Raises:
        ValueError: 當 height 為 0 時

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if height == 0:
        raise ValueError("身高不能為零")
    return weight / (height ** 2)

# 類別 docstring
class BankAccount:
    """銀行帳戶類別

    管理帳戶餘額、存款與提款操作。

    Attributes:
        account_number (str): 帳戶號碼
        balance (float): 帳戶餘額

    Example:
        >>> account = BankAccount("123456")
        >>> account.deposit(1000)
        >>> account.get_balance()
        1000.0
    """

    def __init__(self, account_number):
        """初始化帳戶

        Args:
            account_number (str): 帳戶號碼
        """
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        """存款

        Args:
            amount (float): 存款金額

        Raises:
            ValueError: 當金額為負數時
        """
        if amount < 0:
            raise ValueError("金額必須為正數")
        self.balance += amount
```

**範例 4: Type Hints**
```python
from typing import List, Dict, Optional, Union, Tuple

# 基本型態提示
def greet(name: str) -> str:
    return f"Hello, {name}!"

# List 型態
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Dict 型態
def get_student_info(student_id: int) -> Dict[str, str]:
    return {"name": "Alice", "grade": "A"}

# Optional（可能為 None）
def find_user(user_id: int) -> Optional[str]:
    if user_id > 0:
        return "User found"
    return None

# Union（多種型態）
def process(data: Union[str, int, float]) -> str:
    return str(data)

# Tuple
def get_coordinates() -> Tuple[float, float]:
    return (25.0, 121.5)

# 多個參數與回傳值
def divide(a: float, b: float) -> Tuple[float, float]:
    """回傳商和餘數"""
    quotient = a // b
    remainder = a % b
    return (quotient, remainder)

# 變數型態標註
age: int = 25
names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
```

**範例 5: 程式碼品質工具**
```python
# 使用 flake8 檢查程式碼（在終端機執行）
# pip install flake8
# flake8 myfile.py

# 使用 black 自動格式化（在終端機執行）
# pip install black
# black myfile.py

# 使用 mypy 檢查型態（在終端機執行）
# pip install mypy
# mypy myfile.py

# 範例程式碼
# bad_code.py（有風格問題）
def add( x,y ):
    return x+y

class myClass:
    def __init__( self,name ):
        self.Name=name

# 執行 black 後
def add(x, y):
    return x + y


class MyClass:
    def __init__(self, name):
        self.name = name
```

### 02-worked-examples.ipynb 內容

**範例 1: 重構不良程式碼**
```python
# 原始程式碼（不良）
def f(x):
    if x>0:
        return x*2
    else:
        return 0

# 重構後
def double_positive(number):
    """將正數加倍

    Args:
        number (int): 輸入數字

    Returns:
        int: 正數加倍，負數返回 0
    """
    if number > 0:
        return number * 2
    return 0
```

**範例 2: 為現有函式加文件**
**範例 3: 加入 type hints**

### 03-practice.ipynb 內容

**練習 1**: 修正 PEP 8 違規
**練習 2**: 為函式撰寫 docstring
**練習 3**: 加入 type hints

### 04-exercises.ipynb 內容（10 題）

**基礎題（1-5）**
1. 找出並修正 PEP 8 違規
2. 為 5 個函式撰寫 docstring
3. 重新命名不符合規範的變數
4. 加入適當的空行與註解
5. 使用 type hints 標註型態

**中級題（6-8）**
6. 重構一段不良程式碼
7. 撰寫符合 Google Style 的 docstring
8. 使用 flake8 檢查並修正錯誤

**挑戰題（9-10）**
9. 為完整類別撰寫文件
10. 建立專案風格指南文件

### 05-solutions.ipynb 內容
完整解答

### quiz.ipynb 內容

**選擇題（10 題）**
關於 PEP 8, docstring, type hints

**簡答題（3 題）**
1. 說明 PEP 8 的三個重要規範
2. docstring 應該包含哪些內容？
3. type hints 的好處是什麼？

**程式題（2 題）**
1. 重構不良程式碼
2. 為類別撰寫完整文件

---

## 🔧 Ch30: 版本控制基礎

### README.md（待建立）

參考 Ch27/Ch28/Ch29 的結構，包含：
- 章節資訊（4 小時，中階難度）
- 學習目標（Git 基礎指令，commit，branch，GitHub）
- 核心概念（版本控制的必要性，Git 工作流程）
- 實作能力檢核
- 教學建議（常見困難：merge conflict，detached HEAD）

### 01-lecture.ipynb 內容大綱

**Part I: 理論基礎**
- 為什麼需要版本控制
- Git 的基本概念（repository, commit, branch）
- GitHub 與遠端協作

**Part II: 實作演練（5 個範例）**

**範例 1: Git 基礎操作**
```bash
# 初始化 Git 倉庫
git init

# 設定使用者資訊
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 查看狀態
git status

# 添加檔案到暫存區
git add file.py
git add .  # 添加所有變更

# 提交變更
git commit -m "Add feature"

# 查看歷史
git log
git log --oneline
git log --graph --all
```

**範例 2: .gitignore**
```bash
# .gitignore 範例
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/

# 虛擬環境
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp

# 系統檔案
.DS_Store
Thumbs.db

# 專案特定
config/secrets.py
*.log
data/
```

**範例 3: 分支操作**
```bash
# 查看分支
git branch

# 建立新分支
git branch feature-login

# 切換分支
git checkout feature-login
# 或使用新語法
git switch feature-login

# 建立並切換（一步完成）
git checkout -b feature-register

# 合併分支
git checkout main
git merge feature-login

# 刪除分支
git branch -d feature-login
```

**範例 4: 遠端操作（GitHub）**
```bash
# 複製遠端倉庫
git clone https://github.com/user/repo.git

# 查看遠端
git remote -v

# 添加遠端
git remote add origin https://github.com/user/repo.git

# 推送到遠端
git push origin main

# 從遠端拉取
git pull origin main

# 查看遠端分支
git branch -r
```

**範例 5: 常見情境處理**
```bash
# 撤銷工作區變更
git checkout -- file.py
# 或
git restore file.py

# 取消暫存
git reset HEAD file.py
# 或
git restore --staged file.py

# 修改最後一次 commit
git commit --amend

# 查看變更
git diff
git diff --staged

# 查看特定 commit
git show commit_hash
```

### 02-worked-examples.ipynb 內容

**範例 1: 建立 Git 專案**
```bash
# 步驟 1: 建立專案資料夾
mkdir myproject
cd myproject

# 步驟 2: 初始化 Git
git init

# 步驟 3: 建立檔案
echo "# My Project" > README.md
echo "print('Hello')" > main.py

# 步驟 4: 建立 .gitignore
cat > .gitignore << EOF
__pycache__/
venv/
*.pyc
EOF

# 步驟 5: 第一次提交
git add .
git commit -m "Initial commit"

# 步驟 6: 查看歷史
git log --oneline
```

**範例 2: 功能分支工作流程**
```bash
# 情境：開發新功能

# 1. 從 main 建立功能分支
git checkout -b feature-authentication

# 2. 開發功能（修改檔案）
echo "def login(): pass" >> auth.py
git add auth.py
git commit -m "Add login function"

# 3. 繼續開發
echo "def logout(): pass" >> auth.py
git add auth.py
git commit -m "Add logout function"

# 4. 切回 main 並合併
git checkout main
git merge feature-authentication

# 5. 刪除功能分支
git branch -d feature-authentication
```

**範例 3: 處理合併衝突**
```bash
# 情境：兩個分支修改同一檔案

# 分支 A 修改
git checkout -b branch-a
echo "Version A" > file.txt
git add file.txt
git commit -m "Update from branch A"

# 分支 B 修改
git checkout main
git checkout -b branch-b
echo "Version B" > file.txt
git add file.txt
git commit -m "Update from branch B"

# 合併時發生衝突
git checkout main
git merge branch-a  # 成功
git merge branch-b  # 衝突!

# 解決衝突
# 1. 編輯 file.txt，選擇要保留的版本
# 2. git add file.txt
# 3. git commit -m "Resolve merge conflict"
```

### 03-practice.ipynb 內容

**練習 1**: 初始化 Git 專案並提交
**練習 2**: 建立分支並合併
**練習 3**: 建立 .gitignore

### 04-exercises.ipynb 內容（10 題）

**基礎題（1-5）**
1. 初始化 Git 倉庫並提交第一個檔案
2. 建立 .gitignore 忽略 Python 相關檔案
3. 建立新分支並切換
4. 查看 commit 歷史
5. 撤銷工作區變更

**中級題（6-8）**
6. 使用分支開發新功能並合併
7. 解決簡單的合併衝突
8. 修改 commit 訊息

**挑戰題（9-10）**
9. 建立完整的功能分支工作流程
10. 設定 GitHub 遠端並推送

### 05-solutions.ipynb 內容
完整解答

### quiz.ipynb 內容

**選擇題（10 題）**
關於 Git 指令與概念

**簡答題（3 題）**
1. 什麼是版本控制？為什麼需要？
2. 說明 git add, git commit, git push 的差別
3. 如何解決合併衝突？

**實作題（2 題）**
1. 建立 Git 專案並提交多次
2. 使用分支開發並合併

---

## 🎯 實施步驟 (Implementation Steps)

### 步驟 1: 完成 README 檔案
- [x] Ch27 README.md
- [x] Ch28 README.md
- [ ] Ch29 README.md（重新命名 README_FULL.md）
- [ ] Ch30 README.md（參考上方內容建立）

### 步驟 2: 生成 Jupyter Notebooks
使用以下兩種方式之一：

**方式 A: 手動建立**
1. 開啟 Jupyter Notebook
2. 按照本指南的內容大綱建立各檔案
3. 確保每個範例可執行
4. 加入詳細的中文註解

**方式 B: 使用 Python 腳本**
1. 執行 `python generate_ch27_30_content.py`
2. 在生成的基礎上補充完整內容
3. 測試所有程式碼

### 步驟 3: 品質檢核
每個檔案完成後檢查：
- [ ] 程式碼可執行無誤
- [ ] 包含足夠的範例（lecture 至少 5 個）
- [ ] 習題符合難度分級（基礎/中級/挑戰）
- [ ] 中文說明清晰易懂
- [ ] 符合 Ch01 的品質標準

### 步驟 4: 最終確認
- [ ] 所有 28 個檔案已建立
- [ ] 通過自我測驗
- [ ] 內容連貫性檢查
- [ ] 錯字與格式檢查

---

## 📊 進度追蹤表 (Progress Tracker)

| 章節 | README | Lecture | Examples | Practice | Exercises | Solutions | Quiz | 總進度 |
|:-----|:------:|:-------:|:--------:|:--------:|:---------:|:---------:|:----:|:------:|
| Ch27 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | 14% |
| Ch28 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | 14% |
| Ch29 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | 14% |
| Ch30 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | 0% |
| **總計** | **3/4** | **0/4** | **0/4** | **0/4** | **0/4** | **0/4** | **0/4** | **10.7%** |

---

## 💡 開發建議 (Development Tips)

### 內容品質標準
1. **程式碼**：
   - 必須可執行
   - 包含完整註解
   - 符合 PEP 8
   - 錯誤處理完善

2. **說明文字**：
   - 使用繁體中文
   - 專業術語標註英文
   - 由淺入深
   - 包含 First Principles 分析

3. **範例設計**：
   - 貼近實際應用
   - 循序漸進
   - 包含常見錯誤示範
   - 提供多個角度說明

### 時間估算
- README：每章 2 小時
- 01-lecture：每章 4 小時
- 02-examples：每章 2 小時
- 03-practice：每章 1 小時
- 04-exercises：每章 3 小時
- 05-solutions：每章 2 小時
- quiz：每章 1 小時

**總計**：每章約 15 小時 × 4 章 = **60 小時**

---

## 🔄 持續改進 (Continuous Improvement)

完成初版後：
1. 邀請學習者測試
2. 收集回饋意見
3. 修正錯誤與不清楚的說明
4. 補充延伸資源
5. 更新版本記錄

---

**文件版本**: v1.0 (2025-10-05)
**最後更新**: Claude (Anthropic)
**授權**: 與主專案相同

---

**使用提醒**: 本指南提供完整的內容架構與範例，實際開發時請根據需求調整細節。重點是確保每個檔案都達到 Ch01 的教學品質標準！
