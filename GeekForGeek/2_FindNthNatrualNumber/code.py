#! /usr/bin/env python3

class Solution:
    
    def helper(self, N):

        num, i, remove_count, collect = N, 0, 0, 0
        while num > 0:
            d = num % 10
            
            if d < 9:
                remove_count += d * (10**i - 9**i)            
            else:
                remove_count = d * (10**i - 9**i) + (collect + 1)

            num //= 10
            collect += d * 10**i
            i += 1
        
        return N - remove_count
    
    def findNth(self, N):
        k = 0
        while 9 ** k <= N:
            k += 1
        
        f, t = 1, 10 ** k
        while f < t:
            m = (f + t) // 2
            if self.helper(m) < N:
                f = m + 1
            else:
                t = m
                
        return f
    
if __name__ == '__main__':
    
    N = int(input('Input an integer: '))
    solver = Solution()
    result = solver.findNth(N)
    print(f'The {N}th natrual number without digit 9 is {result}')