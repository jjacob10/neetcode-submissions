class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            big = 0
            for j in range (i + 1, len(arr)):
                big = max(big, arr[j])
            arr[i] = big
        arr[len(arr) - 1] = -1
        return arr
            