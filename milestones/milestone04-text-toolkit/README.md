# Milestone 04: 文字處理工具箱 | Text Processing Toolkit

## 🎯 專案目標（Project Objectives）

本專案旨在整合以下章節所學：
- **Chapter 12（函式設計基礎）**：模組化設計、參數處理、返回值
- **Chapter 13（作用域與生命週期）**：變數作用域、內嵌函式
- **Chapter 14（高階函式與 Lambda）**：map/filter/reduce、函式組合
- **Chapter 15（遞迴思維）**：遞迴處理、分治法、樹狀結構

---

## 📋 專案描述（Project Description）

### 情境說明

您是一名資料分析師，經常需要處理各種文字資料。為了提高工作效率，您決定建立一個綜合性的文字處理工具箱，包含文字統計、格式化、搜尋、轉換等功能。

這個工具箱將展示函式設計的威力：透過組合簡單的函式，建構出複雜而實用的文字處理系統。

### 功能需求

#### 基本需求（必須完成 - 70分）
1. **文字統計模組**：字數、行數、詞頻統計
2. **文字搜尋模組**：關鍵字搜尋、模式匹配
3. **文字轉換模組**：大小寫轉換、字元替換
4. **文字格式化模組**：對齊、縮排、分欄顯示
5. **文字分析模組**：句子分析、重複檢測

#### 進階需求（選做 - 額外30分）
1. **遞迴檔案處理**：遞迴搜尋目錄中的文字檔案
2. **高階函式應用**：使用 map/filter/reduce 進行複雜處理
3. **文字壓縮演算法**：實作簡單的 RLE 壓縮
4. **互動式選單**：建立命令列界面
5. **效能優化**：大檔案處理優化

### 技術規格
- **Python 版本**：3.8+
- **核心技術**：函式設計、遞迴、高階函式、字串處理
- **預計程式碼行數**：300-500 行（基本需求），600-800 行（含進階）
- **預計開發時間**：20-30 小時

---

## 🏗️ 專案結構（Project Structure）

```
milestone04-text-toolkit/
├── README.md              # 專案說明（本文件）
├── requirements.ipynb     # 詳細需求規格與範例
├── starter-code.ipynb     # 起始程式碼框架與提示
└── solution.ipynb         # 完整參考解答
```

---

## 📚 學習成果（Learning Outcomes）

完成此專案後，您將能夠：

### 知識面（Knowledge）
- **整合運用** Ch12-15 的所有概念
- **理解** 模組化程式設計的重要性
- **掌握** 函式間的協作與組合方式

### 技能面（Skills）
- **設計** 清晰的函式介面（API）
- **實作** 遞迴檔案系統遍歷
- **運用** 高階函式進行資料轉換
- **建立** 可重用的函式庫

### 應用面（Application）
- **解決** 實際的文字處理需求
- **建構** 完整的軟體專案
- **體驗** 函式式程式設計思維

---

## 🔧 開發步驟建議（Development Guide）

### Phase 1: 分析與設計（60 分鐘）

#### 步驟 1.1: 模組架構設計
```python
# 核心模組結構
text_toolkit = {
    'statistics': {    # 文字統計模組
        'count_words', 'count_lines', 'word_frequency'
    },
    'search': {        # 文字搜尋模組
        'find_keywords', 'pattern_match', 'search_lines'
    },
    'transform': {     # 文字轉換模組
        'case_transform', 'replace_text', 'normalize'
    },
    'format': {        # 文字格式化模組
        'align_text', 'indent_text', 'columnize'
    },
    'analysis': {      # 文字分析模組
        'sentence_analysis', 'duplicate_detection'
    }
}
```

#### 步驟 1.2: 函式介面設計（API Design）
設計清晰的函式簽名，遵循單一職責原則：
```python
def count_words(text: str) -> dict:
    """統計文字中的詞彙數量"""
    pass

def find_keywords(text: str, keywords: list) -> dict:
    """在文字中搜尋關鍵字"""
    pass

def transform_case(text: str, mode: str) -> str:
    """轉換文字大小寫"""
    pass
```

#### 步驟 1.3: 資料結構規劃
```python
# 文字統計結果
stats_result = {
    'total_chars': 1250,
    'total_words': 200,
    'total_lines': 15,
    'word_freq': {'python': 15, 'function': 8}
}

# 搜尋結果
search_result = {
    'keyword': 'python',
    'count': 5,
    'positions': [12, 45, 89, 123, 167],
    'lines': [1, 3, 7, 9, 12]
}
```

**✅ 檢查點**:
- [ ] 完成模組架構設計圖
- [ ] 定義所有核心函式簽名
- [ ] 設計統一的回傳資料結構

---

### Phase 2: 核心功能實作（180 分鐘）

#### 步驟 2.1: 文字統計模組（45 分鐘）
```python
def count_words(text):
    """統計文字中的詞彙數量 - Ch12 函式基礎應用"""
    # 使用字串方法與字典
    words = text.lower().split()
    word_count = {}

    for word in words:
        # 移除標點符號（示範字串處理）
        clean_word = ''.join(c for c in word if c.isalnum())
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    return word_count

def analyze_text_statistics(text):
    """綜合文字統計 - 展示函式組合"""
    return {
        'char_count': len(text),
        'word_count': len(text.split()),
        'line_count': len(text.splitlines()),
        'word_frequency': count_words(text)
    }
```

#### 步驟 2.2: 高階函式應用（45 分鐘）- Ch14 重點
```python
def apply_text_filters(text_list, *filters):
    """使用高階函式處理文字列表"""
    result = text_list

    # 依序套用所有過濾器
    for filter_func in filters:
        result = list(filter(filter_func, result))

    return result

def transform_text_batch(text_list, transform_func):
    """批次轉換文字 - map 函式應用"""
    return list(map(transform_func, text_list))

# Lambda 函式示範
def create_text_filters():
    """建立常用過濾器 - Lambda 應用"""
    return {
        'non_empty': lambda text: text.strip() != '',
        'min_length': lambda min_len: lambda text: len(text) >= min_len,
        'contains_keyword': lambda keyword: lambda text: keyword in text.lower()
    }
```

#### 步驟 2.3: 作用域與內嵌函式（45 分鐘）- Ch13 重點
```python
def create_text_processor(config):
    """使用閉包建立客製化文字處理器"""
    # 外層函式變數（閉包環境）
    separator = config.get('separator', ' ')
    case_mode = config.get('case', 'none')

    def process_line(line):
        """內層函式 - 具有外層作用域存取權"""
        # 使用外層變數
        words = line.split(separator)

        if case_mode == 'upper':
            words = [word.upper() for word in words]
        elif case_mode == 'lower':
            words = [word.lower() for word in words]

        return separator.join(words)

    def process_text(text):
        """處理整個文字"""
        lines = text.splitlines()
        processed_lines = [process_line(line) for line in lines]
        return '\n'.join(processed_lines)

    # 返回內層函式（閉包）
    return process_text
```

#### 步驟 2.4: 遞迴檔案處理（45 分鐘）- Ch15 重點
```python
def search_files_recursive(directory, pattern, file_extension='.txt'):
    """遞迴搜尋目錄中的文字檔案"""
    import os

    def _search_directory(current_dir, depth=0):
        """內部遞迴函式"""
        results = []

        try:
            # 獲取目錄內容
            items = os.listdir(current_dir)

            for item in items:
                item_path = os.path.join(current_dir, item)

                if os.path.isfile(item_path) and item.endswith(file_extension):
                    # 處理檔案
                    try:
                        with open(item_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if pattern in content:
                                results.append({
                                    'file': item_path,
                                    'matches': content.count(pattern),
                                    'depth': depth
                                })
                    except UnicodeDecodeError:
                        # 忽略無法讀取的檔案
                        continue

                elif os.path.isdir(item_path) and depth < 5:  # 限制深度
                    # 遞迴處理子目錄
                    results.extend(_search_directory(item_path, depth + 1))

        except PermissionError:
            # 處理權限問題
            pass

        return results

    return _search_directory(directory)

def count_text_patterns_recursive(text, pattern):
    """遞迴計算模式出現次數"""
    if not text or not pattern:
        return 0

    if text.startswith(pattern):
        # 找到模式，繼續搜尋剩餘部分
        return 1 + count_text_patterns_recursive(text[len(pattern):], pattern)
    else:
        # 沒找到，繼續搜尋下一個字元
        return count_text_patterns_recursive(text[1:], pattern)
```

**✅ 檢查點**:
- [ ] 文字統計功能正常運作
- [ ] 高階函式正確應用 map/filter
- [ ] 閉包與作用域運用得當
- [ ] 遞迴函式運作正確

---

### Phase 3: 整合與優化（120 分鐘）

#### 步驟 3.1: 建立主介面（40 分鐘）
```python
def create_text_toolkit():
    """建立文字處理工具箱主介面"""

    # 使用字典儲存所有功能（模組化設計）
    toolkit = {
        'statistics': {
            'word_count': count_words,
            'text_stats': analyze_text_statistics,
            'frequency_analysis': word_frequency_analysis
        },
        'search': {
            'find_pattern': find_text_pattern,
            'search_lines': search_in_lines,
            'file_search': search_files_recursive
        },
        'transform': {
            'case_convert': convert_case,
            'replace_text': replace_text_advanced,
            'normalize': normalize_text
        },
        'format': {
            'align': align_text,
            'indent': indent_lines,
            'columnize': create_columns
        }
    }

    return toolkit

def interactive_menu():
    """互動式選單系統"""
    toolkit = create_text_toolkit()

    while True:
        print("\n" + "="*50)
        print("🔧 文字處理工具箱 v1.0")
        print("="*50)
        print("1. 文字統計分析")
        print("2. 文字搜尋功能")
        print("3. 文字轉換工具")
        print("4. 文字格式化")
        print("5. 遞迴檔案處理")
        print("0. 結束程式")

        choice = input("\n請選擇功能 (0-5): ")

        if choice == "0":
            print("感謝使用！")
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            handle_menu_choice(choice, toolkit)
        else:
            print("無效選擇，請重新輸入！")
```

#### 步驟 3.2: 效能優化（40 分鐘）
```python
def optimize_large_file_processing(file_path, chunk_size=8192):
    """大檔案分塊處理 - 記憶體優化"""
    def process_chunks(processor_func):
        """使用生成器處理大檔案"""
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield processor_func(chunk)

    return process_chunks

# 使用裝飾器實作快取功能
def memoize(func):
    """記憶化裝飾器 - 避免重複計算"""
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def expensive_text_analysis(text):
    """昂貴的文字分析操作"""
    # 模擬複雜計算
    return complex_analysis(text)
```

#### 步驟 3.3: 測試與驗證（40 分鐘）
```python
def test_text_toolkit():
    """完整功能測試"""
    print("🧪 開始測試文字處理工具箱...")

    # 測試資料
    test_text = """
    Python 是一種高階程式語言。
    Python 易於學習且功能強大。
    許多公司都使用 Python 開發軟體。
    """

    # 測試 1: 文字統計
    stats = analyze_text_statistics(test_text)
    assert stats['word_count'] > 0, "詞彙統計失敗"
    print("✅ 文字統計測試通過")

    # 測試 2: 搜尋功能
    search_result = find_text_pattern(test_text, "Python")
    assert search_result['count'] == 3, "搜尋功能失敗"
    print("✅ 搜尋功能測試通過")

    # 測試 3: 高階函式
    lines = test_text.strip().split('\n')
    filtered = apply_text_filters(lines, lambda x: 'Python' in x)
    assert len(filtered) == 3, "高階函式測試失敗"
    print("✅ 高階函式測試通過")

    # 測試 4: 遞迴功能
    recursive_count = count_text_patterns_recursive(test_text, "Python")
    assert recursive_count == 3, "遞迴功能失敗"
    print("✅ 遞迴功能測試通過")

    print("🎉 所有測試通過！")

if __name__ == "__main__":
    test_text_toolkit()
    interactive_menu()
```

**✅ 檢查點**:
- [ ] 主介面流暢運作
- [ ] 所有模組正確整合
- [ ] 效能優化實作完成
- [ ] 測試案例全部通過

---

## ✅ 評分標準（Grading Rubric）

### 基本功能實作 (70%)

| 項目 | 優秀 (90-100) | 良好 (75-89) | 及格 (60-74) | 不及格 (<60) |
|:-----|:-------------|:------------|:------------|:------------|
| **文字統計模組** (15%) | 完整實作詞頻、字數、行數統計，有錯誤處理 | 基本統計功能完整，部分錯誤處理 | 基本統計功能正常 | 統計功能不完整或有錯誤 |
| **文字搜尋模組** (15%) | 支援多種搜尋模式，結果詳細 | 基本搜尋功能完整 | 簡單關鍵字搜尋 | 搜尋功能不正常 |
| **文字轉換模組** (15%) | 多種轉換方式，支援批次處理 | 基本轉換功能完整 | 簡單大小寫轉換 | 轉換功能有問題 |
| **格式化模組** (10%) | 對齊、縮排、分欄功能完善 | 基本格式化功能 | 簡單格式化 | 格式化不正常 |
| **分析模組** (15%) | 句子分析、重複檢測完整 | 基本分析功能 | 簡單文字分析 | 分析功能不足 |

### 進階技術應用 (20%)

| 項目 | 優秀 (90-100) | 良好 (75-89) | 及格 (60-74) | 不及格 (<60) |
|:-----|:-------------|:------------|:------------|:------------|
| **高階函式運用** (5%) | 熟練使用 map/filter/reduce, Lambda | 正確使用高階函式 | 基本使用 map/filter | 不會使用高階函式 |
| **作用域與閉包** (5%) | 正確運用閉包，理解作用域 | 基本使用內嵌函式 | 簡單內嵌函式 | 不理解作用域 |
| **遞迴應用** (5%) | 複雜遞迴處理，有終止條件 | 基本遞迴功能 | 簡單遞迴 | 遞迴邏輯錯誤 |
| **函式設計** (5%) | 模組化設計，介面清晰 | 函式化程式設計 | 基本函式分離 | 程式結構混亂 |

### 程式品質 (10%)

| 項目 | 優秀 (90-100) | 良好 (75-89) | 及格 (60-74) | 不及格 (<60) |
|:-----|:-------------|:------------|:------------|:------------|
| **程式架構** (3%) | 模組化設計，結構清晰 | 基本模組化 | 函式分離 | 結構混亂 |
| **文件註解** (3%) | 完整 docstring，註解清楚 | 主要函式有文件 | 基本註解 | 缺乏註解 |
| **錯誤處理** (2%) | 完善的例外處理 | 基本錯誤處理 | 簡單驗證 | 無錯誤處理 |
| **程式風格** (2%) | 遵循 PEP 8，命名規範 | 基本程式風格 | 可讀性良好 | 風格混亂 |

---

## 🎓 教師指引（Instructor Notes）

### 評分重點

#### 1. Ch12-15 概念整合度 (重要指標)
- ✅ **優秀**: 清楚展示每章節核心概念的應用
  - Ch12: 函式設計原則、參數處理、模組化
  - Ch13: 作用域運用、內嵌函式、閉包
  - Ch14: map/filter/reduce、Lambda、函式組合
  - Ch15: 遞迴思維、分治法、終止條件
- ⭐ **良好**: 部分概念運用得當，但不夠全面
- ❌ **不佳**: 只使用基本功能，沒有展示進階概念

#### 2. 函式設計品質 (關鍵評分點)
- ✅ **優秀**: 單一職責、介面清晰、可重用性高
- ⭐ **良好**: 基本函式化設計
- ❌ **不佳**: 函式過於複雜或職責不清

#### 3. 高階函式運用 (Ch14 重點)
- ✅ **優秀**:
  ```python
  # 函式組合示例
  def process_pipeline(text, *operations):
      return reduce(lambda result, op: op(result), operations, text)

  # 使用示例
  result = process_pipeline(text,
                          lambda x: x.lower(),
                          lambda x: filter_words(x),
                          lambda x: format_output(x))
  ```
- ⭐ **良好**: 基本使用 map/filter
- ❌ **不佳**: 沒有使用高階函式

#### 4. 遞迴實作 (Ch15 重點)
- ✅ **優秀**: 清楚的遞迴結構，正確的終止條件，實際應用場景
- ⭐ **良好**: 基本遞迴功能正確
- ❌ **不佳**: 遞迴邏輯錯誤或沒有終止條件

### 常見問題與解決方案

#### 問題 1: 沒有展示 Ch13 作用域概念
**學生表現**: 所有函式都在全域範圍，沒有使用內嵌函式或閉包
**解決方案**: 引導學生設計配置化的文字處理器
```python
def create_text_processor(config):
    encoding = config.get('encoding', 'utf-8')

    def process_file(filename):  # 內嵌函式存取外層變數
        with open(filename, encoding=encoding) as f:
            return f.read()

    return process_file  # 回傳閉包
```

#### 問題 2: 高階函式使用不當
**學生表現**: 使用傳統迴圈而非 map/filter
```python
# 不佳寫法
result = []
for item in items:
    if condition(item):
        result.append(transform(item))
```
**建議改進**:
```python
# 優秀寫法
result = list(map(transform, filter(condition, items)))
# 或使用推導式
result = [transform(item) for item in items if condition(item)]
```

#### 問題 3: 遞迴沒有實際應用場景
**學生表現**: 為了遞迴而遞迴，如遞迴計算字串長度
**建議場景**:
- 目錄樹遞迴搜尋
- 巢狀資料結構處理
- 文字解析樹走訪

#### 問題 4: 函式設計缺乏模組化思維
**學生表現**: 一個函式做太多事情
**建議原則**:
- 單一職責原則 (Single Responsibility)
- 函式長度控制在 20-30 行內
- 清楚的輸入輸出規格
- 避免副作用 (side effects)

### 教學時間分配建議

| 階段 | 時間 | 內容 | 重點 |
|:-----|:-----|:-----|:-----|
| **講解示範** | 2 小時 | Ch12-15 概念回顧，專案架構設計 | 強調概念整合 |
| **Phase 1 指導** | 1 小時 | 模組設計與函式介面規劃 | 設計思維培養 |
| **Phase 2 實作** | 4 小時 | 核心功能開發，技術概念應用 | 個別指導重點 |
| **Phase 3 整合** | 2 小時 | 系統整合與測試 | 品質控制 |
| **程式碼審查** | 1 小時 | 學生作品分享與討論 | 最佳實踐分享 |

### 差異化教學建議

#### 對於進度較快的學生:
- 挑戰延伸功能 (檔案批次處理、正規表達式)
- 效能優化實作 (生成器、記憶化)
- 設計模式應用 (策略模式、工廠模式)

#### 對於需要額外協助的學生:
- 提供更詳細的函式範例
- 重點輔導 Ch14-15 的概念理解
- 簡化需求，先完成基本功能

---

## 🚀 延伸挑戰（Extension Challenges）

### 挑戰 1: 正規表達式整合 ⭐⭐⭐
整合 Python `re` 模組，提供進階文字處理：
```python
import re

def advanced_pattern_search(text, pattern, flags=0):
    """使用正規表達式進行進階搜尋"""
    matches = re.finditer(pattern, text, flags)
    return [{
        'match': match.group(),
        'start': match.start(),
        'end': match.end(),
        'groups': match.groups()
    } for match in matches]

def extract_email_addresses(text):
    """提取文字中的電子郵件地址"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return advanced_pattern_search(text, pattern, re.IGNORECASE)
```

### 挑戰 2: 文字壓縮演算法 ⭐⭐⭐⭐
實作 Run-Length Encoding (RLE) 壓縮：
```python
def rle_compress(text):
    """Run-Length Encoding 壓縮"""
    if not text:
        return ""

    result = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")
    return ''.join(result)

def rle_decompress(compressed):
    """RLE 解壓縮"""
    result = []
    i = 0

    while i < len(compressed):
        # 讀取數字
        count = ""
        while i < len(compressed) and compressed[i].isdigit():
            count += compressed[i]
            i += 1

        # 讀取字元
        if i < len(compressed):
            char = compressed[i]
            result.append(char * int(count))
            i += 1

    return ''.join(result)
```

### 挑戰 3: 平行處理優化 ⭐⭐⭐⭐⭐
使用 `concurrent.futures` 進行多執行緒文字處理：
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def parallel_file_processing(file_list, processor_func, max_workers=4):
    """平行處理多個檔案"""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任務
        futures = {executor.submit(processor_func, file): file
                  for file in file_list}

        # 收集結果
        results = {}
        for future in futures:
            file = futures[future]
            try:
                results[file] = future.result()
            except Exception as e:
                results[file] = f"Error: {e}"

        return results

def benchmark_performance(func, *args, iterations=10):
    """效能測試裝飾器"""
    def wrapper():
        times = []
        for _ in range(iterations):
            start = time.time()
            result = func(*args)
            end = time.time()
            times.append(end - start)

        avg_time = sum(times) / len(times)
        return {
            'result': result,
            'avg_time': avg_time,
            'times': times
        }
    return wrapper
```

### 挑戰 4: 機器學習文字分析 ⭐⭐⭐⭐⭐
整合簡單的 NLP 功能：
```python
def sentiment_analysis_simple(text):
    """簡易情感分析"""
    positive_words = {'好', '棒', '優秀', '讚', '喜歡', '開心'}
    negative_words = {'壞', '糟', '討厭', '難過', '生氣', '失望'}

    words = set(text.lower().split())

    positive_score = len(words & positive_words)
    negative_score = len(words & negative_words)

    if positive_score > negative_score:
        return 'positive'
    elif negative_score > positive_score:
        return 'negative'
    else:
        return 'neutral'

def text_similarity(text1, text2):
    """計算文字相似度（簡易版本）"""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    intersection = words1 & words2
    union = words1 | words2

    # Jaccard 相似度
    return len(intersection) / len(union) if union else 0
```

### 挑戰 5: Web API 整合 ⭐⭐⭐⭐
建立 RESTful API 介面：
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """文字分析 API 端點"""
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # 使用工具箱進行分析
    toolkit = create_text_toolkit()
    results = {
        'statistics': toolkit['statistics']['text_stats'](text),
        'sentiment': sentiment_analysis_simple(text),
        'word_count': len(text.split())
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
```

---

**專案難度**：⭐⭐⭐⭐ (中高級)
**預計完成時間**：20-30 小時
**建議完成期限**：2 週
**先備知識**：完成 Ch12-15 所有內容
**延伸學習**：Ch23 檔案處理、Ch27 模組設計
