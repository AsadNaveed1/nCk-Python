def combinations(n,k):
    print(str(n)+"C"+str(k)+" = ", end="")
    if (k == 0 or n == k):
        print(str(1))
        return 1
    else:
        print(str(n-1)+"C"+str(k-1)+" + "+str(n-1)+"C"+str(k))
        ans = combinations(n-1, k-1) + combinations(n-1, k)
        print(str(n)+"C"+str(k)+" = "+str(ans))
        return ans


n = input("")
k = input("")
combinations(int(n), int(k))
