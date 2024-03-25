from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsDropShadowEffect, QPushButton
from PySide6.QtGui import QCloseEvent, QIcon, QColor
from PySide6 import QtCore
from pyModbusTCP.client import ModbusClient
import os
import sys
import json
import subprocess

try:
    subprocess.run(['pyside6-uic', 'UI/PLCModBus.ui', '-o', 'UI/PLCModBus.py'])
    from UI.PLCModBus import Ui_PLCApp
except Exception as e:
    print('Error occured while converting UI.\n', e)
    sys.exit(1)
        

class PLCApp(Ui_PLCApp, QMainWindow):
    reconnect = QtCore.Signal()
    destroyThreadsandExit = QtCore.Signal()
    def __init__(self) -> None:
        super().__init__()
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
        self.showMaximized()

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
        assistFunctionsPageConfig = styling['AssistFunctionsPage']

        self.spreaderPage.setStyleSheet(spreaderPageConfig['transportModeButton'])
        
        self.chassisPage.setStyleSheet(chassisPageConfig['cpsAlignmentButton'] + chassisPageConfig['cpsReverseDirectionButton']
                                       + chassisPageConfig['cpsTwentyFtButton'] + chassisPageConfig['cpsDualCycleButton'])

        self.boomControlPage.setStyleSheet(boomControlPageConfig['boomUpButton'] + boomControlPageConfig['boomUpFullButton']
                                        + boomControlPageConfig['boomStopButton'] + boomControlPageConfig['boomDownButton']
                                        + boomControlPageConfig['gantryTieDownNotReleasedButton'] + boomControlPageConfig['gantryStormPinNotReleasedButton']
                                        + boomControlPageConfig['gantryMotorBrakesOpenButton'] + boomControlPageConfig['floodLightButton']
                                        + boomControlPageConfig['walkwayLightButton'])
        self.assistFunctionsPage.setStyleSheet(assistFunctionsPageConfig['skewControlButton'] + assistFunctionsPageConfig['swayControlButton'])

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
        self.connection = None

    def run(self):
        if not self.connection:
            self.connection = ModbusClient(host=self.ip, port=self.port, auto_open=True,auto_close=False)
        while self.read:
            QtCore.QThread.msleep(100)

            self.topIndicatorsList = self.connection.read_coils(4779, 8)
            if self.topIndicatorsList:
                self.topIndicators.emit(self.topIndicatorsList)
            
            self.pagesIndicatorsList = self.connection.read_coils(40, 6)
            if self.pagesIndicatorsList:
                self.pagesIndicators.emit(self.pagesIndicatorsList)

            if not self.connection.is_open:
                self.connectionDropped.emit()
                break

        self.connection.close()

class ReadAnalogData(QtCore.QObject):
    analogReadings = QtCore.Signal(list)
    connectionDropped = QtCore.Signal()
    ip = "localhost"
    port = 502
    interval = 100
    read = True
    def __init__(self) -> None:
        super().__init__()
        self.connection = None

    def run(self):
        if not self.connection:
            self.connection = ModbusClient(host=self.ip, port=self.port, auto_open=True,auto_close=False)
        while self.read:
            QtCore.QThread.msleep(100)

            self.analogReadingsList = self.connection.read_holding_registers(4859, 7)
            if self.analogReadingsList:
                self.analogReadings.emit(self.analogReadingsList)
            
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

        self.analogReadings = ReadAnalogData()
        self.analogReadingsThread = QtCore.QThread()
        self.analogReadings.moveToThread(self.analogReadingsThread)
        self.analogReadingsThread.started.connect(self.analogReadings.run)
        self.analogReadings.analogReadings.connect(self.showAnalogData)
        self.analogReadings.connectionDropped.connect(self.connectionDropped)

        #signals and slots connections
        self.plcApp.transportModeButton.clicked.connect(self.setTransportMode)
        self.plcApp.cpsAlignmentButton.clicked.connect(self.toggleCPSAlignment)
        self.plcApp.cpsReverseDirectionButton.clicked.connect(self.toggleCPSDirection)
        self.plcApp.windCompensationSlider.valueChanged.connect(self.setWindCompensation)
        self.plcApp.laneSelectionSlider.valueChanged.connect(self.cpsLaneSelection)
        self.plcApp.cpsModeDial.valueChanged.connect(self.cpsLoadingMode)
        self.plcApp.boomUpButton.clicked.connect(self.setBoomUpSixty)
        self.plcApp.boomUpFullButton.clicked.connect(self.setBoomUpFull)
        self.plcApp.boomStopButton.clicked.connect(self.stopBoom)
        self.plcApp.boomDownButton.clicked.connect(self.boomDown)
        self.plcApp.reconnect.connect(self.openConnection)
        self.plcApp.destroyThreadsandExit.connect(self.closeApp)
        self.plcApp.connectButton.clicked.connect(self.openConnection)

        #additions to signals and slots 25-03-24
        self.plcApp.floodLightButton.clicked.connect(self.toggleFLoodLight)
        self.plcApp.walkwayLightButton.clicked.connect(self.toggleWalkwayLight)
        self.plcApp.skewControlButton.clicked.connect(self.toggleSkewControl)
        self.plcApp.swayControlButton.clicked.connect(self.toggleSwayControl)
        self.plcApp.cpsTwentyFtButton.clicked.connect(self.toggleCPSTwentyFt)
        self.plcApp.cpsDualCycleButton.clicked.connect(self.toggleDualCycle)

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
        if not self.connection.is_open:
            status = self.connection.open()
            if status:
                print('Connection Successful') 
                self.plcApp.centralWidget().setStyleSheet(u"QWidget#centralwidget{\n"
                                                        "background:rgb(255, 255, 255);\n"
                                                        "border-radius: 10px;\n"
                                                        "border: 6px solid transparent;\n"
                                                        "}")
                self.binaryIndicators.read = True
                self.analogReadings.read = True
                self.indicatorsThread.start()
                self.analogReadingsThread.start()
            else:
                self.plcApp.centralWidget().setStyleSheet(u"QWidget#centralwidget{\n"
                                                        "background:rgb(255, 255, 255);\n"
                                                        "border-radius: 10px;\n"
                                                        "border: 6px solid red;\n"
                                                        "}")
                print('Could not connect')

    def closeApp(self):
        self.connection.close()
        self.binaryIndicators.read = False
        self.analogReadings.read = False
        QtCore.QThread.msleep(400)
        self.indicatorsThread.quit()
        self.analogReadingsThread.quit()

    def connectionDropped(self):
        self.binaryIndicators.read = False
        self.analogReadings.read = False

        QtCore.QThread.msleep(400)
        self.indicatorsThread.quit()
        self.analogReadingsThread.quit()
        self.connection.close()

        self.plcApp.centralWidget().setStyleSheet(u"QWidget#centralwidget{\n"
                                                    "background:rgb(255, 255, 255);\n"
                                                    "border-radius: 10px;\n"
                                                    "border: 6px solid red;\n"
                                                    "}")

    #functions for continous readings of all the indicators/lights and meters
    def setTopIndicators(self, readingsList):
        self.plcApp.spreaderLanded.setEnabled(readingsList[0])
        self.plcApp.spreaderTWLUnlocked.setEnabled(readingsList[1])
        self.plcApp.spreaderTWLLocked.setEnabled(readingsList[2])
        self.plcApp.housingDown.setEnabled(readingsList[3])
        self.plcApp.slackRobe.setEnabled(readingsList[4])
        self.plcApp.hoistOverload.setEnabled(readingsList[5])
        self.plcApp.trolleyBlocking.setEnabled(readingsList[6])
        self.plcApp.cpsActive.setEnabled(readingsList[7])
        
    def setPagesIndicators(self, readingsList):
        self.plcApp.overHeightIndicator.setEnabled(readingsList[0])
        self.plcApp.ttdsFaultIndicator.setEnabled(readingsList[1])
        self.plcApp.hoistSnagLoadIndicator.setEnabled(readingsList[2])
        #self.plcApp.highWindSpeedIndicator.setEnabled(readingsList[3])
        self.plcApp.boomUpFullIndication.setEnabled(readingsList[4])
        self.plcApp.bhCycleCompleteIndicator.setEnabled(readingsList[5])

    def showAnalogData(self, readingsList):
        self.plcApp.hoistLoad.setText(str(readingsList[0]))
        self.plcApp.windSpeed.setText(str(readingsList[1]))
        self.plcApp.trimAngle.setText(str(readingsList[2]))
        self.plcApp.listAngle.setText(str(readingsList[3]))
        self.plcApp.skewAngle.setText(str(readingsList[4]))
        self.plcApp.containerSize.setText(str(readingsList[5] + readingsList[6]))

    #spreader page functions
    def setTransportMode(self):
        if self.plcApp.transportModeButton.isChecked():
            status = self.connection.write_single_coil(4719, True)
        else:
            status = self.connection.write_single_coil(4719, False)
        print(status)
               
    #chasssis page functions   
    def toggleCPSAlignment(self):
        if self.plcApp.cpsAlignmentButton.isChecked():
            status = self.connection.write_single_coil(4709, True)
        else:
            status = self.connection.write_single_coil(4709, False)
        print(status)

    def toggleCPSDirection(self):
        if self.plcApp.cpsReverseDirectionButton.isChecked():
            status = self.connection.write_single_coil(4710, True)
        else:
            status = self.connection.write_single_coil(4710, False)
        print(status)

    def toggleCPSTwentyFt(self):
        if self.plcApp.cpsTwentyFtButton.isChecked():
            status = self.connection.write_single_coil(4717, True)
        else:
            status = self.connection.write_single_coil(4717, False)
        print(status)

    def toggleDualCycle(self):
        if self.plcApp.cpsDualCycleButton.isChecked():
            status = self.connection.write_single_coil(4718, True)
        else:
            status = self.connection.write_single_coil(4718, False)
        print(status)
    
    def setWindCompensation(self, value):
        binaryValue = bin(value)[2:].zfill(3)
        status = self.connection.write_multiple_coils(4706, [bool(int(binaryValue[0])), bool(int(binaryValue[1])), bool(int(binaryValue[2]))])
        print(status)

    def cpsLaneSelection(self, value):
        binaryValue = bin(value)[2:].zfill(4)
        status = self.connection.write_multiple_coils(4711, [bool(int(binaryValue[0])), bool(int(binaryValue[1])), bool(int(binaryValue[2])), bool(int(binaryValue[3]))])
        print(status)

    def cpsLoadingMode(self, value):
        if value == -1:
            status = self.connection.write_multiple_coils(4715, [True, True])
        elif value == 1:
            status = self.connection.write_multiple_coils(4715, [False, True])
        else:
            status = self.connection.write_multiple_coils(4715, [False, False])
        print(status)

    #boom control page functions
    def setBoomUpSixty(self):
        if self.plcApp.boomUpButton.isChecked():
            status = self.connection.write_single_coil(4700, True)
        else:
            status = self.connection.write_single_coil(4700, False)
        print(status)

    def setBoomUpFull(self):
        status = self.connection.write_single_coil(4701, True)
        print(status)

    def stopBoom(self):
        status = self.connection.write_single_coil(4702, True)
        print(status)

    def boomDown(self):
        if self.plcApp.boomDownButton.isChecked():
            status = self.connection.write_single_coil(4703, True)
        else:
            status = self.connection.write_single_coil(4703, False)
        print(status)

    def toggleFLoodLight(self):
        if self.plcApp.floodLightButton.isChecked():
            status = self.connection.write_single_coil(4704, True)
        else:
            status = self.connection.write_single_coil(4704, False)
        print(status)

    def toggleWalkwayLight(self):
        if self.plcApp.walkwayLightButton.isChecked():
            status = self.connection.write_single_coil(4705, True)
        else:
            status = self.connection.write_single_coil(4705, False)
        print(status)

    #assist functions page functions
    def toggleSkewControl(self):
        if self.plcApp.skewControlButton.isChecked():
            status = self.connection.write_single_coil(4720, True)
        else:
            status = self.connection.write_single_coil(4720, False)
        print(status)
    
    def toggleSwayControl(self):
        if self.plcApp.swayControlButton.isChecked():
            status = self.connection.write_single_coil(4721, True)
        else:
            status = self.connection.write_single_coil(4721, False)
        print(status)

            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cont = Controller()
    sys.exit(app.exec())