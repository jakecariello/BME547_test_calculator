foods =  ['apples', 'bananas', 'cherries', 'donuts', 'eggplants']
counts = [      11,        22,         33,       44,          55]

def count_me(name: str):
    assert name in foods, f'{name} not found in foods'
    return counts[foods.index(name)]

if __name__ == '__main__':
    print(count_me('cherries'))


