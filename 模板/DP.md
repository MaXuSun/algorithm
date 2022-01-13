* 思考问题

我们不关心“具体的过程”，我们只关心“状态”。舍弃冗余的信息（具体的走法），只记录对解决问题有帮助的信息。

* DP的两大特点：能将大问题拆成几个小问题，且满足无后效性、最优子结构性质。
  * 无后效性：
    * 一旦确定f(i,j)，就不用关心“我们如果计算出f(i,j)”-->也就是说我们只记录求解的数值，不记录求解的过程
    * 想要确定f(i,j)，只需要知道f(i-1,j)和f(i,j-1)的值，而至于它们怎么算出来的，对当前或之后的任何子问题都没有影响。
    * “过去不依赖将来，将来不影响过去”
  * 最优子结构
    * f(i,j)的定义就已经蕴含了“最优”
    * 大问题的最优解可以由若干个小问题的最优解推出。(max,min,sum,.....)

* DP第一种基本型（“时间序列”型）
  * 问题定义：给出一个序列（数组/字符串），其中没一个元素可以认为“一天”，并且“**今天**”的状态**只取决昨天**的状态。
    * House Robber
    * House Robber II
    * Best Time to Buy and Sell Stocks
    * Paint Fence
    * Minimum Falling Path Sum II
    * Wiggle Subsequence
    * Best Time to Buy and Sell Stock with Cooldown
    * 下面的例子是变形题
    * Max Consecutive Ones II
    * Maximum Subarray Sum with One Deletion
  * 套路：
    * 定义dp[i][j]:表示第i-th轮的第j种状态(j=1,2,3,...K)，这里i代表轮，j代表第i轮的j个状态
    * 千方百计将dp[i][j]与前一轮的状态dp[i-1][j]产生关系（j=1,2,..,K）
    * 最终的结果是dp[last][j]中的某种aggregation(sum,max,min,...)
    * 进阶：给一个闭环的序列，我们可以考虑首尾的连接处位置，将其拆开讨论，变成两个基本问题
    * trick: 每次画第i-1的状态和第i轮的状态之间的关系图，根据图确定关系。
    * 变形：题目给你一次“行使某种策略的**权利**”，联想到买卖股票，可以将其抽象为“使用”和“不使用”两种状态

* DP第二种基本型（“时间序列”加强版）
  * 问题定义：给出一个序列（数组/字符串），其中每一个元素可以认为“一天”，但“**今天**”的状态和之前的“**某一天**”有关，需要挑选。
    * Longest Increasing Subsequence
      * 状态定义：照抄问题定义dp[i]==>s[1:i]里以s[i]结尾的、最长的递增子序列的长度。
      * 状态转移：寻找最优的前驱状态j，将dp[i]与dp[j]产生联系
    * Number of Longest Increasing Subsequence
    * Largest Divisible Subset
      * 状态定义：照抄问题dp[i]==>s[1:i]里以s[i]结尾的、满足题意得最大子集的元素数目
      * 状态转移：寻找最优的前驱状态，将dp[i]与dp[j]产生联系
    * Filling Bookcase Shelves （这题挺难的，又迷）
      * 拆解题意：将数组S分成若干个subarray，最小化“每个subarray的最大值之和”，输出该值，同时有一个限制条件 width < W
      * 状态定义：照抄dp[i]==>将数组s[1:i]分成若干个subarray，最小化“每个subarray的最大值之和”，保存该值
      * 状态转移：寻找最优的前驱状态j，将dp[i]与dp[j]产生联系：第i本书所在的这一层可能有多高，取决于上一层的最后一本书在哪里
  * 套路：
    * 定义dp[i]：表示第i-th轮的状态，一般这个状态要求和元素i直接相关
    * 千方百计将dp[i]与之前的状态dp[i']产生关系（i=1,2,...,i-1）(比如sum,max,min)
      * dp[i]肯定不能与>i的轮次有任何关系，否则违反了DP的无后效性
    * 最终的结果是dp[i]中的某一个

* DP第3种基本型（双序列型）
  * 问题定义：给出两个序列s和t（数组/字符串），让你对他们搞事情
    * Longest Common Subsequences
      * 状态定义：照抄问题dp[i][j]==>s[1:i]和t[1:j]的length of LCS
      * 状态转移：外面两层大循环遍历i和j；核心从s[i]与t[j]的关系作为突破口，拼命往dp[i-1][j-1]，dp[i-1][j],dp[i][j-1]转移
    * Shortest Common Supersequence
    * Edit distances
      * 状态定义:照抄问题dp[i][j] ==> s[1:i]和t[1:j]的min edit distance
      * 状态的转移：外面两层大循环遍历i和j；核心从s[i]与t[j]的关系作为突破口，拼命往dp[i-1][j-1]，dp[i][j-1]，dp[i-1][j]转移。
    * Interleaving String
    * Distinct Subsequences
    * Minimum Window Subsequence
    * Delete Operation for Two Strings
    * Minimum ASCII Delete Sum for Two Strings
    * Uncrossed Lines
    * Valid Palindrome III
    * Minimum Insertion Steps to Make a String Palindrome
  * 套路：
    * 定义dp[i][j]：表示针对s[1:i]和t[1:i]的子问题的求解
    * 千方百计将dp[i][j]往之前的状态去转移：dp[i-1][j]，dp[i][j-1],dp[i-1][j-1]
    * 最终的结果是dp[m][n]
* DP第4种基本型: 第I类区间型DP
  * 问题定义：给出一个序列，明确要求分割成K个连续区间，要你计算这些区间的最优性质
    * Palindrome Partitioning III
    * Largest Sum of Averages
    * Split Array Largest Sum
    * Minimum Difficulty of a Job Schedule
  * 套路：
    * 状态定义：dp[i][k]表示针对s[1:i]分成k个区间，此时能够得到的最优解
    * 搜寻**最后一个区间的起始位置j**，将dp[i][k]分割成dp[j-1][k-1]和s[j:i]两部分
    * 最终的结果是dp[N][K]
* DP第5种基本型：第II类区间型DP
  * 问题定义：只给出一个序列S(数组/字符串)，求一个针对这个序列的最优解
    * Longest Palindromic Subsequence
    * Burst Ballons
    * Guess Number Higher or Lower II
    * Palindrome Removal
    * Minimum Cost to Merge Stones
  * 适用条件：这个最优解对于序列的index而言，没有“无后效性”。即无法设计dp[i]使得dp[i]仅依赖于dp[j](i<j>),，但是大区间的最优解，可以依赖小区间的最优解。
  * 套路：
    * 定义dp[i][j]:表示针对s[i:j]的子问题的求解
    * 千方百计将大区间的dp[i][j]往小区间的dp[i'][j'']转移
      * 第一层循环是区间大小，第二层循环是起始点
    * 最终的结果是dp[1][N]
* DP第6种基本型：背包入门


