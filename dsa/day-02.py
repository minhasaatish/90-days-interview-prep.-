def maxProfit(prices):
    """
    Finds the maximum profit from buying and selling a stock once.
    
    Given an array of stock prices, returns the maximum profit that can be achieved
    by buying on one day and selling on a later day. If no profit can be made, returns 0.
    
    Args:
        prices (List[int]): List of stock prices where prices[i] is the price on day i.
    
    Returns:
        int: The maximum profit possible.
    """
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

def twoSum(nums, target):
    """
    Finds two numbers in an array that add up to a target sum.
    
    Given an array of integers and a target sum, returns the indices of the two numbers
    such that they add up to the target. Assumes exactly one solution exists.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[int]: List containing the two indices [i, j] where nums[i] + nums[j] == target.
    """
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i
    return [-1, -1]