import inspect
import os
import pathlib
import sys
import threading
import time

import PySide2
from PySide2.QtCore import Qt
import PySide2.QtWidgets

from Apps.ClientApp.Client import ClientApp
from Apps.ClientApp.ClientMainView import Ui_MainWindow
from RRPA.Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator
from RRPA.Modules.Core.SDK.RedVirtualMachine.RVM import STDRedVirtualMachine
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioLexicalAnalyzer.Lexer import STDRSLLexer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioSyntaxAnalyzer.Parser import STDRSLSyntaxParser
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTranslator.Translator import STDRSLTranslator
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.AppData.Configs.CoreConfig import LOGS_PATH
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioNameBounder.NameBounder import STDRSLNameBounder
from RRPA.Modules.Core.SDK.ScenarioCompiler.CompilerGenerator import STDRSLCompilerGenerator
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Windows.Manager.OSTools import STDOSTools


def client_test(_client):
    _client.start()
    _client.serve()
    _client.end()


def server_test(_server):
    _server.start()
    message = "test"
    _server.send_scenario(message)
    _server.end()


if __name__ == "__main__":

    client = ClientApp()
    client.start_app()

    log_file = LOGS_PATH + "logs.txt"
    Logger.add_output_file(log_file)
    Logger.success("Приложение запущено")
    """
    hWnd_list = []
    windows = win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    #for wnd in hWnd_list:
        #text = win32gui.GetWindowText(wnd)
        #print(text)

    wnd = win32gui.FindWindow(None, "Новости - Google Chrome") #RedRPA – main.py Список друзей
    win32gui.SetForegroundWindow(wnd)
    win32gui.SetActiveWindow(wnd)
    #print(wnd)
    window = Window(wnd)
    ObjectActionizer.click(wnd, TemplateDescriptor([0, 30, 0, 30]))
    od = TFObjectDetector(MODEL_PATH)
    tm = OpenCVTemplateMatcher()
    of = ObjFinder(tm, od)
    wm = WindowManager(window, of)
    wm.scan_for_objects()
    #Actionizer.move(wnd, TemplateDescriptor([sv0, 30, sv0, 30]))
    """

    generator = STDManagerGenerator("127.0.0.1", 5551)
    server = generator.generate_server()
    client = generator.generate_client()
    client_thread = threading.Thread(target=client_test, args=(client,))
    server_thread = threading.Thread(target=server_test, args=(server,))
    client_thread.start()
    time.sleep(1)
    server_thread.start()
    client_thread.join()
    server_thread.join()

    #scenario = "c=5; function \ntest_func(a, b){ \nreturn(a); }loop(5){ click(\"accept\"); " \
               #"hover(1234.5); }" \
               #"user_object = test(3, 4); test_func(1,\n2);\n \n"
    #scenario = "a = b = test(test_func()); function test(d){ return(\"test\");}loop(c){click(a,b);" \
               #"hover(b, func_1());} test(d);"
    #scenario = "test(a, b, c, test(test()));"
    #scenario = "loop(get_number(inner())){test(\"ss\"); a=test(); a=5; a=b; }"
    #scenario = "test(a, b, test(test()), d); a=test(test(test()), test(), 123); d=1; a=d; d=a; test(); b=test(); a=b=test();" # работает
    #scenario = "a=x=test();" # работает
    #scenario = "loop(a){ loop(5){test();} test(test(test()), test()); test(); a=test(); } a=test();"
    scenario = "b=z=2;function test(){ a=5; test();} loop(a){ loop(5){test();} test(test(test()), test()); test(); q=z=test(); } a=test();"
    scenario = "function inner_loop(a, b){ a = b = 5; } loop(5){} CV_scan(get_window(get_name()), \"button\"); click_on_object(); loop(a){ loop(b){ inner_loop(); inner_loop_1(); } outer_loop_1(); outer_loop2(); } outside_loop();"
    lexer = STDRSLLexer(scenario)
    lexems = lexer.get_token_list().get_data()
    parser = STDRSLSyntaxParser(lexems)
    for lex in lexems:
        print(lex)
    res = parser.generate_ast().get_data()
    res.traverse("preorder", print)
    api_names = STDAPICollector("RRPA\\Modules\\Core\\SDK\\ScenarioAPI\\")
    STDAPICollector.collect_all_api_methods(api_names)
    linker = STDRSLNameBounder(res, api_names, STDOSTools)
    print(*linker.link_names().get_data())
    translator = STDRSLTranslator(res)
    print(translator.translate().get_data())
    compiler = STDRSLCompilerGenerator.generate_compiler(STDOSTools)
    rex = compiler.compile(scenario)
    with open("scenario.rex", "w+") as red_executable:
        red_executable.write(rex.deserialize())
    load_rex = STDRedExecutable()
    with open("scenario.rex", "r") as red_executable:
        load_rex.serialize(red_executable.read())
    print("loaded_rex\n", load_rex)
    rvm = STDRedVirtualMachine()
    rvm.execute(rex)

    #node = res.get_next()
    #while node:
    #    print(node)
    #    node = res.get_next()


