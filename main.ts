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

