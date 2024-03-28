cislo2 = 0
cislo = 0

def on_button_pressed_a():
    global cislo2
    basic.show_number(cislo2)
    cislo2 += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    basic.show_number(cislo + cislo2)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_b():
    global cislo
    basic.show_number(cislo)
    cislo += 1
input.on_button_pressed(Button.B, on_button_pressed_b)
