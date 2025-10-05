#!/usr/bin/env python3
"""
Ch19 特殊方法與運算子重載 - 批次建立所有檔案
"""

import json
import os

# 基礎路徑
BASE_PATH = r"D:\python_workspace\github\iSpan_python-basic-cookbooks\fundamentals\ch19-special-methods"

# 02-worked-examples.ipynb
worked_examples = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Chapter 19: 特殊方法與運算子重載 - 詳解範例\n", "\n", "本檔案包含 4 個深入解析的範例，幫助你理解特殊方法的實際應用。"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 範例 1：自訂列表類別（序列協定完整實作）\n", "\n", "**學習目標**：實作完整的序列協定，包括 `__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__contains__`"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class CustomList:\n",
                "    \"\"\"自訂列表類別 - 完整序列協定\"\"\"\n",
                "    \n",
                "    def __init__(self, initial_data=None):\n",
                "        \"\"\"初始化\"\"\"\n",
                "        self.data = list(initial_data) if initial_data else []\n",
                "    \n",
                "    def __len__(self):\n",
                "        \"\"\"返回長度\"\"\"\n",
                "        return len(self.data)\n",
                "    \n",
                "    def __getitem__(self, index):\n",
                "        \"\"\"索引存取\"\"\"\n",
                "        return self.data[index]\n",
                "    \n",
                "    def __setitem__(self, index, value):\n",
                "        \"\"\"索引賦值\"\"\"\n",
                "        self.data[index] = value\n",
                "    \n",
                "    def __delitem__(self, index):\n",
                "        \"\"\"刪除項目\"\"\"\n",
                "        del self.data[index]\n",
                "    \n",
                "    def __contains__(self, item):\n",
                "        \"\"\"成員測試\"\"\"\n",
                "        return item in self.data\n",
                "    \n",
                "    def append(self, item):\n",
                "        \"\"\"新增項目\"\"\"\n",
                "        self.data.append(item)\n",
                "    \n",
                "    def __str__(self):\n",
                "        return f\"CustomList({self.data})\"\n",
                "    \n",
                "    def __repr__(self):\n",
                "        return f\"CustomList({self.data!r})\"\n",
                "\n",
                "# 測試\n",
                "lst = CustomList([1, 2, 3])\n",
                "print(f\"列表：{lst}\")\n",
                "print(f\"長度：{len(lst)}\")\n",
                "print(f\"第一個元素：{lst[0]}\")\n",
                "\n",
                "lst[0] = 10\n",
                "print(f\"修改後：{lst}\")\n",
                "\n",
                "print(f\"2 in lst: {2 in lst}\")\n",
                "\n",
                "del lst[0]\n",
                "print(f\"刪除後：{lst}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["**關鍵知識點**：\n", "1. 實作 `__len__` 和 `__getitem__` 是最基本的序列協定\n", "2. `__setitem__` 讓物件可以被修改\n", "3. `__contains__` 讓物件支援 `in` 運算子\n", "4. 這些方法組合起來，讓自訂類別像內建列表一樣使用"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 範例 2：複數運算類別（完整運算子重載）\n", "\n", "**學習目標**：為複數類別實作所有算術運算子"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class Complex:\n",
                "    \"\"\"複數類別 - 完整運算子重載\"\"\"\n",
                "    \n",
                "    def __init__(self, real, imag):\n",
                "        self.real = real\n",
                "        self.imag = imag\n",
                "    \n",
                "    def __add__(self, other):\n",
                "        \"\"\"加法：(a+bi) + (c+di) = (a+c) + (b+d)i\"\"\"\n",
                "        return Complex(self.real + other.real, self.imag + other.imag)\n",
                "    \n",
                "    def __sub__(self, other):\n",
                "        \"\"\"減法\"\"\"\n",
                "        return Complex(self.real - other.real, self.imag - other.imag)\n",
                "    \n",
                "    def __mul__(self, other):\n",
                "        \"\"\"乘法：(a+bi)(c+di) = (ac-bd) + (ad+bc)i\"\"\"\n",
                "        real = self.real * other.real - self.imag * other.imag\n",
                "        imag = self.real * other.imag + self.imag * other.real\n",
                "        return Complex(real, imag)\n",
                "    \n",
                "    def __eq__(self, other):\n",
                "        \"\"\"相等比較\"\"\"\n",
                "        return self.real == other.real and self.imag == other.imag\n",
                "    \n",
                "    def __abs__(self):\n",
                "        \"\"\"絕對值（模）：|a+bi| = √(a²+b²)\"\"\"\n",
                "        return (self.real**2 + self.imag**2)**0.5\n",
                "    \n",
                "    def __str__(self):\n",
                "        if self.imag >= 0:\n",
                "            return f\"{self.real}+{self.imag}i\"\n",
                "        else:\n",
                "            return f\"{self.real}{self.imag}i\"\n",
                "    \n",
                "    def __repr__(self):\n",
                "        return f\"Complex({self.real}, {self.imag})\"\n",
                "\n",
                "# 測試\n",
                "z1 = Complex(3, 4)\n",
                "z2 = Complex(1, 2)\n",
                "\n",
                "print(f\"z1 = {z1}\")\n",
                "print(f\"z2 = {z2}\")\n",
                "print(f\"z1 + z2 = {z1 + z2}\")\n",
                "print(f\"z1 * z2 = {z1 * z2}\")\n",
                "print(f\"|z1| = {abs(z1)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["**關鍵知識點**：\n", "1. 數學類別非常適合使用運算子重載\n", "2. `__abs__` 讓物件支援 `abs()` 函式\n", "3. 運算子應該返回新物件，不修改原物件\n", "4. `__str__` 可以根據情況調整格式（正負號處理）"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 範例 3：資料庫連線管理器（上下文管理器）\n", "\n", "**學習目標**：實作完整的上下文管理器，處理資源管理與例外"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class DatabaseConnection:\n",
                "    \"\"\"資料庫連線管理器 - 完整上下文管理器\"\"\"\n",
                "    \n",
                "    def __init__(self, host, port, database):\n",
                "        self.host = host\n",
                "        self.port = port\n",
                "        self.database = database\n",
                "        self.connection = None\n",
                "        self.transaction = None\n",
                "    \n",
                "    def __enter__(self):\n",
                "        \"\"\"建立連接並開始交易\"\"\"\n",
                "        print(f\"連接到 {self.host}:{self.port}/{self.database}\")\n",
                "        # 模擬連接\n",
                "        self.connection = f\"Connection({self.database})\"\n",
                "        print(\"開始交易...\")\n",
                "        self.transaction = \"TRANSACTION\"\n",
                "        return self\n",
                "    \n",
                "    def __exit__(self, exc_type, exc_value, traceback):\n",
                "        \"\"\"處理交易提交或回滾，關閉連接\"\"\"\n",
                "        if exc_type is None:\n",
                "            # 沒有例外：提交交易\n",
                "            print(\"提交交易...\")\n",
                "            print(\"交易成功！\")\n",
                "        else:\n",
                "            # 有例外：回滾交易\n",
                "            print(f\"發生錯誤：{exc_value}\")\n",
                "            print(\"回滾交易...\")\n",
                "            print(\"交易已回滾\")\n",
                "        \n",
                "        # 無論如何都關閉連接\n",
                "        print(\"關閉連接\")\n",
                "        self.connection = None\n",
                "        self.transaction = None\n",
                "        \n",
                "        # 返回 False 讓例外繼續傳播\n",
                "        return False\n",
                "    \n",
                "    def execute(self, query):\n",
                "        \"\"\"執行查詢\"\"\"\n",
                "        if not self.connection:\n",
                "            raise RuntimeError(\"未連接到資料庫\")\n",
                "        print(f\"執行查詢：{query}\")\n",
                "        return f\"Result of: {query}\"\n",
                "\n",
                "# 測試 1：正常情況\n",
                "print(\"=== 正常交易 ===\")\n",
                "with DatabaseConnection(\"localhost\", 5432, \"mydb\") as db:\n",
                "    db.execute(\"SELECT * FROM users\")\n",
                "    db.execute(\"UPDATE users SET name='Alice'\")\n",
                "\n",
                "# 測試 2：例外情況\n",
                "print(\"\\n=== 例外交易 ===\")\n",
                "try:\n",
                "    with DatabaseConnection(\"localhost\", 5432, \"mydb\") as db:\n",
                "        db.execute(\"SELECT * FROM users\")\n",
                "        raise ValueError(\"資料驗證失敗！\")\n",
                "        db.execute(\"這不會執行\")\n",
                "except ValueError as e:\n",
                "    print(f\"外部捕獲例外：{e}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["**關鍵知識點**：\n", "1. `__enter__` 取得資源（連接、開始交易）\n", "2. `__exit__` 釋放資源（提交/回滾、關閉連接）\n", "3. 根據 `exc_type` 判斷是否有例外發生\n", "4. 返回 `False` 讓例外繼續傳播，返回 `True` 會抑制例外\n", "5. 資源清理邏輯應該在 `__exit__` 中，保證一定執行"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 範例 4：計數器類別（綜合應用）\n", "\n", "**學習目標**：整合多個特殊方法，建立功能完整的計數器類別"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "from functools import total_ordering\n",
                "\n",
                "@total_ordering\n",
                "class Counter:\n",
                "    \"\"\"計數器類別 - 綜合特殊方法\"\"\"\n",
                "    \n",
                "    def __init__(self, name=\"Counter\", initial=0):\n",
                "        self.name = name\n",
                "        self.value = initial\n",
                "    \n",
                "    # 基本表示\n",
                "    def __str__(self):\n",
                "        return f\"{self.name}: {self.value}\"\n",
                "    \n",
                "    def __repr__(self):\n",
                "        return f\"Counter('{self.name}', {self.value})\"\n",
                "    \n",
                "    # 運算子重載\n",
                "    def __add__(self, other):\n",
                "        \"\"\"兩個計數器相加\"\"\"\n",
                "        if isinstance(other, Counter):\n",
                "            return Counter(f\"{self.name}+{other.name}\", self.value + other.value)\n",
                "        else:\n",
                "            return Counter(self.name, self.value + other)\n",
                "    \n",
                "    def __iadd__(self, value):\n",
                "        \"\"\"就地加法：counter += 5\"\"\"\n",
                "        self.value += value\n",
                "        return self\n",
                "    \n",
                "    # 比較運算子（使用 @total_ordering）\n",
                "    def __eq__(self, other):\n",
                "        if isinstance(other, Counter):\n",
                "            return self.value == other.value\n",
                "        return self.value == other\n",
                "    \n",
                "    def __lt__(self, other):\n",
                "        if isinstance(other, Counter):\n",
                "            return self.value < other.value\n",
                "        return self.value < other\n",
                "    \n",
                "    # 可呼叫\n",
                "    def __call__(self, increment=1):\n",
                "        \"\"\"呼叫時遞增\"\"\"\n",
                "        self.value += increment\n",
                "        return self.value\n",
                "    \n",
                "    # 型態轉換\n",
                "    def __int__(self):\n",
                "        return self.value\n",
                "    \n",
                "    def __bool__(self):\n",
                "        return self.value != 0\n",
                "\n",
                "# 測試\n",
                "c1 = Counter(\"點擊次數\", 5)\n",
                "c2 = Counter(\"瀏覽次數\", 10)\n",
                "\n",
                "print(f\"c1 = {c1}\")\n",
                "print(f\"c2 = {c2}\")\n",
                "\n",
                "# 運算子\n",
                "c3 = c1 + c2\n",
                "print(f\"c1 + c2 = {c3}\")\n",
                "\n",
                "c1 += 3\n",
                "print(f\"c1 += 3 → {c1}\")\n",
                "\n",
                "# 比較\n",
                "print(f\"c1 < c2: {c1 < c2}\")\n",
                "print(f\"c1 == 8: {c1 == 8}\")\n",
                "\n",
                "# 可呼叫\n",
                "print(f\"c1() = {c1()}\")  # 遞增 1\n",
                "print(f\"c1(5) = {c1(5)}\")  # 遞增 5\n",
                "\n",
                "# 型態轉換\n",
                "print(f\"int(c1) = {int(c1)}\")\n",
                "print(f\"bool(c1) = {bool(c1)}\")\n",
                "\n",
                "c_zero = Counter(\"零\", 0)\n",
                "print(f\"bool(c_zero) = {bool(c_zero)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["**關鍵知識點**：\n", "1. `__add__` vs `__iadd__`：前者返回新物件，後者修改並返回 self\n", "2. `@total_ordering` 簡化比較方法的實作\n", "3. `__call__` 讓物件可以像函式一樣呼叫\n", "4. `__int__`、`__bool__` 等型態轉換方法\n", "5. `isinstance()` 用於檢查參數型態，支援多型"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🎯 總結\n", "\n", "通過這 4 個範例，你應該掌握：\n", "\n", "1. **序列協定**：`__len__`、`__getitem__` 等讓類別像容器\n", "2. **運算子重載**：為數學物件實作直覺的運算\n", "3. **上下文管理器**：安全管理資源（連接、檔案、交易）\n", "4. **綜合應用**：組合多個特殊方法建立完整功能\n", "\n", "**下一步**：完成 `03-practice.ipynb` 的 8 道練習題！"]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# 03-practice.ipynb
practice = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Chapter 19: 特殊方法與運算子重載 - 課堂練習\n", "\n", "## 練習指引\n", "- 共 8 題，涵蓋本章核心概念\n", "- 建議時間：40 分鐘\n", "- 完成後對照 `05-solutions.ipynb`"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 1：實作 `__str__` 和 `__repr__`\n", "\n", "建立一個 `Product` 類別，表示商品，包含：\n", "- 屬性：name（名稱）、price（價格）\n", "- `__str__`：返回 \"商品名稱 - $價格\"\n", "- `__repr__`：返回 \"Product('name', price)\""]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# 你的程式碼\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 2：實作序列協定\n", "\n", "建立一個 `Stack` 類別（堆疊），實作：\n", "- `push(item)`：推入元素\n", "- `pop()`：彈出元素\n", "- `__len__()`：返回堆疊大小\n", "- `__getitem__(index)`：索引存取"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# 你的程式碼\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 3：向量加法\n", "\n", "為 `Vector2D` 類別實作 `__add__` 方法，支援向量相加。"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["class Vector2D:\n", "    def __init__(self, x, y):\n", "        self.x = x\n", "        self.y = y\n", "    \n", "    # 實作 __add__\n", "    \n", "    def __str__(self):\n", "        return f\"({self.x}, {self.y})\""]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 4：比較運算子\n", "\n", "為 `Temperature` 類別實作 `__eq__` 和 `__lt__`，根據溫度值比較。"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["class Temperature:\n", "    def __init__(self, celsius):\n", "        self.celsius = celsius\n", "    \n", "    # 實作 __eq__ 和 __lt__\n", "    \n", "    def __str__(self):\n", "        return f\"{self.celsius}°C\""]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 5：可呼叫物件\n", "\n", "建立一個 `Adder` 類別，初始化時接收一個數字，呼叫時返回該數字與參數的和。"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# 你的程式碼\n", "# 使用範例：\n", "# add5 = Adder(5)\n", "# print(add5(10))  # 15"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 6：上下文管理器 - 計時器\n", "\n", "建立一個 `Timer` 上下文管理器，測量 with 區塊的執行時間。"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["import time\n", "\n", "# 你的程式碼\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 7：完整的 Money 類別\n", "\n", "建立一個 `Money` 類別，實作：\n", "- `__add__`、`__sub__`：金額加減\n", "- `__mul__`：金額乘以倍數\n", "- `__eq__`、`__lt__`：比較金額\n", "- `__str__`：格式化輸出（如 \"$100.50\"）"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# 你的程式碼\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 練習 8：綜合應用 - 購物車\n", "\n", "建立一個 `ShoppingCart` 類別，實作：\n", "- `add_item(name, price, quantity)`：新增商品\n", "- `__len__()`：商品種類數\n", "- `__iter__()`：可迭代所有商品\n", "- `total` 屬性：計算總金額"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# 你的程式碼\n"]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# 建立所有檔案
files = {
    "02-worked-examples.ipynb": worked_examples,
    "03-practice.ipynb": practice
}

for filename, content in files.items():
    filepath = os.path.join(BASE_PATH, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"[OK] Created: {filename}")

print("\n[DONE] Ch19 core files created!")
print("Please continue to create remaining files following this pattern.")
