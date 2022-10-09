from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import fonts


# toolbar
def createToolBar(self):
    toolbar = QToolBar()
    toolbar.setObjectName("toolbar")
    # adding actions

    # undo action
    undoAction = QAction(QIcon("./icons/undo.png"), "Undo (Ctrl+Z)", self)
    undoAction.triggered.connect(self.editor.undo)
    undoAction.setShortcut("Ctrl+Z")
    toolbar.addAction(undoAction)

    # redo action
    redoAction = QAction(QIcon("./icons/redo.png"), "Redo (Ctrl+Y)", self)
    redoAction.triggered.connect(self.editor.redo)
    redoAction.setShortcut("Ctrl+Y")
    toolbar.addAction(redoAction)
    toolbar.addSeparator()
    toolbar.addSeparator()
    # cut action
    cutAction = QAction(QIcon("./icons/cut.png"), "Cut", self)
    cutAction.triggered.connect(self.editor.cut)
    toolbar.addAction(cutAction)

    # copy action
    copyAction = QAction(QIcon("./icons/copy.png"), "Copy", self)
    copyAction.triggered.connect(self.editor.copy)
    toolbar.addAction(copyAction)

    # paste action
    pasteAction = QAction(QIcon("./icons/paste.png"), "Paste", self)
    pasteAction.triggered.connect(self.editor.paste)
    toolbar.addAction(pasteAction)
    toolbar.addSeparator()
    toolbar.addSeparator()

    # setting fontfamily box
    self.fontFamilyBox.addItems(fonts.fonts)
    self.fontFamilyBox.activated.connect(self.setFontFamily)
    toolbar.addWidget(self.fontFamilyBox)

    toolbar.addSeparator()
    toolbar.addSeparator()

    # setting fontsize box
    self.fontSizeBox.setValue(14)
    self.fontSizeBox.valueChanged.connect(self.setFontSize)
    toolbar.addWidget(self.fontSizeBox)

    toolbar.addSeparator()
    toolbar.addSeparator()

    # boldFont action
    boldFontAction = QAction(
        QIcon("./icons/bold.png"), "Bold", self)
    boldFontAction.triggered.connect(self.setFontBold)
    toolbar.addAction(boldFontAction)

    # italicFont action
    italicFontAction = QAction(
        QIcon("./icons/italic.png"), "Italic", self)
    italicFontAction.triggered.connect(self.setFontitalic)
    toolbar.addAction(italicFontAction)

    # underlineFont action
    underlineFontAction = QAction(
        QIcon("./icons/underline.png"), "Underline", self)
    underlineFontAction.triggered.connect(self.setFontunderline)
    toolbar.addAction(underlineFontAction)

    toolbar.addSeparator()
    toolbar.addSeparator()

    # lefttext action
    leftTextAction = QAction(
        QIcon("./icons/left-align.png"), "Align left", self)
    leftTextAction.triggered.connect(self.setTextAlignLeft)
    toolbar.addAction(leftTextAction)

    # centertext action
    centerTextAction = QAction(
        QIcon("./icons/center-align.png"), "Align Center", self)
    centerTextAction.triggered.connect(self.setTextAlignCenter)
    toolbar.addAction(centerTextAction)

    
    # righttext action
    rightTextAction = QAction(
        QIcon("./icons/right-align.png"), "Align right", self)
    rightTextAction.triggered.connect(self.setTextAlignRight)
    toolbar.addAction(rightTextAction)

    toolbar.addSeparator()
    toolbar.addSeparator()

    # setting theme box
    self.themeBox.addItems(["Default","Hacker","Monokai","Dracula"])
    self.themeBox.activated.connect(self.setTheme)
    toolbar.addWidget(self.themeBox)

    toolbar.addSeparator()
    toolbar.addSeparator()

    # clear all action
    clearAction = QAction(
        QIcon("./icons/clear.png"), "Clear All", self)
    clearAction.triggered.connect(self.editor.clear)
    toolbar.addAction(clearAction)

    self.addToolBar(toolbar)
