from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.NameBoundingPolicies.ImportPolicy import AbstractImportPolicy


class STDImportPolicy(AbstractImportPolicy):

    @staticmethod
    def generate_import(api_name):
        return "from <import_path> import " + api_name

