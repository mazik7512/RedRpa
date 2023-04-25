from PySide2.QtCore import QRegExp
from PySide2.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


def formatting(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    if 'underline' in style:
        _format.setFontUnderline(True)
    return _format


# Синтаксические стили, которые могут использоваться
STYLES = {
    'special_instruction': formatting('blue', 'bold'),
    'operator': formatting('red', 'bold'),
    'body': formatting('Maroon', 'bold'),
    'function_definition': formatting('black', 'underline'),
    'object': formatting('DarkKhaki', 'bold'),
    'string': formatting('magenta'),
    'numbers': formatting('green', 'bold'),
    'sub_expr': formatting('violet', 'bold')
}


class RSLHighlighter(QSyntaxHighlighter):
    # RSL special instructions
    special_instructions = [
        'loop',
    ]

    # RSL operators
    operators = [
        '=',
    ]

    # RSL braces
    body = [
        '\\{', '\\}',
    ]

    sub_expr = [
        '\\(', '\\)'
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        self.tri_single = (QRegExp("'''"), 1, STYLES['string'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string'])

        rules = []


        # All other rules
        rules += [
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[a-z_A-Z0-9]+\b', 0, STYLES['object']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r'\b(function)\b', 0, STYLES['function_definition']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        rules += [(r'\b%s\b' % w, 0, STYLES['special_instruction'])
                  for w in RSLHighlighter.special_instructions]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in RSLHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['body'])
                  for b in RSLHighlighter.body]
        rules += [(r'%s' % b, 0, STYLES['sub_expr'])
                  for b in RSLHighlighter.sub_expr]

        # Создайте QRegExp для каждого шаблона
        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Применить выделение синтаксиса к данному блоку текста. """
        for expression, nth, _format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, _format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)
        # Многострочные строки
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add

            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False
