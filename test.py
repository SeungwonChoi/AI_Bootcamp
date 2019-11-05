def testgen() :
    n = 0

    while True :
        print(f"n = {n}")
        received = yield n
        print(f"received = {received}")
        if received :
            n = received
        else :
            n = n + 1