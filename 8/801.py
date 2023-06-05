'''
TQC+ 程式語言Python 801 字串索引

1. 題目說明:
請開啟PYD801.py檔案，依下列題意進行作答，顯示每個字元的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA801.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的索引。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
字串每個字元的索引

範例輸入
Sandwich
範例輸出
Index of 'S': 0
Index of 'a': 1
Index of 'n': 2
Index of 'd': 3
Index of 'w': 4
Index of 'i': 5
Index of 'c': 6
Index of 'h': 7
'''
s = input()
for i, c in enumerate(s):
    print(f"Index of '{c}': {i}")