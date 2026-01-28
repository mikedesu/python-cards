from enum import Enum


class CardFace(Enum):
    HEART = 0
    SPADE = 1
    CLUB = 2
    DIAMOND = 3


class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


def valid_face(face):
    return face in CardFace


def valid_value(value):
    return value in CardValue


def face2str(face):
    if face == CardFace.HEART:
        return "heart"
    elif face == CardFace.SPADE:
        return "spade"
    elif face == CardFace.CLUB:
        return "club"
    elif face == CardFace.DIAMOND:
        return "diamond"
    return "face-error"


def value2str(v):
    if v == CardValue.TWO:
        return "2"
    if v == CardValue.THREE:
        return "3"
    if v == CardValue.FOUR:
        return "4"
    if v == CardValue.FIVE:
        return "5"
    if v == CardValue.SIX:
        return "6"
    if v == CardValue.SEVEN:
        return "7"
    if v == CardValue.EIGHT:
        return "8"
    if v == CardValue.NINE:
        return "9"
    if v == CardValue.TEN:
        return "10"
    if v == CardValue.JACK:
        return "J"
    if v == CardValue.QUEEN:
        return "Q"
    if v == CardValue.KING:
        return "K"
    if v == CardValue.ACE:
        return "A"
    return "value-error"


class Card:
    def __init__(self, face=None, value=None):
        if not valid_face(face):
            raise ValueError("Face is not valid")
        elif not valid_value(value):
            raise ValueError("Value is not valid")
        self.face = face
        self.value = value

    def point_value(self):
        if (
            self.value == CardValue.JACK
            or self.value == CardValue.QUEEN
            or self.value == CardValue.KING
        ):
            return 10
        elif self.value == CardValue.ACE:
            return 11
        return self.value.value

    def __str__(self):
        return value2str(self.value) + " " + face2str(self.face)
