from tools.rgb import RGBLED

pin_1 = (2,3,4)
pin_2 = (24,23,18)
f = 0.05

RGB = RGBLED(*pin_1)
RGB.fade(frequencies=[f, f, f], phase=[0, 0.333, 0.666])