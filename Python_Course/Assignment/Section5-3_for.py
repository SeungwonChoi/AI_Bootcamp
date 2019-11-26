from random import randint
from string import printable as p_able

length = int(input("作成するパスワードの長さを入力してください。 "))
pwd = ""

for i in range(length):
    n = randint(0,94)       #string.printableの95番目以降は除外
    pwd += p_able[n]

print(f"作成されたパスワードは {pwd} です。")