'''
TQC+ 程式語言Python 805 字串輸出

1. 題目說明:
請開啟PYD805.py檔案，依下列題意進行作答，將字串依規則進行輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA805.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入一個長度為6的字串，將此字串分別置於10個欄位的寬度的左邊、中間和右邊，並顯示這三個結果，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
一個長度為6的字串

輸出說明
格式化輸出

範例輸入
python
範例輸出
|python    |
|  python  |
|    python|
'''
s = input()
print(f'|{s:<10}|')
print(f'|{s:^10}|')
print(f'|{s:>10}|')