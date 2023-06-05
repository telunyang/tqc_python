'''
TQC+ 程式語言Python 505 依參數格式化輸出

1. 題目說明:
請開啟PYD505.py檔案，依下列題意進行作答，依使用者輸入的參數進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA505.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的三個參數，變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列。

提示：輸出的每一個字元後方有一空格。

3. 輸入輸出：
輸入說明
三個參數，分別為a（代表字元character）、x（代表個數）、y（代表列數）

輸出說明
一列印出x個a字元，總共印出y列

範例輸入
e
5
4
範例輸出
e e e e e 
e e e e e 
e e e e e 
e e e e e 
'''
a = input()
x = eval(input())
y = eval(input())
def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(a, end=" ")
        print()
compute(a, x, y)