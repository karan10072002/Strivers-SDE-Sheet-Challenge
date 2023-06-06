class Solution(object):
    def generate(self, n):
        pascal = []
        for i in range(1, n+1):
            C=[1]  
            for j in range(1, i):  
                C.append(C[-1] * (i - j) // j )
            pascal.append(C)  
        return pascal
