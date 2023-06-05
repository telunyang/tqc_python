'''
TQC+ 程式語言Python 703 數組條件判斷

1. 題目說明:
請開啟PYD703.py檔案，依下列題意進行作答，輸入字串至數組並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA703.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），以字串"end"為結束點（數組中不包含字串"end"）。接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

3. 輸入輸出：
輸入說明
至少輸入五個字串至數組，直至end結束輸入

輸出說明
數組
該數組的前三個元素
該數組最後三個元素

範例輸入
president
dean
chair
staff
teacher
student
end
範例輸出
('president', 'dean', 'chair', 'staff', 'teacher', 'student')
('president', 'dean', 'chair')
('staff', 'teacher', 'student')
'''
t = tuple()
while True:
    s = input()
    if s == 'end': break
    t += (s,)
print(t)
print(t[0:3])
print(t[-3:])