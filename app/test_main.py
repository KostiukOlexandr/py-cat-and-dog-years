from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (25, 2),
        (28, 3),
        (100, 21),
    ],
)
def test_cat_age_boundaries(cat_age: int, expected_cat: int) -> None:
    result = get_human_age(cat_age, 0)
    assert result[0] == expected_cat


@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (30, 3),
        (100, 17),
    ],
)
def test_dog_age_boundaries(dog_age: int, expected_dog: int) -> None:
    result = get_human_age(0, dog_age)
    assert result[1] == expected_dog


import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15.0, 15),
        (15, "20"),
        (15, 20.5),
    ]
)
def test_get_human_age_invalid_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -5),
        (-10, -20),
    ]
)
def test_get_human_age_negative_values(cat_age, dog_age) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)

