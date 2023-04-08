from abc import ABC, abstractmethod


class AbstractNameResolver(ABC):

    @abstractmethod
    def link_names(self):
        pass
