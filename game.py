print("Игра крестики-нолики")
print("Введите координаты")

table = [[" "] * 3 for i in range(3) ]
def game():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {table[i][0]} {table[i][1]} {table[i][2]}")

game()

def ask():
    while True:
        x, y = map(int, input("Введите координаты: ").split())
        if 0 <= x <= 2 and 0 <= y <= 2 :
            if table[x][y] == " ":
                return x, y
            else:
                print("Выберите другую клетку")

ask()

def winner():
    winner_options = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for options in winner:
        a = options[0]
        b = options[1]
        c = options[2]

        if table[a[0]][a[1]] == table[b[0]][b[1]] == table[c[0]][c[1]] != "":
            print(f"Выиграл {table[a[0]][a[1]]}!")
            return True
    return False


