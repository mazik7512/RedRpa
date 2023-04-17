from RRPA.Modules.Core.SDK.ScenarioCompiler.Compilers.Compiler import STDRSLCompiler
from RRPA.Modules.Core.Policies.CompilerPolicies.CompilePolicy import STDRSLCompilePolicy
from RRPA.AppData.Configs.CompilerConfig import OS_UTILS_PATH


class STDRSLCompilerGenerator:

    @staticmethod
    def generate_compiler(compiler_type="STDRSL", compile_policy="STDRSL", os="Windows"):
        os_path = STDRSLCompilerGenerator._generate_os_tools(os)
        policy = STDRSLCompilerGenerator._generate_policy(compile_policy, os_path)
        compiler = STDRSLCompilerGenerator._generate_compiler(compiler_type, policy)
        return compiler

    @staticmethod
    def _generate_compiler(compiler_type, policy):
        if compiler_type == "STDRSL":
            return STDRSLCompiler(policy)
        return None

    @staticmethod
    def _generate_policy(policy_type, os_path):
        if policy_type == "STDRSL":
            return STDRSLCompilePolicy(os_path)
        return None

    @staticmethod
    def _generate_os_tools(os):
        path = OS_UTILS_PATH[:-1].format(os).replace("\\", ".")
        return path
