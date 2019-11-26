n = 3

print(2)

while True:
    i = 2
    flag = 0
    
    while i <= (n / 2):     #多くてもn/2まで調べればよいため
        if (n % i) == 0:
            flag = 1
            break
        i += 1
        
    if flag == 0:
        print(n)
        
    n += 1