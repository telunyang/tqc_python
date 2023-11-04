'''
TQC+ 程式語言Python 110 正n邊形面積計算

1. 題目說明:
請開啟PYD110.py檔案，依下列題意進行作答，計算正n邊形面積，使輸出值符合題意要求。作答完成請另存新檔為PYA110.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下：Area = n*math.pow(s, 2))/(4*math.tan(math.pi/n))
提示3：輸出浮點數到小數點後第四位

3. 輸入輸出：
輸入說明
正數n、s

輸出說明
正n邊形面積

範例輸入
8
6
範例輸出
Area = 173.8234
'''
import math
n = eval(input())
s = eval(input())
print(f'Area = {(n*math.pow(s, 2))/(4*math.tan(math.pi/n)):.4f}')

# 算式也可以寫成:
# (n*s**2)/(4*math.tan(math.pi/n))