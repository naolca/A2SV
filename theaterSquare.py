def theatreSquare(n,m,a):
    vertically=1#this stores the minimum number of granites to cover the vertical part of the square.
    temp=a
    while a<n:
        a*=2
        vertically+=1
    horisontally=1##this stores the minimum number of granites to cover the horisontal part of the square.
    a=temp
    while a<m:
        a*=2
        horisontally+=1

    return horisontally*vertically
print(theatreSquare(6,6,4))

