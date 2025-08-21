import pytest
import solution

@pytest.fixture(scope="module")
def get_positions():
    positions = solution.parse_zen()
    return positions

def test_first_line(get_positions):
    assert get_positions.get("Zen") == [(1, 2)]
    assert get_positions.get("Python") == [(1, 4)]
    assert get_positions.get("Peters") == [(1, 7)]

def test_contractions(get_positions):
    assert get_positions.get("aren't") == [(10, 3)]
    assert get_positions.get("you're") == [(16, 11)]
    assert get_positions.get("let's") == [(21, 7)]

def test_punctuation_ignored(get_positions):
    assert get_positions.get("right") == [(18, 7)]
    assert get_positions.get("obvious") == [(15, 9), (16, 7)]

def test_better_appearances(get_positions):
    better_positions = get_positions.get("better")
    assert better_positions is not None
    assert [ln for (ln, _) in better_positions] == [3, 4, 5, 6, 7, 8, 17, 18]