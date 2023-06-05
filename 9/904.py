'''
TQC+ 程式語言Python 904 資料計算

1. 題目說明:
請開啟PYD904.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA904.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

範例輸入
無

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
'''
l_h = []
l_w = []
l_people = []
with open("read.txt", "r", encoding="utf-8") as f:
    for line in f:
        l = line.split(' ')
        l_h.append(float(l[1]))
        l_w.append(float(l[2]))
        l_people.append({
            'name': l[0],
            'h': float(l[1]),
            'w': float(l[2])
        })
        print(f'{l[0]} {l[1]} {l[2]}')
print(f'Average height: {sum(l_h)/len(l_h):.2f}')
print(f'Average weight: {sum(l_w)/len(l_w):.2f}')
l_tall = sorted(l_people, key=lambda x:x['h'], reverse=True)
l_heavy = sorted(l_people, key=lambda x:x['w'], reverse=True)
print(f'The tallest is {l_tall[0]["name"]} with {l_tall[0]["h"]:.2f}cm')
print(f'The heaviest is {l_heavy[0]["name"]} with {l_heavy[0]["w"]:.2f}kg')