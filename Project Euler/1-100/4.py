
def is_palindrome(num):
    return str(num) == str(num)[::-1]

max = 0
for i in range(999, 800, -1):
    for j in range(999, 800, -1):
        res = i *j
        if is_palindrome(res):
            if max < res:
                max = res


print(max)
