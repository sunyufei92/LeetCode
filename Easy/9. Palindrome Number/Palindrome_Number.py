"""
Solution 1: Convert the integer to a string
This is the easiest approach where we convert the integer to a string and then check if it reads the same forwards and backwards.

Time complexity: O(n), where n is the number of digits in the integer.
Space complexity: O(n) due to the string conversion.
"""
def isPalindrome(x: int) -> bool:
    # Convert the integer to a string
    s = str(x)
    
    # Check if the string is equal to its reverse
    return s == s[::-1]


"""
Solution 2: Without converting to a string (Mathematical Approach)
This solution doesn't convert the integer to a string but instead reconstructs the reversed number mathematically.

Time complexity: O(log(x)), because we divide the number by 10 in each iteration.
Space complexity: O(1).
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solution logic here
        # Example: Let's use the mathematical approach
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x // 10

        return original == reversed_num


"""
Solution 3: Compare Half of the Number (Optimized Mathematical Approach)
Instead of reversing the entire number, we can reverse just the second half of the number and compare it with the first half. 
This approach avoids potential overflow issues with large numbers.

Time complexity: O(log(x)), because we're reversing half the digits.
Space complexity: O(1).
"""
def isPalindrome(x: int) -> bool:
    # Special cases where the number cannot be a palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    # Reverse the second half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10
    
    # Check if the first half of the number is equal to the reversed second half
    return x == reversed_half or x == reversed_half // 10


"""
Solution 4: Recursive Approach
We can also implement this solution recursively by comparing the first and last digits, removing them, and repeating the process for the inner digits.

Time complexity: O(log(x)), due to the recursive nature of checking digits.
Space complexity: O(log(x)), due to recursive call stack.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Helper function to compare digits
        def helper(x, div):
            if x == 0:
                return True
            # Compare the first and last digits
            first_digit = x // div
            last_digit = x % 10
            if first_digit != last_digit:
                return False
            # Remove the first and last digits and continue recursively
            return helper((x % div) // 10, div // 100)
        
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        
        # Find the divisor to extract the first digit
        div = 1
        while x // div >= 10:
            div *= 10
        
        return helper(x, div)
