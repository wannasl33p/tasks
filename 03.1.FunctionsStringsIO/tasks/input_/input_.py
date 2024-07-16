import sys
import typing as tp


def input_(
    prompt: str | None = None,
    inp: tp.IO[str] | None = None,
    out: tp.IO[str] | None = None,
) -> str | None:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    if prompt is not None:
        if out is not None:
            if "\n" in prompt:
                prompt = prompt.replace("\n", "")
            out.write(prompt)
            out.flush()
        else:
            sys.stdout.write(prompt)

    try:
        if inp is not None:
            text = inp.read()

        else:
            text = sys.stdin.read(inp)
        if "\n" in text:
            text = text.replace("\n", "")
            return text

    except EOFError:
        return None


# text = 'wqtytryr tewq e\n'
# if '\n' in text:
#        text=text.replace("\n","")
# print(text)
# print(input())
