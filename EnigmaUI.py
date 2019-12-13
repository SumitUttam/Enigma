#Enigma Simulator By Sumit Uttam

from PyQt5 import QtCore, QtGui, QtWidgets
from enigma import *
alphabet=range(0,26)

class Ui_EnigmaUI(object):
    def setupUi(self, EnigmaUI):
        EnigmaUI.setObjectName("EnigmaUI")
        EnigmaUI.setEnabled(True)
        EnigmaUI.resize(640, 489)
        self.tabWidget = QtWidgets.QTabWidget(EnigmaUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 490))
        self.tabWidget.setObjectName("tabWidget")
        self.MainWindow = QtWidgets.QWidget()
        self.MainWindow.setObjectName("MainWindow")
        self.inputB = QtWidgets.QTextEdit(self.MainWindow)
        self.inputB.setGeometry(QtCore.QRect(20, 40, 471, 151))
        self.inputB.setObjectName("inputB")
        self.inputB.setAcceptRichText(False)
        self.outputB = QtWidgets.QTextBrowser(self.MainWindow)
        self.outputB.setGeometry(QtCore.QRect(20, 250, 471, 181))
        self.outputB.setObjectName("outputB")
        self.EnterB = QtWidgets.QPushButton(self.MainWindow)
        self.EnterB.setGeometry(QtCore.QRect(510, 330, 91, 91))
        self.EnterB.setObjectName("EnterB")
        self.iPFile = QtWidgets.QPushButton(self.MainWindow)
        self.iPFile.setGeometry(QtCore.QRect(510, 40, 91, 31))
        self.iPFile.setObjectName("iPFile")
        self.oPFile = QtWidgets.QPushButton(self.MainWindow)
        self.oPFile.setGeometry(QtCore.QRect(510, 250, 91, 32))
        self.oPFile.setObjectName("oPFile")
        self.enterTextL = QtWidgets.QLabel(self.MainWindow)
        self.enterTextL.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.enterTextL.setObjectName("enterTextL")
        self.ProTextL = QtWidgets.QLabel(self.MainWindow)
        self.ProTextL.setGeometry(QtCore.QRect(20, 230, 111, 16))
        self.ProTextL.setObjectName("ProTextL")
        self.tabWidget.addTab(self.MainWindow, "")
        self.Settings = QtWidgets.QWidget()

        self.Settings.setObjectName("Settings")
        self.checkSettings = QtWidgets.QPushButton(self.Settings)
        self.checkSettings.setGeometry(QtCore.QRect(510, 330, 91, 91))
        self.checkSettings.setObjectName("checkSettings")
        self.saveSettings = QtWidgets.QPushButton(self.Settings)
        self.saveSettings.setGeometry(QtCore.QRect(20, 330, 91, 91))
        self.saveSettings.setObjectName("saveSettings")
        self.loadSettings = QtWidgets.QPushButton(self.Settings)
        self.loadSettings.setGeometry(QtCore.QRect(240, 330, 91, 91))
        self.loadSettings.setObjectName("loadSettings")
        self.r1Pattern = QtWidgets.QLineEdit(self.Settings)
        self.r1Pattern.setGeometry(QtCore.QRect(230, 20, 301, 20))
        self.r1Pattern.setMaxLength(26)
        self.r1Pattern.setObjectName("r1Pattern")
        self.r2Pattern = QtWidgets.QLineEdit(self.Settings)
        self.r2Pattern.setGeometry(QtCore.QRect(230, 50, 301, 20))
        self.r2Pattern.setMaxLength(26)
        self.r2Pattern.setObjectName("r2Pattern")
        self.r3Pattern = QtWidgets.QLineEdit(self.Settings)
        self.r3Pattern.setGeometry(QtCore.QRect(230, 80, 301, 20))
        self.r3Pattern.setMaxLength(26)
        self.r3Pattern.setObjectName("r3Pattern")
        self.r1Spin = QtWidgets.QSpinBox(self.Settings)
        self.r1Spin.setGeometry(QtCore.QRect(200, 180, 42, 22))
        self.r1Spin.setMinimum(1)
        self.r1Spin.setMaximum(26)
        self.r1Spin.setObjectName("r1Spin")
        self.r2Spin = QtWidgets.QSpinBox(self.Settings)
        self.r2Spin.setGeometry(QtCore.QRect(340, 180, 42, 22))
        self.r2Spin.setMinimum(1)
        self.r2Spin.setMaximum(26)
        self.r2Spin.setObjectName("r2Spin")
        self.r3Spin = QtWidgets.QSpinBox(self.Settings)
        self.r3Spin.setGeometry(QtCore.QRect(460, 180, 42, 22))
        self.r3Spin.setMinimum(1)
        self.r3Spin.setMaximum(26)
        self.r3Spin.setObjectName("r3Spin")
        self.error = QtWidgets.QLabel(self.MainWindow)
        self.error.setGeometry(QtCore.QRect(20, 440, 591, 16))
        self.error.setObjectName("error")
        self.Error = QtWidgets.QLabel(self.Settings)
        self.Error.setGeometry(QtCore.QRect(20, 440, 591, 16))
        self.Error.setObjectName("Error")
        self.r1P = QtWidgets.QLabel(self.Settings)
        self.r1P.setGeometry(QtCore.QRect(120, 20, 91, 16))
        self.r1P.setObjectName("r1P")
        self.r2P = QtWidgets.QLabel(self.Settings)
        self.r2P.setGeometry(QtCore.QRect(120, 50, 81, 16))
        self.r2P.setObjectName("r2P")
        self.r3 = QtWidgets.QLabel(self.Settings)
        self.r3.setGeometry(QtCore.QRect(460, 160, 101, 16))
        self.r3.setObjectName("r3")
        self.r2 = QtWidgets.QLabel(self.Settings)
        self.r2.setGeometry(QtCore.QRect(340, 160, 81, 16))
        self.r2.setObjectName("r2")
        self.r1 = QtWidgets.QLabel(self.Settings)
        self.r1.setGeometry(QtCore.QRect(200, 160, 47, 13))
        self.r1.setObjectName("r1")
        self.r3P = QtWidgets.QLabel(self.Settings)
        self.r3P.setGeometry(QtCore.QRect(120, 80, 91, 16))
        self.r3P.setObjectName("r3P")
        self.rPattern = QtWidgets.QComboBox(self.Settings)
        self.rPattern.setGeometry(QtCore.QRect(230, 110, 301, 22))
        self.rPattern.setObjectName("rPattern")
        self.rPattern.addItem("")
        self.rPattern.addItem("WCBVUMHGZXYNFLPOTSRQEDAJKI")
        self.rPattern.addItem("OZHMPWICGULKDSAEXYNVJTFQRB")
        self.rPattern.addItem("EQOLAMKRPSGDFUCIBHJYNWVZTX")
        self.rPattern.addItem("NKXPYQSLOWBHRAIDFMGZVUJCET")
        self.rPattern.addItem("YMZPORTSWKJVBQEDNFHGXLIUAC")
        self.rPattern.addItem("ZUPXGIEJFHQRNMTCKLYOBWVDSA")
        self.rPattern.addItem("NXPWUHTFRSZYQAVCMIJGEODBLK")
        self.rPattern.addItem("FNUITAPZDXWMLBSGVYOECQKJRH")
        self.rPattern.addItem("HIXKJYWABEDSZTQROPLNVUGCFM")
        self.rPattern.addItem("FJKIYAQMDBCOHVLTGUWPRNSZEX")
        self.rPattern.addItem("QUVHMJIDGFNPEKYLATZRBCXWOS")
        self.rPattern.setDuplicatesEnabled(False)
        self.rP = QtWidgets.QLabel(self.Settings)
        self.rP.setGeometry(QtCore.QRect(120, 110, 91, 16))
        self.rP.setObjectName("rP")
        self.tabWidget.addTab(self.Settings, "")
        self.Rotors=[]
        self.retranslateUi(EnigmaUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(EnigmaUI)
        self.initEnigmaMachine()
        self.EnterB.clicked.connect(self.Encrypt)
        self.checkSettings.clicked.connect(self.checkSetting)
        self.saveSettings.clicked.connect(self.storeSetting)
        self.loadSettings.clicked.connect(self.LoadSetting)
        self.iPFile.clicked.connect(self.inputFromFile)
        self.oPFile.clicked.connect(self.outputToFile)
        self.proccessedText=str()


    def retranslateUi(self, EnigmaUI):
        _translate = QtCore.QCoreApplication.translate
        EnigmaUI.setWindowTitle(_translate("EnigmaUI", "Enigma Simulator"))
        self.EnterB.setText(_translate("EnigmaUI", "Process Text"))
        self.iPFile.setText(_translate("EnigmaUI", "Input File"))
        self.oPFile.setText(_translate("EnigmaUI", "Download File"))
        self.checkSettings.setText(_translate("EnigmaUI", "Check Settings"))
        self.saveSettings.setText(_translate("EnigmaUI", "Save Settings"))
        self.loadSettings.setText(_translate("EnigmaUI", "Load Settings"))
        self.enterTextL.setText(_translate("EnigmaUI", "Enter Text"))
        self.ProTextL.setText(_translate("EnigmaUI", "Processed Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainWindow), _translate("EnigmaUI", "Enigma"))
        self.r1Pattern.setText(_translate("EnigmaUI", "ESOVPZJAYQUIRHXLNFTGKDCMWB"))
        self.r2Pattern.setText(_translate("EnigmaUI", "AJDKSIRUXBLHWTMCQGZNPYFVOE"))
        self.r3Pattern.setText("QWERTYUIOPASDFGHJKLZXCVBNM")
        self.r1P.setText(_translate("EnigmaUI", "Rotor 1 Pattern"))
        self.error.setText(_translate("EnigmaUI", "Enigma Simulator by Sumit"))
        self.Error.setText(_translate("EnigmaUI", "Enigma Simulator by Sumit"))
        self.r2P.setText(_translate("EnigmaUI", "Rotor 2 Pattern"))
        self.error.setText(_translate("EnigmaUI", ""))
        self.r3.setText(_translate("EnigmaUI", "Rotor 3 "))
        self.r2.setText(_translate("EnigmaUI", "Rotor 2"))
        self.r1.setText(_translate("EnigmaUI", "Rotor 1"))
        self.r3P.setText(_translate("EnigmaUI", "Rotor 3 Pattern"))
        self.rPattern.setItemText(0, _translate("EnigmaUI", "YRUHQSLDPXNGOKMIEBFZCWVJAT"))
        self.rP.setText(_translate("EnigmaUI", "Reflector Pattern"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("EnigmaUI", "Settings"))


    def initEnigmaMachine(self):
        self.Rotors=[]
        Rotor=[]
        for i in self.r1Pattern.text().upper():
            if ord(i)-65 in alphabet and ord(i)-65 not in Rotor:
                Rotor.append(ord(i)-65)
            else:
                self.showError(1)
                return False
        self.Rotors.append(shift(Rotor,self.r1Spin.value()))
        Rotor=[]
        for i in self.r2Pattern.text().upper():
            if ord(i)-65 in alphabet and ord(i)-65 not in Rotor:
                Rotor.append(ord(i)-65)
            else:
                self.showError(2)
                return False
        self.Rotors.append(shift(Rotor,self.r2Spin.value()))
        Rotor=[]
        for i in self.r3Pattern.text().upper():
            if ord(i)-65 in alphabet and ord(i)-65 not in Rotor:
                Rotor.append(ord(i)-65)
            else:
                self.showError(3)
                return False
        self.Rotors.append(shift(Rotor,self.r3Spin.value()))
        Rotor=[]
        for i in self.rPattern.currentText().upper():
            if ord(i)-65 in alphabet and ord(i)-65 not in Rotor:
                Rotor.append(ord(i)-65)
            else:
                self.showError(4)
                return False
        self.Rotors.append(Rotor)
        return True

    def showError (self,Error):
        if Error==1:
            self.error.setText("Error:Rotor 1 Pattern not defined correctly")
            self.Error.setText("Error:Rotor 1 Pattern not defined correctly")
            return
        elif Error==2:
            self.error.setText("Error:Rotor 2 Pattern not defined correctly")
            self.Error.setText("Error:Rotor 2 Pattern not defined correctly")
            return
        elif Error==3:
            self.error.setText("Error:Rotor 3 Pattern not defined correctly")
            self.Error.setText("Error:Rotor 3 Pattern not defined correctly")
            return
        elif Error==4:
            self.error.setText("Error:Reflector Patterns not defined correctly")
            self.Error.setText("Error:Reflector Patterns not defined correctly")
            return
        elif Error==5:
            self.error.setText("Text Proccessed")
            return
        elif Error==6:
            self.Error.setText("Everything seems fine")
            return


    def Encrypt (self):
        if self.initEnigmaMachine():
            Machine = enigma(3 ,True , self.Rotors)
            self.proccessedText=Machine.encode(self.inputB.toPlainText())
            self.outputB.setText(self.proccessedText)
            self.showError(5)
            return
        else:
            return

    def inputFromFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName:
            self.inputB.setText(open(fileName).read())
            self.error.setText("File Loaded")

    def outputToFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName()
        if fileName:
            open(fileName,"w").write(self.proccessedText)
            self.error.setText("File Saved")

    def checkSetting (self):
        if self.initEnigmaMachine():
            self.showError(6)

    def storeSetting(self):
        if self.initEnigmaMachine():
            open("settings","w")
            settingsFile = open("settings","a")
            settingsFile.write(self.r1Pattern.text()+"\n")
            settingsFile.write(self.r2Pattern.text()+"\n")
            settingsFile.write(self.r3Pattern.text()+"\n")
            settingsFile.write(str(self.rPattern.currentIndex())+"\n")
            settingsFile.write(str(self.r1Spin.value())+"\n")
            settingsFile.write(str(self.r2Spin.value())+"\n")
            settingsFile.write(str(self.r3Spin.value())+"\n")
            settingsFile.close()
            self.Error.setText("Settings Stored")
            

    def LoadSetting (self):
        try:
            settingsFile = open("settings")
        except:
            self.Error.setText("Error: settings file do not exsist")
            return
        self.r1Pattern.setText(settingsFile.readline())
        self.r2Pattern.setText(settingsFile.readline())
        self.r3Pattern.setText(settingsFile.readline())
        self.rPattern.setCurrentIndex(int(settingsFile.readline()))
        self.r1Spin.setValue(int(settingsFile.readline()))
        self.r2Spin.setValue(int(settingsFile.readline()))
        self.r3Spin.setValue(int(settingsFile.readline()))
        settingsFile.close()
        self.Error.setText("Settings Loaded")
        return

        
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnigmaUI = QtWidgets.QDialog()
    ui = Ui_EnigmaUI()
    ui.setupUi(EnigmaUI)
    EnigmaUI.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

