from abc import abstractmethod


class AbstractException(Exception):

    @abstractmethod
    def get_exception_data(self):
        pass

