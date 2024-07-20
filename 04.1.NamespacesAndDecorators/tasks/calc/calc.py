import sys
import math
from typing import Any

PROMPT = '>>> '


def run_calc(context: dict[str, Any] | None = None) -> None:
    """Run interactive calculator session in specified namespace"""
    while True:
        try:
            sys.stdout.write(PROMPT)
            x = sys.stdin.readline()
            y: str = f"{eval(x)}\n"
            sys.stdout.write(y)
        except EOFError:
            break


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
