import os
import demoqa_tests.resources


def create_path(name_file):
    return os.path.abspath(os.path.join(os.path.dirname(demoqa_tests.resources.__file__), name_file))
