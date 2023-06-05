'''
TQC+ 程式語言Python 905 字串資料刪除

1. 題目說明:
請開啟PYD905.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA905.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。

3. 輸入輸出：
輸入說明
輸入data.txt及一個字串

輸出說明
先輸出原檔案內容，再輸入刪除指定字串後的新檔案內容

範例輸入1
data.txt
Tomato
範例輸出1
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian

=== After the deletion
Apple Kiwi Banana
 Pear Durian
 

範例輸入2
data.txt
Kiwi
範例輸出2
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian

=== After the deletion
Apple  Banana
Tomato Pear Durian

'''
file = input()
s = input()
print('=== Before the deletion')
with open(file, "r", encoding="utf-8") as f:
    content = f.read()
print(content)
print('=== After the deletion')
with open(file, "w", encoding="utf-8") as f:
    content = content.replace(s, '')
    f.write(content)
print(content)