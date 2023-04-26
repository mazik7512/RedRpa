import os
import sys
import time
from PySide2.QtCore import QEasingCurve
from PySide2.QtWidgets import QFileDialog
import PySide2.QtWidgets
from PySide2.QtCore import Qt, QByteArray
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import QPropertyAnimation
from Apps.ClientApp.ClientModel import ClientModel
from Apps.ClientApp.ClientMainView import Ui_MainWindow
from Apps.ClientApp.SyntaxHighlighter import RSLHighlighter
from RRPA.Modules.Core.Exceptions.Exceptions import STDRedConnectionStopException, STDException
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.AppData.Configs.CompilerConfig import API_PATH


class ClientApp:
    def __init__(self):
        self.__init_qt()
        self.__init_qt_app()

        self.__init_app_model()
        self.__init_app_info()

        self.__init_slots_and_signals()

        self.__init_editor()
        self.__init_windows_list()

        self.__init_animations()

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
        self._client.startScenarionButton.clicked.connect(self.__execute_scenario)
        self._client.openScenarioMenuOption.triggered.connect(self.__open_scenario_from_file)
        self._client.refreshWindowsListButton.clicked.connect(self.__refresh_windows_list)
        self._client.windowsListView.itemPressed.connect(self.__window_click)
        self._client.infoPanelButton.clicked.connect(self.__slide_info_panel)

    def __init_editor(self):
        api_funcs = STDAPICollector(API_PATH)
        api_funcs.collect_all_api_methods()
        self._highlighter = RSLHighlighter(self._client.scenarioEditor.document(), api_funcs.get_all_api_methods())

    def __init_app_model(self):
        self._model = ClientModel("127.0.0.1", 5553)

    def __init_app_info(self):
        client_path = os.getcwd() + "\\Apps\\ClientApp\\"
        _hash = self._model.hash_app(client_path)
        self._client.infoProgramHashLabel.setText(self._client.infoProgramHashLabel.text().format(_hash))
        self._client.infoProgramVersionLabel.setText(self._client.infoProgramVersionLabel.text().format("Rey", "1.0"))

    def __init_animations(self):
        self._slider = False
        self._start_width = 82
        self._end_width = 250
        self._slide_info_animation = QPropertyAnimation(self._client.infoPanel, QByteArray(b"minimumWidth"))
        self._slide_info_animation.setDuration(250)
        self._slide_info_animation.setEasingCurve(QEasingCurve.InOutQuad)

    def __slide_info_panel_start(self):
        self._slide_info_animation.setStartValue(self._start_width)
        self._slide_info_animation.setEndValue(self._end_width)
        temp = self._start_width
        self._start_width = self._end_width
        self._end_width = temp
        self._slide_info_animation.start()


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
        self.__inactive_app()
        try:
            self._model.compile_and_execute(self._client.scenarioEditor.toPlainText())
        except STDException as exception:
            print(exception.get_exception_data())
        finally:
            self.__active_app()

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

    def __init_windows_list(self):
        self.__refresh_windows_list()

    def __refresh_windows_list(self):
        self._client.windowsListView.clear()
        windows = self._model.get_windows_list()
        self.__fill_windows_tree(windows)

    def __fill_windows_tree(self, _list: list):
        filtered_windows = []
        for elem in _list:
            win_name = self._model.get_window_name(elem)
            item = self.__window_filter(win_name, filtered_windows)
            if item:
                filtered_windows.append(win_name)
                self._client.windowsListView.addTopLevelItem(item)

    def __window_filter(self, win_name: str, filtered_windows):
        _filter = True if len(win_name) > 0 else False
        _filter = True if _filter and not win_name.startswith("_") else False
        _filter = True if _filter and win_name not in filtered_windows else False
        item = QTreeWidgetItem([win_name]) if _filter else None
        return item

    def __window_click(self):
        selected_items = self._client.windowsListView.selectedItems()
        print("selected items are ", [item.text(0) for item in selected_items])

    def __active_app(self):
        self._form.window().setWindowOpacity(1.0)
        self._form.window().update()

    def __inactive_app(self):
        self._form.window().setWindowOpacity(0.8)
        self._form.window().update()

    def __slide_info_panel(self):
        if self._slider:
            self._client.infoPanelButton.setText("Показать")
            self._client.infoPanelButton.setMaximumSize(80, 82)
            self._slider = False
        else:
            self._client.infoPanelButton.setText("Скрыть")
            self._client.infoPanelButton.setMaximumSize(240, 82)
            self._slider = True
        self.__slide_info_panel_start()
