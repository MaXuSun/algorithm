* LC 5：最长回文子串
  * 初始化：dp[i][i]=True, dp[i-1][i]=True if s[i-1]==s[i]
  * 转移方程：dp[i][j] = dp[i+1][j-1] if s[i+1]==s[j-1] else False
* LC 70：爬楼梯
  * 初始化：dp[1] = 1, dp[2]=2
  * 转移方程：dp[i] = dp[i-1]+dp[i-2]
* LC 42：接雨水
  * 初始化：dp[0] = height[0]
  * 转移方程：dp[i] = max(dp[i-1],height[i])
* LC 22：括号生成
  * 初始化：dp[0] = [""],dp[1] = ["()"]
  * 转移方程：dp[i] = '(dp[j])d[i-j-1]'   j from 1 to i
* LC 121：买卖股票的最佳时机
  * 初始化：dp[0] = inf
  * 转移方程：dp[i] = min(dp[i-1],prices[i-1])
* LC 72：编辑距离
  * 初始化 dp[0][i] = i,dp[i][0] = i
  * 转移方程：dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j] else min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
* LC 53：最大子数组和
  * 初始化：dp[0] = nums[0]
  * 转移方程：dp[i] = max(dp[i-1]+nums[i],nums[i])
* LC 152：乘积最大子数组
  * 初始化：pos_dp[-1] = 1, nv_dp[-1] = 1
  * 转移方程：
```python
    if nums[i]>0: 
        pos_dp[i] = max(nums[i],pos_dp[i-1]*nums[i]
        nv_dp[i] = nv_dp[i-1]*nums[i] 
    else:
        pos_dp[i] = nv_dp[i-1]*nums[i]
        nv_dp[i] = min(pos_dp[i-1]*nums[i],nums[i])
```
* LC 124：二叉树中的最大路径和
  * 初始化：left = max(dfs(root.left),0), right = max(dfs(root.left),0)
  * 转移方程：max(left,right)+root.val
* LC 32：最长有效括号
* LC 139：单词拆分
* LC 96：不同的二叉搜索树
* LC 面试题 17.24. 最大子矩：
* LC 309：买卖股票时机含冷冻期
* LC 198：打家劫舍：
* LC 55：跳跃游戏
* LC 300：最长递增子序列
* LC 剑指Offer 42. 连续子数组的最大和
* LC 343：整数拆分
* LC 279：完全平方数
* LC 678：最长递增子序列个数
* LC 62：不同路径
* LC 322：零钱兑换
* LC 118：杨辉三角
* LC 583：两个字符串的删除操作
* LC 416：分割等和子集
* LC 509：斐波拉契数
* LC 64：最小路径和
* LC 689：三个无重叠子数组的最大和
* LC 337：打家劫舍III
* LC 1143：最长公共子序列
* LC 剑指Offer 10-II. 青蛙跳台阶问题
* LC 剑指Offer 46. 把数字翻译成字符串
* LC 剑指Offer 13. 机器人的运动范围
* LC 435：无重叠区间
* LC 188：买卖股票的最佳时机IV
* LC 397：整数替换
* LC 91：解码方法
* LC 131：分割回文串
* LC 312：戳气球
* LC 122：买卖股票的最佳时机II
* LC 718：最长重复子数组
* LC 1218：最长定差子序列
* LC 647：回文子串
* LC 740：删除并获得点数
* LC 458：可怜的小猪