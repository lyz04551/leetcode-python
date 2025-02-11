class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if s_ not in table:
                table[s_] = [s]
            else:
                table[s_].append(s)
        return list(table.values())
