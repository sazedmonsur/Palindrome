def is_plaindrome(str):
    modified_string = "".join(e for e in str if e.isalpha()).lower()
    list_str = list(modified_string)
    left = 0
    right = len(modified_string) - 1

    if modified_string =="":
        return False

    while left < right:
        if list_str[left] != list_str[right]:
            return False #if left pointer is not equal right pointer return false
        else:            #else letters are equal, increment the left pointer and decrement the right pointer
            left += 1
            right -= 1
    return True
