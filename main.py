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
