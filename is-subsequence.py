# https://leetcode.com/problems/is-subsequence/submissions/
# 方針
# アルファベットをkey, valueにはtのindexとするdictを作成する
# sの文字がdictになければFalse
# dictにある場合
#  - posより後に文字があればok -> posを更新
#. - tの最後のloopで後に文字がない場合 -> False
#  - 既にposが最終まで行っている場合はFalse
#  - pos

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hashmap = {}
        
        # hashの作成
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]].append(i)
            else:
                hashmap[t[i]] = [i]
                
        pos = 0
        for j in range(len(s)):
            # posが最後の場合は終了
            if (pos+1) == len(t):
                return False
            
            if s[j] in hashmap:
                arr = hashmap[s[j]]
                for k in range(len(arr)):                
                    if arr[k] > pos or pos == 0:
                        pos = arr[k]
                        break
                    else:
                        if k + 1 == len(arr):
                            return False
                        
            else:
                return False
        
        return True
