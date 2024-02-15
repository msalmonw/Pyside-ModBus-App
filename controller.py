from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsDropShadowEffect, QPushButton
from PySide6.QtGui import QCloseEvent, QIcon, QColor
from PySide6 import QtCore
from pyModbusTCP.client import ModbusClient
import os
import sys
import json
from PLCModBus import Ui_PLCApp


class PLCApp(Ui_PLCApp, QMainWindow):
    reconnect = QtCore.Signal()
    destroyThreadsandExit = QtCore.Signal()
    def __init__(self) -> None:
        super(PLCApp, self).__init__()
        #initialization config of the UI
        self.setupUi(self)
        self.setWindowTitle('ABB PLC App')
        self.stackedWidget.setCurrentIndex(0)

        self.spreaderTWLUnlocked.setEnabled(False)
        self.spreaderTWLLocked.setEnabled(False)
        self.spreaderLanded.setEnabled(False)
        self.housingDown.setEnabled(False)
        self.slackRobe.setEnabled(False)
        self.hoistOverload.setEnabled(False)
        self.trolleyBlocking.setEnabled(False)
        self.cpsActive.setEnabled(False)

        self.cctvButton.clicked.connect(self.goToCCTVPage)
        self.spreaderButton.clicked.connect(self.goToSpreaderPage)
        self.chassisButton.clicked.connect(self.goToChassisPage)
        self.boomControlButton.clicked.connect(self.goToBoomControlPage)
        self.assistFunctionsButton.clicked.connect(self.goToAssistFunctionsPage)
        self.reloadButton.clicked.connect(self.reloadConfig)

    #set shadow effect under buttons and other widget
    def setShadowEffect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.stackedWidget.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.topInfoWidget.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.pageLabel.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.sideInfoWidget.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.hoistLoad.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.windSpeed.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.trimAngle.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.skewAngle.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.listAngle.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.cctvButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.spreaderButton.setGraphicsEffect(shadow)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.boomControlButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.assistFunctionsButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.chassisButton.setGraphicsEffect(shadow)

        buttons = self.cctvPage.children()
        for button in buttons:
            if isinstance(button, QPushButton):
                shadow = QGraphicsDropShadowEffect(self)
                shadow.setBlurRadius(4)
                shadow.setOffset(0, 4)
                shadow.setColor(QColor(0, 0, 0, 64))
                button.setGraphicsEffect(shadow)
        
        buttons = self.spreaderPage.children()
        for button in buttons:
            if isinstance(button, QPushButton):
                shadow = QGraphicsDropShadowEffect(self)
                shadow.setBlurRadius(4)
                shadow.setOffset(0, 4)
                shadow.setColor(QColor(0, 0, 0, 64))
                button.setGraphicsEffect(shadow)

        buttons = self.chassisPage.children()
        for button in buttons:
            if isinstance(button, QPushButton):
                shadow = QGraphicsDropShadowEffect(self)
                shadow.setBlurRadius(4)
                shadow.setOffset(0, 4)
                shadow.setColor(QColor(0, 0, 0, 64))
                button.setGraphicsEffect(shadow)

        buttons = self.boomControlPage.children()
        for button in buttons:
            if isinstance(button, QPushButton):
                shadow = QGraphicsDropShadowEffect(self)
                shadow.setBlurRadius(4)
                shadow.setOffset(0, 4)
                shadow.setColor(QColor(0, 0, 0, 64))
                button.setGraphicsEffect(shadow)

        buttons = self.assistFunctionsPage.children()
        for button in buttons:
            if isinstance(button, QPushButton):
                shadow = QGraphicsDropShadowEffect(self)
                shadow.setBlurRadius(4)
                shadow.setOffset(0, 4)
                shadow.setColor(QColor(0, 0, 0, 64))
                button.setGraphicsEffect(shadow)


    def startApp(self):
        self.setShadowEffect()
        self.reloadConfig()
        self.show()

    def goToCCTVPage(self):
        self.pageLabel.setText('CCTV')
        self.stackedWidget.setCurrentIndex(0)
    
    def goToSpreaderPage(self):
        self.pageLabel.setText('Spreader')
        self.stackedWidget.setCurrentIndex(1)

    def goToChassisPage(self):
        self.pageLabel.setText('Chassis')
        self.stackedWidget.setCurrentIndex(2)

    def goToBoomControlPage(self):
        self.pageLabel.setText('Boom Control')
        self.stackedWidget.setCurrentIndex(3)

    def goToAssistFunctionsPage(self):
        self.pageLabel.setText('Assist Functions')
        self.stackedWidget.setCurrentIndex(4)

    #load/realod styling config for all the buttons on the screens/tabs
    def reloadConfig(self):
        with open('buttons_config.json') as fp:
            styling = json.load(fp)

        spreaderPageConfig = styling['SpreaderPage']
        chassisPageConfig = styling['ChassisPage']
        boomControlPageConfig = styling['BoomControlPage']

        self.spreaderPage.setStyleSheet(spreaderPageConfig['spHookModeButton'] + spreaderPageConfig['overHeightModeButton']
                                         + spreaderPageConfig['lampTestButton'])
        
        self.chassisPage.setStyleSheet(chassisPageConfig['cpsAlignmentButton'] + chassisPageConfig['cpsReverseDirectionButton'])

        self.boomControlPage.setStyleSheet(boomControlPageConfig['boomUpButton'] + boomControlPageConfig['boomUpFullButton']
                                        + boomControlPageConfig['boomStopButton'] + boomControlPageConfig['boomDownButton']
                                        + boomControlPageConfig['gantryTieDownNotReleasedButton'] + boomControlPageConfig['gantryStormPinNotReleasedButton']
                                        + boomControlPageConfig['gantryMotorBrakesOpenButton'])

    def closeEvent(self, event: QCloseEvent) -> None:
        self.destroyThreadsandExit.emit()
        return super().closeEvent(event)


class ReadBinaryOutput(QtCore.QObject):
    topIndicators = QtCore.Signal(list)
    pagesIndicators = QtCore.Signal(list)
    connectionDropped = QtCore.Signal()
    ip = "localhost"
    port = 502
    interval = 100
    read = True
    def __init__(self) -> None:
        super().__init__()
        self.connection = ModbusClient(host=self.ip, port=self.port, auto_open=True, auto_close=False)

    def run(self):
        while self.read:
            QtCore.QThread.msleep(100)

            self.topIndicatorsList = self.connection.read_coils(30, 8)
            if self.topIndicatorsList:
                self.topIndicators.emit(self.topIndicatorsList)
            
            self.pagesIndicatorsList = self.connection.read_coils(40, 6)
            if self.pagesIndicatorsList:
                self.pagesIndicators.emit(self.pagesIndicatorsList)

            if not self.connection.is_open:
                self.connectionDropped.emit()
                break

        self.connection.close()
    

class Controller:
    def __init__(self) -> None:
        
        if getattr(sys, 'frozen', False):
            self.current_dir = os.path.dirname(sys.executable)
        elif __file__:
            self.current_dir = os.path.dirname(os.path.realpath(__file__))
        
        os.chdir(self.current_dir)

        #initialize main GUI and other threads
        self.plcApp = PLCApp()

        self.binaryIndicators = ReadBinaryOutput()
        self.indicatorsThread = QtCore.QThread()
        self.binaryIndicators.moveToThread(self.indicatorsThread)
        self.indicatorsThread.started.connect(self.binaryIndicators.run)
        self.binaryIndicators.topIndicators.connect(self.setTopIndicators)
        self.binaryIndicators.pagesIndicators.connect(self.setPagesIndicators)
        self.binaryIndicators.connectionDropped.connect(self.connectionDropped)

        #signals and slots connections
        self.plcApp.spHookModeButton.clicked.connect(self.setSpreaderHookMode)
        self.plcApp.overHeightModeButton.clicked.connect(self.setOverHeightMode)
        self.plcApp.lampTestButton.clicked.connect(self.lampTest)
        self.plcApp.cpsAlignmentButton.clicked.connect(self.toggleCPSAlignment)
        self.plcApp.cpsReverseDirectionButton.clicked.connect(self.toggleCPSDirection)
        self.plcApp.windCompensationSlider.valueChanged.connect(self.setWindCompensation)
        self.plcApp.laneSelectionSlider.valueChanged.connect(self.cpsLaneSelection)
        self.plcApp.cpsModeDial.valueChanged.connect(self.cpsLoadingMode)
        self.plcApp.boomUpButton.clicked.connect(self.setBoomUpSixty)
        self.plcApp.boomUpFullButton.clicked.connect(self.setBoomUpFull)
        self.plcApp.boomStopButton.clicked.connect(self.stopBoom)
        self.plcApp.boomDownButton.clicked.connect(self.boomDown)
        self.plcApp.gantryTieDownNotReleasedButton.clicked.connect(self.gantryTieDown)
        self.plcApp.gantryStormPinNotReleasedButton.clicked.connect(self.gantryStormPin)
        self.plcApp.gantryMotorBrakesOpenButton.clicked.connect(self.gantryMotorBrakes)
        self.plcApp.reconnect.connect(self.openConnection)
        self.plcApp.destroyThreadsandExit.connect(self.closeApp)

        #get modbus ip and port and create ModBusTCP client object
        with open ('PLC_config_file.json', 'r') as fp:
            self.ip, self.port, self.interval = json.load(fp)['ABBPLC'].values()
            
        self.connection = ModbusClient(host=self.ip, port=self.port, auto_open=False)

        self.binaryIndicators.ip = self.ip
        self.binaryIndicators.port = self.port
        self.binaryIndicators.interval = self.interval
        
        #start the application
        self.plcApp.startApp()

    def openConnection(self):
        status = self.connection.open()
        if status:
            print('Connection Successful') 
            self.plcApp.centralWidget().setStyleSheet('border-color: rgb(0, 255, 0);')
            self.indicatorsThread.start()
        else:
            self.plcApp.centralWidget().setStyleSheet('border-color: rgb(255, 0, 0);')
            print('Could not connect')

    def closeApp(self):
        self.connection.close()
        self.binaryIndicators.read = False
        QtCore.QThread.msleep(300)
        self.indicatorsThread.quit()

    def connectionDropped(self):
        self.indicatorsThread.quit()
        self.plcApp.centralWidget().setStyleSheet('border-color: rgb(255, 0, 0);')

    #functions for continous readings of all the indicators/lights
    def setTopIndicators(self, readingsList):
        self.plcApp.spreaderTWLUnlocked.setEnabled(readingsList[0])
        self.plcApp.spreaderTWLLocked.setEnabled(readingsList[1])
        self.plcApp.spreaderLanded.setEnabled(readingsList[2])
        self.plcApp.housingDown.setEnabled(readingsList[3])
        self.plcApp.slackRobe.setEnabled(readingsList[4])
        self.plcApp.hoistOverload.setEnabled(readingsList[5])
        self.plcApp.trolleyBlocking.setEnabled(readingsList[6])
        self.plcApp.cpsActive.setEnabled(readingsList[7])
        

    def setPagesIndicators(self, readingsList):
        self.plcApp.overHeightIndicator.setEnabled(readingsList[0])
        self.plcApp.ttdsFaultIndicator.setEnabled(readingsList[1])
        self.plcApp.hoistSnagLoadIndicator.setEnabled(readingsList[2])
        self.plcApp.highWindSpeedIndicator.setEnabled(readingsList[3])
        self.plcApp.boomUpFullIndication.setEnabled(readingsList[4])
        self.plcApp.bhCycleCompleteIndicator.setEnabled(readingsList[5])

    #spreader page functions
    def setSpreaderHookMode(self):
        if self.plcApp.spHookModeButton.isChecked():
            status = self.connection.write_single_coil(0, True)
        else:
            status = self.connection.write_single_coil(0, False)

        print(status)

    def setOverHeightMode(self):
        status = self.connection.write_single_coil(2, True)
        print(status)

    def lampTest(self):
        status = self.connection.write_single_coil(5, True)
        print(status)
               
    #boom control page functions   
    def toggleCPSAlignment(self):
        if self.plcApp.cpsAlignmentButton.isChecked():
            status = self.connection.write_single_coil(7, True)
        else:
            status = self.connection.write_single_coil(7, False)
        print(status)

    def toggleCPSDirection(self):
        if self.plcApp.cpsReverseDirectionButton.isChecked():
            status = self.connection.write_single_coil(7, True)
        else:
            status = self.connection.write_single_coil(7, False)
        print(status)
    
    def setWindCompensation(self, value):
        binaryValue = bin(value)[2:].zfill(3)
        status = self.connection.write_multiple_coils(8, [bool(int(binaryValue[0])), bool(int(binaryValue[1])), bool(int(binaryValue[2]))])
        print(status)

    def cpsLaneSelection(self, value):
        binaryValue = bin(value)[2:].zfill(4)
        status = self.connection.write_multiple_coils(11, [bool(int(binaryValue[0])), bool(int(binaryValue[1])), bool(int(binaryValue[2])), bool(int(binaryValue[3]))])
        print(status)

    def cpsLoadingMode(self, value):
        if value == -1:
            status = self.connection.write_multiple_coils(15, [True, True])
        elif value == 1:
            status = self.connection.write_multiple_coils(15, [False, True])
        else:
            status = self.connection.write_multiple_coils(15, [False, False])
        print(status)

    #boom control page functions
    def setBoomUpSixty(self):
        if self.plcApp.boomUpButton.isChecked():
            status = self.connection.write_single_coil(17, True)
        else:
            status = self.connection.write_single_coil(17, False)
        print(status)

    def setBoomUpFull(self):
        status = self.connection.write_single_coil(18, True)
        print(status)

    def stopBoom(self):
        status = self.connection.write_single_coil(19, True)
        print(status)

    def boomDown(self):
        if self.plcApp.boomDownButton.isChecked():
            status = self.connection.write_single_coil(20, True)
        else:
            status = self.connection.write_single_coil(20, False)
        print(status)

    def gantryTieDown(self):
        status = self.connection.write_single_coil(21, True)
        print(status)

    def gantryStormPin(self):
        status = self.connection.write_single_coil(22, True)
        print(status)

    def gantryMotorBrakes(self):
        status = self.connection.write_single_coil(23, True)
        print(status)

            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cont = Controller()
    cont.openConnection()
    sys.exit(app.exec())