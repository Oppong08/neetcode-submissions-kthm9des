class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one = 1
        i  = 0
        while one:
            if i < len(digits): 
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
            
        return digits[::-1]
            




















        #logic: reverse the digits list, loop through from left to right while one has not been set to zero(one is set to zero when we reach the end of the list or the current digit is less done 9)
        #if digits[i] == 9, set the current digit to zero, else add 1 and set the remainder to 0
        #after traversing, if we still have the remainder to be 1, add 1 to the list and set the remainder back to 0
        # digits = digits[::-1]
        # one, i = 1, 0#one represents the remainder

        # while one:
        #     if i < len(digits):
        #         if digits[i] == 9:
        #             digits[i] = 0
        #         else:
        #             digits[i] += 1
        #             one = 0
        #     else:
        #         digits.append(1)
        #         one = 0
        #     i += 1
        # return digits[::-1]

         