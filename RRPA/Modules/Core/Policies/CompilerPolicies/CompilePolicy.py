from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.CompilePolicy import AbstractCompilePolicy
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioLexicalAnalyzer.Lexer import STDRSLLexer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioSyntaxAnalyzer.Parser import STDRSLSyntaxParser
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioNameBounding.NameBounder import STDRSLNameBounder
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioSemanticAnalyzer.SemanticAnalyzer import STDRSLSemanticAnalyzer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTranslator.Translator import STDRSLTranslator
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioLogger.Logger import STDCompilerLogger
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.Modules.Core.SDK.ScenarioExecutable.ExecutableGenerator import STDREXGenerator
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Core.Policies.CompilerPolicies.CompileErrorsProcessingPolicy import STDCompileErrorsProcessingPolicy
from RRPA.AppData.Configs.CompilerConfig import LOGS_PATH
from RRPA.AppData.Configs.CompilerConfig import API_PATH


class STDRSLCompilePolicy(AbstractCompilePolicy):

    def __init__(self, utils):
        self._utils = utils
        compiler_buffer = self._generate_compiler_components()
        self._lexer = compiler_buffer['lexer']
        self._parser = compiler_buffer['parser']
        self._name_bounder = compiler_buffer['name_bounder']
        self._semantic = compiler_buffer['semantic']
        self._translator = compiler_buffer['translator']
        self._api_collector = compiler_buffer['api_collector']

    def _compile(self, scenario):
        tokens = self._lex_analyze(scenario + '\n')
        ast = self._syntax_analyze(tokens)
        self._collect_apis()
        self._semantic_analyze(ast)
        import_data, init_data = self._name_bounding(ast)
        user_code_data = self._translate(ast)
        return import_data, init_data, user_code_data

    def compile(self, scenario):
        import_data, init_data, user_code_data = self._compile(scenario)
        return {'import': import_data, 'init': init_data, 'user_code': user_code_data}

    def _lex_analyze(self, scenario):
        self._lexer.set_data(scenario)
        lex_result = self._lexer.get_token_list()
        STDCompileErrorsProcessingPolicy.process_errors("lex", lex_result.get_errors())
        return lex_result.get_data()

    def _syntax_analyze(self, tokens):
        self._parser.set_tokens(tokens)
        syntax_result = self._parser.generate_ast()
        STDCompileErrorsProcessingPolicy.process_errors("syntax", syntax_result.get_errors())
        return syntax_result.get_data()

    def _name_bounding(self, ast):
        self._name_bounder.set_ast(ast)
        self._name_bounder.set_apis(self._api_collector)
        name_bounder_result = self._name_bounder.link_names()
        STDCompileErrorsProcessingPolicy.process_errors("name_bounding", name_bounder_result.get_errors())
        return name_bounder_result.get_data()

    def _collect_apis(self):
        self._api_collector.collect_all_api_methods()

    def _semantic_analyze(self, ast):
        self._semantic.set_ast(ast)
        self._semantic.set_stdlib(self._api_collector)
        semantic_result = self._semantic.analyze()
        STDCompileErrorsProcessingPolicy.process_errors("semantic", semantic_result.get_errors())

    def _translate(self, ast):
        self._translator.set_data(ast)
        translator_result = self._translator.translate()
        STDCompileErrorsProcessingPolicy.process_errors("translation", translator_result.get_errors())
        return translator_result.get_data()

    def _generate_compiler_components(self):
        components = {}
        logger = STDCompilerLogger(LOGS_PATH)
        components['logger'] = logger
        components['lexer'] = STDRSLLexer(logger=logger)
        components['parser'] = STDRSLSyntaxParser(logger=logger)
        components['name_bounder'] = STDRSLNameBounder(tools=self._utils, logger=logger)
        components['semantic'] = STDRSLSemanticAnalyzer(logger=logger)
        components['translator'] = STDRSLTranslator(logger=logger)
        components['api_collector'] = STDAPICollector(API_PATH, logger=logger)
        return components
