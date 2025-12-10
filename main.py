game_active = False
hand_player = 0
hand_cpu = 0

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

def show_hand(hand: number):
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        # piedra
        basic.show_icon(IconNames.SQUARE)
    else:
        # papel
        basic.show_icon(IconNames.SCISSORS)

def cpu_turn():
    global hand_cpu
    # CPU genera opt random
    hand_cpu = randint(1, 3)
    basic.show_string("CPU")
    show_hand(hand_cpu)
    basic.pause(1000)
    # mostrar resultado
    show_result()

def player_turn():
    # mostrar la opt del player
    basic.show_string("YOU")
    show_hand(hand_player)
    basic.pause(1000)
    # turno de la CPU
    cpu_turn()

def on_pin_pressed_p0():
    global hand_player
    if game_active and hand_player == 0:
        hand_player = 1
        player_turn()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

