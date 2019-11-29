def determination_prime_number(n):
    i = 2
    
    if n < 2:
        return print(f"{n}は素数でない")
    elif n == 2:
        return print(f"{n}は素数")
    else:
        while i <= (n / 2):                 #多くてもn/2まで調べればよいため
            if (n % i) == 0:
                return print(f"{n}は素数でない")
            i += 1
        else:
            return print(f"{n}は素数")


n = int(input("素数か確認したい整数nを入力してください。 "))
determination_prime_number(n)