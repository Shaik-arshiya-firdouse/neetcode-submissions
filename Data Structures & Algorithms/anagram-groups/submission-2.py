class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        n=len(strs)
        indexes={}

        for word in strs:
            key=tuple(sorted(word))

            if key not in indexes:
                indexes[key] = [word]
            
            else:
                indexes[key].append(word)
        print(indexes)

        for value in indexes.values():
            ans.append(value) 
        return ans