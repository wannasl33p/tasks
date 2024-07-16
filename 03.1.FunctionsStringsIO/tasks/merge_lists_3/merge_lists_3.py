import typing as tp
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    values: list[int] = []
    for num in input_streams:
        for n in num:
            value = int(n.strip(b'\n'))
            heapq.heappush(values, value)
    while values:
        output_stream.write((f'{heapq.heappop(values)}\n').encode('utf-8'))
