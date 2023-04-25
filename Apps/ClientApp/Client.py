import os
import sys
import PySide2
import PySide2.QtWidgets
from PySide2.QtCore import Qt
from Apps.ClientApp.ClientModel import ClientModel
from Apps.ClientApp.ClientMainView import Ui_MainWindow


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
        pass

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
