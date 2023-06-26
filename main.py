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

def client_test(_client):
    _client.start()
    _client.serve()
    _client.end()


def server_test(_server):
    _server.start()
    message = 'CV_scan("Конфигурация"); click_on_object("Конфигурация", "Первая"); wait(1); click_on_object(' \
              '"Конфигурация", "Вторая"); wait(1); click_on_object("Конфигурация", "Третья"); wait(1); CV_scan(' \
              '"Конфигурация"); click_on_object("Конфигурация", "Справочник три"); wait(1); CV_scan("Конфигурация"); ' \
              'click_on_object("Конфигурация", "Создать"); wait(1); CV_scan("Справочник три (создание)"); input_text(' \
              '"Справочник три (создание)", "Наименование", "object for test"); wait(1); click_on_points("Справочник ' \
              'три (создание)", 80, 60); web_open("https://google.com", "g"); web_scan("g"); web_click("g",' \
              '"Почта"); web_close("g"); wait(1); CV_scan("data:, - Google Chrome"); wait(1); click_on_points("data:, ' \
              '- Google Chrome", 1000, 18); '
    _server.send_scenario(message)
    _server.end()


def server_start():
    server = ServerApp()
    server.start_app()


def client_start():
    client = ClientApp()
    client.start_app()


if __name__ == "__main__":

    server_start()
    #generator = STDManagerGenerator("127.0.0.1", 5551)
    #server = generator.generate_server()
    #client = generator.generate_client()
    #client_thread = threading.Thread(target=client_test, args=(client,))
    #server_thread = threading.Thread(target=server_test, args=(server,))
    #client_thread.start()
    #time.sleep(1)
    #server_thread.start()
    #client_thread.join()
    #server_thread.join()



