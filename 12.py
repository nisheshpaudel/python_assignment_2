def is_palindrome(text):
    left = 0
    right = len(text)-1
    while True:
        if right < left:
            return True
        if text[left].lower() == text[right].lower():
            left += 1
            right -= 1
        else:
            return False


print("radar", "is a palindrome", is_palindrome("radar"))
print("redivider", "is a palindrome", is_palindrome("redivider"))
print("revive", "is a palindrome", is_palindrome("revive"))
print("kayak", "is a palindrome", is_palindrome("kayak"))