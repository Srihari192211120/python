def pythtriplets(limit):
    a,b,c = 0,0,0
    m = 2
    while(c<limit):
        for n in range(1,m):
            a = m*m -n*n
            b = 2*m*n
            c = m*m+n*n
            if(c>limit):
                break
            print(f"{a} {b} {c}")
        m+=1


limit = int(input("enter a limit: "))
pythtriplets(limit)
