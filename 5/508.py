'''
TQC+ 程式語言Python 508 最大公因數

1. 題目說明:
請開啟PYD508.py檔案，依下列題意進行作答，計算兩個正整數的最大公因數，使輸出值符合題意要求。作答完成請另存新檔為PYA508.py再進行評分。。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

3. 輸入輸出：
輸入說明
兩個正整數（以半形逗號分隔）

x,y

輸出說明
最大公因數

範例輸入1
12,8
範例輸出1
4

範例輸入2
4,6
範例輸出2
2
'''
# 基本的運算思維
x, y = eval(input())
def compute(x, y):
    while y != 0:
        tmp = y
        y = x % y
        x = tmp
    return x
print( compute(x, y) )



# 更快的解法: math.gcd() 是取得最大公因數的函式
# gcd = Greatest Common Divisor
import math
x, y = eval(input())
def compute(x, y):
    return math.gcd(x, y)
print( compute(x, y) )