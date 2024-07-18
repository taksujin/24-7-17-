def on_button_pressed_a():
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 0)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 255)
    basic.pause(3000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 255)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 0)
    basic.pause(3000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 255)
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, 255)
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.pause(1000)
basic.forever(on_forever)
