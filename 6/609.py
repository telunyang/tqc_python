'''
TQC+ 程式語言Python 609 矩陣相加

1. 題目說明:
請開啟PYD609.py檔案，依下列題意進行作答，依輸入值建立2*2矩陣，並計算其相加結果，使輸出值符合題意要求。作答完成請另存新檔為PYA609.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。

3. 輸入輸出：
輸入說明
兩個2*2矩陣，皆輸入整數

輸出說明
矩陣1的內容
矩陣2的內容
矩陣1及矩陣2相加的結果

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter matrix 1:
[1, 1]: 3
[1, 2]: 5
[2, 1]: 7
[2, 2]: 5
Enter matrix 2:
[1, 1]: 6
[1, 2]: 9
[2, 1]: 8
[2, 2]: 3
Matrix 1:
3 5 
7 5 
Matrix 2:
6 9 
8 3 
Sum of 2 matrices:
9 14 
15 8 
'''
l1 = [[0, 0], [0, 0]]
l2 = [[0, 0], [0, 0]]
print('Enter matrix 1:')
for i in range(2):
    for j in range(2):
        l1[i][j] = eval(input(f'[{i+1}, {j+1}]: '))
print('Enter matrix 2:')
for i in range(2):
    for j in range(2):
        l2[i][j] = eval(input(f'[{i+1}, {j+1}]: '))
print('Matrix 1:')
for i in range(2):
    print(f'{l1[i][0]} {l1[i][1]} ')
print('Matrix 2:')
for i in range(2):
    print(f'{l2[i][0]} {l2[i][1]} ')
print('Sum of 2 matrices:')
for i in range(2):
    print(f'{l1[i][0] + l2[i][0]} {l1[i][1] + l2[i][1]} ')