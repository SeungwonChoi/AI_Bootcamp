names = ["sun", "moon", "star"]                                 #任意のリストを定義
print(list(zip([i for i in range(1,len(names)+1)], names)))     #任意のリストの長さを参照し、順番付け