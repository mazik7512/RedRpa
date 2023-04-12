from Modules.Core.Abstract.Policies.CompilerPolicies.TranslatorPolicies.OffsetTranslationPolicy import AbstractOffsetTranslationPolicy


class STDRSLOffsetTranslationPolicy(AbstractOffsetTranslationPolicy):

    _offset_level = 0

    @staticmethod
    def get_current_offset():
        offset = ""
        for i in range(STDRSLOffsetTranslationPolicy._offset_level):
            offset += "\t"
        return offset

    @staticmethod
    def add_offset_level():
        STDRSLOffsetTranslationPolicy._offset_level += 1

    @staticmethod
    def remove_offset_level():
        if STDRSLOffsetTranslationPolicy._offset_level > 0:
            STDRSLOffsetTranslationPolicy._offset_level -= 1
