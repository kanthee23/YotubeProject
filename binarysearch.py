def b_search(arr,x,start,end):
    middle = (start + end) //2

    if arr[middle] == x:
        return middle
    elif arr[middle] > x:
        if start > middle-1 :
            return 'Element is not present in array.'
        else:
            return b_search(arr,x,start, middle-1 )
    elif arr[middle] < x:
        if middle + 1 > end:
            return 'Element is not present in array.'
        else:
            return b_search(arr,x, middle + 1 , end)


a1 = [10,20,30,40,50,60,70,80,90,100,110,120,130]
x = 40
print(b_search(a1,x,0,len(a1)-1))
