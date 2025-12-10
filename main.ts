let game_active = false
let hand_player = 0
let hand_cpu = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    if (!game_active) {
        game_active = true
        hand_player = 0
        hand_cpu = 0
        basic.showString("START")
        basic.showIcon(IconNames.Happy)
        basic.pause(500)
        basic.clearScreen()
    }
    
})
function show_hand(hand: number) {
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        //  piedra
        basic.showIcon(IconNames.Square)
    } else {
        //  papel
        basic.showIcon(IconNames.Scissors)
    }
    
}

function cpu_turn() {
    
    //  CPU genera opt random
    hand_cpu = randint(1, 3)
    basic.showString("CPU")
    show_hand(hand_cpu)
    basic.pause(1000)
    //  mostrar resultado
    show_result()
}

function player_turn() {
    //  mostrar la opt del player
    basic.showString("YOU")
    show_hand(hand_player)
    basic.pause(1000)
    //  turno de la CPU
    cpu_turn()
}

input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    if (game_active && hand_player == 0) {
        hand_player = 1
        player_turn()
    }
    
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    if (game_active && hand_player == 0) {
        hand_player = 2
        player_turn()
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    if (game_active && hand_player == 0) {
        hand_player = 3
        player_turn()
    }
    
})
function show_result() {
    
    //  empate
    if (hand_player == hand_cpu) {
        basic.showIcon(IconNames.Meh)
        basic.pause(1000)
        basic.showString("EMPATE")
    } else if (hand_player == 1 && hand_cpu == 3 || hand_player == 2 && hand_cpu == 1 || hand_player == 3 && hand_cpu == 2) {
        //  player gana
        basic.showIcon(IconNames.Happy)
        basic.pause(1000)
        basic.showString("WIN")
    } else {
        //  CPU gana
        basic.showIcon(IconNames.Sad)
        basic.pause(1000)
        basic.showString("LOSE")
    }
    
    //  end juego
    game_active = false
    basic.pause(1000)
    basic.clearScreen()
    basic.showString("END")
}

