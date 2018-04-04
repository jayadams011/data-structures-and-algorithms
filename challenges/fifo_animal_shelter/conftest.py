import pytest
from fifo_animal_shelter import AnimalShelter as AS


@pytest.fixture
def aniDogDante():
    x = AS([kdog, dog])
    return x


@pytest.fixture
def aniCatMaggie():
    y = AS([maggie, cat])
    return y


# def dequeueNoPref
# should return "kdog, dog"
