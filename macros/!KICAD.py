# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'KICAD', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000055, 'ESC', [Keycode.ESCAPE, -Keycode.ESCAPE]),
        (0xFF6000, 'TRACE', ['x']),
        (0x005055, 'SELECT', ['u']),
        # 2nd row ----------
        (0x550000, 'DELETE', [Keycode.DELETE, -Keycode.DELETE]),
        (0x005500, 'UNDO', [Keycode.CONTROL, 'z', -Keycode.CONTROL]),
        (0x000055, 'REDO', [Keycode.CONTROL, 'y', -Keycode.CONTROL]),
        # 3rd row ----------
        (0x555500, 'X', ['x']),
        (0x555500, 'U', ['u']),
        (0x005500, 'A', ['a']),
        # 4th row ----------
        (0x550056, 'Ruler', [Keycode.CONTROL, Keycode.SHIFT, 'm', -Keycode.CONTROL, -Keycode.SHIFT]),
        (0x444444, 'Via', [Keycode.CONTROL, Keycode.SHIFT, 'v', -Keycode.CONTROL, -Keycode.SHIFT]),
        (0x550000, 'DelTrace', ['u', Keycode.DELETE, -Keycode.DELETE]),

        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
