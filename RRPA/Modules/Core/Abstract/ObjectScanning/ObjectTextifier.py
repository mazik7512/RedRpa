from abc import ABC, abstractmethod


class AbstractObjectTextifier(ABC):

    @abstractmethod
    def textify(self, _object):
        pass
