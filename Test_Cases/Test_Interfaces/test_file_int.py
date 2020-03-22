# test_file_int.py
"""
Test file interface module
"""

from Interfaces import int_file


# test all module functionalities
def test_file_int01():
    int_file.save_data([1, 2, 3], "C:\\Code", "test")
    assert int_file.load_integer_list("C:\\code", "test") == [1, 2, 3]
    assert int_file.load_string("C:\\code", "test") == "1 2 3"
    assert int_file.load_string_list("c:\\code", "test") == ["1", "2", "3"]