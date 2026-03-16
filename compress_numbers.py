from typing import List, Union

def compress_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    if not numbers:  
        return []

    result = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] != result[-1]:
            result.append(numbers[i])

    return result