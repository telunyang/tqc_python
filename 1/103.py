'''
TQC+ 程式語言Python 103 字串格式化輸出

1. 題目說明:
請開啟PYD103.py檔案，依下列題意進行作答，輸入單字及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA103.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個單字

輸出說明
格式化輸出

範例輸入
I
enjoy
learning
Python

範例輸出
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
'''
a = input()
b = input()
c = input()
d = input()
print(f'|{a:>10} {b:>10}|')
print(f'|{c:>10} {d:>10}|')
print(f'|{a:<10} {b:<10}|')
print(f'|{c:<10} {d:<10}|')