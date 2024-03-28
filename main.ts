let cislo2 = 0
let cislo = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(cislo2)
    cislo2 += 1
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(cislo + cislo2)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(cislo)
    cislo += 1
})
