import sys
import time

# Kendrick Lamar - Real, 1:07
lyrics = [
    ("you love French tip and that pay for", 0.030),
    ("You love bank slip that tell you we paid more", 0.3),
    ("You love a good hand whenever the card dealt", 0.3),
    ("But what got to do with it..", 0.3),
    ("when you don't love yourself?", 0.3),
    ("v( ‘.’ )v", 0.30)
]
delays = [0.23, 0.2, 0.2, 0.17, 0.2, 0.2]

for i, (line, char_delay) in enumerate(lyrics):
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(char_delay)
    time.sleep(delays[i])
    print("")
