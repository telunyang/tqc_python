'''
TQC+ 程式語言Python 907 詳細資料顯示

1. 題目說明:
請開啟PYD907.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA907.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名read.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。

3. 輸入輸出：
輸入說明
讀取read.txt

輸出說明
行數
單字數
字元數（不含空白）

範例輸入
read.txt
範例輸出
6 line(s)
102 word(s)
614 character(s)
'''
file = input()
count_line = 0
count_word = 0
count_char = 0
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        count_line += 1
        count_word += len(line.split(' '))
        count_char += len(line.replace(' ', '').replace('\n', ''))
print(f'{count_line} line(s)')
print(f'{count_word} word(s)')
print(f'{count_char} character(s)')