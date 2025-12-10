game_active = False
hand_player = 0
hand_cpu = 0

def on_pin_pressed_p0():
    global hand_player
    if game_active and hand_player == 0:
        hand_player = 1
        player_turn()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def show_hand(hand: number):
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        # piedra
        basic.show_icon(IconNames.SQUARE)
    else:
        # papel
        basic.show_icon(IconNames.SCISSORS)

def on_gesture_shake():
    global game_active, hand_player, hand_cpu
    if not (game_active):
        game_active = True
        hand_player = 0
        hand_cpu = 0
        basic.show_string("START")
        basic.show_icon(IconNames.HAPPY)
        basic.pause(500)
        basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def player_turn():
    # mostrar la opt del player
    basic.show_string("YOU")
    show_hand(hand_player)
    basic.pause(1000)
    # turno de la CPU
    cpu_turn()

def on_pin_pressed_p2():
    global hand_player
    if game_active and hand_player == 0:
        hand_player = 3
        player_turn()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    global hand_player
    if game_active and hand_player == 0:
        hand_player = 2
        player_turn()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def show_result():
    global game_active
    # empate
    if hand_player == hand_cpu:
        basic.show_icon(IconNames.MEH)
        basic.pause(1000)
        basic.show_string("EMPATE")
    elif hand_player == 1 and hand_cpu == 3 or hand_player == 2 and hand_cpu == 1 or hand_player == 3 and hand_cpu == 2:
        # player gana
        basic.show_icon(IconNames.HAPPY)
        basic.pause(1000)
        basic.show_string("WIN")
    else:
        # CPU gana
        basic.show_icon(IconNames.SAD)
        basic.pause(1000)
        basic.show_string("LOSE")
    # end juego
    game_active = False
    basic.pause(1000)
    basic.clear_screen()
    basic.show_string("END")
def cpu_turn():
    global hand_cpu
    # CPU genera opt random
    hand_cpu = randint(1, 3)
    basic.show_string("CPU")
    show_hand(hand_cpu)
    basic.pause(1000)
    # mostrar resultado
    show_result()