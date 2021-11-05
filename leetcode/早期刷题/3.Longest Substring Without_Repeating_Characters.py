"""
解体思路：
使用两个下标start和end遍历数组，两个指针间的数据存储到一个集合count中，如果end遍历的元素不在count中，
添加该元素，如果在count中，就将start向end移动直到遇到和end重复的元素，并将这个过程中遍历的元素从count
中移除，然后更新start并将end此时遍历的元素添加到count中，直到遍历完数组。
"""

def lengthOfLongestSubstring_v1(s):
    """
    time: beats 46.80%
    memory: beats 70.02%
    """
    if len(s) == 0:
        return 0
    count = [0]*129
    max_length = 1
    count[ord(s[0])] += 1
    start = 0
    end = 1
    while True:
        if end == len(s):
            max_length = max(end-start,max_length)
            break
        if count[ord(s[end])] == 0:   # 如果end指针指的也是新的字母，就记录下来
            count[ord(s[end])] += 1
            # print('sucess',start,end)
        else:
            # 更新长度
            max_length = max(end-start,max_length)

            while s[start] != s[end]:
                count[ord(s[start])] -= 1
                start+=1
            count[ord(s[start])] -= 1
            start+=1
            # 

            count[ord(s[end])] += 1
            # print('error',start,end)
        end +=1
    
    return max_length

def lengthOfLongestSubstring(s):
    """
    time: beats 65.33%
    memory: beats 96.95%
    """
    if len(s) == 0:
        return 0

    count = set()        # 使用一个set存储子集
    max_length = 1
    count.add(s[0])
    start = 0
    end = 1

    while True:

        if end == len(s):   # 遍历完毕，更新结果
            max_length = max(end-start,max_length)
            break

        if s[end] not in count:   # 如果end指针指的也是新的字母，就记录下来
            count.add(s[end])
        else:
            # 更新长度
            max_length = max(end-start,max_length)

            # 将start 指针往后移动
            while s[start] != s[end]:
                count.remove(s[start])
                start+=1
            count.remove(s[start])
            start+=1
            
            # 确保没有重复字母后，添加当前遍历的字符
            count.add(s[end])
        end +=1
    
    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))




            
        
            
