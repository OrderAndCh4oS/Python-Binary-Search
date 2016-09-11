def scramble(s1,s2):
    sortedList = sorted(s1)
    for s in s2:
        mid = (len(sortedList))/2
        low = 0
        high = len(sortedList)-1
        while low <= high:
            c = sortedList[mid]
            if s > c:
                low = mid+1
            if s < c:
                high = mid-1
            if s == c:   
                del sortedList[mid]
                break
            if low > high and s != sortedList[mid]:
                return False                
            mid = ((high - low) / 2) + low
    return True
