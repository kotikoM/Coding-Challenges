class Node:
    def __init__(self, n):
        self.num = n
        self.prev = None
        self.next = None


nums = [Node(int(x)) for x in open('input')]

for i in range(len(nums)):
    nums[i].next = nums[(i + 1) % len(nums)]
    nums[i].prev = nums[(i - 1) % len(nums)]

mod = len(nums) - 1

for current in nums:
    if current.num == 0:
        target = current
        continue

    temp = current
    if current.num > 0:
        for _ in range(current.num % mod):
            temp = temp.next
        if current == temp:
            continue
        current.next.prev = current.prev
        current.prev.next = current.next
        temp.next.prev = current
        current.next = temp.next
        temp.next = current
        current.prev = temp

    else:
        for _ in range(-current.num % mod):
            temp = temp.prev
        if current == temp:
            continue
        current.prev.next = current.next
        current.next.prev = current.prev
        temp.prev.next = current
        current.prev = temp.prev
        temp.prev = current
        current.next = temp

total = 0
for _ in range(3):
    for _ in range(1000):
        target = target.next
    total += target.num

print(total)
