let hand = 0
input.onGesture(Gesture.Shake, function () {
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.Ghost)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Heart)
    } else {
    	
    }
})
