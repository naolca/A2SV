def countSwaps(a):
    number_of_swaps=0
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                number_of_swaps+=1
            else:
                continue
    print("Array is sorted in {0} swaps.\nFirst Element: {1}\nLast Element: {2} ".format(number_of_swaps,a[0],a[len(a)-1]))