import logging
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List


def pluralise(word: str, n: int) -> str:
    return word if n == 1 else word + "s"


def quote(s: str) -> str:
    return f'"{s}"'


def join_naturally(items: List[str]) -> str:
    if len(items) == 0:
        raise ValueError("Cannot join an empty list.")
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + f", and {items[-1]}"


def get_static_folder_path() -> Path:
    parser = ArgumentParser()
    parser.add_argument("--static-folder", type=Path, required=True)
    args = parser.parse_args()
    return args.static_folder


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger
