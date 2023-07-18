print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
<<<<<<< master
<<<<<<< master
from kmk.modules.holdtap import HoldTap
<<<<<<< master
<<<<<<< master
<<<<<<< master
from kmk.modules.tapdance import TapDance
=======
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
from kmk.modules.tapdance import TapDance
>>>>>>> TapDance
=======
>>>>>>> Keebio Sinc Rev3 - Preliminary Support
=======
from kmk.modules.holdtap import HoldTap
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
from kmk.modules.tapdance import TapDance
>>>>>>> TapDance
from storage import getmount
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
<<<<<<< master
<<<<<<< master
from kmk.modules.encoder import EncoderHandler

<<<<<<< master
<<<<<<< master
<<<<<<< master

import kc_seq as SQ
=======
import kc_seq as SQ
import kc_tap_dance as TD
>>>>>>> Added Support for Keebio/Sinc Rev3
=======

import kc_seq as SQ
>>>>>>> TapDance
=======
from kmk.modules.encoder import EncoderHandler

import kc_seq as SQ
import kc_tap_dance as TD
>>>>>>> Added Support for Keebio/Sinc Rev3
=======

import kc_seq as SQ
>>>>>>> TapDance

_____ = KC.TRNS
XXXXXXX = KC.NO
FnKey = KC.MO(1)
<<<<<<< master
=======
>>>>>>> Keebio Sinc Rev3 - Preliminary Support

keyboard = KMKKeyboard()
<<<<<<< master
<<<<<<< master
keyboard.debug_enabled = True

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(TapDance())
<<<<<<< master

import kc_holdtap as HT
import kc_tap_dance as TD
=======
=======
keyboard.debug_enabled = True
<<<<<<< master
>>>>>>> Holdtap to replace LGUI+KC.__ABC__

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(TapDance())

<<<<<<< master
<<<<<<< master
keyboard.debug_enabled = True
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
=======
import kc_holdtap as HT
import kc_tap_dance as TD
>>>>>>> TapDance
=======
keyboard.modules.append(Layers())
>>>>>>> Keebio Sinc Rev3 - Preliminary Support
=======

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
<<<<<<< master
>>>>>>> Added Support for Keebio/Sinc Rev3

=======
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
import kc_holdtap as HT
=======
>>>>>>> TapDance

import kc_holdtap as HT
import kc_tap_dance as TD

# Per side configuration is set based on the device label (end with L or R).
# uncomment device_name line for the corresponding side on boot.py
split_side = SplitSide.LEFT if str(getmount('/').label)[-1] == 'L' else SplitSide.RIGHT
split = Split(split_type=SplitType.UART,
              split_side=split_side,
              data_pin=board.GP0,
              data_pin2=board.GP1,
              use_pio=True,
              uart_flip=split_side is SplitSide.RIGHT)
keyboard.modules.append(split)

enc_module = EncoderHandler()
enc_module.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]
keyboard.modules.append(enc_module)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (
    board.GP29,
            board.GP28,
            board.GP27,
            board.GP7,
            board.GP2,
            board.GP3,
            board.GP11,
            board.GP12,
            board.GP13,
)
if split_side is SplitSide.RIGHT:
    enc_module.pins = ((board.GP5, board.GP6, None),)
    num_rgb_pixels = 56
    keyboard.row_pins = (
        board.GP8,
                board.GP9,
                board.GP16,
                board.GP19,
                board.GP26,
                board.GP17,
    )
else:
    enc_module.pins = ((board.GP21, board.GP20, None),)

    num_rgb_pixels = 57
    keyboard.row_pins = (
        board.GP26,
                board.GP25,
                board.GP19,
                board.GP24,
                board.GP17,
                board.GP16,
    )


keyboard.keymap = [
    [
        KC.MUTE, KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,              KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.INS,
        KC.F1, KC.F2, KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,         KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.HOME,
<<<<<<< master
<<<<<<< master
<<<<<<< master
<<<<<<< master
<<<<<<< master
<<<<<<< master
=======
>>>>>>> TapDance
=======
>>>>>>> TapDance
        KC.F3, KC.F4, KC.TAB, TD.Q, TD.W, TD.E, TD.R, TD.T,                     TD.Y, TD.U, TD.I, TD.O, TD.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.END,
        KC.F5, KC.F6, KC.CAPS, TD.A, TD.S, TD.D, TD.F, TD.G,                    TD.H, TD.J, TD.K, TD.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGUP,
        KC.F7, KC.F8, KC.LSFT, TD.Z, TD.X, TD.C, TD.V, TD.B,                    TD.N, TD.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PGDN,
        TD.F9, TD.F10, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI, HT.SPC_FN,             HT.SPC_FN, KC.RALT, KC.RCTL, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT
<<<<<<< master
<<<<<<< master
=======
        KC.F3, KC.F4, KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,                     KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.END,
        KC.F5, KC.F6, KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G,                    KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGUP,
        KC.F7, KC.F8, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,                    KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PGDN,
        KC.F9, KC.F10, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI, HT.SPC_FN,             KC.SPC, KC.RALT, KC.RCTL, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
=======
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
        KC.F3, KC.F4, KC.TAB, HT.Q, HT.W, HT.E, HT.R, HT.T,                     HT.Y, HT.U, HT.I, HT.O, HT.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.END,
        KC.F5, KC.F6, KC.CAPS, HT.A, HT.S, HT.D, HT.F, HT.G,                    HT.H, HT.J, HT.K, HT.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGUP,
        KC.F7, KC.F8, KC.LSFT, HT.Z, HT.X, HT.C, HT.V, HT.B,                    HT.N, HT.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PGDN,
        KC.F9, KC.F10, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI, HT.SPC_FN,             HT.SPC_FN, KC.RALT, KC.RCTL, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT
<<<<<<< master
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
=======
>>>>>>> TapDance
=======
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
=======
>>>>>>> TapDance
    ],

    [
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____, _____,               _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,               _____, _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
<<<<<<< master
<<<<<<< master
<<<<<<< master
<<<<<<< master
<<<<<<< master
        _____, _____, _____, _____, _____, KC.LED_TOG(), KC.ENT,                                    KC.ENT, _____, _____, _____, _____, _____, _____
=======
        _____, _____, _____, _____, _____, _____, _____,                                    _____, _____, _____, _____, _____, _____, _____
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
        _____, _____, _____, _____, _____, _____, KC.ENT,                                    KC.ENT, _____, _____, _____, _____, _____, _____
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
=======
        _____, _____, _____, _____, _____, KC.LED_TOG(), KC.ENT,                                    KC.ENT, _____, _____, _____, _____, _____, _____
>>>>>>> TapDance
=======
        KC.F3, KC.F4, KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,                     KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.END,
        KC.F5, KC.F6, KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G,                    KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGUP,
        KC.F7, KC.F8, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,                    KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PGDN,
<<<<<<< master
        KC.F9, KC.F10, KC.LCTL, KC.LALT, KC.LGUI, KC.MO(1), KC.SPC,     KC.MO(1), KC.SPC, KC.RALT, KC.RCTL, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT
>>>>>>> Keebio Sinc Rev3 - Preliminary Support
=======
        KC.F9, KC.F10, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI, HT.SPC_FN,             KC.SPC, KC.RALT, KC.RCTL, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT
    ],

    [
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____, _____,               _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,               _____, _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____, _____,                      _____, _____, _____, _____, _____, _____, _____, _____,
        _____, _____, _____, _____, _____, _____, _____,                                    _____, _____, _____, _____, _____, _____, _____
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
        _____, _____, _____, _____, _____, _____, KC.ENT,                                    KC.ENT, _____, _____, _____, _____, _____, _____
>>>>>>> Holdtap to replace LGUI+KC.__ABC__
=======
        _____, _____, _____, _____, _____, KC.LED_TOG(), KC.ENT,                                    KC.ENT, _____, _____, _____, _____, _____, _____
>>>>>>> TapDance
    ]
]


keyboard.coord_mapping = [0,  2, 3, 4, 5, 6, 7, 8,                 91, 92, 93, 94, 95, 96, 97, 98,
                          9, 10, 11, 12, 13, 14, 15, 16, 17,          72, 73, 74, 75, 76, 77, 79, 80,
                          18, 19, 20, 21, 22, 23, 24, 25,           81, 82, 83, 84, 85, 86, 87, 88, 89,
                          27, 28, 29, 30, 31, 32, 33, 34,              99, 100, 101, 102, 103, 104, 106, 107,
                          36, 37, 38, 40, 41, 42, 43, 44,            63, 64, 65, 66, 67, 69, 70, 71,
                          45, 46, 47, 48, 49, 50, 52,                 55, 56, 57, 58, 60, 61, 62]

<<<<<<< master
<<<<<<< master

<<<<<<< master
<<<<<<< master
#
# rgb_ext = RGB(pixel_pin=board.NEOPIXEL, num_pixels=num_rgb_pixels)
=======
=======

<<<<<<< master
>>>>>>> Added Support for Keebio/Sinc Rev3
# rgb_ext = RGB(pixel_pin=board.NEOPIXEL,
#               num_pixels=num_rgb_pixels)
#
#
<<<<<<< master
>>>>>>> Added Support for Keebio/Sinc Rev3
=======
#
# rgb_ext = RGB(pixel_pin=board.NEOPIXEL, num_pixels=num_rgb_pixels)
>>>>>>> TapDance
# keyboard.extensions.append(rgb_ext)
=======
keyboard.extensions = []
>>>>>>> Keebio Sinc Rev3 - Preliminary Support
=======
=======
#
# rgb_ext = RGB(pixel_pin=board.NEOPIXEL, num_pixels=num_rgb_pixels)
>>>>>>> TapDance
# keyboard.extensions.append(rgb_ext)
>>>>>>> Added Support for Keebio/Sinc Rev3


if __name__ == '__main__':
    keyboard.go()    