#詞頻分析
import os

path = "C:\\Users\\TibeMe_user\\Desktop\\Project\\article\\TSLA" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱

def gettext(file):
    txt = open(file, "r", errors='ignore').read()
    txt = txt.lower()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]_{|}~':
        txt = txt.replace(ch, "")
    return txt

counts = {}
for file in files: #遍歷資料夾
    if not os.path.isdir(file): #判斷是否是資料夾，不是資料夾才打開
        f = path + "\\" + file  #檔案名稱
    txt = gettext(f)
    words = txt.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
#輸出前十字詞
for i in range(100):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))