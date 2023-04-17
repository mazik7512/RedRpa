from abc import ABC, abstractmethod


class AbstractLexema(ABC):

    def __init__(self, _type, _value):
        self._type = _type
        self._value = _value

    def get_token_type(self):
        return self._type

    def get_token_value(self):
        return self._value

    def __str__(self):
        res = "{type=" + str(self._type) + ";value=" + str(self._value) + "}"
        return res
