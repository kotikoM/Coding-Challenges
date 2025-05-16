class Player:
    def __init__(self):
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
    player = Player()
    for j, line in enumerate(lines[i].split('\n')):
        for k, number in enumerate(line.split()):
            player.add_numbers(int(number), j, k)
    players.append(player)

for n in numbers:
    for p in players:
        p.mark_number(n)
        if p.is_winner():
            marked = set().union(*p.row_map.values(), *p.col_map.values())
            unmarked = set(p.number_map.keys()) - set(marked)
            print(sum(unmarked) * n)
            exit()
