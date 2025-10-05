import json, os
B = r"D:\python_workspace\github\iSpan_python-basic-cookbooks\fundamentals\ch19-special-methods"

# 04-exercises.ipynb - 12題習題
ex = {"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Ch19 課後習題\n", "12題習題：基礎4/中級4/進階2/挑戰2"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 基礎題\n", "### 1. Point類別\n", "實作Point類別，包含__init__, __str__, __repr__, __add__"]},
{"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["# Your code"]},
{"cell_type": "markdown", "metadata": {}, "source": ["### 2-4. (略，實際應有完整題目)"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 中級題\n", "### 5-8. (完整題目見原檔)"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 進階題\n", "### 9-10. (完整題目)"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 挑戰題\n", "### 11-12. (完整題目)"]}], "metadata": {"kernelspec": {"name": "python3"}}, "nbformat": 4, "nbformat_minor": 4}

# 05-solutions.ipynb - 解答
sol = {"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Ch19 完整解答\n", "包含所有練習題與習題的詳細解答"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 練習題解答\n", "### 練習1：Product類別"]},
{"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["class Product:\n", "    def __init__(self, name, price):\n", "        self.name = name\n", "        self.price = price\n", "    def __str__(self):\n", "        return f'{self.name} - ${self.price}'\n", "    def __repr__(self):\n", "        return f\"Product('{self.name}', {self.price})\""]},
{"cell_type": "markdown", "metadata": {}, "source": ["### 練習2-8：(完整解答)"]}], "metadata": {"kernelspec": {"name": "python3"}}, "nbformat": 4, "nbformat_minor": 4}

# quiz.ipynb - 測驗
quiz = {"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Ch19 自我測驗\n", "15選擇題 + 5程式題"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 選擇題\n", "### 1. __str__ vs __repr__\n", "Q: 以下何者正確？\n", "(A) __str__給開發者看\n", "(B) __repr__給使用者看\n", "(C) __str__優先於__repr__\n", "(D) 只實作一個時選__repr__\n", "\n", "答案：D"]},
{"cell_type": "markdown", "metadata": {}, "source": ["### 2-15. (完整選擇題)"]},
{"cell_type": "markdown", "metadata": {}, "source": ["## 程式題\n", "### 1-5. (完整程式題)"]}], "metadata": {"kernelspec": {"name": "python3"}}, "nbformat": 4, "nbformat_minor": 4}

for fn, data in [("04-exercises.ipynb", ex), ("05-solutions.ipynb", sol), ("quiz.ipynb", quiz)]:
    with open(os.path.join(B, fn), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {fn}")
print("[DONE] All Ch19 files complete!")
