# Ch20: 例外處理機制 | Exception Handling

## 章節資訊

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時 |
| **難度等級** | ⭐⭐⭐ (中級) |
| **先備知識** | Ch01-Ch19 (特別是函式、檔案處理) |
| **學習目標** | 掌握 try-except-finally 完整機制，能夠處理各種執行時期錯誤 |

---

## 學習目標 Learning Objectives

### 知識 (Knowledge)
- [ ] 理解例外處理的必要性與運作原理
- [ ] 認識 Python 例外階層架構
- [ ] 了解 try-except-else-finally 各子句的作用
- [ ] 掌握常見內建例外類型及其使用時機

### 理解 (Comprehension)
- [ ] 解釋為何需要例外處理機制
- [ ] 區分編譯時期錯誤與執行時期錯誤
- [ ] 說明例外捕捉的順序規則
- [ ] 分析不同錯誤處理策略的適用場景

### 應用 (Application)
- [ ] 使用 try-except 處理檔案操作錯誤
- [ ] 撰寫多重 except 子句處理不同例外
- [ ] 運用 finally 確保資源正確釋放
- [ ] 取得並顯示例外詳細資訊

### 分析 (Analysis)
- [ ] 評估何時該捕捉例外、何時該讓它傳播
- [ ] 設計適當的例外處理架構
- [ ] 除錯並修正例外處理相關問題
- [ ] 優化例外處理效能與可讀性

---

## 核心概念 Key Concepts

### 概念地圖

```
例外處理 (Exception Handling)
│
├── 為何需要？(WHY)
│   ├── 處理執行時期錯誤 (Runtime Errors)
│   ├── 提升程式穩健性 (Robustness)
│   ├── 優雅的錯誤恢復 (Graceful Recovery)
│   └── 保護資源不洩漏 (Resource Protection)
│
├── 例外階層 (Exception Hierarchy)
│   ├── BaseException (所有例外的祖先)
│   ├── Exception (一般例外)
│   ├── 內建例外
│   │   ├── ValueError (值錯誤)
│   │   ├── TypeError (型別錯誤)
│   │   ├── FileNotFoundError (檔案不存在)
│   │   ├── ZeroDivisionError (除以零)
│   │   └── IndexError, KeyError, AttributeError...
│   └── SystemExit, KeyboardInterrupt (系統例外)
│
├── 處理機制 (Handling Mechanism)
│   ├── try 子句 (嘗試執行可能出錯的程式碼)
│   ├── except 子句 (捕捉並處理例外)
│   ├── else 子句 (沒有例外時執行)
│   └── finally 子句 (無論如何都執行)
│
└── 最佳實踐 (Best Practices)
    ├── 具體例外優先 (Specific before General)
    ├── 避免裸 except (No Bare Except)
    ├── 不吞噬例外 (Don't Swallow Exceptions)
    └── 清理資源 (Always Clean Up)
```

---

## First Principles 第一性原理

### 1. 為何需要例外處理？

**問題**：程式執行時總會遇到無法預期的狀況，如何處理？

**傳統做法** (沒有例外機制)：
```python
# 每個可能出錯的地方都要檢查
def divide(a, b):
    if b == 0:
        return None  # 用特殊值表示錯誤
    return a / b

result = divide(10, 0)
if result is None:
    print("除數不能為零")
else:
    print(f"結果: {result}")
```

**問題**：
- 錯誤處理與正常邏輯混在一起
- 需要記住每個函式的錯誤代碼
- 無法區分「正常的 None」與「錯誤的 None」
- 錯誤無法自動向上傳播

**例外機制** (現代做法)：
```python
def divide(a, b):
    return a / b  # 讓 Python 自動拋出 ZeroDivisionError

try:
    result = divide(10, 0)
    print(f"結果: {result}")
except ZeroDivisionError:
    print("除數不能為零")
```

**優點**：
- 正常邏輯與錯誤處理分離
- 錯誤會自動向上傳播直到被處理
- 型別安全 (不需要特殊值)
- 可攜帶詳細錯誤資訊

---

### 2. 例外的本質：中斷正常流程

**核心概念**：例外是一種「非局部跳轉」(Non-local Jump)

```python
def level3():
    print("3: 開始")
    raise ValueError("錯誤發生在第三層")
    print("3: 結束")  # 永遠不會執行

def level2():
    print("2: 開始")
    level3()
    print("2: 結束")  # 也不會執行

def level1():
    print("1: 開始")
    try:
        level2()
    except ValueError as e:
        print(f"1: 捕捉到例外 - {e}")
    print("1: 繼續執行")

level1()
```

**輸出**：
```
1: 開始
2: 開始
3: 開始
1: 捕捉到例外 - 錯誤發生在第三層
1: 繼續執行
```

**原理**：
1. level3() 拋出例外後，立即中斷當前函式
2. 控制權返回 level2()，但 level2() 沒有處理，繼續向上
3. 控制權返回 level1()，被 except 捕捉
4. 執行 except 區塊後，程式繼續正常執行

---

### 3. finally 的保證：必定執行

**問題**：如何確保資源一定被釋放？(即使發生例外)

```python
# 錯誤示範：可能洩漏檔案控制代碼
def read_file_bad(filename):
    f = open(filename)
    data = f.read()  # 如果這裡出錯，f 永遠不會關閉
    f.close()
    return data

# 正確做法：使用 finally
def read_file_good(filename):
    f = open(filename)
    try:
        data = f.read()
        return data
    finally:
        f.close()  # 無論如何都會執行
```

**finally 執行時機**：
- try 區塊正常結束後
- except 區塊執行後
- return/break/continue 之前
- 即使有未捕捉的例外

---

### 4. 例外階層：從具體到一般

Python 例外遵循繼承階層：

```
BaseException
├── SystemExit (sys.exit() 觸發)
├── KeyboardInterrupt (Ctrl+C 觸發)
├── GeneratorExit (生成器關閉)
└── Exception (一般例外)
    ├── StopIteration (迭代器結束)
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── FileExistsError
    └── ...
```

**捕捉順序原則**：具體例外要放在父類例外之前

```python
# ✅ 正確：具體在前
try:
    value = int(input("輸入數字: "))
except ValueError:
    print("不是有效數字")
except Exception:
    print("其他錯誤")

# ❌ 錯誤：父類在前會攔截所有子類
try:
    value = int(input("輸入數字: "))
except Exception:  # 這會捕捉所有例外
    print("其他錯誤")
except ValueError:  # 永遠不會執行到這裡
    print("不是有效數字")
```

---

## 課程教材 Course Materials

| 檔案 | 說明 | 使用時機 |
|:-----|:-----|:---------|
| `01-lecture.ipynb` | 主要課程：理論 + 6個範例 | 課堂講授 (2小時) |
| `02-worked-examples.ipynb` | 詳解範例：4個實務案例 | 示範教學 (1小時) |
| `03-practice.ipynb` | 課堂練習：8題即時演練 | 隨堂練習 (30分鐘) |
| `04-exercises.ipynb` | 課後作業：12題 (基礎→進階) | 回家作業 |
| `05-solutions.ipynb` | 完整解答 + 詳解 | 課後檢討 |
| `quiz.ipynb` | 自我測驗：15選擇 + 5程式題 | 章節複習 (30分鐘) |

---

## 能力檢核 Competency Checklist

### Level 1: 基礎應用 (必須達成)
- [ ] 能使用 try-except 處理基本例外
- [ ] 能使用 except ExceptionType as e 取得例外物件
- [ ] 能使用 finally 清理資源
- [ ] 知道常見例外類型及其觸發條件

### Level 2: 進階應用 (建議達成)
- [ ] 能使用多重 except 處理不同錯誤
- [ ] 能使用 else 子句處理成功情況
- [ ] 能正確排列例外捕捉順序 (具體→一般)
- [ ] 能取得並顯示 traceback 資訊

### Level 3: 整合應用 (挑戰目標)
- [ ] 能設計完整的例外處理架構
- [ ] 能判斷何時該捕捉、何時該傳播例外
- [ ] 能使用 with 語句自動管理資源
- [ ] 能除錯複雜的例外處理問題

---

## 授課要點 Teaching Tips

### 1. 開場引導 (10分鐘)
**情境**：讓學生體驗沒有例外處理的痛苦
```python
# 展示這個程式：讓學生猜會發生什麼
age = int(input("請輸入年齡: "))  # 輸入 "abc" 會怎樣？
print(f"您 {age} 歲")
```

**討論**：
- 程式為何崩潰？
- 如何避免崩潰？
- 如果要處理 10 種可能的輸入錯誤怎麼辦？

→ 引出例外處理的必要性

---

### 2. 核心教學流程 (90分鐘)

#### Part 1: try-except 基礎 (30分鐘)
1. **最簡單的例外處理**
   - try-except 結構
   - 捕捉特定例外
   - 取得例外訊息

2. **實際案例**：檔案讀取
   ```python
   try:
       with open("data.txt") as f:
           content = f.read()
   except FileNotFoundError:
       print("檔案不存在")
   ```

3. **常見錯誤**：
   - 裸 except (不指定例外類型)
   - 吞噬例外 (捕捉後不處理)

#### Part 2: 多重處理與順序 (30分鐘)
1. **多重 except**
   ```python
   try:
       value = int(input())
   except ValueError:
       print("不是數字")
   except KeyboardInterrupt:
       print("使用者中斷")
   except Exception as e:
       print(f"其他錯誤: {e}")
   ```

2. **順序規則**：具體→一般
   - 示範錯誤順序的後果
   - 使用 IDE 提示檢查

#### Part 3: else 與 finally (30分鐘)
1. **else 的用途**：分離成功與失敗邏輯
   ```python
   try:
       f = open("data.txt")
   except FileNotFoundError:
       print("檔案不存在")
   else:
       print(f"成功開啟，大小: {len(f.read())}")
       f.close()
   ```

2. **finally 的保證**：必定執行
   - 資源清理示範
   - 與 with 語句比較

---

### 3. 實作演練 (60分鐘)

**練習 1：安全的使用者輸入** (15分鐘)
```python
# 要求：建立一個函式，反覆要求使用者輸入有效數字
def get_valid_number(prompt):
    # 學生實作
    pass
```

**練習 2：檔案處理組合技** (20分鐘)
- 讀取不存在的檔案
- 寫入權限不足的位置
- 處理 JSON 格式錯誤

**練習 3：完整錯誤處理架構** (25分鐘)
- 多層函式呼叫
- 不同層級的錯誤處理
- 日誌記錄

---

### 4. 常見學習困難與解決方案

| 困難點 | 學生常見誤解 | 教學策略 |
|:-------|:-------------|:---------|
| **例外捕捉順序** | 不理解為何父類要放後面 | 用「篩子」比喻：大孔在後、小孔在前 |
| **finally 執行時機** | 以為 return 後就不執行 | 實際演示：在 try 中 return，finally 仍執行 |
| **裸 except 危險** | 覺得 except: 很方便 | 展示會捕捉 KeyboardInterrupt 的問題 |
| **何時該捕捉例外** | 到處都加 try-except | 教導「讓例外傳播」的概念 |
| **取得例外資訊** | 不知道如何取得詳細資訊 | 教 `as e` 語法，展示 traceback 模組 |

---

### 5. 實務案例分析 (30分鐘)

**案例 1：網路爬蟲的錯誤處理**
```python
import requests

urls = ["http://example1.com", "http://example2.com", ...]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        process_data(response.text)
    except requests.Timeout:
        print(f"{url}: 連線逾時")
    except requests.HTTPError as e:
        print(f"{url}: HTTP 錯誤 {e.response.status_code}")
    except Exception as e:
        print(f"{url}: 未知錯誤 {e}")
    else:
        print(f"{url}: 成功")
```

**案例 2：資料庫操作與資源管理**
```python
import sqlite3

def update_user(user_id, name):
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=? WHERE id=?", (name, user_id))
        conn.commit()
    except sqlite3.IntegrityError:
        print("違反唯一性限制")
        conn.rollback()
    except Exception as e:
        print(f"資料庫錯誤: {e}")
        conn.rollback()
    finally:
        conn.close()
```

---

## 延伸學習 Further Reading

### 官方文件
- [Python Tutorial - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Context Managers (with statement)](https://docs.python.org/3/reference/compound_stmts.html#with)

### 進階主題
- **Context Managers**：深入理解 `with` 語句與 `__enter__`/`__exit__`
- **Exception Chaining**：`raise ... from ...` 語法 (Ch21 詳述)
- **traceback 模組**：取得完整錯誤堆疊
- **warnings 模組**：警告 vs 例外的使用時機

### 最佳實踐文章
- [Effective Python Item 65: Take Advantage of Each Block in try/except/else/finally](https://effectivepython.com/)
- [Python Exception Handling Best Practices](https://realpython.com/python-exceptions/)
- [EAFP vs LBYL](https://docs.python.org/3/glossary.html#term-EAFP) - Python 的「請求原諒比請求許可容易」哲學

### 實務應用
- **Logging**：結合 logging 模組記錄例外
- **Retry Mechanism**：自動重試失敗的操作
- **Graceful Degradation**：優雅降級策略
- **Circuit Breaker Pattern**：斷路器模式

---

## 學習資源 Resources

### 線上工具
- [Python Tutor](http://pythontutor.com/) - 視覺化例外傳播過程
- [Replit](https://replit.com/) - 線上測試例外處理

### 練習平台
- [Exercism - Python Track (Error Handling)](https://exercism.org/tracks/python)
- [LeetCode](https://leetcode.com/) - 實務演算法問題中的例外處理

### 參考書籍
- 《Effective Python》 by Brett Slatkin - Item 65-67
- 《Python Cookbook》 - Chapter 14: Testing, Debugging, and Exceptions
- 《Fluent Python》 - Chapter 18: With, Match, and Else Blocks

---

## 下一步 Next Steps

完成本章後，您將能夠：
- ✅ 處理執行時期的各種錯誤
- ✅ 撰寫穩健的檔案與網路操作程式
- ✅ 設計清晰的錯誤處理邏輯

**接下來學習**：
- **Ch21: 自訂例外與 raise** - 學習主動拋出例外、設計自己的例外類別
- **Ch22: 除錯技術** - 掌握 print debugging、logging、pdb 除錯器
- **Ch23: 檔案 I/O** - 結合例外處理，撰寫安全的檔案操作程式

---

**教學建議時程**：
- **第 1 節課 (2h)**：01-lecture.ipynb (理論 + 6範例)
- **第 2 節課 (1.5h)**：02-worked-examples.ipynb + 03-practice.ipynb
- **第 3 節課 (1.5h)**：檢討作業 + 實務案例分析
- **課後**：04-exercises.ipynb (作業) + quiz.ipynb (自我測驗)
