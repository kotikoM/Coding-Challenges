ranges, ingredients = open('input').read().split('\n\n')
ranges = [tuple(map(int, t.split('-'))) for t in ranges.split('\n')]
ingredients = list(map(int, ingredients.split('\n')))

fresh = 0
for i in ingredients:
    for l, r in ranges:
        if l <= i <= r:
            fresh += 1
            break
print(fresh)
