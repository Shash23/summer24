def merge(nums1, m, nums2, n):
    """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

    arr1 = nums1[:m]
    print(arr1)
    arr2 = nums2[:n]
    print(arr2)

    for i in arr2:

        arr1.append(i)

    return sorted(arr1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))