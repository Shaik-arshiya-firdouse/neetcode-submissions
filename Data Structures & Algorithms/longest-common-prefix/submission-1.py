class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        i=0
        while i < len(strs[0]):
            ref=strs[0][i]

            for j in range(1,len(strs)):

                if i>=len(strs[j]):
                    return ans

                if ref!=strs[j][i]:
                    return ans

            ans+=ref
            i+=1
        return ans
                
            
        
        