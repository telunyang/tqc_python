'''
TQC+ 程式語言Python 908 單字次數計算

1. 題目說明:
請開啟PYD908.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA908.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

3. 輸入輸出：
輸入說明
讀取read.txt的內容，以及檔案中某單字出現的次數

輸出說明
輸出符合次數的單字，並依單字的第一個字母大小排序

範例輸入
read.txt
3
範例輸出
a
is
programming
'''
file = input()
n = eval(input())
with open(file, "r", encoding="utf-8") as f:
    content = f.read()
    content = content.replace('\n', ' ')
    l_word = content.split(' ')
    s_word = sorted(set(l_word))
    for word in s_word:
        if l_word.count(word) == n:
            print(word)