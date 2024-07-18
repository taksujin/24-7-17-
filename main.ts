input.onButtonPressed(Button.A, function () {
    radio.sendNumber(2)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendNumber(4)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(3)
})
input.onGesture(Gesture.LogoUp, function () {
    radio.sendNumber(5)
})
basic.showIcon(IconNames.Happy)
radio.setGroup(1)
