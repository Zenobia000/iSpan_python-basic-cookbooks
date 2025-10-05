# Milestone 3: 學生成績管理系統 | Student Grade Management System

## 專案資訊 | Project Information

| 項目 | 內容 |
|:-----|:-----|
| **整合章節** | Ch07-Ch11 |
| **預計時數** | 6-8 小時 |
| **難度等級** | ⭐⭐⭐ (中級) |
| **專案類型** | 命令列應用程式 (CLI Application) |

---

## 專案目標 | Project Objectives

### 整合知識點
本專案整合以下章節的核心概念：

- **Ch07 列表 (Lists)**: 儲存多個學生資料
- **Ch08 元組 (Tuples)**: 不可變的成績記錄
- **Ch09 字串 (Strings)**: 格式化輸出與資料驗證
- **Ch10 字典 (Dictionaries)**: 學生資訊的鍵值對應
- **Ch11 集合與推導式 (Sets & Comprehensions)**: 資料去重與快速處理

### 學習目標
1. **資料結構設計**: 選擇合適的資料結構解決實際問題
2. **CRUD 操作**: 實作完整的增刪改查功能
3. **資料驗證**: 處理使用者輸入的各種錯誤情況
4. **統計分析**: 運用列表/字典方法進行資料分析
5. **程式架構**: 建立模組化、可維護的程式結構

---

## 專案描述 | Project Description

### 系統概述
設計一個**學生成績管理系統**，讓使用者能夠透過命令列介面管理學生資料，包括新增、查詢、修改、刪除學生資訊，並提供成績統計分析功能。

### 核心功能

#### 1. 學生管理 (CRUD)
- **新增學生**: 輸入學號、姓名、成績（可多科）
- **查詢學生**: 透過學號或姓名查詢成績
- **修改成績**: 更新學生的成績資料
- **刪除學生**: 從系統中移除學生記錄
- **顯示所有**: 列出所有學生的完整資訊

#### 2. 統計分析
- **班級平均**: 計算所有學生的平均成績
- **最高/最低分**: 找出成績的極值與對應學生
- **及格率統計**: 計算及格人數與百分比
- **成績排名**: 依成績由高到低排序
- **分數分布**: 統計各分數區間的人數

#### 3. 資料結構設計
```python
# 學生資料結構 (使用字典)
student = {
    "student_id": "A001",        # 學號 (唯一識別碼)
    "name": "張小明",             # 姓名
    "grades": [85, 92, 78, 88],  # 成績列表 (可多科)
}

# 班級資料結構 (使用列表)
classroom = [student1, student2, student3, ...]
```

#### 4. 操作介面
```
╔══════════════════════════════════════╗
║   學生成績管理系統 v1.0              ║
╚══════════════════════════════════════╝

【主選單】
1. 新增學生
2. 查詢成績
3. 修改成績
4. 刪除學生
5. 統計分析
6. 顯示所有學生
0. 結束程式

請選擇功能 (0-6):
```

---

## 學習成果 | Learning Outcomes

### 知識層面 (Knowledge)
- ✅ 理解不同資料結構的適用場景
- ✅ 掌握列表、字典、集合的操作方法
- ✅ 了解資料驗證的重要性

### 技能層面 (Skills)
- ✅ 設計合理的資料結構
- ✅ 實作完整的 CRUD 功能
- ✅ 使用推導式簡化程式碼
- ✅ 處理使用者輸入錯誤
- ✅ 運用內建函式進行統計分析

### 態度層面 (Attitude)
- ✅ 重視程式碼的可讀性與維護性
- ✅ 注重使用者體驗與錯誤處理
- ✅ 培養問題分析與解決能力

---

## 開發指南 | Development Guide

### 階段 1: 基本資料結構建立 (2 小時)

#### 步驟 1.1: 定義資料結構
```python
# 學生列表（全域變數）
students = []

# 學生字典範例
example_student = {
    "student_id": "A001",
    "name": "張小明",
    "grades": [85, 92, 78]
}
```

#### 步驟 1.2: 建立選單系統
```python
def display_menu():
    """顯示主選單"""
    print("\n" + "="*40)
    print("  學生成績管理系統")
    print("="*40)
    print("1. 新增學生")
    print("2. 查詢成績")
    # ... 其他選項
```

#### 步驟 1.3: 主程式迴圈
```python
def main():
    while True:
        display_menu()
        choice = input("請選擇功能: ")
        if choice == "0":
            break
        # 處理其他選項
```

**✅ 檢查點**:
- [ ] 能夠顯示選單並接收使用者輸入
- [ ] 選擇 0 能正常結束程式

---

### 階段 2: CRUD 功能實作 (3 小時)

#### 步驟 2.1: 新增學生 (Create)
```python
def add_student(students):
    """新增學生資料"""
    # 1. 輸入學號（檢查唯一性）
    student_id = input("請輸入學號: ")

    # 2. 檢查學號是否已存在（使用集合）
    existing_ids = {s["student_id"] for s in students}
    if student_id in existing_ids:
        print("錯誤: 學號已存在！")
        return

    # 3. 輸入姓名
    name = input("請輸入姓名: ")

    # 4. 輸入成績（可多科）
    grades = []
    while True:
        grade_input = input("請輸入成績 (輸入 q 結束): ")
        if grade_input.lower() == 'q':
            break
        # 驗證成績範圍 (0-100)
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("成績必須在 0-100 之間！")
        except ValueError:
            print("請輸入有效的數字！")

    # 5. 建立學生字典並加入列表
    student = {
        "student_id": student_id,
        "name": name,
        "grades": grades
    }
    students.append(student)
    print(f"✓ 成功新增學生: {name} ({student_id})")
```

#### 步驟 2.2: 查詢學生 (Read)
```python
def query_student(students):
    """查詢學生成績"""
    keyword = input("請輸入學號或姓名: ")

    # 使用列表推導式查找
    results = [s for s in students
               if keyword in s["student_id"] or keyword in s["name"]]

    if not results:
        print("查無此學生！")
        return

    for student in results:
        print(f"\n學號: {student['student_id']}")
        print(f"姓名: {student['name']}")
        print(f"成績: {student['grades']}")
        if student['grades']:
            avg = sum(student['grades']) / len(student['grades'])
            print(f"平均: {avg:.2f}")
```

#### 步驟 2.3: 修改成績 (Update)
```python
def update_grade(students):
    """修改學生成績"""
    student_id = input("請輸入要修改的學號: ")

    # 查找學生
    for student in students:
        if student["student_id"] == student_id:
            print(f"當前成績: {student['grades']}")

            # 輸入新成績
            new_grades = []
            while True:
                grade_input = input("請輸入新成績 (輸入 q 結束): ")
                if grade_input.lower() == 'q':
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        new_grades.append(grade)
                    else:
                        print("成績必須在 0-100 之間！")
                except ValueError:
                    print("請輸入有效的數字！")

            student["grades"] = new_grades
            print("✓ 成績已更新！")
            return

    print("查無此學生！")
```

#### 步驟 2.4: 刪除學生 (Delete)
```python
def delete_student(students):
    """刪除學生資料"""
    student_id = input("請輸入要刪除的學號: ")

    for i, student in enumerate(students):
        if student["student_id"] == student_id:
            confirm = input(f"確定要刪除 {student['name']} 嗎? (y/n): ")
            if confirm.lower() == 'y':
                students.pop(i)
                print("✓ 學生已刪除！")
            return

    print("查無此學生！")
```

#### 步驟 2.5: 顯示所有學生
```python
def show_all_students(students):
    """顯示所有學生資訊"""
    if not students:
        print("目前沒有學生資料！")
        return

    print("\n" + "="*60)
    print(f"{'學號':<10} {'姓名':<10} {'成績':<20} {'平均':<10}")
    print("="*60)

    for student in students:
        grades_str = str(student['grades'])
        if student['grades']:
            avg = sum(student['grades']) / len(student['grades'])
            print(f"{student['student_id']:<10} {student['name']:<10} "
                  f"{grades_str:<20} {avg:<10.2f}")
        else:
            print(f"{student['student_id']:<10} {student['name']:<10} "
                  f"{grades_str:<20} {'N/A':<10}")
```

**✅ 檢查點**:
- [ ] 能新增學生並儲存到列表
- [ ] 能查詢學生並顯示資訊
- [ ] 能修改學生成績
- [ ] 能刪除學生記錄
- [ ] 能顯示所有學生

---

### 階段 3: 統計分析功能 (2-3 小時)

#### 步驟 3.1: 計算班級平均
```python
def calculate_class_average(students):
    """計算班級平均成績"""
    # 使用推導式取得所有成績
    all_grades = [grade for student in students
                  for grade in student['grades']]

    if not all_grades:
        print("目前沒有成績資料！")
        return

    avg = sum(all_grades) / len(all_grades)
    print(f"班級平均成績: {avg:.2f}")
    print(f"總成績數: {len(all_grades)} 筆")
```

#### 步驟 3.2: 找出最高/最低分
```python
def find_extremes(students):
    """找出最高分與最低分"""
    all_grades = [grade for student in students
                  for grade in student['grades']]

    if not all_grades:
        print("目前沒有成績資料！")
        return

    max_grade = max(all_grades)
    min_grade = min(all_grades)

    print(f"最高分: {max_grade}")
    print(f"最低分: {min_grade}")

    # 找出對應學生
    for student in students:
        if max_grade in student['grades']:
            print(f"  最高分學生: {student['name']} ({student['student_id']})")
        if min_grade in student['grades']:
            print(f"  最低分學生: {student['name']} ({student['student_id']})")
```

#### 步驟 3.3: 及格率統計
```python
def calculate_pass_rate(students):
    """計算及格率 (60分以上)"""
    all_grades = [grade for student in students
                  for grade in student['grades']]

    if not all_grades:
        print("目前沒有成績資料！")
        return

    pass_count = sum(1 for grade in all_grades if grade >= 60)
    pass_rate = (pass_count / len(all_grades)) * 100

    print(f"及格人次: {pass_count} / {len(all_grades)}")
    print(f"及格率: {pass_rate:.2f}%")
```

#### 步驟 3.4: 成績排名
```python
def show_ranking(students):
    """顯示成績排名"""
    # 計算每位學生的平均成績
    student_averages = []
    for student in students:
        if student['grades']:
            avg = sum(student['grades']) / len(student['grades'])
            student_averages.append({
                "student_id": student['student_id'],
                "name": student['name'],
                "average": avg
            })

    # 排序（由高到低）
    student_averages.sort(key=lambda x: x['average'], reverse=True)

    print("\n成績排名:")
    print("="*50)
    print(f"{'排名':<6} {'學號':<10} {'姓名':<10} {'平均成績':<10}")
    print("="*50)

    for rank, student in enumerate(student_averages, 1):
        print(f"{rank:<6} {student['student_id']:<10} "
              f"{student['name']:<10} {student['average']:<10.2f}")
```

#### 步驟 3.5: 分數分布
```python
def show_grade_distribution(students):
    """顯示分數分布"""
    all_grades = [grade for student in students
                  for grade in student['grades']]

    if not all_grades:
        print("目前沒有成績資料！")
        return

    # 定義分數區間
    ranges = {
        "90-100": 0,
        "80-89": 0,
        "70-79": 0,
        "60-69": 0,
        "0-59": 0
    }

    for grade in all_grades:
        if 90 <= grade <= 100:
            ranges["90-100"] += 1
        elif 80 <= grade <= 89:
            ranges["80-89"] += 1
        elif 70 <= grade <= 79:
            ranges["70-79"] += 1
        elif 60 <= grade <= 69:
            ranges["60-69"] += 1
        else:
            ranges["0-59"] += 1

    print("\n分數分布:")
    print("="*40)
    for range_name, count in ranges.items():
        percentage = (count / len(all_grades)) * 100
        bar = "█" * (count // 2)  # 簡易長條圖
        print(f"{range_name}: {count:3d} ({percentage:5.1f}%) {bar}")
```

**✅ 檢查點**:
- [ ] 能計算班級平均成績
- [ ] 能找出最高/最低分
- [ ] 能統計及格率
- [ ] 能顯示成績排名
- [ ] 能顯示分數分布

---

## 評分標準 | Grading Rubric

### 基本功能 (60%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 新增學生 | 15% | - 能正確新增學生資料 (5%)<br>- 檢查學號唯一性 (5%)<br>- 驗證成績範圍 (5%) |
| 查詢學生 | 10% | - 能透過學號查詢 (5%)<br>- 能透過姓名查詢 (5%) |
| 修改成績 | 15% | - 能找到學生並修改 (10%)<br>- 有確認機制 (5%) |
| 刪除學生 | 10% | - 能正確刪除學生 (5%)<br>- 有確認機制 (5%) |
| 顯示所有 | 10% | - 格式化輸出 (5%)<br>- 顯示完整資訊 (5%) |

### 統計功能 (20%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 班級平均 | 5% | 正確計算平均成績 |
| 最高/最低分 | 5% | 找出極值與對應學生 |
| 及格率 | 5% | 正確計算及格率 |
| 成績排名 | 5% | 正確排序並顯示 |

### 程式品質 (20%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 程式結構 | 7% | - 函式化設計 (4%)<br>- 邏輯清晰 (3%) |
| 註解說明 | 6% | - 函式有文件字串 (3%)<br>- 關鍵邏輯有註解 (3%) |
| 錯誤處理 | 7% | - 輸入驗證 (4%)<br>- 例外處理 (3%) |

---

## 教學建議 | Teaching Tips

### 評分重點

#### 1. 資料結構設計 (關鍵)
- ✅ **正確**: 使用字典儲存學生資訊，列表儲存成績
- ❌ **錯誤**: 使用多個獨立列表分別儲存學號、姓名、成績

#### 2. 學號唯一性檢查
- ✅ **優秀**: 使用集合推導式 `{s["student_id"] for s in students}`
- ⭐ **良好**: 使用迴圈逐一檢查
- ❌ **不佳**: 沒有檢查，允許重複學號

#### 3. 資料驗證
- ✅ **優秀**: 使用 try-except 處理，並驗證範圍
- ⭐ **良好**: 使用 if-else 驗證範圍
- ❌ **不佳**: 沒有任何驗證

#### 4. 推導式使用
- ✅ **優秀**: 使用推導式簡化程式碼
  ```python
  all_grades = [g for s in students for g in s['grades']]
  ```
- ⭐ **良好**: 使用傳統迴圈
  ```python
  all_grades = []
  for student in students:
      for grade in student['grades']:
          all_grades.append(grade)
  ```

### 常見問題與解決方案

#### 問題 1: 學生找不到時沒有提示
**解決方案**: 在所有查詢、修改、刪除函式中加入 `else` 處理
```python
for student in students:
    if student["student_id"] == student_id:
        # 處理邏輯
        return
else:  # 迴圈正常結束表示沒找到
    print("查無此學生！")
```

#### 問題 2: 空列表除以零錯誤
**解決方案**: 在統計函式開頭檢查資料是否為空
```python
if not students or not all_grades:
    print("目前沒有資料！")
    return
```

#### 問題 3: 選單無法重複執行
**解決方案**: 確保主程式使用 `while True` 迴圈
```python
def main():
    while True:
        choice = input("請選擇: ")
        if choice == "0":
            break
```

### 教學時間分配建議

| 階段 | 時間 | 內容 |
|:-----|:-----|:-----|
| **講解示範** | 1.5 小時 | 資料結構設計、CRUD 基本概念 |
| **實作指導** | 2 小時 | 階段 1-2 帶領開發 |
| **獨立開發** | 3 小時 | 學生完成階段 3 與測試 |
| **討論分享** | 1 小時 | 程式碼 Review、最佳實踐分享 |

---

## 延伸挑戰 | Extension Challenges

### 挑戰 1: 多科目管理 ⭐⭐
將成績從簡單列表改為**字典結構**，支援多科目：
```python
student = {
    "student_id": "A001",
    "name": "張小明",
    "grades": {
        "國文": 85,
        "英文": 92,
        "數學": 78
    }
}
```

**新增功能**:
- 按科目查詢成績
- 計算各科平均
- 找出每科最高分

### 挑戰 2: 檔案存取 (結合 Ch23) ⭐⭐⭐
將資料儲存到檔案，實現持久化：
```python
import json

def save_to_file(students, filename="students.json"):
    """儲存學生資料到 JSON 檔案"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def load_from_file(filename="students.json"):
    """從 JSON 檔案讀取學生資料"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
```

### 挑戰 3: 資料視覺化 ⭐⭐⭐⭐
使用簡易字元繪製圖表：
```python
def draw_bar_chart(students):
    """繪製成績分布長條圖"""
    # 使用 ASCII 字元繪製
    # 範例輸出:
    # 90-100: ████████ (8)
    # 80-89:  ████████████ (12)
    # 70-79:  ██████ (6)
```

### 挑戰 4: 匯出報表 ⭐⭐⭐
產生 CSV 格式的成績報表：
```python
import csv

def export_to_csv(students, filename="report.csv"):
    """匯出成績報表到 CSV 檔案"""
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['學號', '姓名', '平均成績', '排名'])
        # 寫入資料...
```

### 挑戰 5: 進階統計 ⭐⭐⭐⭐
實作更多統計功能：
- 計算標準差 (Standard Deviation)
- 計算中位數 (Median)
- 四分位數分析 (Quartiles)
- 成績趨勢分析（如果有多次考試）

---

## 相關資源 | Related Resources

### 複習章節
- **Ch07**: 列表操作、切片、方法
- **Ch08**: 元組的不可變特性
- **Ch09**: 字串格式化、驗證
- **Ch10**: 字典操作、鍵值對應
- **Ch11**: 集合去重、列表推導式

### 延伸閱讀
- [Python 官方文件 - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Dictionaries in Python](https://realpython.com/python-dicts/)
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)

### 參考專案
- Simple Student Management System
- Grade Calculator CLI
- Data Analysis with Python

---

## 檢核清單 | Checklist

開發完成前，請確認以下項目：

### 功能檢核
- [ ] 所有 CRUD 功能正常運作
- [ ] 統計分析功能正確計算
- [ ] 選單系統流暢運作
- [ ] 能正常結束程式

### 品質檢核
- [ ] 所有函式有文件字串
- [ ] 關鍵邏輯有註解說明
- [ ] 有完整的輸入驗證
- [ ] 有錯誤處理機制

### 測試檢核
- [ ] 測試新增重複學號
- [ ] 測試輸入無效成績
- [ ] 測試刪除不存在的學生
- [ ] 測試空資料情況

---

**祝開發順利！**
