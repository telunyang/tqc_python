'''
TQC+ 程式語言Python 610 平均溫度

1. 題目說明:
請開啟PYD610.py檔案，依下列題意進行作答，依輸入值計算四週的平均溫度及最高、最低溫度，使輸出值符合題意要求。作答完成請另存新檔為PYA610.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

3. 輸入輸出：
輸入說明
四週各三天的溫度

輸出說明
平均溫度
最高溫度
最低溫度

輸入與輸出會交雜如下，輸出的部份以粗體字表示
下圖中的 粉紅色點 為 空格


'''
l1 = [0, 0, 0]
l2 = [0, 0, 0]
l3 = [0, 0, 0]
l4 = [0, 0, 0]
print('Week 1:')
for i in range(3):
    l1[i] = eval(input(f'Day {i+1}:'))
print('Week 2:')
for i in range(3):
    l2[i] = eval(input(f'Day {i+1}:'))
print('Week 3:')
for i in range(3):
    l3[i] = eval(input(f'Day {i+1}:'))
print('Week 4:')
for i in range(3):
    l4[i] = eval(input(f'Day {i+1}:'))
l = l1 + l2 + l3 + l4
print(f'Average: {sum(l)/len(l):.2f}')
print(f'Highest: {max(l)}')
print(f'Lowest: {min(l)}')