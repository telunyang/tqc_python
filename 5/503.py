'''
TQC+ 程式語言Python 503 連加計算

1. 題目說明:
請開啟PYD503.py檔案，依下列題意進行作答，依使用者輸入的整數作為參數傳遞進行連加，使輸出值符合題意要求。作答完成請另存新檔為PYA503.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。

3. 輸入輸出：
輸入說明
兩個整數

輸出說明
從a連加到b的和

範例輸入
33
66
範例輸出
1683
'''
a = eval(input())
b = eval(input())
def compute(a, b):
    sum = 0
    for n in range(a, b + 1):
        sum += n
    return sum
print( compute(a, b) )