'''
TQC+ 程式語言Python 705 子集合與超集合

1. 題目說明:
請開啟PYD705.py檔案，依下列題意進行作答，將整數各自儲存至三個集合中並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA705.py再進行評分。

2. 設計說明：
請撰寫一程式，依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。接著回答：set2是否為set1的子集合（subset）？set3是否為set1的超集合（superset）？

3. 輸入輸出：
輸入說明
依序分別輸入五個、三個、九個整數

輸出說明
顯示回覆：
set2是否為set1的子集合（subset）？
set3是否為set1的超集合（superset）？

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Input to set1:
3
28
-2
7
39
Input to set2:
2
77
0
Input to set3:
3
28
12
99
39
7
-1
-2
65
set2 is subset of set1: False
set3 is superset of set1: True
'''
set1 = set()
set2 = set()
set3 = set()
print('Input to set1:')
for i in range(5):
    set1.add(eval(input()))
print('Input to set2:')
for i in range(3):
    set2.add(eval(input()))
print('Input to set3:')
for i in range(9):
    set3.add(eval(input()))
print(f'set2 is subset of set1: {set2.issubset(set1)}')
print(f'set3 is superset of set1: {set3.issuperset(set1)}')