'''
TQC+ 程式語言Python 506 一元二次方程式

1. 題目說明:
請開啟PYD506.py檔案，依下列題意進行作答，依使用者輸入的數字作為參數傳遞進行公式計算，使輸出值符合題意要求。作答完成請另存新檔為PYA506.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式 a * x**2 + b * x + c = 0 的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

提示：
輸出有順序性
回傳方程式的解，無須考慮小數點位數

3. 輸入輸出：
輸入說明
三個整數，分別為a、b、c

輸出說明
代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】

範例輸入1
2
-3
1
範例輸出1
1.0, 0.5

範例輸入2
9
9
8
範例輸出2
Your equation has no root.

範例輸入3
1
2
1
範例輸出3
-1.0
'''
# 參考圖片: https://www.liveism.com/images/live-math-iconcept-online_600x315_i8142_6.jpg
a = eval(input())
b = eval(input())
c = eval(input())
def compute(a, b, c):
    check = b**2 - 4*a*c
    if check < 0: return 'Your equation has no root.'
    elif check == 0:
        return f'{-b / 2*a:.1f}'
    else:
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        return f'{x1:.1f}, {x2:.1f}'
print( compute(a, b, c) )