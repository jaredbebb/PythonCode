#binary search of array using python

numbarr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = 5

def numsearch(inarr, integ):
    low = 0
    high = len(inarr)-1
    
    while low <=high:
        i = (low + high)//2
        if inarr[i] == integ:
            print("found the int! Its at arr position ",inarr[i])
            break
            
        else:
            if integ < inarr[i]:
                high = i-1
            else:
                low = i +1 

numsearch(numbarr, number)