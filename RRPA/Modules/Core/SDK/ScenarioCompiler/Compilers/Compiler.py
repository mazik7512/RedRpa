from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.Compilers.Compiler import AbstractCompiler
from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.CompilePolicy import AbstractCompilePolicy
from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioLinker.Linker import AbstractLinker


class STDRSLCompiler(AbstractCompiler):

    def __init__(self, compile_policy: AbstractCompilePolicy, linker: AbstractLinker):
        self._compile_policy = compile_policy
        self._linker = linker

    def compile(self, scenario):
        compiled_data = self._compile_policy.compile(scenario)
        for key in compiled_data.keys():
            self._linker.add_data_to_link(key, compiled_data[key])
        rex = self._linker.link()
        return rex
