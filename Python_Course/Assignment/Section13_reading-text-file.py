#仮にsample.txtを使用
file = "../data/sample.txt"

with open(file) as fileobj:
    text = fileobj.read()
    wordlist = text.split(" ")              #区切り文字を基準に全単語を求める
    worddict = dict.fromkeys(wordlist, 0)   #全単語を辞書化し、値の初期値を0とする
    
    #全単語を確認し、辞書のキーごとにカウントアップする
    for word in wordlist:
        worddict[word] += 1
    
    for key, count in worddict.items():
        print(f"{key}は{count}回使われました。")