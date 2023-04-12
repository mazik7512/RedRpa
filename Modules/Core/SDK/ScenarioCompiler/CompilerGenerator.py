from Modules.Core.SDK.ScenarioCompiler.Compilers.Compiler import STDRSLCompiler
from Modules.Core.Policies.CompilerPolicies.CompilePolicy import STDRSLCompilePolicy
from AppData.Configs.CompilerConfig import COMPILERS_PATH


class STDRSLCompilerGenerator:

    @staticmethod
    def generate_compiler(compiler_type="STDRSL", compile_policy="STDRSL"):
        policy = STDRSLCompilerGenerator._generate_policy(compile_policy)
        compiler = STDRSLCompilerGenerator._generate_compiler(compiler_type, policy)
        return compiler

    @staticmethod
    def _generate_compiler(compiler_type, policy):
        if compiler_type == "STDRSL":
            return STDRSLCompiler(policy)
        return None

    @staticmethod
    def _generate_policy(policy_type):
        if policy_type == "STDRSL":
            return STDRSLCompilePolicy()
        return None
