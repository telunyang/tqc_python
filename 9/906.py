'''
TQC+ 程式語言Python 906 字串資料取代

1. 題目說明:
請開啟PYD906.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA906.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。

3. 輸入輸出：
輸入說明
輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）

輸出說明
輸出檔案中的內容
輸出取代指定字串後的檔案內容

範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants
'''
file = input()
s1 = input()
s2 = input()
print('=== Before the replacement')
with open(file, "r", encoding="utf-8") as f:
    content = f.read()
print(content)
print('=== After the replacement')
content = content.replace(s1, s2)
print(content)