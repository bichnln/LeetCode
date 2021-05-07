class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """ Merge nums2 to nums2 1, with m is the number of valid element of nums1 and n is the len of nums2 """
        i = 0
        k = 0
        count = m
        while i <= count and len(nums2) > 0:
            # print(i, k, nums1, nums2)
            if nums1[i] >= nums2[k]:
                self.shiftBackward(nums1, i, count)
                nums1[i] = nums2[k]
                nums2.pop(k)
                count += 1
            else:
                i += 1
        if (len(nums2) > 0):
            for i in range(0, len(nums2)):
                nums1[i + count] = nums2[i]

    def shiftBackward(self, arr: [], index: int, num: int) -> None:
        """ Shift elements from input index backward by one, num is number of valid elements in arr """
        for i in range(num, index, -1):
            arr[i] = arr[i-1]
        arr[index] = 0


if __name__ == "__main__":
    s = Solution()

    list1 = [4, 0, 0, 0, 0, 0]
    list2 = [1, 2, 3, 5, 6]

    s.merge(list1, 1, list2, 5)

    print(list1)

