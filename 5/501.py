'''
TQC+ 程式語言Python 501 訊息顯示

1. 題目說明:
請開啟PYD501.py檔案，依下列題意進行作答，依使用者輸入之訊息進行顯示，使輸出值符合題意要求。作答完成請另存新檔為PYA501.py再進行評分。

2. 設計說明：
請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、學號（Student ID）和姓名（Name）並顯示這些訊息。

3. 輸入輸出：
輸入說明
三個字串

輸出說明
系別（Department）
學號（Student ID）
姓名（Name）

範例輸入
Information Management
123456789
Tina Chen
範例輸出
Department: Information Management
Student ID: 123456789
Name: Tina Chen
'''
d = input()
s = input()
n = input()
def compute(d, s, n):
    print(f'Department: {d}')
    print(f'Student ID: {s}')
    print(f'Name: {n}')
compute(d, s, n)