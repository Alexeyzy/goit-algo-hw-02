from collections import deque

def palindrome(d):
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True

word = "       Level        "
word = word.replace(" ", "")
word = word.upper()

d = deque()
d.extend([x for x in word])

print(palindrome(d))  


