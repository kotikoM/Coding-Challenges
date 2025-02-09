from sympy import symbols, solve


class HailStone:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz


hailStones = [HailStone(*map(int, line.replace(' @', ',').split(', '))) for line in open('input')]
# looking for sx, sy, sz, sdx, sdy, sdz such that at some points t we intersect all hailstones
# 6 unknowns
# governing equations that must be met
# t = (x - sx) / (sdx - dx)
# t = (y - sy) / (sdy - dy)
# t = (z - sz) / (sdz - dz)

equations = []
sx, sy, sz, sdx, sdy, sdz, t = symbols('sx sy sz sdx sdy sdz t')
for h in hailStones[3:]:
    equations.append((sx - h.x) * (h.dy - sdy) - (sy - h.y) * (h.dx - sdx))
    equations.append((sy - h.y) * (h.dz - sdz) - (sz - h.z) * (h.dy - sdy))

solution = solve(equations)
print(sum(list(solution[0].values())[3:]))
