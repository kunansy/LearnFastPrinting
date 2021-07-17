#!/usr/bin/env python3
import random
import time

from colorama import Fore


HJKL = {
    "UP": 'k',
    "DOWN": 'j',
    "LEFT": 'h',
    "RIGHT": 'l'
}

KEYS_TO_LEARN = {
    **HJKL
}

def learn() -> None:
    answers_time = 0
    answers = right_answers = 0
    keys = list(KEYS_TO_LEARN.keys())
    while True:
        key = random.choice(keys)
        sleep = random.randint(2, 10)
        time.sleep(sleep)

        answers += 1
        start = time.perf_counter()
        answer = input(key)
        answ_time = round(time.perf_counter() - start, 2)
        answers_time += answ_time

        if answer == KEYS_TO_LEARN[key]:
            print(Fore.GREEN, f"[{answ_time}]      RIGHT", Fore.RESET)
            right_answers += 1
        else:
            print(Fore.RED, f"[{answ_time}]     WRONG", Fore.RESET)

    print(f"Avg answer time={round(answers_time / answers)}s")



def main() -> None:
    learn()


if __name__ == "__main__":
    main()

