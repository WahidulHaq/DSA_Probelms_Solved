# MERGE SORT IN PYTHON 
left = [1,2,3,4]
right = [1,2,3,4,5,6,7]
# HERE TWO LIST SORTED WITH COMBINED MOR MERGE  
def merge_array(left,right):
    reuslt = []
    i,j = 0, 0
    n = len(left)
    m = len(right)

    while i<n and j<m:
        if left[i] <= right[j]:
            reuslt.append(left[i])
            i+=1
        else:
            reuslt.append(right[j])
            j+=1
    # print(reuslt) HERE ONLY THE MATCH INDEX WILL SORT
    # NOW REMAINING INDEX I WANT TO SORT 
    if i<n:
        while i<n:
            reuslt.append(left[i])
            i+=1
    if j<m:
        while j<m:
            reuslt.append(right[j])
            j+=1
    # print(reuslt) HERE FULL INDEX  WILL SORT
    return reuslt

# NOW MERGE  SORT USING RECURSION

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2 
    left_half = array[:mid]
    right_half = array[mid:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge_array(left=left, right=right)

array = [3,1,2,6,2,4,8,7]
print("-----",merge_sort(array=array))
