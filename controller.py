from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsDropShadowEffect, QPushButton
from PySide6.QtGui import QIcon, QColor
from PySide6 import QtCore
from pyModbusTCP.client import ModbusClient
import os
import sys
import json
from PLCModBus import Ui_PLCApp


class PLCApp(Ui_PLCApp, QMainWindow):
    def __init__(self) -> None:
        super(PLCApp, self).__init__()
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
        self.showFullScreen()

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
    

class Controller:
    def __init__(self) -> None:
        
        if getattr(sys, 'frozen', False):
            self.current_dir = os.path.dirname(sys.executable)
        elif __file__:
            self.current_dir = os.path.dirname(os.path.realpath(__file__))
        
        os.chdir(self.current_dir)

        self.plcApp = PLCApp()

        self.plcApp.spHookModeButton.clicked.connect(self.setSpreaderHookMode)
        self.plcApp.startApp()

    def openConnection(self):
        with open ('PLC_config_file.json', 'r') as fp:
            self.ip, self.port, self.interval = json.load(fp)['ABBPLC'].values()
            
        self.connection = ModbusClient(host=self.ip, port=self.port)
        status = self.connection.open()
        print('Connection Successful') if status else print('Could not connect')

    def setSpreaderHookMode(self):
        if self.plcApp.spHookModeButton.isChecked():
            status = self.connection.write_single_coil(1, False)
        else:
            status = self.connection.write_single_coil(1, True)

    def overHeightIndication(self):
        status = self.connection.read_coils(2, 1)
        if not status:
            print(f'Failed to read bit {1} at address {2}')
        else:
            self.plcApp.overHeightIndicator.setEnabled(True) if status[0] else self.plcApp.overHeightIndicator.setEnabled(False)

    def setOverHeightMode(self):
        status = self.connection.write_single_coil(3, True)

    def ttdsFault(self):
        status = self.connection.read_coils(4, 1)
        if not status:
            print(f'Failed to read bit {1} at address {4}')
        else:
            self.plcApp.ttdsFaultIndicator.setEnabled(True) if status[0] else self.plcApp.ttdsFaultIndicator.setEnabled(False)

    def hoistSnagLoad(self):
        status = self.connection.read_coils(5, 1)
        if not status:
            print(f'Failed to read bit {1} at address {5}')
        else:
            self.plcApp.hoistSnagLoadIndicator.setEnabled(True) if status[0] else self.plcApp.hoistSnagLoadIndicator.setEnabled(False)

    def lampTest(self):
        status = self.connection.write_single_coil(6, True)

    def highWindSpeed(self):
        status = self.connection.read_coils(7, 1)
        if not status:
            print(f'Failed to read bit {1} at address {7}')
        else:
            self.plcApp.highWindSpeedIndicator.setEnabled(True) if status[0] else self.plcApp.highWindSpeedIndicator.setEnabled(False)
               
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cont = Controller()
    cont.openConnection()
    sys.exit(app.exec())