import turtle
import random
import time
#board size:
nn , mm = 800, 800
mx_pl, mx_st = 5, 5
stone = []
location = []
gru = []
rem = [2, 3]
radius = 20

win = ""
player1 = ""
player2 = ""
player1_sel = ""
player2_sel = ""
player1_loc = []
player2_loc = []
player1_turn_loc = []
player2_turn_loc = []
versus = ""

def set_position(xxx, yyy) :
    turtle.up()
    turtle.setpos(xxx, yyy)
    turtle.down()

def erase_stone(pl, st) :
    global stone, location
    for i in range(1, st + 1) :
        x, y = location[pl][-1]
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.fillcolor("green")
        turtle.color("green")
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        location[pl].pop()
        stone[pl] -= 1

def alternate_area() :
    global player1, player2, player1_loc, player2_loc, player1_turn_loc, player2_turn_loc
    turtle.clear()
    turtle.width(5)
    set_position(0, 250)
    turtle.color("orange")
    turtle.write(versus, align = "center", font = ("arial", 30, "bold"))

    turtle.width(3)
    turtle.color("black")

    set_position(player1_loc[0], player1_loc[1])
    turtle.write(player1, align = "left", font = ("arial", 25, "bold"))
    set_position(player1_turn_loc[0], player1_turn_loc[1])
    turtle.write(player1_sel, font = ("arial", 20, "bold"))

    set_position(player2_loc[0], player2_loc[1])
    turtle.write(player2, align = "left", font = ("arial", 25, "bold"))
    set_position(player2_turn_loc[0], player2_turn_loc[1])
    turtle.write(player2_sel, font = ("arial", 20, "bold"))

def board_drawing() :
    global stone, location, radius, mx_pl, mx_st, nn, mm

    col = ["aliceblue","black","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet"]
    col_len = len(col)
    turtle.screensize(canvwidth = 800, canvheight = 800, bg = 'green')
    turtle.width(3)
    turtle.speed(0)
    ind = 0
    for i in range(1, mx_pl + 1) :
        ind = ind % col_len
        turtle.color(col[ind])
        turtle.width(10)
        x, y = location[i][1]
        turtle.up()
        turtle.setpos(x - 24, y - 15)
        turtle.down()
        turtle.forward(50)
        turtle.width(3)
        ch = chr(i + 65 - 1)
        turtle.up()
        turtle.setpos(x, y - 70)
        turtle.down()
        turtle.write(ch, align = 'center', font = ("arial", 30, "bold"))

        for j in range(1, stone[i] + 1) :
            x, y = location[i][j]

            turtle.up()
            turtle.setpos(x, y)
            turtle.down()
            turtle.fillcolor(col[ind])
            turtle.begin_fill()
            turtle.circle(radius)
            turtle.end_fill()
        ind = ind + 1

def take_stone() :
    global stone
    
    stone.clear()
    stone.append(0)
    for i in range(1, mx_pl + 1) :
        rn = random.randint(2, mx_st)
        stone.append(rn)

def take_location() :
    global location

    location.clear()
    a = int(-(mx_pl / 2) * 70)
    b = -200   
    location.append([(0, 0)])
    for i in range(1, mx_pl + 1) :
        one = [(0, 0)]
        for j in range(1, stone[i] + 1) :
            one.append((a, b + (j - 1) * 56))
        location.append(one)
        a = a + 70

def possible() :
    global stone
    for i in range(1, mx_pl + 1) :
        if stone[i] >= 2 :
            return True
    return False

def clear_player1() :
    global player1_sel, player1_turn_loc

    set_position(player1_turn_loc[0], player1_turn_loc[1])
    turtle.color("green")
    turtle.write(player1_sel, font = ("arial", 20, "bold"))
    turtle.right(90)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.left(90)

def clear_player2() :
    global player2_sel, player2_turn_loc

    set_position(player2_turn_loc[0], player2_turn_loc[1])
    turtle.color("green")
    turtle.write(player2_sel, font = ("arial", 20, "bold"))
    turtle.right(90)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.left(90)

def write_player1() :
    global player1_sel, player1_turn_loc

    set_position(player1_turn_loc[0], player1_turn_loc[1])
    turtle.color("black")
    turtle.write(player1_sel, font = ("arial", 20, "bold"))

def write_player2() :
    global player2_sel, player2_tuen_loc

    set_position(player2_turn_loc[0], player2_turn_loc[1])
    turtle.color("black")
    turtle.write(player2_sel, font = ("arial", 20, "bold"))

def reset() :
    turtle.listen()
    screen.onkeypress(main_menu, "Return")

def end_game() :
    global win

    set_position(0, 0)
    turtle.color("yellow")
    turtle.width(7)
    champion = win
    champion = champion[:-1]
    champion = champion + " WinS!"
    turtle.write(champion, align = "center", font = ("arial", 70, "bold"))
    set_position(0, -50)
    turtle.write("(press 'enter' to continue)", align = "center", font = ("arial", 20, ""))
    reset()

def choose_player2_cnt(character) :
    global player1_sel, player2_sel, stone
    if len(player2_sel) >= 2 :
        clear_player2()
    player2_sel = player2_sel + character
    write_player2()
    if len(player2_sel) == 1 and player2_sel[0] >= '0' and player2_sel[0] <= '9' :
        clear_player2()
        player2_sel = ""
        return
    elif len(player2_sel) == 2 and player2_sel[1] != '2' and player2_sel[1] != '3' :
        clear_player2()
        player2_sel = ""
        return
    
    elif len(player2_sel) == 2 :
        pl = ord(player2_sel[0]) - 64
        st = ord(player2_sel[1]) - 48
        if stone[pl] >= st :
            time.sleep(1)
            erase_stone(pl, st)
            turn_with_player1()
        else :
            clear_player2()
            player2_sel = ""

def choose_player2() :
    turtle.listen()
    for i in range(1, mx_pl + 1) :
        ch = chr(i + 64)
        screen.onkeypress(lambda c1 = ch : choose_player2_cnt(c1), ch)
    for i in range(1, 4) :
        ch = chr(i + 48)
        screen.onkeypress(lambda c1 = ch : choose_player2_cnt(c1), ch)
    screen.onkeypress(main_menu, 'Return')
    screen.onkeypress(pick_opponents, 'Down')
    screen.onkeypress(pick_opponents, 'Left')

def turn_with_player2() :
    global win, player1, player2, player1_sel, player2_sel
    if possible() == False :
        win = player1 
        end_game()
    clear_player2()
    player2_sel = ""
    choose_player2()

def choose_player1_cnt(character) :
    global player1_sel, stone

    #clear_player1()
    player1_sel = player1_sel + character
    write_player1()
    if len(player1_sel) == 1 and player1_sel[0] >= '0' and player1_sel[0] <= '9' :
        clear_player1()
        player1_sel = ""
        return
    elif len(player1_sel) == 2 and player1_sel[1] != '2' and player1_sel[1] != '3' :
        clear_player1()
        player1_sel = ""
        return
    
    elif len(player1_sel) == 2 :
        pl = ord(player1_sel[0]) - 64
        st = ord(player1_sel[1]) - 48
        if stone[pl] >= st :
            time.sleep(1)
            erase_stone(pl, st)
            turn_with_player2()
        else :
            clear_player1()
            player1_sel = ""

def choose_player1() :
    turtle.listen()
    for i in range(1, mx_pl + 1) :
        ch = chr(i + 64)
        screen.onkeypress(lambda c1 = ch : choose_player1_cnt(c1), ch)
    for i in range(1, 4) :
        ch = chr(i + 48)
        screen.onkeypress(lambda c1 = ch : choose_player1_cnt(c1), ch)
    screen.onkeypress(main_menu, 'Return')
    screen.onkeypress(pick_opponents, 'Down')
    screen.onkeypress(pick_opponents, 'Left')

def turn_with_player1() :
    global win, player1, player2, player1_sel, player2_sel
    if possible() == False :
        win = player2 
        end_game()
    clear_player1()
    player1_sel = ""
    choose_player1()
    
def game_with_friends() :
    global player1, player2, player1_loc, player2_loc, player1_turn_loc, player2_turn_loc, player1_sel, player2_sel, versus
    turtle.clear()
    take_stone()
    take_location()
    
    player1 = "Player1:"
    player2 = "Player2:"
    player1_sel = ""
    player2_sel = "GO"
    player1_loc = [-600, 200]
    player2_loc = [400, 200]
    
    player1_turn_loc = [-460, 200]
    player2_turn_loc = [540, 200]
    versus = "PLAYER-1  VS  PLAYER-2"
    alternate_area()
    board_drawing()
    turn_with_player1()

def turn_with_computer() :
    global player1, player2, player1_sel, player2_sel, win, stone, location, gru

    if possible() == False :
        win = player1
        end_game()
    clear_player2()
    player2_sel = ""

    xr = [0]
    for i in range(1, mx_pl + 1) :
        tmp = xr[i - 1] ^ gru[stone[i]]
        xr.append(tmp)
    mn, pl, st = [100, 100, 100] #100 for any max value 
    for x in rem :
        for i in range(1, mx_pl + 1) :
            if stone[i] < x :
                continue
            else :
                tmp = xr[mx_pl] ^ gru[stone[i]] ^ gru[stone[i] - x]
                if tmp < mn :
                    mn = tmp
                    pl = i 
                    st = x
    player2_sel = chr(pl + 64) + chr(st + 48)
    time.sleep(2)
    write_player2()
    time.sleep(2)
    erase_stone(pl, st)
    turn_with_player()

def choose_player_cnt(character) :
    global player1_sel, stone

    #clear_player1()
    player1_sel = player1_sel + character
    write_player1()
    if len(player1_sel) == 1 and player1_sel[0] >= '0' and player1_sel[0] <= '9' :
        clear_player1()
        player1_sel = ""
        return
    elif len(player1_sel) == 2 and player1_sel[1] != '2' and player1_sel[1] != '3' :
        clear_player1()
        player1_sel = ""
        return
    
    elif len(player1_sel) == 2 :
        pl = ord(player1_sel[0]) - 64
        st = ord(player1_sel[1]) - 48
        if stone[pl] >= st :
            time.sleep(1)
            erase_stone(pl, st)
            turn_with_computer()
        else :
            clear_player1()
            player1_sel = ""

def choose_player() :
    turtle.listen()
    for i in range(1, mx_pl + 1) :
        ch = chr(i + 64)
        screen.onkeypress(lambda c1 = ch : choose_player_cnt(c1), ch)
    for i in range(1, 4) :
        ch = chr(i + 48)
        screen.onkeypress(lambda c1 = ch : choose_player_cnt(c1), ch)
    screen.onkeypress(main_menu, 'Return')
    screen.onkeypress(pick_opponents, 'Down')
    screen.onkeypress(pick_opponents, 'Left')

def turn_with_player() :
    global win, player1, player2, player1_sel, player2_sel
    if possible() == False :
        win = player2 
        end_game()
    clear_player1()
    player1_sel = ""
    choose_player()
    
def game_with_computers() :
    global player1, player2, player1_loc, player2_loc, player1_turn_loc, player2_turn_loc, player1_sel, player2_sel, versus
    turtle.clear()
    take_stone()
    take_location()
    player1 = "Player:"
    player2 = "Computer:"
    player1_sel = ""
    player2_sel = "GO"
    player1_loc = [-600, 200]
    player2_loc = [400, 200]
    
    player1_turn_loc = [-480, 200]
    player2_turn_loc = [580, 200]
    versus = "PLAYER VS COMPUTER"
    alternate_area()
    board_drawing()
    turn_with_player()

def pick_opponents_option() :
    screen.listen()
    turtle.onkeypress(game_with_computers, '1')
    turtle.onkeypress(game_with_friends, '2')
    turtle.onkeypress(main_menu, 'Return')
    screen.onkeypress(difficulty, 'Down')
    screen.onkeypress(difficulty, 'Left')

def pick_opponents() :
    global nn, mm

    turtle.clear()
    turtle.width(5)
    xx, yy = 0, mm / 4
    set_position(xx, yy)
    turtle.color("yellow")
    turtle.write("CHOOSE OPPONENTS", align = "center", font = ("arial", 50, "bold"))

    turtle.width(3)
    turtle.color("black")
    yy -= 100
    xx = -1 * mm / 2 + 100
    set_position(xx, yy)
    turtle.write("1.Play with computers", align = "left", font = ("arial", 40, "bold"))

    yy -= 70
    set_position(xx, yy)
    turtle.write("2.Play with your friends", align = "left", font = ("arial", 40,"bold"))

    pick_opponents_option()

def game_overview() :
    global nn, mm

    turtle.clear()
    xx, yy = 0, mm / 4 + 50
    set_position(xx, yy)
    turtle.color("orange")
    turtle.write("GAME OVERVIEW", align = "center", font = ("arial", 40, "bold"))

    turtle.width(3)
    turtle.color("black")
    xx = -1 * mm / 3 * 2
    yy -= 80
    set_position(xx, yy)
    turtle.write("(I)There are some piles of stones.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(II)Each pile contains some stones.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(III)The game includes three categories(beginner, intermediate & advance)", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(IV)The game is played by two players who alternate turns.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(V)A player must remove exactly 2 or 3 stones from a single pile.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(VI)A player can only remove stones from one pile per turn.", align = "left", font = ("arial", 25, "bold"))
    
    yy -= 50
    set_position(xx, yy)
    turtle.write("(VII)The player who takes the last stone wins the game.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(VIII)The player who can't make a valid move lose the game.", align = "left", font = ("arial", 25, "bold"))

    yy -= 50
    set_position(xx, yy)
    turtle.write("(IX)The game ends when current player can't make a move.", align = "left", font = ("arial", 25, "bold"))

def beginner() :
    global mx_pl, mx_st
    mx_pl, mx_st = 4, 4
    pick_opponents()

def intermediate() :
    global mx_pl, mx_st
    mx_pl, mx_st = 6, 5
    pick_opponents()

def advance() :
    global mx_pl, mx_st
    mx_pl, mx_st = 10, 5
    pick_opponents()

def difficulty_option() :
    turtle.listen()
    screen.onkeypress(beginner, '1')
    screen.onkeypress(intermediate, '2')
    screen.onkeypress(advance, '3')
    screen.onkeypress(main_menu, 'Return')
    screen.onkeypress(main_menu, "Down")
    screen.onkeypress(main_menu, "Left")

def difficulty() :
    global nn
    turtle.clear()
    xx, yy = 0, nn / 4
    set_position(xx, yy)
    turtle.width(5)
    turtle.color("yellow")
    turtle.write("DIFFICULTY", align = "center", font = ("arial", 50, "bold"))

    xx -= 150
    yy -= 100
    set_position(xx, yy)
    turtle.color("black")
    turtle.write("1.Beginner", align = "left", font = ("arial", 40, "bold"))

    yy -= 70
    set_position(xx, yy)
    turtle.write("2.Intermediate", align = "left", font = ("arial", 40, "bold"))

    yy -= 70
    set_position(xx, yy)
    turtle.write("3.Advance", align = "left", font = ("arial", 40, "bold"))
    difficulty_option()

def main_menu_option() :
    screen.listen()
    turtle.onkeypress(difficulty, '1')
    turtle.onkeypress(game_overview, '2')
    turtle.onkeypress(main_menu, 'Return')

def main_menu() :
    global nn, mm

    turtle.clear()
    turtle.setheading(0)
    xx , yy = 0 , mm / 4
    set_position(xx, yy)
    turtle.width(6)
    turtle.color("orange")
    turtle.write("STONE REMOVAL GAME", align = "center", font = ("arial", 50, "bold"))

    xx = -1 * nn / 4
    yy -= 100
    set_position(xx, yy)
    turtle.width(3)
    turtle.color("black")
    turtle.write("1.New Game", align = "left", font = ("arial", 40, "bold"))

    yy -= 70
    set_position(xx, yy)
    turtle.write("2.Game Overview", align = "left", font = ("arial", 40, "bold"))

    main_menu_option()

def calculate_grundy() :
    gru.append(0)
    for i in range(1, mx_st + 1) :
        poss = []
        for x in rem :
            if x > i :
                break
            else :
                poss.append(gru[i - x])
        inc = 0
        while True:
            flag = 0
            for x in poss :
                if x == inc :
                    flag = 1
                    break
            if flag == 0 or len(poss) == 0:
                break
            else :
                inc = inc + 1
        gru.append(inc)

#main function()
screen = turtle.Screen()
turtle.screensize(canvwidth = nn, canvheight = mm, bg = "green")
turtle.hideturtle()
turtle.width(3)
turtle.color("black")
turtle.speed(0)

calculate_grundy()
main_menu()

turtle.done()
