nums1= [1,1,2,3,4,5,6]
nums2 = [1,2,3,7,8,9]
def merge_two_soted_array(nums1 , nums2):
    n = len(nums1)
    m = len(nums2)
    i,j = 0,0
    result = []

    while i<n and j<m:
        if nums1[i]<= nums2[j]:
            if len(result) == 0 or result[-1]!= nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result) ==0 or result[-1]!= nums2[j]:
                result.append(nums2[j])
            j+=1
    while i < n:
        if len(result) ==0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1
    while j< m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j+=1
    return result
# ✅ Time Complexity:
# O(N + M) — Linear with the sizes of the two arrays.

# ✅ Space Complexity:
# O(N + M) — For the result list.

print(merge_two_soted_array(nums1,nums2))