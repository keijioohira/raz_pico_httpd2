from machine import Pin, PWM
import time

def play(should_continue=lambda: True):
    buzzer = PWM(Pin(2))  # GP2ピン使用
    buzzer.duty_u16(65535)

    C4  = 261.63
    E4  = 329.63
    G4  = 392.00
    A4  = 440.00
    AS4 = 466.16
    B4  = 493.88
    C5  = 523.25
    D5  = 587.33
    E5  = 659.25
    F5  = 698.46
    G5  = 783.99
    A5  = 880.00
    B5  = 987.77
    C6  = 1046.50
    D6  = 1174.66
    E6  = 1318.51
    G6  = 1567.98
    A6  = 1760.00
    REST = 0

    melody = [E5, E5, REST, E5, REST, C5, E5, REST, G5, REST, REST, REST,
              G4, REST, REST, REST, C5, REST, REST, G4, REST, E4, REST,
              A4, REST, B4, REST, AS4, A4, REST, G4, E5, G5, A5, REST,
              F5, G5, REST, E5, REST, C5, D5, B4, REST, REST,
              C5, REST, REST, G4, REST, E4, REST, A4, REST, B4, REST, AS4, A4,
              REST, G4, E5, G5, A5, REST, F5, G5, REST, E5, REST, C5, D5, B4,
              REST, REST]

    tempo = [0.15] * len(melody)

    length = min(len(melody), len(tempo))

    for i in range(length):
        if not should_continue():
            break
        note = melody[i]
        duration = tempo[i]
        if note == REST:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(int(note))
            buzzer.duty_u16(32768)
        time.sleep(duration)

    buzzer.duty_u16(0)
    buzzer.deinit()