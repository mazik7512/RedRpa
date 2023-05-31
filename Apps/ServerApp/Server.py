import datetime
import os
import sys
from threading import Thread
import PySide2.QtWidgets
from PIL.ImageQt import ImageQt
from PySide2.QtCore import QEasingCurve, QSize, QEvent
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtCore import Qt, QByteArray
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QTreeWidgetItem, QListWidgetItem
from PySide2.QtWidgets import QMdiSubWindow, QWidget
from Apps.ServerApp.ServerMainView import Ui_MainWindow
from Apps.ServerApp.ServerModel import ServerModel
from Apps.ClientApp.CodeEditor import RSLEditor
from RRPA.AppData.Configs.CompilerConfig import API_PATH
from RRPA.Modules.Core.Exceptions.Exceptions import STDRedConnectionStopException, STDException
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from Apps.ServerApp.client_window import Ui_ClientWindow


CLIENT_STATES = ['Выполнение...', 'Ожидание...']
CLIENT_STATES_COLOR_SCHEMES = ["background-color: green;color: black;border: 1px solid black;border-radius: 10px;",
                               "background-color: #87CEEB;color: black;border: 1px solid black;border-radius: 10px;"]


class ServerApp:
    _info_count = 0
    _current_host = "127.0.0.1"
    _current_port = 5551
    clients_count = 1
    api_collector = STDAPICollector(API_PATH)

    def __init__(self):
        self.__init_qt()
        self.__init_qt_app()

        self.__init_app_model()
        self.__init_app_info()

        self.__init_slots_and_signals()

        self.__init_editor()
        self.__init_windows_list()

        self.__init_animations()

        self.__init_resources()

        self.__init_clients_windows()

    def __init_qt(self):
        dirname = os.path.dirname(PySide2.__file__)
        plugin_path = os.path.join(dirname, 'plugins', 'platforms')
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    def __init_qt_app(self):
        self._app = PySide2.QtWidgets.QApplication(sys.argv)
        self._app.setStyle('Fusion')
        self._form = PySide2.QtWidgets.QMainWindow()
        self._server = Ui_MainWindow(self._form)
        self._form.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint |
                                  Qt.WindowMinimizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    def __init_slots_and_signals(self):
        self._server.startScenarioButton.clicked.connect(self.__execute_scenario)
        self._server.loadScenarioButton.triggered.connect(self.__open_scenario_from_file)
        self._server.refreshWindowsListButton.clicked.connect(self.__refresh_windows_list)
        self._server.windowsListView.itemPressed.connect(self.__window_click)
        self._server.showButton.clicked.connect(self.__slide_info_panel)
        self._server.saveScenarioButton.triggered.connect(self.__save_scenario_to_file)
        self._server.exitButton.triggered.connect(self.__exit)
        self._server.showBottomButton.clicked.connect(self.__slide_bottom_panel)
        self._server.addClientButton.triggered.connect(self.__create_client_window)

    def __init_editor(self):
        self.api_collector.collect_all_api_methods()
        code_editor = self.__create_rsl_editor()
        old = self._server.codeLayout.takeAt(1)
        old.widget().deleteLater()
        self._server.codeLayout.removeWidget(self._server.codeEditor)
        self._server.codeEditor = code_editor
        self._server.codeLayout.addWidget(self._server.codeEditor)
        # self._highlighter = RSLHighlighter(self._client.scenarioEditor.document(), api_funcs.get_all_api_methods())

    def __create_rsl_editor(self):
        code_editor = RSLEditor(self.api_collector.get_all_api_methods())
        editor_qss = self._server.codeEditor.styleSheet()
        editor_object_name = self._server.codeEditor.objectName()
        code_editor.setStyleSheet(editor_qss)
        code_editor.setObjectName(editor_object_name)
        return code_editor

    def __init_app_model(self):
        self._model = ServerModel("127.0.0.1", 5551)

    def __init_app_info(self):
        server_path = os.getcwd() + "\\Apps\\ServerApp\\"
        _hash = self._model.hash_app(server_path)
        self._server.hashInfoLabel.setText(self._server.hashInfoLabel.text().format(_hash))

    def __init_clients_windows(self):
        for i in range(2):
            self.__create_client_window()

    def __init_animations(self):
        self._slider = False
        self._start_panel_width = 110
        self._end_panel_width = 300

        self._start_button_width = 95
        self._end_button_width = 285

        self._slide_info_animation = QPropertyAnimation(self._server.infoDataWidget, QByteArray(b"minimumWidth"))
        self._slide_info_animation.setDuration(250)
        self._slide_info_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self._slide_button_animation = QPropertyAnimation(self._server.showButton, QByteArray(b"maximumWidth"))
        self._slide_button_animation.setDuration(250)
        self._slide_button_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self._bottom_slider = False
        self._start_bottom_panel_height = 100
        self._end_bottom_panel_height = 620
        self._slide_bottom_animation = QPropertyAnimation(self._server.dataWidget, QByteArray(b"minimumHeight"))
        self._slide_bottom_animation.setDuration(350)
        self._slide_bottom_animation.setEasingCurve(QEasingCurve.InOutQuad)

    def __init_resources(self):
        self._error_icon = QIcon()
        self._info_icon = QIcon()
        self._error_icon.addFile(u":/TabIcons/icons/error-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self._info_icon.addFile(u":/TabIcons/icons/info-icon.png", QSize(), QIcon.Normal, QIcon.Off)

    def __slide_info_panel_start(self):
        self._slide_info_animation.setStartValue(self._start_panel_width)
        self._slide_info_animation.setEndValue(self._end_panel_width)
        self._server.infoDataWidget.setMaximumWidth(self._end_panel_width)
        temp = self._start_panel_width
        self._start_panel_width = self._end_panel_width
        self._end_panel_width = temp
        self._slide_info_animation.start()

    def __slide_info_button_start(self):
        self._slide_button_animation.setStartValue(self._start_button_width)
        self._slide_button_animation.setEndValue(self._end_button_width)
        temp = self._start_button_width
        self._start_button_width = self._end_button_width
        self._end_button_width = temp
        self._slide_button_animation.start()

    def start_app(self):
        self._form.show()
        ret = self._app.exec_()
        # sys.exit(ret)

    def __open_file(self):
        filepath = QFileDialog.getOpenFileName(None,
                                               "Открыть сценарий",
                                               os.getcwd(),
                                               "RSL-сценарий (*.rsl *.scenario *.txt)")
        return filepath

    def __execute_scenario(self):
        self.__set_client_current_state(0)
        self._server.infoErrosTabWidget.setTabText(1, "Ошибки")
        self._server.errorsView.clear()
        self.__inactive_app()
        try:
            self._model.compile_and_execute(self._server.codeEditor.toPlainText())
            self.__add_info_to_info_panel(["[{}] Сценарий успешно выполнен.".format(datetime.datetime.now())])
        except STDException as exception:
            self.__add_errors_to_info_panel(exception.get_exception_data())
        finally:
            self.__active_app()
            self.__set_client_current_state(1)

    def __open_scenario_from_file(self, s):
        file = self.__open_file()
        filename, _ = file
        text = self._model.load_scenario(filename)
        self._server.codeEditor.setPlainText(text)
        self.__set_scenario_to_clients()

    def __end_thread(self, thread):
        if thread.is_alive():
            thread.join(1)

    def __init_windows_list(self):
        self.__refresh_windows_list()

    def __refresh_windows_list(self):
        self._server.windowsListView.clear()
        windows = self._model.get_windows_list()
        self.__fill_windows_tree(windows)

    def __fill_windows_tree(self, _list: list):
        filtered_windows = []
        for elem in _list:
            win_name = self._model.get_window_name(elem)
            item = self.__window_filter(win_name, filtered_windows)
            if item:
                # self.__get_window_icon(item, elem)
                filtered_windows.append(win_name)
                self._server.windowsListView.addTopLevelItem(item)

    def __window_filter(self, win_name: str, filtered_windows):
        _filter = True if len(win_name) > 0 else False
        _filter = True if _filter and not win_name.startswith("_") else False
        _filter = True if _filter and win_name not in filtered_windows else False
        item = QTreeWidgetItem([win_name]) if _filter else None
        return item

    def __window_click(self):
        selected_items = self._server.windowsListView.selectedItems()
        text_to_add = "CV_scan(\"{}\");\n".format(selected_items[0].text(0))
        self._server.codeEditor.setPlainText(text_to_add + self._server.codeEditor.toPlainText())

    def __active_app(self):
        self._form.window().setWindowOpacity(1.0)
        self._form.window().update()

    def __inactive_app(self):
        self._form.window().setWindowOpacity(0.8)
        self._form.window().update()

    def __slide_info_panel(self):
        if self._slider:
            self._server.showButton.setText("Показать")
            self._slider = False
        else:
            self._server.showButton.setText("Скрыть")
            self._slider = True
        self.__slide_info_panel_start()
        self.__slide_info_button_start()

    def __slide_bottom_panel(self):
        if self._bottom_slider:
            self._server.showBottomButton.setText("Показать")
            self._bottom_slider = False
        else:
            self._server.showBottomButton.setText("Скрыть")
            self._bottom_slider = True
        self.__slide_bottom_panel_start()

    def __slide_bottom_panel_start(self):
        self._slide_bottom_animation.setStartValue(self._start_bottom_panel_height)
        self._slide_bottom_animation.setEndValue(self._end_bottom_panel_height)
        self._server.dataWidget.setMaximumHeight(self._end_bottom_panel_height)
        temp = self._start_bottom_panel_height
        self._start_bottom_panel_height = self._end_bottom_panel_height
        self._end_bottom_panel_height = temp
        self._slide_bottom_animation.start()

    def __add_errors_to_info_panel(self, errors):
        self._server.infoErrosTabWidget.setTabText(1, "({}) Ошибки".format(len(errors)))
        for error in errors:
            item = QListWidgetItem(error)
            item.setIcon(self._error_icon)
            item.setToolTip(error)
            self._server.errorsView.addItem(item)

    def __add_info_to_info_panel(self, info_data):
        self._info_count += len(info_data)
        self._server.infoErrosTabWidget.setTabText(0, "({}) Информация".format(self._info_count))
        for info in info_data:
            item = QListWidgetItem(info)
            item.setIcon(self._info_icon)
            item.setToolTip(info)
            self._server.infoView.addItem(item)

    def __save_scenario_to_file(self):
        save_file = QFileDialog.getSaveFileName(self._form, "Сохранить сценарий",
                                                os.getcwd(), "RSL-сценарий (*.rsl *.scenario *.txt)")
        filename, _ = save_file
        if filename:
            self._model.save_to_file(filename, self._server.codeEditor.toPlainText())

    def __exit(self):
        sys.exit(0)

    def __set_client_current_state(self, index):
        self._server.currentStatusLabel.setText(CLIENT_STATES[index])
        self._server.currentStatusLabel.setStyleSheet(CLIENT_STATES_COLOR_SCHEMES[index])

    def __create_client_window(self):
        code_editor = self.__create_rsl_editor()
        client = Ui_ClientWindow()
        old = client.codeLayout.takeAt(0)
        old.widget().deleteLater()
        client.codeLayout.removeWidget(client.codeEditor)
        client.codeEditor = code_editor
        client.codeLayout.addWidget(client.codeEditor)
        client.startConnectionButton.clicked.connect(self.__send_scenario_to_client)
        client.codeEditor.setPlainText(self._server.codeEditor.toPlainText())
        client.clientNameEdit.setText("Клиент №{}".format(self.clients_count))
        self.clients_count += 1
        self._server.clientsArea.addSubWindow(client)
        client.show()

    def __send_scenario_to_client(self):
        active_client = self._server.clientsArea.activeSubWindow()
        host = active_client.clientIPEdit.text()
        port = active_client.clientPortEdit.value()
        scenario = active_client.codeEditor.toPlainText()
        self.__add_info_to_info_panel(["Отправляю сценарий клиенту: ({}, {})".format(host, port)])
        self._model.send_scenario_to_client(host, port, scenario)

    def __set_scenario_to_clients(self):
        sub_windows = self._server.clientsArea.subWindowList()
        for sub in sub_windows:
            sub.codeEditor.setPlainText(self._server.codeEditor.toPlainText())
