class Player:
    def __init__(self, name):
        self.name = name
        self.number_map = {}
        self.row_map = {}
        self.col_map = {}

    def add_numbers(self, number, row, col):
        self.number_map[number] = (row, col)

    def mark_number(self, number):
        if number in self.number_map:
            row, col = self.number_map[number]
            if row not in self.row_map:
                self.row_map[row] = set()
            self.row_map[row].add(number)
            if col not in self.col_map:
                self.col_map[col] = set()
            self.col_map[col].add(number)

    def is_winner(self):
        for row in self.row_map:
            if len(self.row_map[row]) == 5:
                return True
        for col in self.col_map:
            if len(self.col_map[col]) == 5:
                return True
        return False


lines = open('input').read().split('\n\n')
numbers = map(int, lines[0].split(','))
players = []
for i in range(1, len(lines)):
    p = Player(i)
    for j, line in enumerate(lines[i].split('\n')):
        for k, number in enumerate(line.split()):
            p.add_numbers(int(number), j, k)
    players.append(p)

for n in numbers:
    winners = []
    for p in players:
        p.mark_number(n)
        if p.is_winner():
            winners.append(p)
    for winner in winners:
        if len(players) == 1:
            marked = set().union(*winner.row_map.values(), *winner.col_map.values())
            unmarked = set(winner.number_map.keys()) - marked
            print(sum(unmarked) * n)
            exit()
        players.remove(winner)
