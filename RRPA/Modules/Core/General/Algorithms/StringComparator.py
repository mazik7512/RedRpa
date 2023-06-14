from RRPA.Modules.Core.Abstract.General.Algorithms.StringComparator import AbstractStringComparator
from fuzzywuzzy import fuzz


class STDStringComparator(AbstractStringComparator):

    @staticmethod
    def compare_strings(s1: str, s2: str) -> int:
        _s1 = s1.lower()
        _s2 = s2.lower()
        result = fuzz.partial_ratio(_s1, _s2)
        return result
