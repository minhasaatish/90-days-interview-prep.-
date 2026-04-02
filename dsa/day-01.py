def reverseString(s):
    """
    Reverses a string in-place.
    
    Modifies the input list of characters s such that it is reversed.
    Does not return anything, modifies s in-place.
    
    Args:
        s (List[str]): List of characters to be reversed.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # swap
        s[left], s[right] = s[right], s[left]
        
        left += 1
        right -= 1

def isValid(s):
    """
    Checks if a string of parentheses is valid.
    
    A string is valid if open brackets are closed by the same type of brackets
    and in the correct order. Uses a stack to keep track of opening brackets.
    
    Args:
        s (str): String containing only parentheses characters.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    """
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