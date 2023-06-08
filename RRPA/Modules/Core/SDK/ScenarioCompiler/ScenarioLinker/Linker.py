from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.LinkerPolicies.LinkPolicy import AbstractLinkPolicy
from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioLinker.Linker import AbstractLinker
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.Modules.Core.Policies.CompilerPolicies.LinkerPolicies.LinkPolicy import STDRSLLinkPolicy
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Core.SDK.ScenarioExecutable.ExecutableGenerator import STDREXGenerator


MODULE_PREFIX = "[Linker]"


class STDRSLLinker(AbstractLinker):

    def __init__(self, link_policy: AbstractLinkPolicy = STDRSLLinkPolicy):
        self._sections = {}
        self._policy = link_policy

    def add_data_to_link(self, data_name, data):
        self._sections[data_name] = data

    def link(self):
        rex = self._policy.link(self._sections)
        return rex
