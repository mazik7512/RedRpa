from RRPA.Modules.Core.Abstract.OS.Tools.OSTools import AbstractOSTools
from RRPA.Modules.Core.Abstract.Web.Tools.WebTools import AbstractWebTools
from RRPA.Modules.Core.SDK.ScenarioCompiler.Compilers.Compiler import STDRSLCompiler
from RRPA.Modules.Core.Policies.CompilerPolicies.CompilePolicy import STDRSLCompilePolicy


class STDRSLCompilerGenerator:

    @staticmethod
    def generate_compiler(os: AbstractOSTools, web: AbstractWebTools, compiler_type="STDRSL", compile_policy="STDRSL"):
        tools = STDRSLCompilerGenerator._generate_tools(os, web)
        policy = STDRSLCompilerGenerator._generate_policy(compile_policy, tools)
        compiler = STDRSLCompilerGenerator._generate_compiler(compiler_type, policy)
        return compiler

    @staticmethod
    def _generate_compiler(compiler_type, policy):
        if compiler_type == "STDRSL":
            return STDRSLCompiler(policy)
        return None

    @staticmethod
    def _generate_policy(policy_type, tools):
        if policy_type == "STDRSL":
            return STDRSLCompilePolicy(tools)
        return None

    @staticmethod
    def _generate_tools(os, web):
        return {'os': os, 'web': web}

