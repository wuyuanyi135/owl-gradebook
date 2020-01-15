from typing import *


class StudentEntry(NamedTuple):
    name: str
    student_id: str
    mark: float


def load_csv_file(filename: str) -> (List[StudentEntry]):
    """
    Load csv file and build the student entry maps
    :param filename: path to the csv file
    :return: list of student entry
    """
    pass


def save_csv_file(output_filename: str, entries: List[StudentEntry]):
    """
    Save student entries into a csv file.
    :param output_filename:
    :param entries:
    :return:
    """
    pass
