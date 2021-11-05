"""
解题思路：
1. 因为只有26个字母，将每个单词映射到大小为26的数组里进行编码，然后使用dict存储
2. 对每个字符串排序，然后同样使用dict存储
"""

def groupAnagrams(strs):
    """
    time: beats 24.80%
    memory: beats 64.17%
    """
    result = {}
    for _str in strs:
        temp = [0]*26
        for s in _str:
            temp[ord(s)-ord('a')]+=1
        temp = str(temp)
        # temp = ''.join(sorted(_str))
        val = result.setdefault(temp,[])
        val.append(_str)
    return list(result.values())

def groupAnagrams(strs):
    """
    time: beats 38.50%
    memory: beats 77.38%
    """
    result = {}
    for _str in strs:
        temp = ''.join(sorted(_str))
        val = result.setdefault(temp,[])
        val.append(_str)
    return list(result.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
