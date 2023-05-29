def wrongPasswordValidation():
    global password_wrong
    password_wrong = password_wrong + 1
    if password_wrong == 3:
        music.start_melody(music.built_in_melody(Melodies.FUNERAL),
            MelodyOptions.FOREVER)
        radio.send_string("Safe is Being Attacked!")

def on_button_pressed_a():
    global master_password_entered
    master_password_entered = "" + master_password_entered + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def clearScreen():
    basic.pause(100)
    basic.clear_screen()
def hidePassword():
    global password_length
    I2C_LCD1602.show_string(passwordentered, 0, 0)
    password_length = len(passwordentered)
    basic.pause(100)
    if password_length == 1:
        I2C_LCD1602.show_string("*", 0, 0)
    elif password_length == 2:
        I2C_LCD1602.show_string("**", 0, 0)
    elif password_length == 3:
        I2C_LCD1602.show_string("***", 0, 0)
    elif password_length == 4:
        I2C_LCD1602.show_string("****", 0, 0)
    else:
        I2C_LCD1602.show_string("Too Long!", 0, 0)
        I2C_LCD1602.clear()

def on_button_pressed_ab():
    global master_password_entered
    if master_password_entered == master_password:
        music.stop_all_sounds()
        I2C_LCD1602.show_string("Welcome!", 0, 0)
        master_password_entered = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global master_password_entered
    master_password_entered = "" + master_password_entered + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

password_length = 0
master_password_entered = ""
passwordentered = ""
master_password = ""
password_wrong = 0
password_wrong = 0
password = "1234"
master_password = "ABA"
passwordentered = ""
I2C_LCD1602.lcd_init(0)
I2C_LCD1602.show_string("Enter Password", 0, 0)

def on_forever():
    global passwordentered
    pins.digital_write_pin(DigitalPin.P2, 1)
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        basic.show_number(1)
        clearScreen()
        passwordentered = "" + passwordentered + "1"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P15) == 1:
        basic.show_number(4)
        clearScreen()
        passwordentered = "" + passwordentered + "4"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P14) == 1:
        basic.show_number(7)
        clearScreen()
        passwordentered = "" + passwordentered + "7"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P13) == 1:
        basic.show_string("*")
        clearScreen()
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        basic.show_number(2)
        clearScreen()
        passwordentered = "" + passwordentered + "2"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P15) == 1:
        basic.show_number(5)
        clearScreen()
        passwordentered = "" + passwordentered + "5"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P14) == 1:
        basic.show_number(8)
        clearScreen()
        passwordentered = "" + passwordentered + "8"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P13) == 1:
        basic.show_number(0)
        clearScreen()
        passwordentered = "" + passwordentered + "0"
        hidePassword()
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        basic.show_number(3)
        clearScreen()
        passwordentered = "" + passwordentered + "3"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P15) == 1:
        basic.show_number(6)
        clearScreen()
        passwordentered = "" + passwordentered + "6"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P14) == 1:
        basic.show_number(9)
        clearScreen()
        passwordentered = "" + passwordentered + "9"
        hidePassword()
    elif pins.digital_read_pin(DigitalPin.P13) == 1:
        basic.show_string("#")
        clearScreen()
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        basic.show_string("A")
        clearScreen()
        pins.servo_write_pin(AnalogPin.P0, 90)
    elif pins.digital_read_pin(DigitalPin.P15) == 1:
        basic.show_string("B")
        clearScreen()
    elif pins.digital_read_pin(DigitalPin.P14) == 1:
        basic.show_string("C")
        clearScreen()
    elif pins.digital_read_pin(DigitalPin.P13) == 1:
        basic.show_string("D")
        clearScreen()
        if password == passwordentered:
            basic.show_icon(IconNames.YES)
            pins.servo_write_pin(AnalogPin.P0, 0)
            I2C_LCD1602.clear()
            passwordentered = ""
        else:
            basic.show_icon(IconNames.NO)
            wrongPasswordValidation()
        basic.pause(100)
        basic.clear_screen()
    pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)