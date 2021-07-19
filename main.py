#!/usr/bin/env python3
import random
import time
from src import keys
from dataclasses import dataclass

from colorama import Fore


KEYS_TO_LEARN = {
    **keys.ENGLISH_UP_KEYS
}


@dataclass
class KeyStat:
    _key: dict[str, str]
    right_answers: int = 0
    wrong_answers: int = 0

    @property
    def key(self) -> str:
        return list(self._key.keys())[0]

    @property
    def value(self) -> str:
        return list(self._key.values())[0]

    @property
    def answers_count(self) -> int:
        return self.wrong_answers + self.right_answers

    @property
    def effectiveness(self) -> float:
        return round(self.answers_count / self.right_answers * 100, 2)

    def answer(self,
               answer: str,
               answer_time: float) -> None:
        if answer == self.value:
            print(Fore.GREEN, f"[{answer_time}]{' ' * 5} RIGHT", Fore.RESET, sep='')
            self.right_answers += 1
        else:
            print(Fore.RED, f"[{answer_time}]{' ' * 5} WRONG", Fore.RESET, sep='')
            self.wrong_answers += 1

    def __str__(self) -> str:
        return list(self._key.keys())[0]

    def __repr__(self) -> str:
        return f"{self.key}: {self.value},\n" \
               f"{self.wrong_answers=},\n" \
               f"{self.right_answers=},\n" \
               f"{self.effectiveness=}%"


@dataclass
class KeysStat:
    keys: list[KeyStat]

    def __init__(self,
                 keys: dict[str, str] or str or list[str]) -> None:
        if isinstance(keys, dict):
            keys = [
                KeyStat({key: value})
                for key, value in keys.items()
            ]
        elif isinstance(keys, (list, str)):
            keys = [
                KeyStat({key.upper(): key.lower()})
                for key in keys
            ]
        self.keys = keys


    @property
    def wrongest_key(self) -> KeyStat:
        return max(
            self.keys,
            key=lambda key: key.effectiveness
        )

    @property
    def rightest_key(self) -> KeyStat:
        return min(
            self.keys,
            key=lambda key: key.effectiveness
        )

    @property
    def answers_count(self) -> int:
        return sum(
            key.answers_count
            for key in self.keys
        )

    def __getitem__(self,
                    index: int) -> KeyStat:
        return self.keys[index]

    def __len__(self) -> int:
        return len(self.keys)

    def __str__(self) -> str:
        return '\n\n'.join(
            f"{key!r}"
            for key in sorted(self.keys, key=lambda key: key.answers_count)
        )


def learn() -> None:
    keys = KeysStat(KEYS_TO_LEARN)
    while True:
        key: KeyStat = random.choice(keys)
        sleep = random.randint(2, 6)
        time.sleep(sleep)

        start = time.perf_counter()
        answer = input(f"{key}\n")
        answer_time = round(time.perf_counter() - start, 2)

        if answer == ':q':
            break
        elif answer == ':h':
            print(keys)
        else:
            key.answer(answer, answer_time)

    print(keys)


def main() -> None:
    learn()


if __name__ == "__main__":
    main()
