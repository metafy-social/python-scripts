""" Docx

author: Piyush Kumar
mail  : piyushprasad816@gmail.com

"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys
import os
import menubar
import toolbar
import themes



class PyTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # to add text widget
        self.editor = QTextEdit()
        self.editor.setObjectName("editor")
    

        # seting default font size
        self.editor.setFontPointSize(14)
        
        self.setCentralWidget(self.editor)
        # icon
        self.setWindowIcon(QIcon("./icons/icon.png"))
        # theme 
        self.setStyleSheet(themes.Default)
    
        # setting minimum size 
        self.setMinimumSize(1000, 800)

        # creating fontsize box
        self.fontSizeBox = QSpinBox()
        self.fontSizeBox.setToolTip("Font Size")

        # creating font family box
        self.fontFamilyBox = QComboBox()
        self.fontFamilyBox.setToolTip("Font Family")

        # creating theme box
        self.themeBox = QComboBox()
        self.themeBox.setToolTip("Editor Theme")

        # setting window title
        self.setWindowTitle("Untiteld - PyTextEditor")

        # toolbar
        toolbar.createToolBar(self)
        # menubar 
        menubar.createMenuBar(self)
        # filepath to save existing file 
        self.filepath = ""

    # font size
    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)

    # font family
    def setFontFamily(self):
        font = self.fontFamilyBox.currentText()
        self.editor.setFontFamily(font)

    # bold font
    def setFontBold(self):
        if self.editor.fontWeight() == 50:
            self.editor.setFontWeight(500)
        else:
            self.editor.setFontWeight(50)

    # italic font
    def setFontitalic(self):
        if self.editor.fontItalic():
            self.editor.setFontItalic(False)

        else:
            self.editor.setFontItalic(True)

    # underline font
    def setFontunderline(self):
        if self.editor.fontUnderline():
            self.editor.setFontUnderline(False)

        else:
            self.editor.setFontUnderline(True)

    # save file
    def saveFile(self):
        # check if file already exists just overwrite the file
        if self.filepath:
            with open(self.filepath, "w") as file:
                file.write(self.editor.toPlainText())
            return

        # if file not exists create new file 
        # asking for path to save
        filepath = QFileDialog.getSaveFileName(
            self, "Save File", "/", "*.txt")[0]
        try:
            # writting file
            with open(filepath, "w") as file:
                file.write(self.editor.toPlainText())
                # geting the filename form file path
            filename = os.path.basename(filepath)
            # setting window title to filename
            self.setWindowTitle(f"{filename} - PyTextEditor")
            self.filepath = filepath

        except:
            return

    # open file
    def openFile(self):
        # asking for file to open
        filepath = QFileDialog.getOpenFileName(
            self, "Open File", "/", "*.txt")[0]

        try:
            # reading file 
            with open(filepath) as file:
                fileData = file.read()
            # geting the filename form file path
            filename = os.path.basename(filepath)
            # setting window title to filename
            self.setWindowTitle(f"{filename} - PyTextEditor")
            # inserting file content to editor 
            self.editor.setText(fileData)
            # adding file path to check file exist or not when save the file 
            self.filepath = filepath

        except:
            return
    # new file 
    def newFile(self):
        self.setWindowTitle(f"Untiteld - PyTextEditor")
        self.editor.setText("")
        self.filepath = ""

    # align text center 
    def setTextAlignCenter(self):
        if self.editor.alignment() == Qt.AlignCenter:
            self.editor.setAlignment(Qt.AlignAbsolute)
        else:
            self.editor.setAlignment(Qt.AlignCenter)
    # align text left
    def setTextAlignLeft(self):
        if self.editor.alignment() == Qt.AlignLeft:
            self.editor.setAlignment(Qt.AlignAbsolute)
        else:
            self.editor.setAlignment(Qt.AlignLeft)

    # align text right 
    def setTextAlignRight(self):
        if self.editor.alignment() == Qt.AlignRight:
            self.editor.setAlignment(Qt.AlignAbsolute)
        else:
            self.editor.setAlignment(Qt.AlignRight)

    # theme 
    def setTheme(self):
        theme = self.themeBox.currentText()
    
        if theme == "Default":
            self.setStyleSheet(themes.Default)
        elif theme == "Monokai":
            self.setStyleSheet(themes.Monokai)
        elif theme == "Dracula":
            self.setStyleSheet(themes.Dracula)
        elif theme == "Hacker":
            self.setStyleSheet(themes.Hacker)

    def getPopup(self,mssg,icon,buttons):
        msg = QMessageBox()
        msg.setWindowTitle("PyTextEditor")
        msg.setText(mssg)
        msg.setIcon(icon)
        msg.setStandardButtons(buttons)
        msg.buttonClicked.connect(self.msgBtn)

        retval = msg.exec_()


    # rename file 
    def renameFile(self):
        if self.filepath:
            # geeting name 
            name, done = QInputDialog.getText(
             self, 'Rename file', 'Enter file name:') 

            if done:
                # replacing old name to new one 
                dst = str(self.filepath).replace(os.path.basename(self.filepath),f"{name}.txt")
                os.rename(self.filepath, dst)

                self.filepath = dst
                self.setWindowTitle(f"{os.path.basename(self.filepath)} - PyTextEditor")

        else:
            self.getPopup("Save file to rename",QMessageBox.Information,(QMessageBox.Save | QMessageBox.Cancel))


    def msgBtn(self,i):
        if i.text() == "Save":
            self.saveFile()




# application 
app = QApplication(sys.argv)
window = PyTextEditor()
window.show()
sys.exit(app.exec_())
