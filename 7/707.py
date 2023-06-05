'''
TQC+ 程式語言Python 707 共同科目

1. 題目說明:
請開啟PYD707.py檔案，依下列題意進行作答，輸入X組和Y組各自的科目至集合中並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA707.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。請依序分行顯示(1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。

提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

3. 輸入輸出：
輸入說明
輸入X組和Y組各自的科目至集合，直至end結束輸入

輸出說明
X組和Y組的所有科目
X組和Y組的共同科目
Y組有但X組沒有的科目
X組和Y組彼此沒有的科目（不包含相同科目）

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter group X's subjects:
Math
Literature
English
History
Geography
end
Enter group Y's subjects:
Math
Literature
Chinese
Physical
Chemistry
end
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'Physical']
['Literature', 'Math']
['Chemistry', 'Chinese', 'Physical']
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']
'''
set_x = set()
set_y = set()
print("Enter group X's subjects:")
while True:
    s = input()
    if s == 'end': break
    set_x.add(s)
print("Enter group Y's subjects:")
while True:
    s = input()
    if s == 'end': break
    set_y.add(s)
print(sorted(set_x.union(set_y)))
print(sorted(set_x.intersection(set_y)))
print(sorted(set_y.difference(set_x)))
print(sorted(set_y.symmetric_difference(set_x)))