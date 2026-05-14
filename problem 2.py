def is_palindrome(s):
    #here checking the palindrome in lowercase and uppercase letter to check and return will cleaned
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]