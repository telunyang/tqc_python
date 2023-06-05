'''
TQC+ 程式語言Python 902 資料加總

1. 題目說明:
請開啟PYD902.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA902.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。

3. 輸入輸出：
輸入說明
讀取read.txt的內容（內容為數字，以空白分隔）

輸出說明
總和

範例輸入
無

範例輸出
660
'''
sum = 0
with open("read.txt", "r", encoding="utf-8") as f:
    s = f.read()
    for n in s.split(' '):
        sum += int(n)
print(sum)