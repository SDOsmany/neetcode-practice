
def check(mod, eq):
    s = mod.Solution()
    eq(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3]), 2.0)
    eq(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2, 4]), 2.5)
    eq(s.findMedianSortedArrays(nums1=[], nums2=[1]), 1.0)
