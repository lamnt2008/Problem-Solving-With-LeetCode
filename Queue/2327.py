from collections import deque

#Problem: https://leetcode.com/problems/number-of-people-aware-of-a-secret/?envType=problem-list-v2&envId=queue

#Know: luu nhung nguoi biet bi mat nhung chua den delay share
#Share luu nhung nguoi biet bi mat va da duoc share.
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know, share = deque([(1,1)]), deque([])
        know_cnt, share_cnt = 1, 0

        for i in range(2, n+1):
            if know and know[0][0] == i - delay:
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget:
                share_cnt -= share[0][1]
                share.popleft()
            if share:
                know_cnt += share_cnt
                know.append((i, share_cnt))
        
        return (know_cnt + share_cnt) % (10**9 + 7)
