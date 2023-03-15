class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rev_arr = arr[::-1]
        max_num = -1

        for i in range(len(rev_arr)):
            temp = rev_arr[i]
            rev_arr[i] = max_num
            max_num = max(max_num, temp)
        
        return rev_arr[::-1]