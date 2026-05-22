#Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

def LongestPalindromicSubstring(st):
    n = len(st)

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    ans = [0,0]
    maxLength = 0
    for startIndex in range(n-1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if st[startIndex] == st[endIndex]:
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True 
                    if maxLength < endIndex - startIndex + 1:
                        maxLength = endIndex - startIndex + 1
                        ans = [startIndex, endIndex]
    
    i, j = ans
    return st[i:j+1]
            
#return the substring stri has max length å

#recursive 
def findLPSByRecursive(st):
    def solve(st, startIndex, endIndex):
        if startIndex > endIndex:
            return 0
        if startIndex == endIndex:
            return 1
        
        if st[startIndex] == st[endIndex]:
            remainingLength = endIndex - startIndex - 1
            if remainingLength == solve(st, startIndex + 1, endIndex - 1):
                return remainingLength + 2
        c1 = solve(st, startIndex + 1, endIndex)
        c2 = solve(st, startIndex, endIndex - 1)

        return max(c1, c2)
