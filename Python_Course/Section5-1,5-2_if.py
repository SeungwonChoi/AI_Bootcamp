
i = 2

if n < 2:
    print(f"{n}は素数でない")
elif n == 2:
    print(f"{n}は素数")
else:
    while i <= (n / 2):                 #多くてもn/2まで調べればよいため
        if (n % i) == 0:
            print(f"{n}は素数でない")
            break
        i += 1
    else:
        print(f"{n}は素数")