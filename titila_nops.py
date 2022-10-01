import machine_sim as machine
import time
import rp2_sim as rp2
from rp2_sim import *

# Blink state machine program. Blinks LED at 10 Hz (with freq=2000)
# 2000 Hz / (20 cycles per instruction * 10 instructions) = 10 Hz
# Single pin (base pin) starts at output and logic low

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1) [19]
    nop()        [19]
    nop()        [19]
    nop()        [19]
    nop()        [19]
    set(pins, 0) [19]
    nop()        [19]
    nop()        [19]
    nop()        [19]
    nop()        [19]
    wrap()

# Init state machine with "blink" program
# (state machine 0, running at 2kHz, base pin is GP25 (LED))
sm = rp2.StateMachine(0, blink, freq=2000, set_base=machine.Pin(25))

# start and stop state machine
print("Starting state machine...")
sm.active(1)
time.sleep(1)
print("Stopping state machine...")
sm.active(0)
time.sleep(1)
