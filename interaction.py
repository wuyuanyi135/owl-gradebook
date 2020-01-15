from collections import OrderedDict

from prompt_toolkit import prompt
from typing import List

from file_io import load_csv_file, StudentEntry


def report(entries: List[StudentEntry]):
    """
    print how many students are loaded
    :param entries:
    :return:
    """
    pass


def request_action():
    """

    :return:
    """
    return prompt("Please input student name or id: ")


def find_entry(key: str, entries: List[StudentEntry]) -> StudentEntry:
    """

    :param key:
    :param entries:
    :return:
    """
    pass


def assign_mark(entry: StudentEntry):
    """
    Ask user for mark, assign into the entry.
    :param entry:
    :return:
    """
    pass


def process_loop(entries: List[StudentEntry]):
    """
    repeatedly request user action and dispatch the task.
    check the command first, then id, then name.

    :param entries:
    :return:
    """
    pass


def interaction_entry(filename):
    entries = load_csv_file(filename)

    report(entries)

    process_loop(entries)
