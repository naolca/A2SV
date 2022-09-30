def selectionSort(lst):
    
    min_idx=0
    min_value=lst[min_idx]
    for value in lst[min_idx+1:]:
        min_value=lst[min_idx]
        if value<min_value:
            shifter=lst.index(value)
            lst[min_idx],lst[shifter]=lst[shifter], lst[min_idx]
            min_idx+=1
            print(lst)
        else:
            min_idx+=1
            print(lst)
    print(lst)
            
         



