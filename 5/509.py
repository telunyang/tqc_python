'''
TQC+ 程式語言Python 509 最簡分數

1. 題目說明:
請開啟PYD509.py檔案，依下列題意進行作答，加總兩個分數總和，並簡化為最簡分數，使輸出值符合題意要求。作答完成請另存新檔為PYA509.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數的和為p/q，接著將p和q傳遞給名為compute()函式，此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）。再將p和q各除以其最大公因數，最後輸出的結果必須以最簡分數表示。

3. 輸入輸出：
輸入說明
四個正整數（以半形逗號分隔）
x,y
m,n

輸出說明
兩個分數和的最簡分數

無

範例輸入1
1,2
1,6
範例輸出1
1/2 + 1/6 = 2/3

範例輸入2
12,16
18,32
範例輸出2
12/16 + 18/32 = 21/16
'''
# 基本的運算思維
x, y = eval(input())
m, n = eval(input())
q = y * n
p = x * n + y * m
def compute(p, q):
    while q != 0:
        tmp = q
        q = p % q
        p = tmp
    return p
gcd = compute(p, q)
print( f'{x}/{y} + {m}/{n} = {p / gcd:.0f}/{ q / gcd:.0f}' )



# 更快的解法: math.gcd() 是取得最大公因數的函式
# gcd = Greatest Common Divisor
import math
x, y = eval(input())
m, n = eval(input())
q = y * n
p = x * n + y * m
def compute(p, q):
    return math.gcd(p, q)
gcd = compute(p, q)
print( f'{x}/{y} + {m}/{n} = {p / gcd:.0f}/{ q / gcd:.0f}' )