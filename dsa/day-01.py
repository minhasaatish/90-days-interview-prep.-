def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Step 1: update minimum price (buy)
        min_price = min(min_price, price)

        # Step 2: calculate profit if sold today
        profit = price - min_price

        # Step 3: update max profit
        max_profit = max(max_profit, profit)

    return max_profit

def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # swap
        s[left], s[right] = s[right], s[left]
        
        left += 1
        right -= 1

def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for c in s:
        if c in mapping:  # closing bracket
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0

def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i
    return [-1, -1]