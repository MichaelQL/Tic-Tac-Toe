# write your code here
def output_print(printouts):
    print("---------")
    for i in range(0, len(printouts), 3):
        print(f"| {printouts[i]} {printouts[i + 1]} {printouts[i + 2]} |")
    print("---------")


def user_input():
    while True:
        # judge weather input is correct
        while True:
            try:
                x_position, y_position = input().split()
                x_position = int(x_position)
                y_position = int(y_position)
                break
            except ValueError:
                print("You should enter numbers!")
        if x_position in range(1, 4) and y_position in range(1, 4):
            if status[(x_position - 1) * 3 + y_position - 1] == " ":
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    return x_position, y_position


def judge():
    win_tuple = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    draw_flag = True
    x_wins = 0
    o_wins = 0
    end_game_flag = False
    for i in win_tuple:
        test_set = set()
        for j in i:
            test_set.add(status[j])
        if len(test_set) == 1:
            draw_flag = False
            if "X" in test_set:
                x_wins += 1
            elif "O" in test_set:
                o_wins += 1
            else:
                print("Game not finished")
    if x_wins and not o_wins:
        print("X wins")
        end_game_flag = True
    elif o_wins and not x_wins:
        print("O wins")
        end_game_flag = True
    if draw_flag and status.count(" ") == 0:
        print("Draw")
        end_game_flag = True
    return end_game_flag


status = list(" " * 9)
output_print(status)
flag_XO = True
xo = ["O", "X"]
while True:
    x, y = user_input()
    status[(x - 1) * 3 + y - 1] = xo[flag_XO]
    flag_XO = not flag_XO
    output_print(status)
    if judge():
        break