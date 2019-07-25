def flip(ls, k):
    for i in range(k//2):
        ls[i], ls[k-i-1] = ls[k-i-1], ls[i]

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []

        for exempt in range(0, len(A)):
            max_i,_ = max(enumerate(A[:len(A)-exempt]), key=lambda t: t[1])
                
            if max_i == len(A)-exempt-1:
                continue

            flip(A, max_i+1)
            flip(A, len(A)-exempt)

            flips.extend([max_i+1, len(A)-exempt])
        
        return flips
