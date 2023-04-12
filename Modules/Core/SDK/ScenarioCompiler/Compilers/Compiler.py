from Modules.Core.Abstract.SDK.ScenarioCompiler.Compilers.Compiler import AbstractCompiler
from Modules.Core.Abstract.Policies.CompilerPolicies.CompilePolicy import AbstractCompilePolicy


class STDRSLCompiler(AbstractCompiler):

    def __init__(self, compile_policy: AbstractCompilePolicy):
        self._compile_policy = compile_policy

    def compile(self, scenario):
        return self._compile_policy.compile(scenario)
