import pytest
import unittest.mock as mock

from challenge_two.randomness import get_winner_list

test_datas = [
    {
        'mock_input': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'expected_output': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'result': True
    },
    {
        'mock_input': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'expected_output': [1, 2, 3, 4, 5, 6, 7, 8, 9, 11],
        'result': False
    }
]


@mock.patch('challenge_two.randomness.get_random_choices')
def test_random_winner(my_mock_choices):
    for case in test_datas:
        my_mock_choices.return_value = case['mock_input']
        test_result = get_winner_list() == case['expected_output']
        assert test_result == case['result']
