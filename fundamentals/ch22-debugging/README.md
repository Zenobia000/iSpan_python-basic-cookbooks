# Ch22: 除錯技術 | Debugging Techniques

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3.5 小時（2 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Ch20 (例外處理), Ch21 (自訂例外), 基本程式除錯經驗 |
| **相關章節** | 參見 Ch27 (測試), Ch23 (檔案 I/O), Ch12 (函式) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** 除錯的主要方法：print debugging, logging, pdb, IDE debugger
- **定義** logging 的五個級別：DEBUG, INFO, WARNING, ERROR, CRITICAL
- **說明** pdb 除錯器的常用指令：n, s, c, p, l, w, q

### 理解面（Comprehension）
- **解釋** 為什麼需要系統化除錯（效率、可重現性、科學方法）
- **比較** print debugging vs logging vs pdb 的優缺點與適用情境
- **歸納** 科學除錯法的四個步驟：重現 → 隔離 → 假設 → 驗證

### 應用面（Application）
- **運用** logging 模組記錄不同層級的訊息
- **實作** 使用 pdb 設定中斷點、單步執行、檢視變數
- **解決** 使用 breakpoint() 動態插入除錯點

### 分析面（Analysis）
- **分析** 錯誤訊息（traceback）找出問題根源
- **診斷** 複雜程式的邏輯錯誤（不會崩潰但結果錯誤）
- **選擇** 針對不同錯誤類型採用最有效的除錯策略

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
除錯技術 (Debugging Techniques)
│
├── 為何需要除錯？(WHY)
│   ├── 提高問題定位效率 (Efficiency)
│   ├── 建立可重現的除錯流程 (Reproducibility)
│   ├── 採用科學方法而非猜測 (Scientific Method)
│   └── 減少除錯時間成本 (Cost Reduction)
│
├── 除錯方法 (Debugging Methods)
│   ├── Print Debugging
│   │   ├── 插入 print() 追蹤變數
│   │   ├── 優點：簡單直覺
│   │   └── 缺點：侵入性、需手動移除
│   │
│   ├── Logging 模組
│   │   ├── DEBUG (詳細診斷資訊)
│   │   ├── INFO (一般資訊)
│   │   ├── WARNING (警告訊息)
│   │   ├── ERROR (錯誤訊息)
│   │   ├── CRITICAL (嚴重錯誤)
│   │   └── 優點：分級、可控、可保存
│   │
│   ├── pdb 除錯器
│   │   ├── 設定中斷點 (breakpoint, set_trace)
│   │   ├── 單步執行 (n, s, c)
│   │   ├── 檢視變數 (p, pp)
│   │   ├── 檢視堆疊 (w, u, d)
│   │   └── 優點：互動式、全功能
│   │
│   └── IDE 除錯器
│       ├── 視覺化中斷點
│       ├── 變數監看視窗
│       └── 呼叫堆疊視圖
│
├── 錯誤類型 (Error Types)
│   ├── 語法錯誤 (Syntax Errors) - 編譯時期
│   ├── 執行時期錯誤 (Runtime Errors) - 例外
│   ├── 邏輯錯誤 (Logic Errors) - 最難除錯
│   └── 效能問題 (Performance Issues)
│
└── 科學除錯法 (Scientific Debugging)
    ├── 1. 重現 (Reproduce) - 建立最小測試案例
    ├── 2. 隔離 (Isolate) - 縮小問題範圍
    ├── 3. 假設 (Hypothesize) - 提出可能原因
    └── 4. 驗證 (Validate) - 測試假設並修正
```

---

## 🔬 First Principles 第一性原理

### 1. 為何需要系統化除錯？

**問題**：程式出錯時，如何快速找到問題並修正？

**傳統做法** (無系統化除錯)：
```python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# 使用時出現 ZeroDivisionError，但不知道為什麼
result = calculate_average([])  # 崩潰！
```

**常見除錯方式**（缺乏效率）：
- **猜測法**：「應該是這裡錯了吧？」→ 改了又改，越改越亂
- **亂槍打鳥**：到處加 print()，最後忘記移除
- **重新開始**：看不懂自己的程式碼，乾脆重寫

**系統化除錯** (科學方法)：
```python
import logging

logging.basicConfig(level=logging.DEBUG)

def calculate_average(numbers):
    logging.debug(f"計算平均值，輸入: {numbers}")

    if len(numbers) == 0:
        logging.warning("輸入列表為空，返回 0")
        return 0

    total = sum(numbers)
    avg = total / len(numbers)
    logging.info(f"計算完成，平均值: {avg}")
    return avg

result = calculate_average([])  # 有警告但不會崩潰
```

**優點**：
- **可追蹤**：所有訊息都有記錄
- **可分級**：開發時顯示 DEBUG，生產環境只顯示 ERROR
- **可保存**：寫入檔案以供事後分析
- **可控制**：不需修改程式碼即可調整記錄級別

---

### 2. Print Debugging vs Logging：為何需要升級？

**Print Debugging 的限制**：

```python
def process_data(data):
    print(f"DEBUG: data = {data}")  # 問題 1: 侵入性
    result = transform(data)
    print(f"DEBUG: result = {result}")  # 問題 2: 混雜在正常輸出中
    return result

# 發布時要手動移除所有 print，容易遺漏
# 無法控制顯示級別（全顯示或全不顯示）
```

**Logging 的改進**：

```python
import logging

logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"data = {data}")  # 不侵入正常輸出
    result = transform(data)
    logger.debug(f"result = {result}")
    return result

# 發布時只需調整級別
logging.basicConfig(level=logging.WARNING)  # 自動過濾 DEBUG
```

**核心差異**：
| 特性 | print() | logging |
|:-----|:--------|:--------|
| 輸出目標 | 固定 stdout | 可設定（檔案、網路、email） |
| 分級控制 | 無 | 5 個級別 |
| 時間戳記 | 需手動加 | 自動產生 |
| 效能影響 | 無法關閉 | 可完全停用 |
| 多執行緒 | 不安全 | 執行緒安全 |

---

### 3. pdb 除錯器：互動式探索

**問題**：變數太多、邏輯複雜時，print 和 logging 都不夠用

**pdb 的核心能力**：
```python
def buggy_function(n):
    result = 0
    for i in range(n):
        breakpoint()  # Python 3.7+ 內建中斷點
        result += i * 2
    return result

buggy_function(5)
```

**執行後進入 pdb 互動模式**：
```
> buggy_function(5)
-> result += i * 2
(Pdb) p i          # 印出變數 i
0
(Pdb) p result     # 印出變數 result
0
(Pdb) n            # 執行下一行
(Pdb) p result     # 再次檢查
0
(Pdb) c            # 繼續執行直到下個中斷點
```

**pdb 常用指令**：
| 指令 | 全名 | 功能 | 使用時機 |
|:-----|:-----|:-----|:---------|
| `n` | next | 執行下一行（不進入函式） | 單步執行 |
| `s` | step | 執行下一行（進入函式） | 追蹤函式內部 |
| `c` | continue | 繼續執行直到下個中斷點 | 快速跳過已確認區域 |
| `p` | print | 印出變數值 | 檢視狀態 |
| `pp` | pprint | 美化印出（字典、列表） | 檢視複雜資料 |
| `l` | list | 顯示當前程式碼位置 | 確認執行位置 |
| `w` | where | 顯示呼叫堆疊 | 追蹤函式呼叫鏈 |
| `u` | up | 移到上層堆疊 | 檢視呼叫來源 |
| `d` | down | 移到下層堆疊 | 回到當前執行點 |
| `q` | quit | 離開除錯器 | 結束除錯 |

---

### 4. 科學除錯法：四步驟系統化流程

**Step 1: 重現（Reproduce）**
- **目標**：建立最小可重現測試案例（Minimal Reproducible Example, MRE）
- **方法**：
  1. 記錄錯誤發生的確切條件
  2. 移除不相關的程式碼
  3. 固定輸入資料

```python
# 原始複雜程式 (500 行)
def complex_system():
    # ... 大量程式碼 ...
    result = buggy_function(data)
    # ... 更多程式碼 ...

# 最小重現案例 (5 行)
def test_bug():
    data = [1, 2, 3]  # 固定輸入
    result = buggy_function(data)
    print(result)  # 觀察錯誤
```

**Step 2: 隔離（Isolate）**
- **目標**：縮小問題範圍，找出「最後一行正確的程式碼」
- **方法**：二分搜尋法

```python
def process():
    step1()  # ✓ 正確
    step2()  # ✓ 正確
    step3()  # ✗ 錯誤 ← 問題出在這裡
    step4()
    step5()
```

**Step 3: 假設（Hypothesize）**
- **目標**：提出可能原因（不是猜測，是根據證據）
- **方法**：
  1. 檢查錯誤訊息（traceback）
  2. 檢查輸入資料的邊界情況
  3. 檢查假設前提是否成立

```python
# 假設：「可能是除以零」
def calculate(a, b):
    return a / b  # 如果 b=0 會出錯

# 驗證假設
print(f"b 的值：{b}")  # 確認 b 是否為 0
```

**Step 4: 驗證（Validate）**
- **目標**：測試假設並修正
- **方法**：
  1. 加入檢查機制
  2. 執行測試
  3. 確認修正有效

```python
# 修正方案
def calculate(a, b):
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b

# 驗證修正
try:
    result = calculate(10, 0)
except ValueError as e:
    print(f"成功捕捉錯誤：{e}")  # ✓ 修正有效
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 除錯 | Debugging | 找出並修正程式錯誤的過程 |
| 中斷點 | Breakpoint | 程式執行暫停的位置，用於檢查狀態 |
| 堆疊追蹤 | Stack Trace / Traceback | 錯誤發生時的函式呼叫序列記錄 |
| 單步執行 | Step Execution | 逐行執行程式碼以觀察行為 |
| 日誌記錄 | Logging | 記錄程式執行過程的訊息 |
| 最小重現案例 | Minimal Reproducible Example | 能重現錯誤的最簡化程式碼 |
| 隔離 | Isolation | 縮小問題範圍的過程 |
| 語法錯誤 | Syntax Error | 違反 Python 語法規則的錯誤 |
| 執行時期錯誤 | Runtime Error | 程式執行時發生的錯誤（例外） |
| 邏輯錯誤 | Logic Error | 程式可執行但結果不正確的錯誤 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示（6 個範例） | 80 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（4 個完整除錯案例） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（8 題找錯並修正） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（12 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 + 除錯思路 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（15 選擇 + 5 程式） | 30 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解除錯的系統化方法
2. **上課**（120 min）：
   - 講義學習（80 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（90 min）：
   - 完成習題（60 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（30 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能使用 print() 追蹤變數值
- [ ] 能設定 logging 的基本配置
- [ ] 能使用 breakpoint() 或 pdb.set_trace() 設定中斷點
- [ ] 能讀懂 Python 的 traceback 錯誤訊息

### 進階能力
- [ ] 能使用 logging 的五個級別記錄不同類型訊息
- [ ] 能在 pdb 中使用 n, s, c, p, l, w 指令
- [ ] 能建立最小重現案例（MRE）
- [ ] 能使用二分法隔離問題範圍

### 應用能力
- [ ] 能除錯遞迴函式的邏輯錯誤
- [ ] 能除錯多層函式呼叫的問題
- [ ] 能根據錯誤類型選擇適當的除錯方法
- [ ] 能撰寫完整的除錯報告（重現步驟、原因、修正方案）

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從痛苦經驗切入**：
   - 展示一個有 bug 的程式，問學生如何找錯
   - 讓學生體驗「亂加 print」的無效率
   - 引出系統化除錯的必要性

2. **漸進式教學**：
   - 第 1 階段：print debugging（簡單但有限）
   - 第 2 階段：logging（專業但需學習）
   - 第 3 階段：pdb（強大但需熟悉指令）

3. **實際操作演示**：
   - 使用投影螢幕即時示範 pdb 除錯流程
   - 讓學生看到「中斷點 → 檢視變數 → 單步執行」的完整過程

### 常見學生困難點

#### 困難點 1：不知從何開始除錯
**症狀**：面對錯誤程式碼毫無頭緒，只能猜測

**解決方法**：
- 教導「科學除錯法四步驟」
- 要求學生填寫除錯表格：

  | 步驟 | 內容 |
  |:-----|:-----|
  | 重現 | 輸入什麼資料會出錯？ |
  | 隔離 | 哪一行程式碼有問題？ |
  | 假設 | 可能的原因是什麼？ |
  | 驗證 | 修正後是否解決？ |

**練習案例**：
```python
# 給學生一個有 bug 的程式，要求填寫除錯表格
def factorial(n):
    result = 1
    for i in range(n):  # Bug: range(n) 不包含 n
        result *= i
    return result

print(factorial(5))  # 期望 120，實際得到 0
```

#### 困難點 2：過度依賴 print
**症狀**：到處加 print()，最後程式變成一堆除錯訊息

**解決方法**：
- 展示 print 的缺點：
  ```python
  # 不良示範
  def complex_function(data):
      print(f"1. data = {data}")
      step1 = process(data)
      print(f"2. step1 = {step1}")
      step2 = transform(step1)
      print(f"3. step2 = {step2}")
      # ... 20 行 print ...
  ```

- 改用 logging：
  ```python
  # 良好示範
  import logging
  logger = logging.getLogger(__name__)

  def complex_function(data):
      logger.debug(f"data = {data}")
      step1 = process(data)
      logger.debug(f"step1 = {step1}")
      # 發布時設定 level=INFO，自動隱藏所有 DEBUG
  ```

#### 困難點 3：不會用 pdb 除錯器
**症狀**：進入 pdb 後不知道該用什麼指令

**解決方法**：
- **口訣教學**：「查看用 p，前進用 n，進入用 s，跳過用 c」
- **製作指令卡**：
  ```
  ╔════════════════════════════╗
  ║  pdb 除錯器指令速查表      ║
  ╠════════════════════════════╣
  ║ p 變數名    → 查看變數     ║
  ║ n          → 下一行        ║
  ║ s          → 進入函式      ║
  ║ c          → 繼續執行      ║
  ║ l          → 顯示程式碼    ║
  ║ q          → 離開          ║
  ╚════════════════════════════╝
  ```

- **互動練習**：
  ```python
  # 課堂練習：要求學生使用 pdb 找出錯誤
  def mystery_bug(numbers):
      total = 0
      for i in range(len(numbers)):
          breakpoint()  # 在這裡暫停
          total += numbers[i] * 2
      return total / len(numbers)  # Bug: 除以長度
  ```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **pdb 指令**：「**p**rint 查看，**n**ext 前進，**s**tep 深入，**c**ontinue 跳過」
- **logging 級別**：「**D**ebug 細節，**I**nfo 資訊，**W**arning 警告，**E**rror 錯誤，**C**ritical 致命」
- **除錯流程**：「**重**現問題，**隔**離範圍，**假**設原因，**驗**證修正」

### 實作練習建議
1. **刻意練習 pdb**：每天用 pdb 除錯一個小程式（即使沒有 bug）
2. **建立除錯筆記**：記錄遇到的錯誤類型與解決方法
3. **挑戰題**：找開源專案的 issue，嘗試除錯並提交修正

### 除錯技巧集錦
```python
# 技巧 1: 使用 f-string 追蹤變數
x = 10
print(f"{x=}")  # Python 3.8+，輸出：x=10

# 技巧 2: 使用 pprint 美化輸出
from pprint import pprint
data = {"key": [1, 2, 3], "nested": {"a": 1}}
pprint(data)  # 格式化顯示

# 技巧 3: 使用 traceback 模組
import traceback
try:
    buggy_function()
except Exception:
    traceback.print_exc()  # 印出完整 traceback

# 技巧 4: 使用 sys.exit() 快速測試
import sys
print("測試到這裡")
sys.exit()  # 立即停止，檢查前面的輸出

# 技巧 5: 使用 assert 檢查假設
def process(data):
    assert len(data) > 0, "資料不可為空"  # 假設檢查
    return data[0]
```

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [pdb — The Python Debugger](https://docs.python.org/3/library/pdb.html)
- [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
- [traceback — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)

### 推薦閱讀
- Zeller, A. (2009). *Why Programs Fail: A Guide to Systematic Debugging* (2nd ed.)
- Spinellis, D. (2006). *Code Debugging* in *Code Quality*
- *Python Cookbook* (3rd ed.), Chapter 14: Testing, Debugging, and Exceptions

### 互動式工具
- [Python Tutor](http://pythontutor.com/) - 視覺化程式執行流程
- [Replit](https://replit.com/) - 線上 Python 環境（支援除錯）

### 延伸主題（進階學習）
- **pytest 除錯**：使用 pytest --pdb 在測試失敗時自動進入除錯器
- **remote debugging**：遠端除錯技術（pdb over network）
- **profiling**：效能分析工具（cProfile, line_profiler）
- **memory debugging**：記憶體洩漏檢測（tracemalloc, memory_profiler）

---

## ❓ 常見問題（FAQ）

**Q1: print debugging 和 logging 該如何選擇？**
A:
- **開發階段**：print() 適合快速測試（寫完記得刪除）
- **長期維護**：logging 適合保留在程式碼中（可控制顯示級別）
- **經驗法則**：如果這段除錯程式碼未來可能還需要，就用 logging

**Q2: 為什麼進入 pdb 後按 n 沒反應？**
A: 可能是變數名稱與 pdb 指令衝突（如變數名為 `n`），使用 `!n` 強制執行指令：
```python
(Pdb) n = 10      # 設定變數 n
(Pdb) n           # 這會被當作 next 指令
(Pdb) !n          # 強制印出變數 n
```

**Q3: logging 的訊息沒有顯示怎麼辦？**
A: 檢查 logging 級別設定：
```python
import logging

# 預設級別是 WARNING，DEBUG 和 INFO 不會顯示
logging.debug("這不會顯示")

# 解決方法：設定級別為 DEBUG
logging.basicConfig(level=logging.DEBUG)
logging.debug("現在會顯示了")
```

**Q4: 如何在不修改程式碼的情況下使用 pdb？**
A: 使用命令列參數：
```bash
# 方法 1: 使用 -m pdb
python -m pdb script.py

# 方法 2: 設定環境變數 PYTHONBREAKPOINT
export PYTHONBREAKPOINT=pdb.set_trace
python script.py  # breakpoint() 會自動使用 pdb
```

**Q5: 除錯遞迴函式時，pdb 進入太多次中斷點怎麼辦？**
A: 使用條件中斷點：
```python
def factorial(n):
    if n == 3:  # 只在 n=3 時中斷
        breakpoint()
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 20（例外處理）**：理解 try-except 與錯誤處理
- **Chapter 21（自訂例外）**：認識例外的階層架構
- **Chapter 12（函式）**：理解函式呼叫堆疊

### 後續章節
- **Chapter 27（測試）**：單元測試與 TDD（測試驅動開發）
- **Chapter 23（檔案 I/O）**：除錯檔案操作的常見問題
- **Milestone 6**：結合例外處理與除錯技術

### 對應的 Milestone 專案
- **Milestone 6: 使用者註冊系統**（結合 Ch20-22，處理輸入驗證與錯誤除錯）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，基於教科書標準結構
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能在 10 分鐘內使用 pdb 找出一個中等複雜度的邏輯錯誤
- ✅ 能設計一個完整的 logging 架構（包含檔案輸出與級別控制）
- ✅ 能向他人解釋科學除錯法的四個步驟

---

**學習提醒**：除錯是程式設計師最重要的技能之一！優秀的程式設計師不是不寫 bug，而是能快速找到並修正 bug。請確實練習每一個除錯工具！
