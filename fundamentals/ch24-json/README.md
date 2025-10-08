# Chapter 24: 結構化資料：JSON | Structured Data: JSON

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 3 小時（1.5 小時理論 + 1.5 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (3/5) |
| **先備知識** | Chapter 23（檔案操作基礎）、Chapter 9（字典）、Chapter 7（列表） |
| **相關章節** | Chapter 25（CSV）、Chapter 26（路徑管理）、Milestone 7（待辦事項應用） |

---

## 🎯 學習目標（Learning Objectives）

完成本章後，學習者應能夠：

### 知識面（Knowledge）
- **列出** JSON 的六種資料型態：object、array、string、number、boolean、null
- **定義** JSON 格式的語法規則與結構特性
- **說明** json 模組的核心方法：dumps、loads、dump、load

### 理解面（Comprehension）
- **解釋** 為什麼需要 JSON（資料交換、API 通訊、設定檔）
- **比較** JSON vs Python 字典、JSON vs CSV 的差異與應用場景
- **歸納** JSON 序列化與反序列化的工作原理

### 應用面（Application）
- **運用** json 模組進行資料的讀取、寫入、轉換
- **實作** 處理巢狀結構的 JSON 資料（如 API 回應）
- **解決** JSON 資料的驗證、格式化、錯誤處理

### 分析面（Analysis）
- **分析** 何時使用 JSON 而非其他資料格式（CSV、XML、YAML）
- **診斷** JSON 格式錯誤與 Python 型態轉換問題
- **選擇** 適當的 JSON 處理策略（完整載入 vs 串流處理）

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
JSON（JavaScript Object Notation）
├── 核心特性
│   ├── 輕量級資料交換格式
│   ├── 人類可讀、機器可解析
│   ├── 語言無關（與 Python 無關聯）
│   └── 廣泛應用於 Web API、設定檔
│
├── JSON 資料型態
│   ├── object（物件）→ Python dict
│   ├── array（陣列）→ Python list
│   ├── string（字串）→ Python str
│   ├── number（數字）→ Python int/float
│   ├── boolean（布林）→ Python True/False
│   └── null（空值）→ Python None
│
├── Python json 模組
│   ├── 序列化（Serialization）
│   │   ├── dumps()：Python → JSON 字串
│   │   └── dump()：Python → JSON 檔案
│   └── 反序列化（Deserialization）
│       ├── loads()：JSON 字串 → Python
│       └── load()：JSON 檔案 → Python
│
├── 實務應用
│   ├── API 資料交換（RESTful API）
│   ├── 應用程式設定檔（config.json）
│   ├── 資料儲存與備份
│   └── 網頁前後端通訊
│
└── 常見問題
    ├── 格式錯誤（語法錯誤）
    ├── 編碼問題（中文處理）
    ├── 型態轉換（datetime、set）
    └── 巢狀結構處理
```

### First Principles 解析

#### 為什麼需要 JSON？

**根本問題**：不同程式語言之間如何交換資料？

**場景**：
- Python 程式產生了一個字典 `{"name": "小明", "age": 20}`
- 需要傳送給 JavaScript 前端或 Java 後端
- 問題：不同語言的資料結構無法直接相容

**解決方案**：使用「語言無關」的文字格式作為中間媒介

**最小實作**：
```python
import json

# Python 字典
data = {"name": "小明", "age": 20}

# 轉換為 JSON 字串（可以傳給任何語言）
json_string = json.dumps(data)
print(json_string)  # 輸出: {"name": "小明", "age": 20}

# 其他語言收到這個字串後，用自己的解析器轉回該語言的資料結構
```

**推導過程**：
1. **觀察**：資料交換需要統一格式
2. **設計**：選擇人類可讀的文字格式（而非二進位）
3. **標準化**：定義清楚的語法規則（JSON 規範）
4. **實作**：每個語言提供解析器（Python 的 json 模組）

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| JSON | JavaScript Object Notation | 輕量級資料交換格式，源自 JavaScript 但語言無關 |
| 序列化 | Serialization | 將資料結構轉換為可儲存或傳輸的格式（Python → JSON） |
| 反序列化 | Deserialization | 將儲存的格式還原為資料結構（JSON → Python） |
| 物件 | Object | JSON 中的鍵值對結構，對應 Python 的 dict |
| 陣列 | Array | JSON 中的有序列表，對應 Python 的 list |
| 字串 | String | JSON 中的文字，必須用雙引號包圍 |
| 縮排 | Indent | 格式化 JSON 時的空格數，提升可讀性 |
| 轉義字元 | Escape Character | JSON 字串中的特殊字元，如 `\"`, `\\`, `\n` |
| API | Application Programming Interface | 應用程式介面，常使用 JSON 格式交換資料 |

---

## 📚 教材內容（Course Materials）

| 檔案 | 說明 | 預計時長 | 使用時機 |
|:-----|:-----|:---------|:---------|
| `01-lecture.ipynb` | 📖 理論講義與範例演示 | 60 分鐘 | 課堂講授 |
| `02-worked-examples.ipynb` | 💡 詳解範例（5 題） | 30 分鐘 | 課堂演練 |
| `03-practice.ipynb` | 🛠️ 課堂練習（12 題） | 30 分鐘 | 隨堂實作 |
| `04-exercises.ipynb` | ✍️ 課後習題（18 題） | 90 分鐘 | 課後自習 |
| `05-solutions.ipynb` | ✅ 習題完整解答 | 參考用 | 自我檢核 |
| `quiz.ipynb` | 📝 自我測驗（25 題） | 20 分鐘 | 學習驗收 |

---

## 🛠️ 實作能力檢核（Competency Checklist）

完成本章後，請確認您能夠：

### 基本能力
- [ ] 使用 `json.dumps()` 將 Python 資料轉換為 JSON 字串
- [ ] 使用 `json.loads()` 將 JSON 字串轉換為 Python 資料
- [ ] 使用 `json.dump()` 將資料寫入 JSON 檔案
- [ ] 使用 `json.load()` 從 JSON 檔案讀取資料
- [ ] 處理 JSON 格式錯誤（JSONDecodeError）
- [ ] 理解 JSON 與 Python 資料型態的對應關係

### 進階能力
- [ ] 使用 `indent` 參數格式化 JSON 輸出
- [ ] 使用 `ensure_ascii=False` 正確處理中文字元
- [ ] 處理巢狀結構的 JSON 資料（多層字典與列表）
- [ ] 自訂 JSON 編碼器處理特殊型態（如 datetime）
- [ ] 驗證 JSON 資料的結構與內容
- [ ] 使用 `sort_keys` 參數排序 JSON 鍵

### 應用能力
- [ ] 實作應用程式設定檔的讀取與儲存
- [ ] 處理 API 回應資料（模擬或真實 API）
- [ ] 建立和維護結構化的資料檔案
- [ ] 實作資料的匯入/匯出功能
- [ ] 處理大型 JSON 檔案的效能問題
- [ ] 整合 JSON 與檔案操作、異常處理

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **先展示實際應用場景**：從 API 回應或設定檔開始，讓學生理解「為什麼需要 JSON」
2. **對比 Python 字典與 JSON**：強調 JSON 是「字串格式」，需要序列化/反序列化
3. **強調編碼問題**：中文處理務必使用 `ensure_ascii=False`
4. **實作設定檔系統**：讓學生建立小型應用的 config.json
5. **連結前後章節**：結合 Ch23（檔案操作）與 Ch9（字典），為 Ch25（CSV）做準備

### 常見學生困難點

#### 困難點 1：混淆 Python 字典與 JSON 字串
**症狀**：
- 嘗試對 JSON 字串使用字典操作（如 `json_str["key"]`）
- 不理解為什麼需要 `dumps()` 和 `loads()`

**解決方法**：
- 用類比說明：「JSON 是文字檔案格式，就像 Word 文件；Python 字典是記憶體中的資料結構」
- 展示 `type()` 檢查：`type(data)` vs `type(json.dumps(data))`
- 強調：「檔案儲存的是字串，記憶體中操作的是字典」

#### 困難點 2：JSON 格式語法錯誤
**症狀**：
- 使用單引號而非雙引號
- 忘記逗號或多餘逗號（trailing comma）
- 使用 Python 的 `True` 而非 JSON 的 `true`

**解決方法**：
- 提供 JSON 驗證工具（如 jsonlint.com）
- 展示 `JSONDecodeError` 的錯誤訊息解讀
- 建立「JSON 語法檢查表」

#### 困難點 3：中文字元顯示問題
**症狀**：
- JSON 字串中中文變成 `\uXXXX` 的 Unicode 編碼

**解決方法**：
- 明確說明 `ensure_ascii=False` 的作用
- 展示對比：有無此參數的輸出差異
- 標準寫法：`json.dumps(data, ensure_ascii=False, indent=2)`

#### 困難點 4：無法序列化特殊型態
**症狀**：
- `TypeError: Object of type datetime is not JSON serializable`
- 嘗試序列化 set、自訂類別等

**解決方法**：
- 說明 JSON 只支援 6 種基本型態
- 展示手動轉換：`datetime → str`、`set → list`
- 進階：示範自訂 `JSONEncoder`

---

## 💡 學習技巧（Learning Strategies）

### JSON vs Python 對照表

| Python 型態 | JSON 型態 | 範例 |
|:------------|:----------|:-----|
| `dict` | object | `{"key": "value"}` |
| `list`, `tuple` | array | `[1, 2, 3]` |
| `str` | string | `"hello"` |
| `int`, `float` | number | `42`, `3.14` |
| `True`, `False` | `true`, `false` | `true` |
| `None` | `null` | `null` |

### 實作練習建議
1. **建立個人設定檔**：實作一個簡單的應用程式設定檔
2. **解析 API 回應**：使用公開 API 練習解析 JSON 資料
3. **資料轉換練習**：嘗試將 CSV 資料轉換為 JSON 格式
4. **巢狀結構練習**：處理多層嵌套的 JSON 資料

---

## 🔗 延伸資源（Additional Resources）

### Python 官方文件
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [JSON 格式規範（RFC 8259）](https://tools.ietf.org/html/rfc8259)

### 推薦閱讀
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [JSONLint - JSON 驗證工具](https://jsonlint.com/)
- [公開 API 列表（練習用）](https://github.com/public-apis/public-apis)

### 實務工具
- **JSON Viewer**: 瀏覽器擴充套件，美化 JSON 顯示
- **Postman**: API 測試工具，查看 JSON 回應
- **jq**: 命令列 JSON 處理器

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-08): 完整內容發布，包含 10 個範例、18 題習題、25 題測驗

---

**學習提醒**：JSON 是 Web 開發必備技能！請多練習 API 資料處理，為未來的專案開發打好基礎。
