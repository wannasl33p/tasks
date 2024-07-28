import sys
import math
from typing import Any

PROMPT = ">>> "


def run_calc(context: dict[str, Any] | None = None) -> None:
    """Run interactive calculator session in specified namespace"""
    n_glob: dict[Any] = globals()
    del n_glob["__builtins__"]
    while True:
        try:
            sys.stdout.write(PROMPT)
            x = sys.stdin.readline()
            if x == "" or x is None:
                sys.stdout.write("\n")
                break
            y = eval(x, n_glob, context)
            sys.stdout.write(f"{y}\n")
        except EOFError:
            break


if __name__ == "__main__":
    context = {"math": math}
    run_calc(context)
