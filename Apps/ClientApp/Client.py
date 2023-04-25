import os
import sys
from PySide2.QtWidgets import QFileDialog
import PySide2.QtWidgets
from PySide2.QtCore import Qt
from Apps.ClientApp.ClientModel import ClientModel
from Apps.ClientApp.ClientMainView import Ui_MainWindow
from Apps.ClientApp.SyntaxHighlighter import RSLHighlighter
from RRPA.Modules.Core.Exceptions.Exceptions import STDRedConnectionStopException
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.AppData.Configs.CompilerConfig import API_PATH


class ClientApp:

    def __init__(self):
        self.__init_qt()
        self.__init_qt_app()

        self.__init_app_model()
        self.__init_app_info()

        self.__init_slots_and_signals()

    def __init_qt(self):
        dirname = os.path.dirname(PySide2.__file__)
        plugin_path = os.path.join(dirname, 'plugins', 'platforms')
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    def __init_qt_app(self):
        self._app = PySide2.QtWidgets.QApplication(sys.argv)
        self._form = PySide2.QtWidgets.QMainWindow()
        self._client = Ui_MainWindow(self._form)
        self._form.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint |
                                  Qt.WindowMinimizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    def __init_slots_and_signals(self):
        api_funcs = STDAPICollector(API_PATH)
        api_funcs.collect_all_api_methods()
        self._highlighter = RSLHighlighter(self._client.scenarioEditor.document(), api_funcs.get_all_api_methods())
        self._client.startScenarionButton.clicked.connect(self.__execute_scenario)
        self._client.openScenarioMenuOption.triggered.connect(self.__open_scenario_from_file)

    def __init_app_model(self):
        self._model = ClientModel("127.0.0.1", 5553)

    def __init_app_info(self):
        client_path = os.getcwd() + "\\Apps\\ClientApp\\"
        _hash = self._model.hash_app(client_path)
        self._client.infoProgramHashLabel.setText(self._client.infoProgramHashLabel.text().format(_hash))
        self._client.infoProgramVersionLabel.setText(self._client.infoProgramVersionLabel.text().format("Rey", "1.0"))

    def start_app(self):
        self._form.show()
        ret = self._app.exec_()
        #sys.exit(ret)

    def __open_file(self):
        filepath = QFileDialog.getOpenFileName(None,
                                               "Открыть сценарий",
                                               os.getcwd(),
                                               "RSL-сценарий (*.rsl *.scenario *.txt)")
        return filepath

    def __execute_scenario(self):
        self._model.compile_and_execute(self._client.scenarioEditor.toPlainText())

    def __open_scenario_from_file(self, s):
        file = self.__open_file()
        filename, _ = file
        text = self._model.load_scenario(filename)
        self._client.scenarioEditor.setPlainText(text)

    def __start_serve(self):
        while True:
            data = ""
            try:
                data = self._model.serve_for_commands()
            except STDRedConnectionStopException:
                self.__stop_serving()
                return None
            self.__serve_loop(data)

    def __serve_loop(self, scenario):
        self._client.scenarioEditor.setPlainText(scenario)
        self.__execute_scenario()

    def __stop_serving(self):
        self._model.end_client()
