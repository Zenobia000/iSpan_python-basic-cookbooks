# Chapter 30: 版本控制基礎 | Version Control Basics

## 📚 章節資訊（Chapter Information）

| 項目 | 內容 |
|:-----|:-----|
| **學習時數** | 4 小時（2 小時理論 + 2 小時實作） |
| **難度等級** | ⭐⭐⭐☆☆ (中階) |
| **先備知識** | Chapter 27 (模組與套件), Chapter 28 (虛擬環境), 基本命令列操作 |
| **相關章節** | Chapter 27 (模組與套件), Chapter 28 (套件管理), Chapter 29 (程式碼風格) |

---

## 🎯 學習目標（Learning Objectives）

完成本章後,學習者應能夠:

### 知識面（Knowledge）
- **列出** Git 的基本指令與用途
- **定義** repository, commit, branch, merge 的概念
- **說明** .gitignore 的作用與格式

### 理解面（Comprehension）
- **解釋** 為什麼需要版本控制系統
- **比較** 集中式與分散式版本控制的差異
- **歸納** Git 工作流程（工作區→暫存區→倉庫）

### 應用面（Application）
- **運用** git add, commit, push, pull 等基本指令
- **實作** 分支（branch）的建立、切換與合併
- **解決** 簡單的合併衝突（merge conflict）

### 分析面（Analysis）
- **分析** commit 歷史找出問題發生點
- **診斷** 常見的 Git 錯誤（detached HEAD, merge conflict）
- **選擇** 適合專案的分支策略（feature branch, git flow）

---

## 🔑 核心概念（Key Concepts）

### 概念地圖
```
版本控制基礎
├── Git 基礎概念
│   ├── Repository（倉庫）
│   ├── Commit（提交）
│   ├── Branch（分支）
│   └── 工作流程（工作區→暫存區→倉庫）
│
├── 基本操作
│   ├── git init（初始化）
│   ├── git add（暫存）
│   ├── git commit（提交）
│   ├── git status（狀態）
│   └── git log（歷史）
│
├── 分支管理
│   ├── git branch（建立分支）
│   ├── git checkout/switch（切換分支）
│   ├── git merge（合併分支）
│   └── 解決衝突
│
├── 遠端協作
│   ├── git clone（複製）
│   ├── git push（推送）
│   ├── git pull（拉取）
│   └── GitHub 基本操作
│
└── .gitignore
    ├── 忽略模式（wildcards）
    ├── Python 專案常見設定
    └── 系統檔案排除
```

### First Principles 解析

#### 為什麼需要版本控制？
**根本問題**: 如何追蹤程式碼的變更歷史？

**沒有版本控制的困境**:
```
project_final.py
project_final_v2.py
project_final_v2_modified.py
project_final_v3_really_final.py
project_final_v3_really_final_FIXED.py  # 😱
```

**版本控制的解決方案**:
```bash
# 清晰的歷史記錄
git log --oneline
a3f2c1b Add user authentication
b5d4e2a Fix database connection bug
c7f6g3h Implement login feature
d9h8i4j Initial commit
```

**推導過程**:
1. 程式需要修改 → 需要保留歷史版本
2. 歷史需要管理 → 需要系統化記錄
3. 記錄需要查詢 → 需要版本控制系統
4. 多人協作 → 需要分支與合併機制

#### 為什麼選擇 Git？
**根本問題**: 集中式 vs 分散式版本控制

**集中式（SVN）**:
```
中央伺服器（Single Point of Failure）
    ↑↓
開發者 A, B, C（必須連網）
```

**分散式（Git）**:
```
每個開發者都有完整歷史
A ←→ B ←→ C
    ↕
GitHub/GitLab（遠端備份）
```

---

## 📖 重要術語（中英對照）

| 中文 | English | 定義 |
|:-----|:--------|:-----|
| 倉庫 | Repository | 專案的版本控制資料庫（.git 資料夾） |
| 提交 | Commit | 一次程式碼變更的快照 |
| 分支 | Branch | 獨立的開發線，可平行進行 |
| 合併 | Merge | 將兩個分支的變更整合在一起 |
| 衝突 | Conflict | 兩個分支修改同一處導致的問題 |
| 暫存區 | Staging Area | commit 前的中繼區域 |
| 工作區 | Working Directory | 實際編輯檔案的目錄 |
| 遠端 | Remote | 託管在伺服器的倉庫（如 GitHub） |
| 克隆 | Clone | 複製遠端倉庫到本地 |
| 推送 | Push | 將本地 commit 上傳到遠端 |
| 拉取 | Pull | 從遠端下載最新變更 |
| HEAD | HEAD | 指向當前分支最新 commit 的指標 |

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
1. **預習**（30 min）: 閱讀本 README,了解版本控制概念
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
- [ ] 能初始化 Git 倉庫（git init）
- [ ] 能添加檔案到暫存區（git add）
- [ ] 能提交變更（git commit）
- [ ] 能查看狀態與歷史（git status, git log）
- [ ] 能建立 .gitignore 忽略不需要的檔案

### 進階能力
- [ ] 能建立與切換分支（git branch, git checkout）
- [ ] 能合併分支（git merge）
- [ ] 能解決簡單的合併衝突
- [ ] 能撤銷變更（git restore, git reset）

### 應用能力
- [ ] 能使用 GitHub 進行遠端協作
- [ ] 能實施功能分支工作流程
- [ ] 能閱讀與理解 commit 歷史
- [ ] 能為專案建立完整的 Git 設定

---

## 📝 理論重點（Key Theoretical Points）

### 1. Git 工作流程
```
工作區（Working Directory）
    ↓  git add
暫存區（Staging Area）
    ↓  git commit
本地倉庫（Local Repository）
    ↓  git push
遠端倉庫（Remote Repository - GitHub）
```

### 2. Git 基本指令
```bash
# 初始化
git init                    # 建立新倉庫
git clone <url>             # 複製遠端倉庫

# 基本操作
git status                  # 查看狀態
git add <file>              # 添加到暫存區
git add .                   # 添加所有變更
git commit -m "message"     # 提交變更
git log                     # 查看歷史
git log --oneline           # 簡潔歷史

# 分支操作
git branch                  # 列出分支
git branch <name>           # 建立分支
git checkout <name>         # 切換分支
git switch <name>           # 切換分支（新語法）
git merge <branch>          # 合併分支
git branch -d <name>        # 刪除分支

# 遠端操作
git remote add origin <url> # 添加遠端
git push origin main        # 推送到遠端
git pull origin main        # 從遠端拉取
```

### 3. .gitignore 範例
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/

# Jupyter
.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp
*.swo

# 系統檔案
.DS_Store
Thumbs.db

# 專案特定
config/secrets.py
*.log
data/
*.sqlite3
```

### 4. Commit Message 慣例
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type**:
- `feat`: 新功能
- `fix`: 修復 bug
- `docs`: 文件變更
- `style`: 格式調整（不影響功能）
- `refactor`: 重構程式碼
- `test`: 測試相關
- `chore`: 雜項（如更新依賴）

**範例**:
```
feat(auth): add user login functionality

- Implement login form validation
- Add JWT token generation
- Create user session management

Closes #123
```

---

## 🎓 教學建議（Teaching Tips）

### 授課要點
1. **視覺化教學**:
   - 使用圖表展示 Git 工作流程
   - 展示 Git Graph（VS Code 擴充功能）
   - 畫出分支合併示意圖

2. **實際操作演示**:
   - 現場建立 Git 專案
   - 故意製造合併衝突並解決
   - 展示 GitHub 介面操作

3. **團隊協作情境**:
   - 模擬多人開發情境
   - 強調 commit message 的重要性
   - 分享業界最佳實務

### 常見學生困難點

#### 困難點 1: 不理解工作區/暫存區/倉庫的區別
**症狀**: 不知道何時用 git add, git commit

**解決方法**:
```bash
# 視覺化三個區域
工作區（你編輯的檔案）
    ↓ git add（拍照準備）
暫存區（準備提交的檔案）
    ↓ git commit（正式提交）
本地倉庫（歷史記錄）

# 實際操作
echo "Hello" > test.txt        # 工作區變更
git status                      # 顯示 "Untracked files"
git add test.txt                # 移到暫存區
git status                      # 顯示 "Changes to be committed"
git commit -m "Add test.txt"    # 提交到倉庫
git status                      # 顯示 "nothing to commit"
```

#### 困難點 2: 合併衝突（Merge Conflict）
**症狀**: 看到 `<<<<<<< HEAD` 不知所措

**解決方法**:
```bash
# 衝突標記說明
<<<<<<< HEAD
當前分支的內容
=======
要合併進來的分支內容
>>>>>>> branch-name

# 解決步驟
# 1. 編輯檔案，移除標記，保留想要的內容
# 2. git add <file>
# 3. git commit -m "Resolve merge conflict"
```

#### 困難點 3: Detached HEAD State
**症狀**: `You are in 'detached HEAD' state`

**解決方法**:
```bash
# 發生原因：直接 checkout 到某個 commit
git checkout a3f2c1b  # 進入 detached HEAD

# 解決方案 1: 回到分支
git checkout main

# 解決方案 2: 從這裡建立新分支
git checkout -b new-branch-from-here
```

---

## 💡 學習技巧（Learning Strategies）

### 記憶口訣
- **Git 三區**: 工作區（改檔案）→ 暫存區（拍照）→ 倉庫（存檔）
- **分支三步**: 建立（branch）→ 切換（checkout）→ 合併（merge）
- **遠端三動作**: 克隆（clone）→ 拉取（pull）→ 推送（push）

### 實作練習建議
1. **個人專案練習**: 為之前的專案建立 Git 倉庫
2. **分支練習**: 建立功能分支並合併
3. **GitHub 練習**: 上傳專案到 GitHub

### 常用指令速查
```bash
# 快速查看狀態
git status -s

# 圖形化歷史
git log --graph --oneline --all

# 查看變更
git diff
git diff --staged

# 撤銷操作
git restore <file>              # 撤銷工作區變更
git restore --staged <file>     # 取消暫存
git reset --soft HEAD~1         # 撤銷最後一次 commit（保留變更）
git reset --hard HEAD~1         # 撤銷最後一次 commit（丟棄變更）
```

---

## 🔗 延伸資源（Additional Resources）

### Git 官方文件
- [Pro Git Book](https://git-scm.com/book/zh-tw/v2)（繁體中文）
- [Git Reference](https://git-scm.com/docs)
- [GitHub Docs](https://docs.github.com/)

### 推薦閱讀
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Git Guides](https://github.com/git-guides)
- [Oh My Git!](https://ohmygit.org/)（互動式學習遊戲）

### 視覺化工具
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - VS Code 擴充功能
- [GitKraken](https://www.gitkraken.com/) - GUI 工具
- [Sourcetree](https://www.sourcetreeapp.com/) - 免費 Git GUI

### 延伸主題（進階學習）
- Git Flow 工作流程
- Git Rebase vs Merge
- Git Hooks（自動化腳本）
- Conventional Commits 規範
- GitHub Actions（CI/CD）
- Git Submodules（子模組）

---

## ❓ 常見問題（FAQ）

**Q1: Git 和 GitHub 有什麼區別？**
A: Git 是版本控制系統（軟體），GitHub 是託管 Git 倉庫的平台（網站）。類似的平台還有 GitLab, Bitbucket。

**Q2: 什麼時候應該 commit？**
A: 每完成一個小功能或修正一個 bug 就 commit。原則：每個 commit 應該是一個「原子性」的變更。

**Q3: commit message 寫中文還是英文？**
A: 團隊內部專案可用中文，開源專案建議英文。重點是清晰描述變更內容。

**Q4: 不小心 commit 了機密資訊怎麼辦？**
A:
```bash
# 如果還沒 push
git reset --soft HEAD~1  # 撤銷 commit
# 移除機密檔案，加入 .gitignore
git commit -m "Remove sensitive data"

# 如果已經 push（嚴重！）
# 1. 立即更改機密資訊（如密碼）
# 2. 使用 git filter-branch 或 BFG Repo-Cleaner 清除歷史
# 3. force push（會改寫歷史，需謹慎）
```

**Q5: 如何選擇 merge 還是 rebase？**
A: 新手建議使用 merge。Rebase 會改寫歷史，適合在 push 前整理 commit。原則：**公開的分支不要 rebase**。

---

## 📊 本章與課程架構的關係

### 前置章節
- **Chapter 27（模組與套件）**: Git 管理多檔案專案
- **Chapter 28（虛擬環境）**: .gitignore 忽略 venv/
- **Chapter 29（程式碼風格）**: commit 前確保程式碼品質

### 後續章節
- **Milestone 8: 專案重構**（結合 Ch27-30 的知識）

### 實際應用
- 所有後續專案都應使用 Git 進行版本控制
- GitHub 可作為作業繳交平台
- 團隊專案的協作基礎

---

## 📝 版本記錄（Version History）
- **v1.0** (2025-10-05): 初版發布,基於教科書標準結構

---

## 🎯 成功標準（Success Criteria）

完成本章學習後,您應該能夠:
- ✅ 獨立完成課後習題（正確率 ≥ 80%）
- ✅ 通過自我測驗（分數 ≥ 70 分）
- ✅ 能為專案建立 Git 倉庫並提交 5 次以上
- ✅ 能解決簡單的合併衝突
- ✅ 能將專案上傳到 GitHub

---

**學習提醒**: Git 是現代軟體開發的必備技能。不要害怕犯錯，Git 的設計就是讓你可以安全地實驗！從今天開始，為每個專案使用 Git 吧！
