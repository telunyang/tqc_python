'''
TQC+ 程式語言Python 910 學生基本資料

1. 題目說明:
請開啟PYD910.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA910.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.dat檔案為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。

3. 輸入輸出：
輸入說明
讀取read.dat

輸出說明
讀取檔案內容，並格式化輸出男生人數和女生人數

範例輸入
無

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2
'''
sum_male = 0
sum_female = 0
with open('read.dat', "r", encoding="utf-8") as f:
    for line in f:
        print(line)
        l = line.split(' ')
        if l[2] == '1': sum_male += 1
        if l[2] == '0': sum_female += 1
print(f'Number of males: {sum_male}')
print(f'Number of females: {sum_female}')