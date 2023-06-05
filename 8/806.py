'''
TQC+ 程式語言Python 806 字元次數計算

1. 題目說明:
請開啟PYD806.py檔案，依下列題意進行作答，計算指定字元出現的次數，使輸出值符合題意要求。作答完成請另存新檔為PYA806.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。

3. 輸入輸出：
輸入說明
一個字串和一個字元

輸出說明
字串中指定字元出現的次數

範例輸入
Our country is beautiful
u
範例輸出
u occurs 4 time(s)
'''
s = input()
c = input()
def compute(s, c):
    return s.count(c)
print(f'{c} occurs {compute(s, c)} time(s)')