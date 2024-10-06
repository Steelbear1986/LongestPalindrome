class Solution:
    def longestPalindrome(self, s: str) -> int:
        g=(Counter(s).values())
        f=[]
        for i in g:
            if i>1 and i%2!=0: f.append(i-1)
            elif i%2==0: f.append(i)
        if sum(g)>sum(f): f.append(1)
        return sum(f)