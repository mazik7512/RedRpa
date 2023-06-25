import threading
import time

from Apps.ClientApp.Client import ClientApp
from Apps.ServerApp.Server import ServerApp
from RRPA.Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator
from RRPA.Modules.Core.SDK.RedVirtualMachine.RVM import STDRedVirtualMachine
from RRPA.Modules.Core.SDK.ScenarioAPI.WebAPI import STDWebAPI
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioLexicalAnalyzer.Lexer import STDRSLLexer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioSyntaxAnalyzer.Parser import STDRSLSyntaxParser
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTranslator.Translator import STDRSLTranslator
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.AppData.Configs.CoreConfig import LOGS_PATH
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioNameBounding.NameBounder import STDRSLNameBounder
from RRPA.Modules.Core.SDK.ScenarioCompiler.CompilerGenerator import STDRSLCompilerGenerator
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Web.Tools.WebTools import STDWebTools
from RRPA.Modules.Windows.Tools.OSTools import STDOSTools


def server_start():
    server = ServerApp()
    server.start_app()


def client_start():
    client = ClientApp()
    client.start_app()


if __name__ == "__main__":

    server_start()


