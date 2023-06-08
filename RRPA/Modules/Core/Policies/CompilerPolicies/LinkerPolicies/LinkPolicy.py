from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.LinkerPolicies.LinkPolicy import AbstractLinkPolicy
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Core.SDK.ScenarioExecutable.ExecutableGenerator import STDREXGenerator


class STDRSLLinkPolicy(AbstractLinkPolicy):

    @staticmethod
    def link(data):
        rex_generator = STDREXGenerator()
        for key in data.keys():
            rex_generator.add_section(key, data[key])
        rex = STDRedExecutable(rex_generator.generate_executable_sections())
        return rex
