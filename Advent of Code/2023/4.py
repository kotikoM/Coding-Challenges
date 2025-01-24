

cards = open("input").read().splitlines()
lines = [line.replace("  ", " ")[8:] for line in cards]

winning = []
numbers = []

for line in lines:
    win, num = line.split(" | ")
    winning.append(win.split(" "))
    numbers.append(num.split(" "))

card_wins = {}
for i, nums in enumerate(numbers):

    wins = 0
    for number in nums:
        if number in winning[i]:
            wins += 1

    card_wins[i + 1] = wins


won = []
for i in range(len(cards)):
    won.append(i + 1)

for w in won:
    wins = card_wins[w]

    for i in range(wins):
        won.append(w + i + 1)

print(winning)
print(numbers)
print(lines)
print(card_wins)
print(len(won))
