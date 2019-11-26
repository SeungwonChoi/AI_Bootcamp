try:
    M = float(input("被除数を入力してください。 "))
    N = float(input("除数を入力してください。 "))
    print(f"割り算の結果は {M/N} です。")
except:
    print(f"割り算出来ない値が入力されました。")