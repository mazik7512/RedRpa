from RRPA.Modules.Core.Abstract.Policies.VMPolicies.LinkPolicy import AbstractLinkPolicy


class STDLinkPolicy(AbstractLinkPolicy):

    @staticmethod
    def link_lib(import_data, lib_path):
        return import_data.replace('<import_path>', lib_path)
