class Solution:
    def longestPalindrome(self, s: str) -> int:
        g=(Counter(s).values())
        f=0
        for i in g:
            if i>1 and i%2!=0: f+=(i-1)
            elif i%2==0: f+=i
        if sum(g)>f: f+=1
        return f
