# Milestone 07: Todo App Management System | 待辦事項管理程式

## 專案資訊 | Project Information

| 項目 | 內容 |
|:-----|:-----|
| **整合章節** | Ch23-26 (檔案輸入輸出、JSON、CSV、路徑管理) |
| **難度等級** | ⭐⭐⭐⭐☆ (Advanced) |
| **預估時間** | 20-30 小時 |
| **專案類型** | 命令列應用程式 (CLI Application) |
| **核心技術** | File I/O, JSON, CSV, pathlib, datetime |

---

## 一、專案目標 | Project Objectives

### 1.1 整合知識點

本專案整合 **Part VII: 檔案處理與資料持久化** (Ch23-26) 的核心概念：

| 章節 | 核心技能 | 應用情境 |
|:-----|:---------|:---------|
| **Ch23** | 檔案讀寫基礎 | 任務資料的儲存與讀取 |
| **Ch24** | JSON 格式處理 | 結構化資料序列化與反序列化 |
| **Ch25** | CSV 檔案操作 | 匯出報表與統計資料 |
| **Ch26** | 路徑管理 (pathlib) | 跨平台檔案路徑處理 |

### 1.2 學習成果 | Learning Outcomes

完成本專案後，學生將能夠：

**知識層次 (Knowledge)**:
- 理解檔案持久化的重要性與應用場景
- 掌握 JSON 與 CSV 格式的差異與適用時機
- 了解檔案系統的組織與路徑管理
- 認識資料備份與錯誤恢復機制

**技能層次 (Skills)**:
- 設計並實作資料結構 (Task, TodoManager)
- 使用 JSON 進行資料序列化與反序列化
- 實作完整的 CRUD 操作 (Create, Read, Update, Delete)
- 處理檔案讀寫的例外情況
- 使用 pathlib 進行跨平台路徑管理
- 匯出 CSV 格式報表
- 實作搜尋、過濾、排序功能

**態度層次 (Attitudes)**:
- 重視資料安全與錯誤處理
- 注重使用者體驗與介面設計
- 培養系統化思維與模組化設計能力
- 實踐程式碼可維護性與可擴展性原則

---

## 二、專案描述 | Project Description

### 2.1 專案情境

您將開發一個**命令列待辦事項管理系統**，幫助使用者管理日常任務。系統需要：

1. **持久化儲存**: 任務資料儲存在 JSON 檔案中，程式關閉後資料不會遺失
2. **完整功能**: 支援任務的新增、查看、更新、刪除、搜尋、過濾
3. **優先級管理**: 任務可設定優先級 (High/Medium/Low)
4. **狀態追蹤**: 追蹤任務狀態 (Pending/In Progress/Completed)
5. **資料匯出**: 支援匯出為 CSV 格式以便分析
6. **備份機制**: 自動備份資料以防資料遺失

### 2.2 使用者故事 (User Stories)

```
作為一個使用者，我希望能夠：
1. 新增待辦任務，設定標題、描述、優先級、截止日期
2. 查看所有任務，並依照優先級或截止日期排序
3. 更新任務的狀態 (進行中、已完成)
4. 刪除不需要的任務
5. 搜尋特定關鍵字的任務
6. 依照優先級、狀態、標籤過濾任務
7. 查看任務統計資訊 (總數、已完成、進行中)
8. 匯出任務清單為 CSV 檔案
9. 封存已完成的任務
10. 確保資料不會因程式錯誤而遺失
```

### 2.3 系統架構

```
todo_app/
├── todos.json           # 主要資料檔案
├── todos_backup.json    # 自動備份檔案
├── archive/             # 封存資料目錄
│   └── archive_2025.json
└── exports/             # 匯出檔案目錄
    └── tasks_export.csv
```

---

## 三、功能需求 | Functional Requirements

### 3.1 基本需求 (70分)

#### 3.1.1 資料結構設計 (10分)

**Task 資料結構**:
```python
{
    "id": "unique_uuid",           # 唯一識別碼
    "title": "string",             # 任務標題 (必填)
    "description": "string",       # 任務描述 (選填)
    "priority": "High|Medium|Low", # 優先級 (預設 Medium)
    "status": "Pending|InProgress|Completed",  # 狀態 (預設 Pending)
    "created_date": "2025-10-08T10:30:00",    # 建立時間 (ISO格式)
    "due_date": "2025-10-15T18:00:00",        # 截止時間 (選填)
    "tags": ["work", "urgent"]     # 標籤列表 (選填)
}
```

**評分標準**:
- 使用 UUID 或時間戳作為唯一 ID (2分)
- 正確使用 datetime 處理日期時間 (3分)
- 資料驗證 (優先級、狀態必須為預定義值) (3分)
- 提供合理的預設值 (2分)

#### 3.1.2 核心 CRUD 操作 (30分)

**必須實作的方法**:

1. **新增任務** (8分)
   ```python
   def add_task(self, title, description="", priority="Medium",
                due_date=None, tags=None):
       """新增一個待辦任務"""
       # 1. 驗證輸入
       # 2. 生成唯一 ID
       # 3. 建立 Task 物件
       # 4. 加入任務清單
       # 5. 儲存至檔案
   ```
   - 輸入驗證 (2分)
   - ID 生成機制 (2分)
   - 正確設定建立時間 (2分)
   - 儲存至檔案 (2分)

2. **列出任務** (6分)
   ```python
   def list_tasks(self, filter_by=None, sort_by=None):
       """列出所有任務，支援過濾與排序"""
   ```
   - 格式化顯示 (3分)
   - 支援基本排序 (3分)

3. **更新任務** (8分)
   ```python
   def update_task(self, task_id, **kwargs):
       """更新任務的指定欄位"""
   ```
   - 找到指定任務 (2分)
   - 更新指定欄位 (3分)
   - 驗證更新值 (2分)
   - 儲存變更 (1分)

4. **刪除任務** (4分)
   ```python
   def delete_task(self, task_id):
       """刪除指定任務"""
   ```
   - 找到並刪除任務 (2分)
   - 確認訊息與錯誤處理 (2分)

5. **標記完成** (4分)
   ```python
   def mark_completed(self, task_id):
       """標記任務為已完成"""
   ```

#### 3.1.3 檔案持久化 (15分)

1. **儲存至檔案** (8分)
   ```python
   def save_to_file(self):
       """儲存所有任務至 JSON 檔案"""
       # 1. 序列化任務清單
       # 2. 寫入檔案
       # 3. 錯誤處理
   ```
   - 正確使用 JSON 序列化 (3分)
   - 使用 pathlib 處理路徑 (2分)
   - 完整錯誤處理 (3分)

2. **從檔案讀取** (7分)
   ```python
   def load_from_file(self):
       """從 JSON 檔案載入任務"""
       # 1. 檢查檔案是否存在
       # 2. 讀取並反序列化
       # 3. 資料驗證
       # 4. 錯誤處理與恢復
   ```
   - 檔案存在性檢查 (2分)
   - 正確反序列化 (2分)
   - 處理空檔案或損毀檔案 (3分)

#### 3.1.4 搜尋與過濾 (10分)

1. **關鍵字搜尋** (5分)
   ```python
   def search_tasks(self, keyword):
       """搜尋標題或描述中包含關鍵字的任務"""
   ```
   - 不區分大小寫搜尋 (2分)
   - 搜尋標題與描述 (2分)
   - 回傳結果列表 (1分)

2. **條件過濾** (5分)
   ```python
   def filter_by_priority(self, priority):
       """依照優先級過濾任務"""

   def filter_by_status(self, status):
       """依照狀態過濾任務"""
   ```
   - 正確過濾邏輯 (3分)
   - 支援多條件過濾 (2分)

#### 3.1.5 命令列介面 (5分)

```python
def main():
    """主程式選單"""
    # 1. 顯示選單
    # 2. 接收使用者輸入
    # 3. 執行對應功能
    # 4. 迴圈執行直到退出
```

- 清晰的選單顯示 (2分)
- 輸入驗證 (2分)
- 迴圈與退出機制 (1分)

---

### 3.2 進階需求 (30分)

#### 3.2.1 截止日期管理 (8分)

1. **逾期檢查** (4分)
   ```python
   def get_overdue_tasks(self):
       """取得所有逾期任務"""
   ```

2. **即將到期提醒** (4分)
   ```python
   def get_upcoming_tasks(self, days=3):
       """取得未來N天內到期的任務"""
   ```

#### 3.2.2 標籤系統 (6分)

1. **依標籤過濾** (3分)
   ```python
   def filter_by_tag(self, tag):
       """依照標籤過濾任務"""
   ```

2. **列出所有標籤** (3分)
   ```python
   def get_all_tags(self):
       """取得所有使用中的標籤"""
   ```

#### 3.2.3 資料匯出 (8分)

1. **匯出為 CSV** (6分)
   ```python
   def export_to_csv(self, filename="tasks_export.csv"):
       """匯出任務清單為 CSV 格式"""
   ```
   - 正確使用 csv 模組 (3分)
   - 包含所有欄位 (2分)
   - 錯誤處理 (1分)

2. **匯出統計報表** (2分)
   ```python
   def export_statistics(self):
       """匯出統計資訊"""
   ```

#### 3.2.4 統計與報表 (5分)

```python
def get_statistics(self):
    """取得任務統計資訊"""
    return {
        "total": 100,
        "completed": 60,
        "in_progress": 20,
        "pending": 20,
        "overdue": 5,
        "completion_rate": 0.6
    }
```

- 計算各狀態任務數量 (2分)
- 計算完成率 (1分)
- 格式化顯示 (2分)

#### 3.2.5 封存系統 (3分)

```python
def archive_completed_tasks(self):
    """將已完成任務移至封存檔案"""
```

- 移動已完成任務 (2分)
- 按年份組織封存檔案 (1分)

---

## 四、技術規格 | Technical Specifications

### 4.1 檔案儲存格式

**主要資料檔案 (todos.json)**:
```json
{
    "tasks": [
        {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "完成 Python 專案",
            "description": "實作待辦事項管理系統",
            "priority": "High",
            "status": "InProgress",
            "created_date": "2025-10-08T10:30:00",
            "due_date": "2025-10-15T18:00:00",
            "tags": ["work", "programming"]
        }
    ],
    "metadata": {
        "last_modified": "2025-10-08T15:45:00",
        "version": "1.0"
    }
}
```

### 4.2 資料驗證規則

| 欄位 | 驗證規則 |
|:-----|:---------|
| `title` | 必填，長度 1-100 字元 |
| `priority` | 必須為 "High", "Medium", "Low" 之一 |
| `status` | 必須為 "Pending", "InProgress", "Completed" 之一 |
| `due_date` | ISO 8601 格式，或 None |
| `tags` | 列表，每個標籤長度 1-20 字元 |

### 4.3 路徑管理

使用 `pathlib.Path` 進行跨平台路徑處理：

```python
from pathlib import Path

class TodoManager:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

        self.data_file = self.data_dir / "todos.json"
        self.backup_file = self.data_dir / "todos_backup.json"
        self.archive_dir = self.data_dir / "archive"
        self.export_dir = self.data_dir / "exports"
```

### 4.4 錯誤處理策略

```python
# 1. 檔案不存在
try:
    data = load_from_file()
except FileNotFoundError:
    # 建立新檔案
    initialize_empty_file()

# 2. JSON 格式錯誤
except json.JSONDecodeError:
    # 嘗試從備份恢復
    restore_from_backup()

# 3. 權限錯誤
except PermissionError:
    # 提示使用者檢查權限
    print("錯誤: 沒有檔案存取權限")

# 4. 磁碟空間不足
except OSError as e:
    # 記錄錯誤並提示
    log_error(e)
```

---

## 五、開發步驟 | Development Guide

### Phase 1: 資料結構與檔案操作 (30%)

**目標**: 建立資料模型與檔案讀寫基礎

**步驟**:
1. **設計 Task 類別** (建議時間: 2小時)
   - 定義 `__init__` 方法
   - 實作資料驗證
   - 實作 `to_dict()` 轉換方法
   - 實作 `from_dict()` 類別方法
   - 實作 `__str__` 方法以便顯示

2. **實作檔案操作** (建議時間: 3小時)
   - 實作 `save_to_file()` 方法
   - 實作 `load_from_file()` 方法
   - 實作自動備份機制
   - 處理各種檔案錯誤情況

3. **測試資料持久化** (建議時間: 1小時)
   - 測試儲存與讀取
   - 測試錯誤恢復機制
   - 驗證資料完整性

**檢核點**:
- [ ] Task 類別可正確建立物件
- [ ] 資料可成功儲存至 JSON 檔案
- [ ] 程式重啟後可讀取先前資料
- [ ] 檔案損毀時可從備份恢復

---

### Phase 2: 核心功能實作 (40%)

**目標**: 實作完整的 CRUD 操作

**步驟**:
1. **實作 TodoManager 類別** (建議時間: 4小時)
   - 初始化載入資料
   - 實作 `add_task()` 方法
   - 實作 `list_tasks()` 方法
   - 實作 `update_task()` 方法
   - 實作 `delete_task()` 方法
   - 實作 `mark_completed()` 方法

2. **實作搜尋與過濾** (建議時間: 2小時)
   - 實作關鍵字搜尋
   - 實作優先級過濾
   - 實作狀態過濾
   - 實作排序功能

3. **建立 CLI 介面** (建議時間: 3小時)
   - 設計主選單
   - 實作各功能的輸入處理
   - 實作格式化顯示
   - 實作輸入驗證

**檢核點**:
- [ ] 可新增、查看、更新、刪除任務
- [ ] 可搜尋並過濾任務
- [ ] CLI 介面友善易用
- [ ] 所有操作都會儲存至檔案

---

### Phase 3: 進階功能 (30%)

**目標**: 實作進階功能與優化

**步驟**:
1. **截止日期管理** (建議時間: 2小時)
   - 實作逾期檢查
   - 實作即將到期提醒
   - 在列表中標示逾期任務

2. **標籤系統** (建議時間: 2小時)
   - 實作標籤過濾
   - 實作標籤管理
   - 顯示所有標籤

3. **資料匯出** (建議時間: 3小時)
   - 實作 CSV 匯出
   - 實作統計報表
   - 建立 exports 目錄管理

4. **封存系統** (建議時間: 2小時)
   - 實作封存已完成任務
   - 按年份組織封存檔案
   - 實作封存查看功能

5. **優化與測試** (建議時間: 3小時)
   - 全面測試所有功能
   - 優化使用者體驗
   - 補充錯誤處理
   - 撰寫使用說明

**檢核點**:
- [ ] 可管理截止日期並提醒
- [ ] 標籤系統運作正常
- [ ] 可匯出 CSV 與統計報表
- [ ] 封存系統正常運作
- [ ] 所有功能經過完整測試

---

## 六、評分標準 | Grading Rubric

### 6.1 基本需求 (70分)

| 項目 | 配分 | 評分標準 |
|:-----|:----:|:---------|
| **資料結構設計** | 10 | - UUID/唯一ID (2分)<br>- datetime 處理 (3分)<br>- 資料驗證 (3分)<br>- 預設值設定 (2分) |
| **新增任務** | 8 | - 輸入驗證 (2分)<br>- ID 生成 (2分)<br>- 時間戳記 (2分)<br>- 檔案儲存 (2分) |
| **列出任務** | 6 | - 格式化顯示 (3分)<br>- 排序功能 (3分) |
| **更新任務** | 8 | - 查找任務 (2分)<br>- 更新欄位 (3分)<br>- 驗證更新 (2分)<br>- 儲存變更 (1分) |
| **刪除任務** | 4 | - 刪除功能 (2分)<br>- 確認與錯誤處理 (2分) |
| **標記完成** | 4 | - 狀態更新 (2分)<br>- 儲存變更 (2分) |
| **儲存至檔案** | 8 | - JSON 序列化 (3分)<br>- pathlib 使用 (2分)<br>- 錯誤處理 (3分) |
| **從檔案讀取** | 7 | - 檔案檢查 (2分)<br>- 反序列化 (2分)<br>- 錯誤恢復 (3分) |
| **搜尋功能** | 5 | - 不區分大小寫 (2分)<br>- 多欄位搜尋 (2分)<br>- 回傳結果 (1分) |
| **過濾功能** | 5 | - 過濾邏輯 (3分)<br>- 多條件支援 (2分) |
| **CLI 介面** | 5 | - 選單顯示 (2分)<br>- 輸入驗證 (2分)<br>- 迴圈機制 (1分) |

### 6.2 進階需求 (30分)

| 項目 | 配分 | 評分標準 |
|:-----|:----:|:---------|
| **截止日期管理** | 8 | - 逾期檢查 (4分)<br>- 即將到期提醒 (4分) |
| **標籤系統** | 6 | - 標籤過濾 (3分)<br>- 列出標籤 (3分) |
| **CSV 匯出** | 6 | - csv 模組使用 (3分)<br>- 完整欄位 (2分)<br>- 錯誤處理 (1分) |
| **統計報表** | 2 | - 統計功能 (2分) |
| **統計顯示** | 5 | - 計算各狀態 (2分)<br>- 完成率 (1分)<br>- 格式化顯示 (2分) |
| **封存系統** | 3 | - 封存功能 (2分)<br>- 檔案組織 (1分) |

### 6.3 程式碼品質 (Bonus +10分)

| 項目 | 配分 | 評分標準 |
|:-----|:----:|:---------|
| **程式碼風格** | 3 | - 遵循 PEP 8<br>- 命名清晰<br>- 適當註解 |
| **錯誤處理** | 3 | - 完整的例外處理<br>- 友善錯誤訊息<br>- 錯誤恢復機制 |
| **模組化設計** | 2 | - 函式職責單一<br>- 適當的抽象層次 |
| **使用者體驗** | 2 | - 介面直覺<br>- 操作流暢<br>- 提示清楚 |

**總分計算**: 基本需求 (70) + 進階需求 (30) + Bonus (最多10) = 110分 (滿分100)

---

## 七、教師指引 | Teaching Guidelines

### 7.1 教學重點

1. **檔案持久化概念** (Ch23-24)
   - 強調為什麼需要將資料儲存至檔案
   - 說明 JSON 格式的優勢 (人類可讀、結構化、跨語言)
   - 示範序列化與反序列化的過程

2. **pathlib 的重要性** (Ch26)
   - 展示 pathlib 與傳統字串路徑的差異
   - 說明跨平台相容性 (Windows vs Unix 路徑)
   - 示範路徑操作的常用方法 (`/`, `mkdir`, `exists`)

3. **錯誤處理策略** (Ch20-21)
   - 討論可能發生的檔案錯誤
   - 示範備份與恢復機制
   - 強調資料安全的重要性

4. **資料結構設計** (Ch16-18)
   - 討論 Task 類別的設計考量
   - 說明為什麼使用 UUID 作為 ID
   - 展示 datetime 的使用與格式化

### 7.2 常見問題與解決方案

**問題 1**: 學生不知道如何設計資料結構
- **解法**: 提供 Task 類別的基本架構，引導學生思考需要哪些欄位
- **提示**: 從使用者需求反推資料結構 (需要優先級 → 加入 priority 欄位)

**問題 2**: JSON 序列化 datetime 物件時出錯
- **原因**: datetime 物件無法直接序列化為 JSON
- **解法**: 轉換為 ISO 格式字串 (`dt.isoformat()`)
- **範例**:
  ```python
  # 儲存時
  task_dict["created_date"] = task.created_date.isoformat()

  # 讀取時
  from datetime import datetime
  task.created_date = datetime.fromisoformat(task_dict["created_date"])
  ```

**問題 3**: 檔案路徑在不同作業系統出現問題
- **原因**: 使用字串拼接路徑 (`"data" + "/" + "todos.json"`)
- **解法**: 使用 pathlib 的 `/` 運算子
- **範例**:
  ```python
  from pathlib import Path
  data_file = Path("data") / "todos.json"  # 跨平台相容
  ```

**問題 4**: 程式崩潰導致資料遺失
- **解法**: 實作自動備份機制
- **範例**:
  ```python
  def save_to_file(self):
      # 1. 先備份舊檔案
      if self.data_file.exists():
          shutil.copy(self.data_file, self.backup_file)

      # 2. 再寫入新資料
      with open(self.data_file, 'w', encoding='utf-8') as f:
          json.dump(data, f, ensure_ascii=False, indent=2)
  ```

**問題 5**: 搜尋功能無法找到中文關鍵字
- **原因**: 編碼問題或大小寫比對
- **解法**: 使用 `.lower()` 統一轉小寫，並確保檔案使用 UTF-8 編碼
- **範例**:
  ```python
  def search_tasks(self, keyword):
      keyword = keyword.lower()
      return [t for t in self.tasks
              if keyword in t.title.lower() or keyword in t.description.lower()]
  ```

### 7.3 評分重點

**及格標準 (60分)**:
- 完成基本 CRUD 操作 (新增、查看、更新、刪除)
- 資料可正確儲存至檔案
- 程式重啟後可讀取資料
- CLI 介面可正常運作

**良好標準 (70-80分)**:
- 完成所有基本需求
- 實作搜尋與過濾功能
- 具備基本錯誤處理
- 程式碼結構清晰

**優秀標準 (80-90分)**:
- 完成大部分進階需求
- 完整的錯誤處理與資料備份
- 使用者體驗良好
- 程式碼品質高

**卓越標準 (90-100分)**:
- 完成所有進階需求
- 實作統計報表與資料匯出
- 程式碼具備高可維護性
- 提供完整的使用說明

### 7.4 時間分配建議

| 階段 | 建議時間 | 重點工作 |
|:-----|:--------:|:---------|
| **Phase 1** | 6 小時 | 資料結構設計、檔案操作 |
| **Phase 2** | 9 小時 | CRUD 功能、CLI 介面 |
| **Phase 3** | 12 小時 | 進階功能、測試優化 |
| **總計** | 27 小時 | 適合 3-4 週完成 |

---

## 八、延伸挑戰 | Extension Challenges

### 8.1 圖形化介面 (GUI) 版本

使用 `tkinter` 建立桌面應用程式：

**功能需求**:
- 任務列表顯示 (Treeview)
- 新增/編輯任務的對話框
- 優先級顏色標示 (紅/黃/綠)
- 搜尋與過濾面板
- 統計資料視覺化

**技術要點**:
```python
import tkinter as tk
from tkinter import ttk

class TodoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")

        # 建立任務列表
        self.tree = ttk.Treeview(root, columns=("title", "priority", "status"))

        # 建立操作按鈕
        self.add_button = tk.Button(root, text="新增任務", command=self.add_task)
```

### 8.2 Web API 版本

使用 `Flask` 或 `FastAPI` 建立 RESTful API：

**API 端點設計**:
```
GET    /api/tasks          # 取得所有任務
POST   /api/tasks          # 新增任務
GET    /api/tasks/{id}     # 取得特定任務
PUT    /api/tasks/{id}     # 更新任務
DELETE /api/tasks/{id}     # 刪除任務
GET    /api/tasks/search?q=keyword  # 搜尋任務
GET    /api/statistics     # 取得統計資訊
```

**範例實作 (Flask)**:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)
manager = TodoManager()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [t.to_dict() for t in manager.tasks]
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = manager.add_task(**data)
    return jsonify(task.to_dict()), 201
```

### 8.3 資料庫版本

使用 SQLite 儲存資料：

**資料表設計**:
```sql
CREATE TABLE tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT CHECK(priority IN ('High', 'Medium', 'Low')),
    status TEXT CHECK(status IN ('Pending', 'InProgress', 'Completed')),
    created_date TEXT,
    due_date TEXT,
    tags TEXT  -- 儲存為 JSON 陣列字串
);

CREATE INDEX idx_priority ON tasks(priority);
CREATE INDEX idx_status ON tasks(status);
```

**使用 sqlite3 模組**:
```python
import sqlite3

class TodoManager:
    def __init__(self, db_file="todos.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def add_task(self, title, description="", priority="Medium"):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (id, title, description, priority, status, created_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (task_id, title, description, priority, "Pending", now))
        self.conn.commit()
```

### 8.4 雲端同步版本

整合 Google Drive API 或 Dropbox API：

**功能需求**:
- 自動上傳資料至雲端
- 多裝置同步
- 衝突解決機制

**技術要點**:
```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

class CloudSync:
    def __init__(self):
        self.service = build('drive', 'v3', credentials=creds)

    def upload_file(self, file_path):
        # 上傳檔案至 Google Drive
        pass

    def download_file(self, file_id):
        # 從 Google Drive 下載檔案
        pass
```

### 8.5 自然語言輸入

使用正則表達式解析自然語言輸入：

**範例**:
```
輸入: "明天下午5點前完成Python作業 #work #urgent"
解析結果:
- title: "完成Python作業"
- due_date: 2025-10-09 17:00:00
- tags: ["work", "urgent"]
```

**實作提示**:
```python
import re
from datetime import datetime, timedelta

def parse_natural_language(text):
    # 解析標籤
    tags = re.findall(r'#(\w+)', text)

    # 解析時間
    if '明天' in text:
        due_date = datetime.now() + timedelta(days=1)

    # 移除標籤與時間，剩下的就是標題
    title = re.sub(r'#\w+', '', text)
    title = re.sub(r'明天|下午|點前', '', title).strip()

    return title, due_date, tags
```

---

## 九、學習資源 | Learning Resources

### 9.1 官方文件

- **json 模組**: https://docs.python.org/3/library/json.html
- **csv 模組**: https://docs.python.org/3/library/csv.html
- **pathlib 模組**: https://docs.python.org/3/library/pathlib.html
- **datetime 模組**: https://docs.python.org/3/library/datetime.html
- **uuid 模組**: https://docs.python.org/3/library/uuid.html

### 9.2 延伸閱讀

1. **檔案 I/O 最佳實踐**
   - Context Manager 的使用 (`with` 語句)
   - 編碼問題處理 (UTF-8)
   - 大檔案讀寫優化

2. **資料序列化格式比較**
   - JSON vs CSV vs XML vs YAML
   - Pickle 的使用時機與風險
   - Protocol Buffers 簡介

3. **跨平台開發注意事項**
   - 路徑分隔符號差異
   - 換行符號差異 (`\n` vs `\r\n`)
   - 檔案權限管理

### 9.3 相關專案參考

- **Todoist**: https://todoist.com (專業待辦事項應用)
- **Microsoft To Do**: https://todo.microsoft.com
- **Taskwarrior**: https://taskwarrior.org (CLI 待辦事項工具)

---

## 十、總結 | Summary

本專案整合了 **Ch23-26** 的核心知識，透過實作一個完整的待辦事項管理系統，學生將掌握：

1. **檔案持久化**: 使用 JSON 儲存與讀取結構化資料
2. **路徑管理**: 使用 pathlib 進行跨平台路徑操作
3. **錯誤處理**: 實作健全的錯誤處理與資料備份機制
4. **資料匯出**: 將資料匯出為 CSV 格式以便分析
5. **系統設計**: 設計可維護、可擴展的應用程式架構

完成本專案後，學生將具備開發**資料驅動型應用程式**的能力，為後續學習資料庫、Web 開發等進階主題奠定基礎。

---

**專案版本**: v1.0
**最後更新**: 2025-10-08
**維護者**: iSpan Python 教學團隊
