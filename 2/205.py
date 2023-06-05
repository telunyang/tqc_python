'''
TQC+ 程式語言Python 205 字元判斷

1. 題目說明:
請開啟PYD205.py檔案，依下列題意進行作答，判斷輸入值的字元，使輸出值符合題意要求。作答完成請另存新檔為PYA205.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元。

3. 輸入輸出：
輸入說明
一個字元

輸出說明
判斷是英文字母（包括大、小寫）、數字、或者其它字元

範例輸入1
P
範例輸出1
P is an alphabet.

範例輸入2
@
範例輸出2
@ is a symbol.

範例輸入3
7
範例輸出3
7 is a number.
'''
c = input()
if c.isalpha(): print(f'{c} is an alphabet.')
elif c.isdigit(): print(f'{c} is a number.')
else: print(f'{c} is a symbol.')