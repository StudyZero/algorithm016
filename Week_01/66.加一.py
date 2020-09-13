#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIndex = len(digits) - 1
        for i in range(lastIndex, -1, -1):
            print(i)
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
            else:
                digits[i] = digits[i] + 1
                break
        return digits
# @lc code=end

