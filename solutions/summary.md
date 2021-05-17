- **0001 - Two Sum**
  ```python
  # 0001 - Two Sum
  #
  # Road:
  # target - elem1 = elem2 as mapping A to B
  #
  # Writing cost time 11min
  
  from typing import List
  
  
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          cache = {}
  
          for i, elem in enumerate(nums):
              indexes = cache.get(target - elem)
              if not indexes:
                  if elem in cache:
                      cache[elem].append(i)
                  else:
                      cache[elem] = [i]
                  continue
              else:
                  j = indexes[0]
                  if i < j:
                      return [i, j]
                  else:
                      return [j, i]
  ```

- **0002 - Add Two Numbers**
  ```python
  # 0002 - Add Two Numbers
  #
  # Road:
  # Skipping
  #
  # Writing cost time 10min
  
  # Definition for singly-linked list.
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
  
  
  class Solution:
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          root = ListNode()
          r = root
  
          remain = 0
          while l1 or l2:
              n1 = 0
              if l1:
                  n1 = l1.val
                  l1 = l1.next
              n2 = 0
              if l2:
                  n2 = l2.val
                  l2 = l2.next
  
              s = n1 + n2 + remain
              val = s % 10
              remain = s // 10
  
              node = ListNode(val)
              r.next = node
              r = node
  
          if remain:
              node = ListNode(remain)
              r.next = node
              r = node
  
          return root.next
  ```

- **0003 - Longest Substring Without Repeating Characters**
  ```python
  # 0003 - Longest Substring Without Repeating Characters
  #
  # Road:
  # if
  # [. . . o . . .]o
  # then
  #         [. . . o]
  # special:
  # a b b a
  #     | |
  #     | |-> to 0
  #     |-> p1 is here, so p1 must be > 0
  #
  # . are each different
  #
  # Writing cost time 70min
  
  
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          if not s:
              return 0
  
          p1 = 0
          p2 = 0
          cache = {}
          max_len = 0
          while p2 < len(s):
              index = cache.get(s[p2])
              cache[s[p2]] = p2
              p2 += 1
              if index is not None:
                  # case: 'abba'
                  p1 = max(index + 1, p1)
              max_len = max(max_len, p2 - p1)
  
          return max_len
  ```

- **0004 - Median of Two Sorted Arrays**
  ```python
  # 0004 - Median of Two Sorted Arrays
  #
  # Road:
  # [ A ] [ B ]
  # [ C ] [ D ]
  # cat(A, C) < cat [B, D]
  #
  # Writing cost time 120min
  
  
  from typing import List
  
  
  class Solution:
      def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
          N = len(nums1) + len(nums2)
          if N == 1:
              return (nums1 + nums2)[0]
  
          # Let nums1 is longer than nums2
          if len(nums1) < len(nums2):
              nums1, nums2 = nums2, nums1
  
          if len(nums2) == 0:
              return (nums1[len(nums1) // 2] + nums1[(len(nums1) - 1) // 2]) / 2
  
          is_even = (len(nums1) + len(nums2)) % 2 == 0
          half = (len(nums1) + len(nums2)) // 2
  
          p1 = half - len(nums2)
          p2 = half - p1
          while p1 < len(nums1) and p2 > 0:
              if nums1[p1] < nums2[p2 - 1]:
                  p1 += 1
                  p2 -= 1
              else:
                  break
  
          if is_even:
              if p1 == 0:
                  return (nums1[0] + nums2[-1]) / 2
              if p1 == len(nums1):
                  return (nums1[-1] + nums2[0]) / 2
              if p2 == 0:
                  return (nums1[p1 - 1] + min(nums1[p1], nums2[0])) / 2
              if p2 == len(nums2):
                  return (max(nums1[p1 - 1], nums2[p2 - 1]) + nums1[p1]) / 2
              else:
                  return (
                      max(nums1[p1 - 1], nums2[p2 - 1]) + min(nums1[p1], nums2[p2])
                  ) / 2
          else:
              if p1 == 0:
                  return nums1[0]
              if p2 == len(nums2):
                  return nums1[p1]
              else:
                  return min(nums1[p1], nums2[p2])
  
  
  a = Solution()
  
  l1 = [3]
  l2 = [-1, -2]
  s = a.findMedianSortedArrays(l1, l2)
  print(s)
  ```

- **0005 - Longest Palindromic Substring**
  ```python
  # 0005 - Longest Palindromic Substring
  #
  # Road:
  # 1. search  <---(i)--->
  # 2. search  <---(i)(i+1)--->
  #
  # Writing cost time 23min
  
  
  class Solution:
      def longestPalindrome(self, s: str) -> str:
          maxs = ""
          for i in range(len(s)):
              pal = self.findPal(s, i, i, min(i + 1, len(s) - i))
              print(i, pal)
              if len(pal) > len(maxs):
                  maxs = pal
  
              if i != len(s) - 1:
                  pal = self.findPal(s, i, i + 1, min(i + 1, len(s) - i - 1))
                  print(i, pal)
                  if len(pal) > len(maxs):
                      maxs = pal
  
          return maxs
  
      def findPal(self, s, left, right, length):
          for _ in range(length):
              if s[left] != s[right]:
                  break
  
              left -= 1
              right += 1
          return s[left + 1 : right]
  
  
  a = Solution()
  a.longestPalindrome("babad")
  ```

- **0006 - ZigZag Conversion**
  ```python
  # 0006 - ZigZag Conversion
  #
  # Road:
  # indexes:
  # 0     0
  # 1  1     1
  # 2           2
  #
  # Writing cost time 12min
  
  
  class Solution:
      def convert(self, s: str, numRows: int) -> str:
          idx = list(range(numRows)) + list(range(numRows - 2, 0, -1))
  
          rs = [""] * numRows
  
          for i, c in enumerate(s):
              j = idx[i % len(idx)]
              rs[j] += c
  
          return "".join(rs)
  ```

- **0007 - Reverse Integer**
  ```python
  # 0007 - Reverse Integer
  #
  # Road:
  # see code
  #
  # Writing cost time 12min
  
  
  class Solution:
      def reverse(self, x: int) -> int:
          if x == 0:
              return 0
  
          is_neg = -x > 0
          x = abs(x)
  
          rev = 0
          while x != 0:
              remain = x % 10
              rev = rev * 10 + remain
              x = x // 10
  
          if is_neg:
              rev = -rev
  
          if -(1 << 31) <= rev <= ((1 << 31) - 1):
              return rev
          else:
              return 0
  ```

- **0008 - String to Integer (atoi)**
  ```python
  # 0008 - String to Integer (atoi)
  #
  # Road:
  # see code
  #
  # Writing cost time 17min
  
  
  class Solution:
      def myAtoi(self, s: str) -> int:
          num = 0
          is_neg = False
          started = False
          for c in s:
              if not started:
                  if c == " " and not num:
                      continue
                  if c == "0" and not num:
                      started = True
                      continue
                  if c == "-" and not num:
                      is_neg = not is_neg
                      started = True
                      continue
                  if c == "+" and not num:
                      started = True
                      continue
  
              started = True
              uni = ord(c) - ord("0")
              if 0 <= uni < 10:
                  num = num * 10 + uni
              else:
                  break
  
          if not num:
              return 0
  
          if is_neg:
              num = -num
  
          if num < -(1 << 31):
              return -(1 << 31)
          if num > (1 << 31) - 1:
              return (1 << 31) - 1
          return num
  ```

- **0009 - Palindrome Number**
  ```python
  # 0009 - Palindrome Number
  #
  # Road:
  # num == ? rev
  #
  # Writing cost time 16min
  
  
  class Solution:
      def isPalindrome(self, x: int) -> bool:
          if x == 0:
              return True
          if -x > 0:
              return False
  
          num = x
  
          rev = 0
          while x != 0:
              remain = x % 10
              rev = rev * 10 + remain
              x = x // 10
  
          return num == rev
  ```

- **0010 - Regular Expression Matching**
  ```python
  # 0010 - Regular Expression Matching
  #
  # Road:
  # DP
  # 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
  # 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
  # 3, If p.charAt(j) == '*':
  #    here are two sub conditions:
  #                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
  #                2   if p.charAt(j-1) == s.charAt(i) or p.charAt(j-1) == '.':
  #                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
  #                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
  #                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
  #
  # Writing cost time 127min
  
  
  class Solution:
      def isMatch(self, s: str, p: str) -> bool:
          dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
          dp[0][0] = True
  
          for j in range(len(p)):
              if p[j] == "*" and dp[0][j - 1]:
                  dp[0][j + 1] = True
  
          for i in range(1, len(s) + 1):
              for j in range(1, len(p) + 1):
                  if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                      dp[i][j] = dp[i - 1][j - 1]
  
                  if p[j - 1] == "*":
                      if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                          dp[i][j] = (
                              dp[i][j - 2]  # a* match empty
                              or dp[i][j - 1]  # a* match one a
                              or dp[i - 1][j]  # a* match multi a
                          )
                      else:
                          dp[i][j] = dp[i][j - 2]  # a* match empty
  
          return dp[-1][-1]
  ```

