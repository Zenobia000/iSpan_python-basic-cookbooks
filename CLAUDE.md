# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**iSpan_python-basic-cookbooks** is a comprehensive Python learning curriculum designed for absolute beginners (零基礎學習者). The repository follows a **textbook-style structure** based on First Principles → Fundamentals → Body of Knowledge framework, with all materials in **Traditional Chinese (繁體中文)**.

## New Curriculum Architecture (v2.0)

The repository has been restructured following university-level computer science textbook standards:

### Core Structure
```
fundamentals/          # 30 chapters (ch01-ch30), each self-contained
milestones/           # 8 project-based assessments
curriculum/           # Course design & teaching guides
resources/            # Cheatsheets, references, tools
legacy/              # Original Module2-9 (preserved for reference)
```

### Chapter Organization (Fundamentals)
Each chapter (e.g., `fundamentals/ch01-variables-and-types/`) contains:

| File | Purpose | Format |
|:-----|:--------|:-------|
| `README.md` | Chapter overview, learning objectives, concepts | Textbook-style guide |
| `01-lecture.ipynb` | Main lecture with theory & examples | Jupyter Notebook |
| `02-worked-examples.ipynb` | Step-by-step solved problems | Jupyter Notebook |
| `03-practice.ipynb` | In-class exercises | Jupyter Notebook |
| `04-exercises.ipynb` | Homework problems | Jupyter Notebook |
| `05-solutions.ipynb` | Complete solutions | Jupyter Notebook |
| `quiz.ipynb` | Self-assessment quiz | Jupyter Notebook |

### Milestone Projects
Each milestone (e.g., `milestones/milestone01-calculator/`) includes:
- `README.md`: Project description, requirements, rubric
- `requirements.ipynb`: Detailed specs
- `starter-code.ipynb`: Template code
- `solution.ipynb`: Reference implementation

## Pedagogical Principles

### 1. Textbook Structure
Every chapter follows this proven format:
```
📖 Learning Objectives → 🔑 Key Concepts → 📝 Theory →
💡 Worked Examples → 🛠️ Practice → 📊 Summary →
✍️ Review Questions → 💻 Exercises → 🔗 Further Reading
```

### 2. First Principles Teaching
- Start each concept with "Why does this exist?"
- Show minimal viable implementation
- Build up from fundamentals to advanced usage

### 3. Learning-Oriented Design
- **Competency-based**: Clear skill checkboxes for each chapter
- **Progressive difficulty**: Easy → Medium → Challenge
- **Immediate feedback**: Solutions provided for all exercises

## Running Code

### Jupyter Notebooks
```bash
# Launch Jupyter in the project directory
jupyter notebook

# Or use JupyterLab
jupyter lab
```

### Python Scripts
```bash
# Run individual scripts from their module directory
python Module3/practice.py
python Module9/9-1.py

# Or from project root
python -m Module3.practice
```

## Content Creation Guidelines

### When Creating New Chapters
Follow this template structure for consistency:

**README.md must include**:
1. Chapter Information (學習時數, 難度, 先備知識)
2. Learning Objectives (知識/理解/應用/分析四層次)
3. Key Concepts (概念地圖 + First Principles 解析)
4. Course Materials (檔案說明表)
5. Competency Checklist (能力檢核)
6. Teaching Tips (授課要點 + 常見困難)
7. Further Reading (延伸資源)

**Lecture Notebook (01-lecture.ipynb) structure**:
```markdown
# Part I: 理論基礎
- Chapter Overview (學習目標, 先備知識, 時長)
- Key Concepts (定義, First Principles 分析)

# Part II: 實作演練
- 範例 1-5 (由淺入深)

# Part III: 本章總結
- 知識回顧
- 常見誤區
- 自我檢核
- 延伸閱讀
```

### When Creating Milestone Projects
**README.md must include**:
1. Project Objectives (整合哪些章節)
2. Project Description (情境, 需求, 規格)
3. Learning Outcomes (知識/技能/態度)
4. Development Guide (3 階段開發步驟)
5. Grading Rubric (評分標準)
6. Teaching Tips (評分重點, 常見問題)
7. Extension Challenges (延伸挑戰)

## Language and Content Notes

- **Primary Language**: All instructional content in **Traditional Chinese (繁體中文)**
- **Code Comments**: Chinese for explanatory comments, English for variable names (following PEP 8)
- **Bilingual Terms**: Key concepts presented as "中文 | English" (e.g., "變數 | Variables")
- **Maintain Consistency**: When creating new materials, follow the textbook-style tone and structure

## Working with Legacy Content

- **Legacy folder**: Original Module2-9 preserved for reference only
- **Migration**: Gradually migrate content to new chapter structure
- **Do not modify**: Keep legacy files unchanged; create new versions in fundamentals/

## Curriculum Roadmap

### 30 Chapters Overview
```
Part I   (Ch 1-3):   Variables, Operators, I/O
Part II  (Ch 4-6):   Conditionals, Loops, Advanced Iteration
Part III (Ch 7-11):  Lists, Tuples, Strings, Dicts, Sets, Comprehensions
Part IV  (Ch 12-15): Functions, Scope, Higher-Order, Recursion
Part V   (Ch 16-19): Classes, Encapsulation, Inheritance, Special Methods
Part VI  (Ch 20-22): Exceptions, Custom Exceptions, Debugging
Part VII (Ch 23-26): File I/O, JSON, CSV, Paths
Part VIII(Ch 27-30): Modules, Packages, Style, Version Control
```

### 8 Milestones
```
M1: Calculator          (Ch 1-3)
M2: Guessing Game       (Ch 4-6)
M3: Grade System        (Ch 7-11)
M4: Text Toolkit        (Ch 12-15)
M5: Banking System      (Ch 16-19)
M6: User Registration   (Ch 20-22)
M7: Todo App            (Ch 23-26)
M8: Project Refactor    (Ch 27-30)
```

## Architecture Considerations

- **Pure Python**: No external dependencies beyond standard library and Jupyter
- **No Tests**: Intentionally no pytest/unittest; focus is on learning, not TDD
- **Sequential Learning**: Chapters build upon each other (1→2→3→...→30)
- **Self-Contained**: Each chapter can be studied independently with prerequisites noted

## Development Workflow

### Completing a Chapter or Milestone

When you finish developing a chapter or milestone, follow this workflow:

#### 1. **Content Completion Checklist**
- [ ] All required files created (7 files for chapter, 4 files for milestone)
- [ ] All code tested and working
- [ ] README.md updated
- [ ] Meets quality standards (see below)

#### 2. **Git Commit Process**
```bash
# Add changes
git add .

# Commit with standard message format
git commit -m "feat: 完成 Ch0X - 章節名稱 | Chapter Title

- 新增 README.md
- 新增 01-lecture.ipynb
- 新增 02-worked-examples.ipynb
- 新增 03-practice.ipynb
- 新增 04-exercises.ipynb
- 新增 05-solutions.ipynb
- 新增 quiz.ipynb
- X 個範例，Y 個習題

Co-Authored-By: Claude <noreply@anthropic.com>
"

# Push to GitHub
git push origin main
```

#### 3. **Update WBS and CLAUDE.md**

After each chapter/milestone completion:

1. **Update `curriculum/wbs.md`**:
   - Change GitHub status from ⏳ to ✅
   - Update completion date
   - Update progress statistics

2. **Update `CLAUDE.md`** (this file):
   - Add completed item to "Completed Chapters/Milestones" section below
   - Update overall progress percentage
   - Update any workflow changes if applicable

#### 4. **Commit Documentation Updates**
```bash
git add curriculum/wbs.md CLAUDE.md
git commit -m "docs: 更新 WBS 與 CLAUDE.md - Ch0X 完成狀態"
git push origin main
```

### Quality Standards for Completion

**Each Chapter Must Have**:
- [ ] README with complete First Principles analysis
- [ ] Lecture with 5+ examples
- [ ] Worked Examples with 3-5 detailed solutions
- [ ] Exercises with 10+ problems (basic/intermediate/challenge)
- [ ] Complete solutions
- [ ] Quiz with multiple choice + coding questions

**Each Milestone Must Have**:
- [ ] Clear functional requirements (basic + advanced)
- [ ] Complete development guide
- [ ] Grading rubric
- [ ] Teaching tips (common issues, grading focus)
- [ ] Reference solution with best practices

---

## Completed Chapters/Milestones

### ✅ Completed (Current Progress: 43.3%)

**Part I: 計算基礎 (Ch01-Ch03) - 100% 完成** ✅
- **Ch01: Variables and Data Types (變數與資料型態)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 5 個詳解範例、15 題課堂練習、20 題課後習題、30 題自我測驗

- **Ch02: Operators and Expressions (運算子與表達式)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 8 個講義範例 + 5 個詳解範例、8 題課堂練習、12 題課後習題、20 題自我測驗
  - ✅ 涵蓋算術、比較、邏輯運算子及優先順序

- **Ch03: Input/Output and Formatting (輸入輸出與格式化)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 8 個講義範例 + 5 個詳解範例、6 題課堂練習、12 題課後習題、20 題自我測驗
  - ✅ 涵蓋 print(), input(), f-string 格式化、對齊、精度

**Part II: 控制結構 (Ch04-Ch06) - 100% 完成** ✅
- **Ch04: Conditionals (條件判斷)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 8 個講義範例 + 5 個詳解範例、15 題課堂練習、20 題課後習題、25 題自我測驗
  - ✅ 涵蓋 if/elif/else、比較運算子、邏輯運算子、巢狀條件、三元運算子

- **Ch05: Loops (迴圈控制)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 12 個講義範例 + 5 個詳解範例、15 題課堂練習、20 題課後習題、25 題自我測驗
  - ✅ 涵蓋 for/while 迴圈、break/continue、巢狀迴圈、累加器模式

- **Ch06: Advanced Loop Techniques (迴圈進階技巧)** - 2025-10-05
  - ✅ 7 個檔案完整建立（README + 6 個 notebooks）
  - ✅ 10 個講義範例 + 5 個詳解範例、12 題課堂練習、15 題課後習題、20 題自我測驗
  - ✅ 涵蓋 enumerate()、zip()、迴圈模式、效能優化

**Milestones - 3/8 完成 (37.5%)** ✅
- **M01: Simple Calculator (簡易計算機)** - 2025-10-05
  - ✅ 4 個檔案完整建立
  - ✅ 整合 Ch01-Ch03 知識點

- **M02: Number Guessing Game (終極密碼遊戲)** - 2025-10-05
  - ✅ 4 個檔案完整建立（README + requirements + starter + solution）
  - ✅ 整合 Ch04-Ch06 知識點
  - ✅ 基本版 + 進階版參考解答

- **M03: Grade Management System (學生成績管理系統)** - 2025-10-05
  - ✅ 4 個檔案完整建立（README + requirements + starter + solution）
  - ✅ 整合 Ch07-Ch11 知識點
  - ✅ CRUD + 統計分析功能完整實作

**Part III: 資料結構 (Ch07-Ch11) - 100% 完成** ✅
- **Ch07: Lists (序列資料：列表)** - 2025-10-05
  - ✅ 7 個檔案完整建立
  - ✅ 12 個講義範例 + 5 個詳解範例、15 題課堂練習、20 題課後習題、25 題自我測驗

- **Ch08: Tuples and Strings (序列資料：元組與字串)** - 2025-10-05
  - ✅ 7 個檔案完整建立
  - ✅ 12 個講義範例 + 5 個詳解範例、15 題課堂練習、20 題課後習題、25 題自我測驗

- **Ch09: Dictionaries (映射資料：字典)** - 2025-10-05
  - ✅ 7 個檔案完整建立
  - ✅ 10 個講義範例 + 5 個詳解範例、15 題課堂練習、18 題課後習題、25 題自我測驗

- **Ch10: Sets (集合資料)** - 2025-10-05
  - ✅ 7 個檔案完整建立
  - ✅ 8 個講義範例 + 5 個詳解範例、12 題課堂練習、15 題課後習題、20 題自我測驗

- **Ch11: Comprehensions (推導式與生成器)** - 2025-10-05
  - ✅ 7 個檔案完整建立
  - ✅ 11 個講義範例 + 5 個詳解範例、12 題課堂練習、15 題課後習題、20 題自我測驗

**Part V: 物件導向基礎 (Ch18) - 100% 完成** ✅
- **Ch18: Inheritance and Polymorphism (繼承與多型)** - 2025-10-05
  - ✅ 7 個檔案完整 (~85KB)
  - ✅ 6 個範例 + 4 個案例 + 8 練習 + 12 習題 + 20 測驗

**Part V-VI: 物件導向進階與例外處理 (Ch19-Ch21) - 100% 完成** ✅
- **Ch19: Special Methods and Operator Overloading (特殊方法與運算子重載)** - 2025-10-05
  - ✅ 7 個檔案完整 (~151KB)
  - ✅ 7 個講義範例 + 4 個詳解案例 + 8 題課堂練習 + 12 題完整習題 + 20 題測驗

- **Ch20: Exception Handling (例外處理機制)** - 2025-10-05
  - ✅ 7 個檔案完整 (~133KB)
  - ✅ 6 個講義範例 + 4 個詳解案例 + 8 題課堂練習 + 12 題完整習題 + 20 題測驗

- **Ch21: Custom Exceptions and raise (自訂例外與 raise)** - 2025-10-05
  - ✅ 7 個檔案完整 (~140KB)
  - ✅ 5 個講義範例 + 3 個詳解案例 + 6 題課堂練習 + 10 題課後習題 + 17 題測驗

### 🔄 In Progress

**Part IV: 函式與模組化 (Ch12-Ch15) - 進行中**
- **Ch12: Function Fundamentals (函式設計基礎)** - 進行中 30%
  - ✅ README.md (17.8KB) + 01-lecture.ipynb (26.5KB) 框架完成
  - ⏳ 02-05 檔案及 quiz 待補充

- **Ch13-15: Scope, Higher-Order, Recursion** - 進行中 20-25%
  - ✅ 檔案框架已建立
  - ⏳ 內容待補充

**Part VI: 例外處理 (Ch22) - 進行中 71%**
- **Ch22: Debugging (除錯技術)** - 2025-10-05
  - ✅ README.md (21KB) + 01-lecture.ipynb (35.4KB) + 02-worked-examples (31.3KB)
  - ✅ 03-practice.ipynb (17.6KB) + 04-exercises.ipynb (23.3KB)
  - ⏳ 05-solutions.ipynb + quiz.ipynb 待補充（剩餘 9 小時）

**Part VII-VIII: 檔案處理與工程實務 (Ch23-30) - 框架 20%**
- **Ch23-30: 進階主題框架已建立** (2025-10-05)
  - Part VII: Ch23-Ch26 (檔案處理) - 28 檔案框架 ✅
  - Part VIII: Ch27-Ch30 (工程實務) - 28 檔案框架 ✅
  - **完成度: 20%** (框架完整，內容待補充)

### ⏳ Planned

**待開始章節 (12 chapters remaining)**:
- Ch16-17: 類別與物件、封裝 (Part V 基礎)
- Ch23-30: 檔案處理與工程實務 (Part VII-VIII)

**待開始專案 (5 milestones remaining)**:
- M04: 文字處理工具箱 (Ch12-15)
- M05: 銀行帳戶系統 (Ch16-19)
- M06: 使用者註冊系統 (Ch20-22)
- M07: 待辦事項管理 (Ch23-26)
- M08: 專案模組化重構 (Ch27-30)

See `curriculum/wbs.md` for complete roadmap.

---

## Key Files for Reference

- `curriculum/curriculum-design.md`: Complete course architecture documentation
- `curriculum/wbs.md`: **Work Breakdown Structure with detailed progress tracking**
- `curriculum/learning-roadmap.md`: Learning paths for different learner types
- `fundamentals/ch01-variables-and-types/`: Example chapter showing standard structure
- `milestones/milestone01-calculator/`: Example project showing standard structure
