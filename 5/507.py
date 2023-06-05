'''
TQC+ 程式語言Python 507 質數

1. 題目說明:
請開啟PYD507.py檔案，依下列題意進行作答，判斷輸入值是否為質數，使輸出值符合題意要求。作答完成請另存新檔為PYA507.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個整數x，並將x傳遞給名為compute()的函式，此函式將回傳x是否為質數（Prime number）的布林值，接著再將判斷結果輸出。如輸入值為質數顯示【Prime】，否則顯示【Not Prime】。

3. 輸入輸出：
輸入說明
一個整數

輸出說明
判斷是否為質數，若為質數顯示【Prime】，否則顯示【Not Prime】

範例輸入1
3
範例輸出1
Prime

範例輸入2
6
範例輸出2
Not Prime

範例輸入3
1
範例輸出3
Not Prime

範例輸入4
0
範例輸出4
Not Prime

範例輸入5
-5
範例輸出5
Not Prime
'''
x = eval(input())
def compute(x):
    if x <= 1: return 'Not Prime'
    result = 'Prime'
    for i in range(2, x):
        if x % i == 0: 
            result = 'Not Prime'
            break
    return result
print( compute(x) )