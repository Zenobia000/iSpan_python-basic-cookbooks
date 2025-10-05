# Chapter 27: 自訂模組與套件 | Custom Modules and Packages

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Chapter 12 (函式), Chapter 16 (類別), Chapter 23 (檔案操作) |
| **相關章節** | Chapter 28 (套件管理), Chapter 30 (版本控制) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠:

### 知識面（Knowledge）
- **列出** 模組與套件的差異與層級關係
- **定義** `__name__`, `__init__.py`, `__all__` 的作用
- **說明** Python 的模組搜尋路徑（sys.path）機制

### 理解面（Comprehension）
- **解釋** 為什麼需要模組化程式設計
- **比較** 絕對匯入與相對匯入的使用時機
- **歸納** 循環匯入（circular import）問題的成因

### 應用面（Application）
- **運用** import 語句的多種形式（import, from, as）
- **實作** 可重用的自訂模組與套件結構
- **解決** 模組命名空間衝突的問題

### 分析面（Analysis）
- **分析** 專案的模組化拆分策略
- **診斷** 匯入錯誤（ImportError, ModuleNotFoundError）
- **選擇** 適合專案規模的套件組織方式

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
自訂模組與套件
├── 模組（Module）
│   ├── .py 檔案即為模組
│   ├── import 匯入機制
│   ├── __name__ 特殊變數
│   └── 模組搜尋路徑（sys.path）
│
├── 套件（Package）
│   ├── 包含 __init__.py 的資料夾
│   ├── 子套件結構
│   ├── 絕對匯入 vs 相對匯入
│   └── __all__ 控制匯出
│
└── 最佳實務
    ├── 單一職責原則
    ├── 避免循環匯入
    └── if __name__ == "__main__" 慣用法
```

### First Principles 解析

#### 為什麼需要模組？
**根本問題**: 所有程式碼寫在單一檔案會造成:
- 難以維護（程式碼超過數百行）
- 難以重用（功能無法在其他專案使用）
- 難以協作（多人編輯同一檔案易衝突）

**最小實作**:
```python
# math_utils.py (模組)
def add(a, b):
    return a + b

# main.py (使用模組)
import math_utils
print(math_utils.add(3, 5))  # 8
```

**推導過程**:
1. 程式碼需要組織 → 拆分成多個檔案
2. 檔案需要協作 → 定義匯入機制
3. 匯入需要識別 → Python 把每個 .py 視為模組

#### 為什麼需要套件？
**根本問題**: 模組數量增加後需要階層式組織

**實例說明**:
```
專案結構
├── main.py
└── utils/          # 套件（資料夾）
    ├── __init__.py # 標記為套件
    ├── math.py     # 子模組
    └── string.py   # 子模組
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 模組 | Module | 單一 .py 檔案,包含 Python 定義與陳述 |
| 套件 | Package | 包含 `__init__.py` 的資料夾,組織多個模組 |
| 匯入 | Import | 將其他模組的功能引入當前命名空間 |
| 命名空間 | Namespace | 變數名稱的作用域,避免名稱衝突 |
| 絕對匯入 | Absolute Import | 從專案根目錄開始的完整路徑匯入 |
| 相對匯入 | Relative Import | 基於當前模組位置的相對路徑匯入 |
| 模組搜尋路徑 | Module Search Path | Python 尋找模組的目錄列表（sys.path） |
| 循環匯入 | Circular Import | 兩個模組互相匯入導致的錯誤 |

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
1. **預習**（30 min）: 閱讀本 README,了解模組概念
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
- [ ] 能建立自訂模組（.py 檔案）並在其他檔案匯入
- [ ] 能使用 import, from...import, import...as 三種語法
- [ ] 能理解 `__name__ == "__main__"` 的用途
- [ ] 能查看模組的屬性與函式（dir(), help()）

### 進階能力
- [ ] 能建立套件結構（含 `__init__.py`）
- [ ] 能使用絕對匯入與相對匯入
- [ ] 能設定 `__all__` 控制模組匯出內容
- [ ] 能理解並修改 sys.path 模組搜尋路徑

### 應用能力
- [ ] 能將大型專案拆分成合理的模組結構
- [ ] 能診斷並解決 ImportError, ModuleNotFoundError
- [ ] 能避免循環匯入問題
- [ ] 能建立可在其他專案重用的工具模組

---

## 📝 理論重點（Key Theoretical Points）

### 1. 模組的本質
```python
# 每個 .py 檔案都是一個模組
# utils.py
PI = 3.14159
def circle_area(radius):
    return PI * radius ** 2

# main.py
import utils
print(utils.PI)              # 3.14159
print(utils.circle_area(5))  # 78.53975
```

### 2. import 的三種形式
| 語法 | 範例 | 使用時機 | 命名空間 |
|:-----|:-----|:---------|:---------|
| `import` | `import math` | 匯入整個模組 | `math.sqrt(4)` |
| `from...import` | `from math import sqrt` | 匯入特定函式 | `sqrt(4)` |
| `import...as` | `import numpy as np` | 避免名稱衝突 | `np.array([1,2])` |

### 3. `__name__` 特殊變數
```python
# utils.py
def greet():
    print("Hello from utils!")

# 當模組直接執行時: __name__ == "__main__"
# 當模組被匯入時: __name__ == "utils"
if __name__ == "__main__":
    greet()  # 只在直接執行時呼叫
```

### 4. 套件結構範例
```
myproject/
├── main.py
└── mypackage/
    ├── __init__.py      # 標記為套件
    ├── module1.py
    ├── module2.py
    └── subpackage/
        ├── __init__.py
        └── module3.py
```

```python
# 絕對匯入
from mypackage.module1 import func1
from mypackage.subpackage.module3 import func3

# 相對匯入（在套件內部使用）
from . import module2         # 同層級
from .subpackage import module3  # 子套件
from .. import module1        # 上層級
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **從實際需求出發**:
   - 先展示單一檔案專案的問題（程式碼超過 500 行）
   - 再示範模組化拆分的好處

2. **視覺化套件結構**:
   - 使用檔案總管實際展示資料夾與檔案
   - 強調 `__init__.py` 的必要性（Python 3.3+ 可省略,但建議保留）

3. **實際操作演示**:
   - 在 Jupyter 中使用 `%%writefile` 建立模組檔案
   - 示範 `importlib.reload()` 重新載入已修改的模組

### 常見學生困難點

#### 困難點 1: ModuleNotFoundError
**症狀**: 明明檔案存在,卻無法匯入

**解決方法**:
```python
# 檢查模組搜尋路徑
import sys
print(sys.path)

# 手動加入路徑（臨時方案）
sys.path.append('/path/to/module')

# 正確做法: 使用套件結構或調整工作目錄
```

#### 困難點 2: 混淆絕對匯入與相對匯入
**症狀**: 不知道何時用 `import pkg.module` vs `from . import module`

**原則**:
- **絕對匯入**: 在套件外部使用,路徑清晰明確
- **相對匯入**: 在套件內部使用,增加可移植性

#### 困難點 3: 循環匯入
**症狀**: `ImportError: cannot import name 'X' from partially initialized module`

**避免方法**:
```python
# 錯誤示範
# a.py
from b import func_b

# b.py
from a import func_a  # 循環匯入!

# 解決方案 1: 延遲匯入（在函式內部）
# a.py
def my_func():
    from b import func_b
    func_b()

# 解決方案 2: 重構程式碼,避免雙向依賴
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **Module = File**: 一個 .py 檔案就是一個模組
- **Package = Folder**: 有 `__init__.py` 的資料夾就是套件
- **Import 三劍客**: import, from...import, import...as

### 實作練習建議
1. **模組拆分練習**: 選一個舊專案,嘗試拆分成 3-5 個模組
2. **套件建立練習**: 建立自己的工具套件（如 myutils）
3. **除錯練習**: 故意製造 ImportError,練習查錯技巧

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [The import system](https://docs.python.org/3/reference/import.html)

### 推薦閱讀
- Real Python: [Python Modules and Packages](https://realpython.com/python-modules-packages/)
- PEP 8: [Package and Module Names](https://peps.python.org/pep-0008/#package-and-module-names)

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化模組匯入過程
- [Import Linter](https://import-linter.readthedocs.io/) - 檢查匯入規則

### 延伸主題（進階學習）
- `importlib` 動態匯入
- `__init__.py` 的進階用法
- 命名空間套件（Namespace Packages, PEP 420）
- 打包發布自訂套件（setuptools, pyproject.toml）

---

## ❓ 常見問題（FAQ）

**Q1: `__init__.py` 一定要存在嗎?**
A: Python 3.3+ 引入 Namespace Packages,可以省略。但建議保留,明確標記為套件,且可在其中初始化套件。

**Q2: 什麼時候用 `from module import *`?**
A: 幾乎不應該用！會污染命名空間,且不清楚匯入了什麼。例外: 互動式測試時可用。

**Q3: 如何處理模組名稱與標準庫衝突?**
A: 1) 重新命名自訂模組 2) 使用 `import ... as` 別名 3) 避免使用常見標準庫名稱（如 math, random）

**Q4: 相對匯入的 `.` 和 `..` 是什麼意思?**
A: `.` 表示當前套件, `..` 表示上層套件,類似檔案系統的 `./` 和 `../`。

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 12（函式）**: 模組主要匯出函式
- **Chapter 16（類別）**: 模組也可匯出類別
- **Chapter 23（檔案操作）**: 理解檔案路徑有助於模組組織

### 後續章節
- **Chapter 28（套件管理）**: 安裝與管理第三方套件
- **Chapter 30（版本控制）**: Git 管理多檔案專案

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
- ✅ 能建立包含 3 個以上模組的專案結構
- ✅ 能在 10 分鐘內診斷並修正 ImportError

---

**學習提醒**: 模組化是軟體工程的核心技能。請務必動手建立實際的專案結構,而非只閱讀範例！
