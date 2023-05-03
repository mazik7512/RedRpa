from PySide2 import QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QCompleter, QPlainTextEdit
from Apps.ClientApp.SyntaxHighlighter import RSLHighlighter


class RSLEditor(QPlainTextEdit):

    def __init__(self, keywords):
        super().__init__()
        _keywords = ['loop', 'return']
        completer = QCompleter(_keywords + keywords)
        completer.activated.connect(self.insert_completion)
        completer.setWidget(self)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.popup().setStyleSheet("font-size: 14px;background-color: black; color: aliceblue;"
                                        "")
        self._completer = completer
        self.textChanged.connect(self.complete)
        self._highlighter = RSLHighlighter(self.document(), keywords)

    def insert_completion(self, completion):
        tc = self.textCursor()
        extra = len(completion) - len(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.MoveOperation.Left)
        tc.movePosition(QTextCursor.MoveOperation.EndOfWord)
        tc.insertText(completion[-extra:] + " ")
        self.setTextCursor(tc)

    @property
    def text_under_cursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.SelectionType.WordUnderCursor)
        return tc.selectedText()

    def complete(self):
        prefix = self.text_under_cursor
        self._completer.setCompletionPrefix(prefix)
        popup = self._completer.popup()
        cr = self.cursorRect()
        popup.setCurrentIndex(self._completer.completionModel().index(0, 0))
        cr.setWidth(
            self._completer.popup().sizeHintForColumn(0)
            + self._completer.popup().verticalScrollBar().sizeHint().width()
        )
        self._completer.complete(cr)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if self._completer.popup().isVisible() and event.key() in [
            Qt.Key.Key_Enter,
            Qt.Key.Key_Return,
            Qt.Key.Key_Up,
            Qt.Key.Key_Down,
            Qt.Key.Key_Tab,
            Qt.Key.Key_Backtab,
        ]:
            event.ignore()
            return
        super().keyPressEvent(event)
