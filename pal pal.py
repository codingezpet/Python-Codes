import time
import sys


def print_lyrics():
    lyrics = [
        "Kyon ho khum hosh me aata nahi",
        "Sukoon ye dil kyun paata nahi",
        "Kyun teri hansi mujhe yaad hai",
        "Kyun teri baatein mujhe yaad hai",
        "Mera mann toh tujhme hi bas gaya",
        "Dobara milna naman hai yahaan",
        "Yeh duniya jahan nayi meri dard",
        "Tujhe yeh nazar kyun aata nahi",
    ]

    delays = [0.3, 0.6, 0.3, 0.3, 0.3, 0.8]

    print("\nPal Pal\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)


print_lyrics()
