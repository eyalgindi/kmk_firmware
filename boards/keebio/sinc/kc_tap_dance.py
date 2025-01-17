from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import simple_key_sequence

GGL_SEARCH = simple_key_sequence(
    (
        KC.LGUI(KC.C),
                KC.LCTL(KC.N1),
                KC.MACRO_SLEEP_MS(100),
                KC.LGUI(KC.V),
                KC.MACRO_SLEEP_MS(100),
                KC.ENT
    )
)


F9 = KC.TD(
    # Tap once for "F9"
    KC.F9,
    # Tap twice for lang change
    KC.LALT(KC.Z)
)
F10 = KC.TD(
    # Tap once for "F10"
    KC.F10,
    # Tap twice for raycast, tap and hold for google search of the selected text
    KC.HT(KC.LGUI(KC.SPC), GGL_SEARCH),
    GGL_SEARCH
)

# for every alpha-beth char - single tap = lower case, double tap = Cap case , double tap and hold = command+char
A = KC.TD(KC.A, KC.HT(KC.LSFT(KC.A), KC.LGUI(KC.A)), tap_time=70)
B = KC.TD(KC.B, KC.HT(KC.LSFT(KC.B), KC.LGUI(KC.B)), tap_time=70)
C = KC.TD(KC.C, KC.HT(KC.LSFT(KC.C), KC.LGUI(KC.C)), tap_time=70)
D = KC.TD(KC.D, KC.HT(KC.LSFT(KC.D), KC.LGUI(KC.D)), tap_time=70)
E = KC.TD(KC.E, KC.HT(KC.LSFT(KC.E), KC.LGUI(KC.E)), tap_time=70)
F = KC.TD(KC.F, KC.HT(KC.LSFT(KC.F), KC.LGUI(KC.F)), tap_time=70)
G = KC.TD(KC.G, KC.HT(KC.LSFT(KC.G), KC.LGUI(KC.G)), tap_time=70)
H = KC.TD(KC.H, KC.HT(KC.LSFT(KC.H), KC.LGUI(KC.H)), tap_time=70)
I = KC.TD(KC.I, KC.HT(KC.LSFT(KC.I), KC.LGUI(KC.I)), tap_time=70)
J = KC.TD(KC.J, KC.HT(KC.LSFT(KC.J), KC.LGUI(KC.J)), tap_time=70)
K = KC.TD(KC.K, KC.HT(KC.LSFT(KC.K), KC.LGUI(KC.K)), tap_time=70)
L = KC.TD(KC.L, KC.HT(KC.LSFT(KC.L), KC.LGUI(KC.L)), tap_time=70)
M = KC.TD(KC.M, KC.HT(KC.LSFT(KC.M), KC.LGUI(KC.M)), tap_time=70)
N = KC.TD(KC.N, KC.HT(KC.LSFT(KC.N), KC.LGUI(KC.N)), tap_time=70)
O = KC.TD(KC.O, KC.HT(KC.LSFT(KC.O), KC.LGUI(KC.O)), tap_time=70)
P = KC.TD(KC.P, KC.HT(KC.LSFT(KC.P), KC.LGUI(KC.P)), tap_time=70)
Q = KC.TD(KC.Q, KC.HT(KC.LSFT(KC.Q), KC.LGUI(KC.Q)), tap_time=70)
R = KC.TD(KC.R, KC.HT(KC.LSFT(KC.R), KC.LGUI(KC.R)), tap_time=70)
S = KC.TD(KC.S, KC.HT(KC.LSFT(KC.S), KC.LGUI(KC.S)), tap_time=70)
T = KC.TD(KC.T, KC.HT(KC.LSFT(KC.T), KC.LGUI(KC.T)), tap_time=70)
U = KC.TD(KC.U, KC.HT(KC.LSFT(KC.U), KC.LGUI(KC.U)), tap_time=70)
V = KC.TD(KC.V, KC.HT(KC.LSFT(KC.V), KC.LGUI(KC.V)), tap_time=70)
W = KC.TD(KC.W, KC.HT(KC.LSFT(KC.W), KC.LGUI(KC.W)), tap_time=70)
X = KC.TD(KC.X, KC.HT(KC.LSFT(KC.X), KC.LGUI(KC.X)), tap_time=70)
Y = KC.TD(KC.Y, KC.HT(KC.LSFT(KC.Y), KC.LGUI(KC.Y)), tap_time=70)
Z = KC.TD(KC.Z, KC.HT(KC.LSFT(KC.Z), KC.LGUI(KC.Z)), KC.LGUI(KC.LCTL(KC.Q)), tap_time=70)
