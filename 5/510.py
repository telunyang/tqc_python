'''
TQC+ 程式語言Python 510 費氏數列

1. 題目說明:
請開啟PYD510.py檔案，依下列題意進行作答，計算費氏數列，並依輸入的正整數回傳費氏數列前n個數值，使輸出值符合題意要求。作答完成請另存新檔為PYA510.py再進行評分。

2. 設計說明：
請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2


3. 輸入輸出：
輸入說明
一個正整數num (num>=2)

輸出說明
依輸入值num，輸出費氏數列前num個的數值（每個數值後方為一個半形空格）

範例輸入1
10
範例輸出1
0 1 1 2 3 5 8 13 21 34 

範例輸入2
20
範例輸出2
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
'''
# 簡易寫法
num = eval(input())
def compute(num):
    l = [0,1]
    if num > 2:
        for i in range(num-2): 
            l.append(l[-2] + l[-1])
    return l

l = compute(num)
for n in l:
    print(n, end=" ")



# 一般寫法
num = eval(input())
def compute(num):
    if num == 0: return 0
    if num == 1: return 1
    return compute(num - 1) + compute(num - 2)
s = ''
for i in range(0, num):
    s += str(compute(i)) + ' '
print(s)