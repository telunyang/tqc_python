'''
TQC+ 程式語言Python 809 密碼規則

1. 題目說明:
請開啟PYD809.py檔案，依下列題意進行作答，檢查密碼是否符合規則，使輸出值符合題意要求。作答完成請另存新檔為PYA809.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
　a. 必須至少八個字元。
　b. 只包含英文字母和數字。
　c. 至少要有一個大寫英文字母。
　d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
判斷是否符合密碼規則

範例輸入1
39Gfjkd98
範例輸出1
Valid password

範例輸入2
39dk8fh
範例輸出2
Invalid password
'''
s = input()
a = len(s)
b = s.isalnum()
c = 0
for char in s:
    if char.isupper(): c = 1
if a >= 8 and b == True and c == 1:
    print('Valid password')
else:
    print('Invalid password')