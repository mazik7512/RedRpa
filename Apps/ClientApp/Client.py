import os
import sys
import time
from multiprocessing import Process
from threading import Thread
from threading import Event

from PIL.ImageQt import ImageQt
from PySide2.QtCore import QEasingCurve, QSize
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QCompleter
import PySide2.QtWidgets
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt, QByteArray
from PySide2.QtWidgets import QTreeWidgetItem, QListWidgetItem
from PySide2.QtCore import QPropertyAnimation
from Apps.ClientApp.ClientModel import ClientModel
from Apps.ClientApp.ClientMainView import Ui_MainWindow
from Apps.ClientApp.SyntaxHighlighter import RSLHighlighter
from RRPA.Modules.Core.Exceptions.Exceptions import STDRedConnectionStopException, STDException
from RRPA.Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from RRPA.AppData.Configs.CompilerConfig import API_PATH
from Apps.ClientApp.CodeEditor import RSLEditor


CLIENT_STATES = ['Неактивно', 'Выполнение...', 'Ожидание...']
CLIENT_STATES_COLOR_SCHEMES = ["#currentStatus{\nbackground-color: red;\n color: white;\n }",
                               "#currentStatus{\nbackground-color: forestgreen;\n color: white;\n }",
                               "#currentStatus{\nbackground-color: navy;\n color: white;\n }"]


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

        self.__init_network()

        self.__init_threads()

        self.__init_resources()

        self.__init_settings()

    def __init_qt(self):
        dirname = os.path.dirname(PySide2.__file__)
        plugin_path = os.path.join(dirname, 'plugins', 'platforms')
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    def __init_qt_app(self):
        self._app = PySide2.QtWidgets.QApplication(sys.argv)
        self._app.setStyle('Fusion')
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
        self._client.refreshHostsButton.clicked.connect(self.__update_network_config)
        self._client.refreshPortButton.clicked.connect(self.__update_network_config)
        self._client.saveScenarioMenuOption.triggered.connect(self.__save_scenario_to_file)
        self._client.exitMenuOption.triggered.connect(self.__exit)
        self._client.startListenButton.clicked.connect(self.__start_serve)
        self._client.stopListenButton.clicked.connect(self.__stop_serving)

    def __init_editor(self):
        api_funcs = STDAPICollector(API_PATH)
        api_funcs.collect_all_api_methods()
        code_editor = RSLEditor(api_funcs.get_all_api_methods())
        editor_qss = self._client.scenarioEditor.styleSheet()
        editor_object_name = self._client.scenarioEditor.objectName()
        code_editor.setStyleSheet(editor_qss)
        code_editor.setObjectName(editor_object_name)
        self._client.scenarioLayout.removeWidget(self._client.scenarioEditor)
        self._client.scenarioEditor = code_editor
        self._client.scenarioLayout.addWidget(self._client.scenarioEditor)
        #self._highlighter = RSLHighlighter(self._client.scenarioEditor.document(), api_funcs.get_all_api_methods())

    def __init_app_model(self):
        self._model = ClientModel("127.0.0.1", 5553)

    def __init_app_info(self):
        client_path = os.getcwd() + "\\Apps\\ClientApp\\"
        _hash = self._model.hash_app(client_path)
        self._client.infoProgramHashLabel.setText(self._client.infoProgramHashLabel.text().format(_hash))
        self._client.infoProgramVersionLabel.setText(self._client.infoProgramVersionLabel.text().format("Rey", "1.0"))

    def __init_animations(self):
        self._slider = False

        self._start_panel_width = 82
        self._end_panel_width = 250

        self._start_button_width = 82
        self._end_button_width = 240

        self._slide_info_animation = QPropertyAnimation(self._client.infoPanel, QByteArray(b"minimumWidth"))
        self._slide_info_animation.setDuration(250)
        self._slide_info_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self._slide_button_animation = QPropertyAnimation(self._client.infoPanelButton, QByteArray(b"maximumWidth"))
        self._slide_button_animation.setDuration(250)
        self._slide_button_animation.setEasingCurve(QEasingCurve.InOutQuad)

    def __init_resources(self):
        self._error_icon = QIcon()
        self._info_icon = QIcon()
        self._error_icon.addFile(u":/TabIcons/icons/error-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self._info_icon.addFile(u":/TabIcons/icons/info-icon.png", QSize(), QIcon.Normal, QIcon.Off)

    def __init_network(self):
        self._host = "127.0.0.1"
        self._port = 5559
        self.__update_network_config()

    def __init_threads(self):
        self.__init_serve_thread()

    def __init_serve_thread(self):
        self._serving_thread = Thread(target=self.__serve_wrapper, daemon=True)

    def __init_settings(self):
        self.__init_hosts()

    def __init_hosts(self):
        hosts = self._model.get_ip_interfaces()
        for host in hosts:
            self._client.hostComboBox.addItem(host)

    def __slide_info_panel_start(self):
        self._slide_info_animation.setStartValue(self._start_panel_width)
        self._slide_info_animation.setEndValue(self._end_panel_width)
        self._client.infoPanel.setMaximumWidth(self._end_panel_width)
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
        self.__set_client_current_state(1)
        self._client.infoTabsWidget.setTabText(0, "Ошибки")
        self._client.errorsView.clear()
        self.__inactive_app()
        try:
            self._model.compile_and_execute(self._client.scenarioEditor.toPlainText())
            self.__add_info_to_info_panel(["Сценарий успешно выполнен."])
        except STDException as exception:
            self.__add_errors_to_info_panel(exception.get_exception_data())
        finally:
            self.__active_app()
            self.__set_client_current_state(0)

    def __open_scenario_from_file(self, s):
        file = self.__open_file()
        filename, _ = file
        text = self._model.load_scenario(filename)
        self._client.scenarioEditor.setPlainText(text)

    def __start_serve(self):
        self.__set_client_current_state(2)
        self.__init_serve_thread()
        self._serving_thread.start()

    def __serve_wrapper(self):
        self._model.start_client()
        while True:
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
        self.__end_thread(self._serving_thread)
        self.__set_client_current_state(0)

    def __end_thread(self, thread):
        if thread.is_alive():
            thread.join(1)

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
                #image = self._model.get_window_icon(elem)
                #if image:
                #    q_image = ImageQt(image)
                #    pixmap = QPixmap(q_image)
                #    icon = QIcon()
                #    icon.addPixmap(pixmap, QIcon.Normal, QIcon.State.Off)
                #    item.setIcon(0, icon)
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
        text_to_add = "CV_scan(\"{}\");\n".format(selected_items[0].text(0))
        self._client.scenarioEditor.setPlainText(text_to_add + self._client.scenarioEditor.toPlainText())

    def __active_app(self):
        self._form.window().setWindowOpacity(1.0)
        self._form.window().update()

    def __inactive_app(self):
        self._form.window().setWindowOpacity(0.8)
        self._form.window().update()

    def __slide_info_panel(self):
        if self._slider:
            self._client.infoPanelButton.setText("Показать")
            self._slider = False
        else:
            self._client.infoPanelButton.setText("Скрыть")
            self._slider = True
        self.__slide_info_panel_start()
        self.__slide_info_button_start()

    def __add_errors_to_info_panel(self, errors):
        self._client.infoTabsWidget.setTabText(0, "({}) Ошибки".format(len(errors)))
        for error in errors:
            item = QListWidgetItem(error)
            item.setIcon(self._error_icon)
            item.setToolTip(error)
            self._client.errorsView.addItem(item)

    def __add_info_to_info_panel(self, info_data):
        self._client.infoTabsWidget.setTabText(1, "({}) Информация".format(len(info_data)))
        for info in info_data:
            item = QListWidgetItem(info)
            item.setIcon(self._info_icon)
            item.setToolTip(info)
            self._client.infoView.addItem(item)

    def __update_network_config(self):
        self._host = self._client.hostComboBox.currentText()
        self._port = int(self._client.portNumberSpinBox.text())
        self._model.refresh_client_data(self._host, self._port)

    def __save_scenario_to_file(self):
        save_file = QFileDialog.getSaveFileName(self._form, "Сохранить сценарий",
                                                os.getcwd(), "RSL-сценарий (*.rsl *.scenario *.txt)")
        filename, _ = save_file
        if filename:
            self._model.save_to_file(filename, self._client.scenarioEditor.toPlainText())

    def __exit(self):
        self.__close_all_threads()
        sys.exit(0)

    def __close_all_threads(self):
        self.__end_thread(self._serving_thread)

    def __set_client_current_state(self, index):
        self._client.currentStatus.setText(CLIENT_STATES[index])
        self._client.currentStatus.setStyleSheet(CLIENT_STATES_COLOR_SCHEMES[index])
