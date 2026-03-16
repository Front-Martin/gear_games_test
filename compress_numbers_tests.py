from compress_numbers import compress_numbers

def test_first_example():
    assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]

def test_second_example():
    assert compress_numbers([0, 0, 1, 1, 0]) == [0, 1, 0]

def test_no_duplicates():
    assert compress_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_same():
    assert compress_numbers([1, 1, 1, 1]) == [1]

def test_single_element():
    assert compress_numbers([2]) == [2]

def test_empty_list():
    assert compress_numbers([]) == []

def test_float_numbers():
    assert compress_numbers([1.1, 1.1, 2.2, 2.2, 3.3]) == [1.1, 2.2, 3.3]

def test_mixed_types_int_float():
    assert compress_numbers([1, 1.0, 2, 2.0]) == [1, 2]

def test_negative_numbers():
    assert compress_numbers([-1, -1, -2, -2, -3]) == [-1, -2, -3]

def test_zero_values():
    assert compress_numbers([0, 0, 0, 1, 1, 0, 0, 2]) == [0, 1, 0, 2]