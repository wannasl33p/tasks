import typing as tp

def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    logged_text = inp.read()
    lines = logged_text.split('\n')
    
    for line in lines:
        if line:
            parts = line.split('\t')
            sha1 = parts[0]
            message = parts[-1]
            dots_count = 73 - len(message)
            reformatted_line = f"{sha1[:7]}{'.'.ljust(dots_count, '.')}{message}"
            out.write(reformatted_line + '\n')