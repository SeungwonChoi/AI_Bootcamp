from random import random

length = int(input("作成する数値列の長さを入力してください。 "))
numbers = []

for i in range(length):
    numbers.append(random())

print(f"作成した数値列の平均は {sum(numbers)/len(numbers)} です。")