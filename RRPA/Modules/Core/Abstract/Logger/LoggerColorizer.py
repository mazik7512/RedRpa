from abc import ABC, abstractmethod


class Colorizer(ABC):
    @property
    @abstractmethod
    def HEADER(self):
        pass

    @property
    @abstractmethod
    def OKBLUE(self):
        pass

    @property
    @abstractmethod
    def OKCYAN(self):
        pass

    @property
    @abstractmethod
    def OKGREEN(self):
        pass

    @property
    @abstractmethod
    def WARNING(self):
        pass

    @property
    @abstractmethod
    def FAIL(self):
        pass

    @property
    @abstractmethod
    def ENDC(self):
        pass

    @property
    @abstractmethod
    def BOLD(self):
        pass

    @property
    @abstractmethod
    def UNDERLINE(self):
        pass

    @property
    @abstractmethod
    def DEFAULT(self):
        pass
