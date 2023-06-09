'''
TQC+ 程式語言Python 304 迴圈倍數總和

1. 題目說明:
請開啟PYD304.py檔案，依下列題意進行作答，依輸入值計算所有5之倍數總和，使輸出值符合題意要求。作答完成請另存新檔為PYA304.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
所有5之倍數數字總和

範例輸入
21
範例輸出
50
'''
a = eval(input())
sum = 0
for n in range(1, a+1):
    if n % 5 == 0:
        sum += n
print(sum)