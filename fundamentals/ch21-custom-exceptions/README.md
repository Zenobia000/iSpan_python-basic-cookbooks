# Chapter 21: 自訂例外與 raise | Custom Exceptions and raise

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中級) |
| **先備知識** | Chapter 20 (例外處理基礎), Chapter 16 (類別基礎) |
| **相關章節** | 參見 Chapter 22 (除錯技術), Chapter 16 (物件導向) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠：

### 知識面（Knowledge）
- **列出** Python 中拋出例外的方法：raise、assert
- **定義** 自訂例外類別的結構與繼承關係
- **說明** 例外鏈（exception chaining）的概念

### 理解面（Comprehension）
- **解釋** 為什麼需要自訂例外類別
- **比較** raise 與 assert 的差異與應用場景
- **歸納** 例外類別的命名與組織規範

### 應用面（Application）
- **運用** raise 主動拋出例外
- **實作** 自訂的例外類別階層
- **解決** 業務邏輯中的錯誤處理需求

### 分析面（Analysis）
- **分析** 何時應使用內建例外 vs 自訂例外
- **診斷** 例外鏈中的錯誤追蹤路徑
- **設計** 符合專案需求的例外系統

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
自訂例外與 raise
├── 主動拋出例外（raise）
│   ├── raise 基本語法
│   ├── 重新拋出例外（re-raise）
│   └── 例外鏈（raise...from）
│
├── 自訂例外類別
│   ├── 繼承 Exception
│   ├── 添加自訂屬性
│   └── 例外階層設計
│
└── 斷言（assert）
    ├── assert 語法
    ├── AssertionError
    └── 除錯 vs 錯誤處理
```

### First Principles 解析

#### 為什麼要主動拋出例外（raise）？
**根本問題**：程式需要在檢測到錯誤時立即停止執行，並通知上層處理

**最小實作**：
```python
def divide(a, b):
    if b == 0:
        raise ValueError("除數不能為 0")
    return a / b
```

**推導過程**：
1. 檢測到無效狀態（b == 0）→ 需要中斷執行
2. 需要傳遞錯誤資訊 → 使用例外物件
3. 觸發例外機制 → raise 關鍵字

#### 為什麼需要自訂例外？
**根本問題**：內建例外無法精確表達業務邏輯的錯誤類型

**實例說明**：
```python
# 使用內建例外（語意不明確）
if balance < amount:
    raise ValueError("餘額不足")

# 使用自訂例外（語意清晰）
if balance < amount:
    raise InsufficientFundsError(account_id, balance, amount)
```

**自訂例外的三大優勢**：
1. **語意清晰**：一看類別名稱就知道錯誤類型
2. **錯誤分類**：可以建立例外階層，分層處理
3. **攜帶資訊**：可添加自訂屬性，提供更多上下文

#### 為什麼需要例外鏈（Exception Chaining）？
**根本問題**：處理例外時，需要保留原始錯誤的完整資訊

**實例說明**：
```python
# 沒有例外鏈（遺失原始錯誤資訊）
try:
    data = json.loads(text)
except JSONDecodeError:
    raise ValidationError("資料格式錯誤")  # 遺失 JSON 錯誤細節

# 使用例外鏈（保留完整錯誤追蹤）
try:
    data = json.loads(text)
except JSONDecodeError as e:
    raise ValidationError("資料格式錯誤") from e  # 保留原始錯誤
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 拋出例外 | Raise Exception | 主動觸發例外的行為 |
| 自訂例外 | Custom Exception | 繼承自 Exception 的使用者定義類別 |
| 例外鏈 | Exception Chaining | 將新例外與原始例外連結的機制（raise...from） |
| 斷言 | Assertion | 用於檢查程式假設的除錯工具（assert） |
| 重新拋出 | Re-raise | 在 except 區塊中再次拋出例外（raise） |
| 例外階層 | Exception Hierarchy | 例外類別的繼承樹狀結構 |
| 追蹤鏈 | Traceback Chain | 例外傳播的完整路徑記錄 |
| 斷言錯誤 | AssertionError | assert 失敗時拋出的例外 |

---

## 📚 教材內容（Course Materials）

### 檔案說明

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義（5 個範例） | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（3 個實務案例） | 40 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（6 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（10 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（12 選擇 + 5 程式） | 25 分鐘 | 學習驗收 |

### 學習流程建議
1. **預習**（30 min）：閱讀本 README，了解自訂例外的必要性
2. **上課**（100 min）：
   - 講義學習（60 min）：`01-lecture.ipynb`
   - 範例演練（40 min）：`02-worked-examples.ipynb`
3. **課堂練習**（30 min）：完成 `03-practice.ipynb`
4. **課後複習**（90 min）：
   - 完成習題（60 min）：`04-exercises.ipynb`
   - 對照解答（30 min）：`05-solutions.ipynb`
5. **自我測驗**（25 min）：`quiz.ipynb`

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 能使用 raise 拋出內建例外
- [ ] 能創建基本的自訂例外類別
- [ ] 能在 except 區塊中重新拋出例外
- [ ] 能使用 assert 進行條件檢查

### 進階能力
- [ ] 能為自訂例外添加屬性和方法
- [ ] 能使用 raise...from 建立例外鏈
- [ ] 能設計多層次的例外階層
- [ ] 能區分 assert 與 raise 的使用時機

### 應用能力
- [ ] 能根據業務邏輯設計合適的例外類別
- [ ] 能在例外中攜帶足夠的除錯資訊
- [ ] 能使用 __cause__ 和 __context__ 追蹤例外鏈
- [ ] 能撰寫清晰的例外處理文件

---

## 📝 理論重點（Key Theoretical Points）

### 1. raise 的三種用法

#### 用法一：拋出新例外
```python
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("提款金額不能為負數")
    if amount > balance:
        raise ValueError("餘額不足")
    return balance - amount
```

#### 用法二：重新拋出當前例外（在 except 中）
```python
try:
    risky_operation()
except Exception:
    log_error()
    raise  # 重新拋出相同的例外
```

#### 用法三：例外鏈（raise...from）
```python
try:
    data = json.loads(text)
except JSONDecodeError as e:
    raise DataError("無法解析資料") from e
```

### 2. 自訂例外的最佳實作

#### 命名規範
- ✅ 以 `Error` 或 `Exception` 結尾
- ✅ 使用描述性名稱：`InsufficientFundsError` 而非 `Error1`
- ✅ 遵循駝峰命名法（PascalCase）

#### 最小自訂例外
```python
class ValidationError(Exception):
    """資料驗證失敗時拋出"""
    pass
```

#### 攜帶資訊的自訂例外
```python
class InsufficientFundsError(Exception):
    """餘額不足時拋出"""

    def __init__(self, account_id, balance, amount):
        self.account_id = account_id
        self.balance = balance
        self.amount = amount
        message = f"帳戶 {account_id} 餘額不足：需要 {amount}，但只有 {balance}"
        super().__init__(message)
```

### 3. 例外階層設計

#### 銀行系統範例
```python
class BankError(Exception):
    """銀行系統例外的基底類別"""
    pass

class AccountError(BankError):
    """帳戶相關錯誤"""
    pass

class TransactionError(BankError):
    """交易相關錯誤"""
    pass

class InsufficientFundsError(TransactionError):
    """餘額不足"""
    pass

class InvalidAccountError(AccountError):
    """帳戶不存在或無效"""
    pass
```

**優勢**：可以分層捕獲
```python
try:
    bank.transfer(from_id, to_id, amount)
except InsufficientFundsError:
    # 處理餘額不足
    pass
except TransactionError:
    # 處理其他交易錯誤
    pass
except BankError:
    # 處理所有銀行錯誤
    pass
```

### 4. assert vs raise 的區別

| 特性 | assert | raise |
|:-----|:-------|:------|
| **用途** | 除錯檢查 | 錯誤處理 |
| **執行環境** | 開發/測試 | 所有環境 |
| **可被停用** | 是（-O 選項） | 否 |
| **例外類型** | AssertionError | 任意例外 |
| **使用場景** | 檢查內部假設 | 驗證外部輸入 |

```python
# ✅ assert 的正確用法（內部檢查）
def calculate_average(numbers):
    assert len(numbers) > 0, "內部錯誤：不應傳入空列表"
    return sum(numbers) / len(numbers)

# ✅ raise 的正確用法（外部驗證）
def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("無法計算空列表的平均值")
    return sum(numbers) / len(numbers)
```

### 5. 例外鏈的機制

#### 隱式鏈（__context__）
```python
try:
    1 / 0
except:
    raise ValueError("發生錯誤")
# 自動設定 __context__ 指向 ZeroDivisionError
```

#### 顯式鏈（__cause__）
```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("發生錯誤") from e
# 明確設定 __cause__ 指向原始例外
```

#### 抑制鏈
```python
try:
    1 / 0
except:
    raise ValueError("發生錯誤") from None
# from None 會抑制例外鏈
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點

1. **從內建例外的限制切入**：
   - 展示 ValueError 過於泛用的問題
   - 說明業務邏輯需要更精確的例外類型

2. **強調例外命名的重要性**：
   - 好的命名 = 自解釋的錯誤訊息
   - 壞的命名 = 需要查文件才懂

3. **實際操作演示**：
   - 展示例外鏈的 traceback
   - 對比有鏈與無鏈的差異

### 常見學生困難點

#### 困難點 1：何時該自訂例外 vs 使用內建例外
**症狀**：過度自訂例外，或完全不自訂

**判斷準則**：
```python
# ✅ 使用內建例外（通用錯誤）
def get_item(index):
    if index < 0:
        raise IndexError("索引不能為負數")

# ✅ 自訂例外（業務邏輯）
def process_payment(card):
    if card.is_expired():
        raise CardExpiredError(card.number, card.expiry_date)
```

**規則**：
- 通用資料結構錯誤 → 內建例外
- 業務規則違反 → 自訂例外
- 需要特殊處理邏輯 → 自訂例外

#### 困難點 2：例外命名規範不熟悉
**症狀**：使用 `MyError`, `CustomException`, `ErrorType1` 等不明確名稱

**解決方法**：
- ✅ 使用動詞+名詞：`InsufficientFunds`, `InvalidFormat`
- ✅ 描述錯誤狀態：`AccountLocked`, `SessionExpired`
- ❌ 避免：`Error1`, `MyException`, `CustomError`

**命名模板**：
- 狀態錯誤：`[Adjective][Noun]Error`（如 `InvalidCredentials`）
- 動作失敗：`[Action]FailedError`（如 `PaymentFailed`）
- 資源問題：`[Resource]NotFoundError`（如 `UserNotFound`）

#### 困難點 3：例外鏈的使用時機
**症狀**：不知道何時用 `raise...from`

**使用時機**：
```python
# ✅ 需要保留原始錯誤時
try:
    response = requests.get(url)
except RequestException as e:
    raise DataFetchError(f"無法取得 {url}") from e

# ✅ 包裝低階錯誤為高階錯誤時
try:
    with open(path) as f:
        data = json.load(f)
except (IOError, JSONDecodeError) as e:
    raise ConfigurationError(f"設定檔 {path} 無效") from e

# ❌ 不需要原始錯誤時
if age < 0:
    raise ValueError("年齡不能為負數")  # 不需要 from
```

---

## 💡 學習技巧（Learning Strategies）

### 設計檢查清單
設計自訂例外時，檢查：
- [ ] 類別名稱是否清楚表達錯誤類型？
- [ ] 是否繼承自適當的基底類別？
- [ ] 是否攜帶足夠的除錯資訊？
- [ ] 錯誤訊息是否對使用者友善？
- [ ] 是否需要建立例外階層？

### 實作練習建議
1. **例外收集**：記錄專案中的錯誤類型，設計對應例外
2. **階層設計**：為一個系統（如電商、遊戲）設計完整例外樹
3. **錯誤追蹤**：練習閱讀包含例外鏈的 traceback

### 記憶口訣
- **raise**：主動拋（內建或自訂都可拋）
- **assert**：除錯用（開發時才有用）
- **from**：鏈起來（保留原始錯誤）

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- [raise statement](https://docs.python.org/3/reference/simple_stmts.html#raise)
- [assert statement](https://docs.python.org/3/reference/simple_stmts.html#assert)

### 推薦閱讀
- PEP 3134 - Exception Chaining and Embedded Tracebacks
- Effective Python (2nd ed.), Item 87: Define a Root Exception
- Clean Code, Chapter 7: Error Handling

### 互動式工具
- [Python Exception Hierarchy Visualizer](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)

### 延伸主題（進階學習）
- 例外的效能影響（EAFP vs LBYL）
- 非同步程式的例外處理
- 例外的序列化（用於網路傳輸）
- 自訂 traceback 格式化

---

## ❓ 常見問題（FAQ）

**Q1: 自訂例外一定要定義 `__init__` 嗎？**
A: 不一定。如果不需要額外屬性，只需 `pass` 即可。但若要攜帶資訊，就需要定義。

**Q2: `raise` 和 `raise e` 有什麼區別？**
A: `raise` 重新拋出當前例外（保留 traceback），`raise e` 拋出新例外（重置 traceback）。通常使用前者。

**Q3: assert 在生產環境會執行嗎？**
A: 如果使用 `python -O`（最佳化模式），assert 會被忽略。因此不應用於錯誤處理。

**Q4: 例外類別要放在哪個檔案？**
A: 通常放在 `exceptions.py` 或模組的 `__init__.py` 中，方便統一管理和匯入。

**Q5: 自訂例外需要繼承 Exception 還是 BaseException？**
A: 幾乎總是繼承 `Exception`。`BaseException` 是給系統級例外用的（如 KeyboardInterrupt）。

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 20（例外處理基礎）**：try-except 基礎
- **Chapter 16（類別）**：繼承與類別設計

### 後續章節
- **Chapter 22（除錯技術）**：使用例外進行除錯
- **Chapter 23（檔案 I/O）**：檔案操作的例外處理

### 對應的 Milestone 專案
- **Milestone 6: 使用者註冊系統**（結合 Ch20-22 的例外處理）

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布，完整涵蓋自訂例外與 raise
- 後續版本更新請記錄於此

---

## 🎯 成功標準（Success Criteria）

完成本章學習後，您應該能夠：
- ✅ 獨立設計一套業務邏輯的例外階層
- ✅ 正確使用 raise、assert、例外鏈
- ✅ 通過自我測驗（分數 ≥ 75 分）
- ✅ 能解釋例外鏈的運作機制

---

**學習提醒**：好的例外設計是專業程式的標誌。請花時間練習設計清晰、有意義的例外階層！
