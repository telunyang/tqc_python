'''
TQC+ 程式語言Python 608 最大最小值索引

1. 題目說明:
請開啟PYD608.py檔案，依下列題意進行作答，建立3*3矩陣並輸出矩陣最大值與最小值的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA608.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
'''
l = [eval(input()) for i in range(9)]
max_value = max(l)
min_value = min(l)
print(f'Index of the largest number {max_value} is: ({l.index(max_value)//3}, {l.index(max_value)%3})')
print(f'Index of the smallest number {min_value} is: ({l.index(min_value)//3}, {l.index(min_value)%3})')