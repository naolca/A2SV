def dominoPilling(m,n):
    max_Area=m*n
    dominoes=0
    area=1
    while area<max_Area:
        dominoes+=1
        area+=2
    return dominoes

