'''
TQC+ 程式語言Python 407 不定數迴圈-閏年判斷

1. 題目說明:
請開啟PYD407.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA407.py再進行評分。

2. 設計說明：
(1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈。

3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
判斷是否為閏年或平年

輸入與輸出會交雜如下，輸出的部份以粗體字表示
2017
2017 is not a leap year.
2000
2000 is a leap year.
2016
2016 is a leap year.
2009
2009 is not a leap year.
2018
2018 is not a leap year.
-9999
'''
while True:
    y = eval(input())
    if y == -9999: break
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(f'{y} is a leap year.')
    else:
        print(f'{y} is not a leap year.')