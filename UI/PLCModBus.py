# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PLCModBus.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_PLCApp(object):
    def setupUi(self, PLCApp):
        if not PLCApp.objectName():
            PLCApp.setObjectName(u"PLCApp")
        PLCApp.resize(1280, 720)
        PLCApp.setMinimumSize(QSize(1280, 720))
        PLCApp.setMaximumSize(QSize(16777215, 16777215))
        PLCApp.setStyleSheet(u"QWidget{\n"
"background:rgba(237, 244, 250, 255);\n"
"border-radius: 10px;\n"
"font-family: Poppins;\n"
"font-size: 16px;\n"
"font-weight: 600;\n"
"}\n"
"QPushButton{\n"
"border: 0px;\n"
"background: rgb(0, 70, 100);\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: 600;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 3px solid transparent;\n"
"}\n"
"QPushButton#cctvButton, #spreaderButton, #chassisButton, #boomControlButton, #assistFunctionsButton{\n"
"border: 0px;\n"
"background: rgba(0, 36, 71, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: 600;\n"
"}\n"
"QPushButton#reloadButton, #connectButton{\n"
"background: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#reloadButton:pressed, #connectButton:pressed{\n"
"border: 3px solid grey;\n"
"}\n"
"QLabel#hoistLoad, #windSpeed, #trimAngle, #listAngle, #skewAngle{\n"
"background: rgb(255, 204, 188);\n"
"color: rgb(255, 61, 0);\n"
"font-size: 22px;\n"
"}\n"
"QLabel#pageLabel{\n"
"font-size: 22px;\n"
"}\n"
"QDial{\n"
"background: rgb(0, 70, 100);\n"
"color: rbg"
                        "(0, 0, 0);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"height: 20px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background: rgb(0, 70, 100);\n"
"border-radius: 3px;\n"
"}")
        PLCApp.setIconSize(QSize(32, 48))
        self.centralwidget = QWidget(PLCApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background:rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 6px solid red;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 20, 15)
        self.sideInfoWidget = QWidget(self.centralwidget)
        self.sideInfoWidget.setObjectName(u"sideInfoWidget")
        self.sideInfoWidget.setMinimumSize(QSize(120, 0))
        self.verticalLayout = QVBoxLayout(self.sideInfoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hoistLoad = QLabel(self.sideInfoWidget)
        self.hoistLoad.setObjectName(u"hoistLoad")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoistLoad.sizePolicy().hasHeightForWidth())
        self.hoistLoad.setSizePolicy(sizePolicy)
        self.hoistLoad.setMinimumSize(QSize(80, 80))
        self.hoistLoad.setMaximumSize(QSize(16777215, 80))
        self.hoistLoad.setAlignment(Qt.AlignCenter)
        self.hoistLoad.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.hoistLoad)

        self.hoistLoadLabel = QLabel(self.sideInfoWidget)
        self.hoistLoadLabel.setObjectName(u"hoistLoadLabel")
        self.hoistLoadLabel.setMinimumSize(QSize(0, 30))
        self.hoistLoadLabel.setMaximumSize(QSize(16777215, 30))
        self.hoistLoadLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.hoistLoadLabel)

        self.windSpeed = QLabel(self.sideInfoWidget)
        self.windSpeed.setObjectName(u"windSpeed")
        sizePolicy.setHeightForWidth(self.windSpeed.sizePolicy().hasHeightForWidth())
        self.windSpeed.setSizePolicy(sizePolicy)
        self.windSpeed.setMinimumSize(QSize(80, 80))
        self.windSpeed.setMaximumSize(QSize(16777215, 80))
        self.windSpeed.setAlignment(Qt.AlignCenter)
        self.windSpeed.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.windSpeed)

        self.windSpeedLabel = QLabel(self.sideInfoWidget)
        self.windSpeedLabel.setObjectName(u"windSpeedLabel")
        self.windSpeedLabel.setMinimumSize(QSize(0, 30))
        self.windSpeedLabel.setMaximumSize(QSize(16777215, 30))
        self.windSpeedLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.windSpeedLabel)

        self.trimAngle = QLabel(self.sideInfoWidget)
        self.trimAngle.setObjectName(u"trimAngle")
        sizePolicy.setHeightForWidth(self.trimAngle.sizePolicy().hasHeightForWidth())
        self.trimAngle.setSizePolicy(sizePolicy)
        self.trimAngle.setMinimumSize(QSize(80, 80))
        self.trimAngle.setMaximumSize(QSize(16777215, 80))
        self.trimAngle.setAlignment(Qt.AlignCenter)
        self.trimAngle.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.trimAngle)

        self.trimAngleLabel = QLabel(self.sideInfoWidget)
        self.trimAngleLabel.setObjectName(u"trimAngleLabel")
        self.trimAngleLabel.setMinimumSize(QSize(0, 30))
        self.trimAngleLabel.setMaximumSize(QSize(16777215, 30))
        self.trimAngleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.trimAngleLabel)

        self.listAngle = QLabel(self.sideInfoWidget)
        self.listAngle.setObjectName(u"listAngle")
        sizePolicy.setHeightForWidth(self.listAngle.sizePolicy().hasHeightForWidth())
        self.listAngle.setSizePolicy(sizePolicy)
        self.listAngle.setMinimumSize(QSize(80, 80))
        self.listAngle.setMaximumSize(QSize(16777215, 80))
        self.listAngle.setAlignment(Qt.AlignCenter)
        self.listAngle.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.listAngle)

        self.listAngleLabel = QLabel(self.sideInfoWidget)
        self.listAngleLabel.setObjectName(u"listAngleLabel")
        self.listAngleLabel.setMinimumSize(QSize(0, 30))
        self.listAngleLabel.setMaximumSize(QSize(16777215, 30))
        self.listAngleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.listAngleLabel)

        self.skewAngle = QLabel(self.sideInfoWidget)
        self.skewAngle.setObjectName(u"skewAngle")
        sizePolicy.setHeightForWidth(self.skewAngle.sizePolicy().hasHeightForWidth())
        self.skewAngle.setSizePolicy(sizePolicy)
        self.skewAngle.setMinimumSize(QSize(80, 80))
        self.skewAngle.setMaximumSize(QSize(16777215, 80))
        self.skewAngle.setAlignment(Qt.AlignCenter)
        self.skewAngle.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.skewAngle)

        self.skewAngleLabel = QLabel(self.sideInfoWidget)
        self.skewAngleLabel.setObjectName(u"skewAngleLabel")
        self.skewAngleLabel.setMinimumSize(QSize(0, 30))
        self.skewAngleLabel.setMaximumSize(QSize(16777215, 30))
        self.skewAngleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.skewAngleLabel)


        self.gridLayout.addWidget(self.sideInfoWidget, 0, 2, 3, 1)

        self.pageLabel = QLabel(self.centralwidget)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setMinimumSize(QSize(0, 50))
        self.pageLabel.setMaximumSize(QSize(16777215, 50))
        self.pageLabel.setMargin(10)

        self.gridLayout.addWidget(self.pageLabel, 1, 1, 1, 1)

        self.topInfoWidget = QWidget(self.centralwidget)
        self.topInfoWidget.setObjectName(u"topInfoWidget")
        self.topInfoWidget.setMinimumSize(QSize(0, 140))
        self.topInfoWidget.setMaximumSize(QSize(16777215, 140))
        self.horizontalLayout_2 = QHBoxLayout(self.topInfoWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.spreaderTWLUnlocked = QToolButton(self.topInfoWidget)
        self.spreaderTWLUnlocked.setObjectName(u"spreaderTWLUnlocked")
        self.spreaderTWLUnlocked.setMinimumSize(QSize(120, 100))
        icon = QIcon()
        icon.addFile(u"UI/resources/redlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spreaderTWLUnlocked.setIcon(icon)
        self.spreaderTWLUnlocked.setIconSize(QSize(80, 80))
        self.spreaderTWLUnlocked.setCheckable(True)
        self.spreaderTWLUnlocked.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderTWLUnlocked)

        self.spreaderTWLLocked = QToolButton(self.topInfoWidget)
        self.spreaderTWLLocked.setObjectName(u"spreaderTWLLocked")
        self.spreaderTWLLocked.setMinimumSize(QSize(120, 100))
        icon1 = QIcon()
        icon1.addFile(u"UI/resources/greenlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spreaderTWLLocked.setIcon(icon1)
        self.spreaderTWLLocked.setIconSize(QSize(80, 80))
        self.spreaderTWLLocked.setCheckable(True)
        self.spreaderTWLLocked.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderTWLLocked)

        self.spreaderLanded = QToolButton(self.topInfoWidget)
        self.spreaderLanded.setObjectName(u"spreaderLanded")
        self.spreaderLanded.setMinimumSize(QSize(120, 100))
        self.spreaderLanded.setIcon(icon1)
        self.spreaderLanded.setIconSize(QSize(80, 80))
        self.spreaderLanded.setCheckable(True)
        self.spreaderLanded.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderLanded)

        self.housingDown = QToolButton(self.topInfoWidget)
        self.housingDown.setObjectName(u"housingDown")
        self.housingDown.setMinimumSize(QSize(120, 100))
        icon2 = QIcon()
        icon2.addFile(u"UI/resources/yellowlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.housingDown.setIcon(icon2)
        self.housingDown.setIconSize(QSize(80, 80))
        self.housingDown.setCheckable(True)
        self.housingDown.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.housingDown)

        self.slackRobe = QToolButton(self.topInfoWidget)
        self.slackRobe.setObjectName(u"slackRobe")
        self.slackRobe.setMinimumSize(QSize(120, 100))
        self.slackRobe.setIcon(icon2)
        self.slackRobe.setIconSize(QSize(80, 80))
        self.slackRobe.setCheckable(True)
        self.slackRobe.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.slackRobe)

        self.hoistOverload = QToolButton(self.topInfoWidget)
        self.hoistOverload.setObjectName(u"hoistOverload")
        self.hoistOverload.setMinimumSize(QSize(120, 100))
        self.hoistOverload.setIcon(icon2)
        self.hoistOverload.setIconSize(QSize(80, 80))
        self.hoistOverload.setCheckable(True)
        self.hoistOverload.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.hoistOverload)

        self.trolleyBlocking = QToolButton(self.topInfoWidget)
        self.trolleyBlocking.setObjectName(u"trolleyBlocking")
        self.trolleyBlocking.setMinimumSize(QSize(120, 100))
        self.trolleyBlocking.setIcon(icon2)
        self.trolleyBlocking.setIconSize(QSize(80, 80))
        self.trolleyBlocking.setCheckable(True)
        self.trolleyBlocking.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.trolleyBlocking)

        self.cpsActive = QToolButton(self.topInfoWidget)
        self.cpsActive.setObjectName(u"cpsActive")
        self.cpsActive.setMinimumSize(QSize(120, 100))
        self.cpsActive.setIcon(icon1)
        self.cpsActive.setIconSize(QSize(80, 80))
        self.cpsActive.setCheckable(True)
        self.cpsActive.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.cpsActive)


        self.gridLayout.addWidget(self.topInfoWidget, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.reloadButton = QPushButton(self.centralwidget)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setMinimumSize(QSize(50, 50))
        self.reloadButton.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"UI/resources/reloading.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadButton.setIcon(icon3)
        self.reloadButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.reloadButton)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMinimumSize(QSize(50, 50))
        self.connectButton.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u"UI/resources/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connectButton.setIcon(icon4)
        self.connectButton.setIconSize(QSize(40, 40))
        self.connectButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.connectButton)

        self.cctvButton = QPushButton(self.centralwidget)
        self.cctvButton.setObjectName(u"cctvButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cctvButton.sizePolicy().hasHeightForWidth())
        self.cctvButton.setSizePolicy(sizePolicy1)
        self.cctvButton.setMinimumSize(QSize(180, 50))
        self.cctvButton.setMaximumSize(QSize(180, 50))
        self.cctvButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.cctvButton)

        self.spreaderButton = QPushButton(self.centralwidget)
        self.spreaderButton.setObjectName(u"spreaderButton")
        sizePolicy1.setHeightForWidth(self.spreaderButton.sizePolicy().hasHeightForWidth())
        self.spreaderButton.setSizePolicy(sizePolicy1)
        self.spreaderButton.setMinimumSize(QSize(180, 50))
        self.spreaderButton.setMaximumSize(QSize(180, 50))
        self.spreaderButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.spreaderButton)

        self.chassisButton = QPushButton(self.centralwidget)
        self.chassisButton.setObjectName(u"chassisButton")
        sizePolicy1.setHeightForWidth(self.chassisButton.sizePolicy().hasHeightForWidth())
        self.chassisButton.setSizePolicy(sizePolicy1)
        self.chassisButton.setMinimumSize(QSize(180, 50))
        self.chassisButton.setMaximumSize(QSize(180, 50))
        self.chassisButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.chassisButton)

        self.boomControlButton = QPushButton(self.centralwidget)
        self.boomControlButton.setObjectName(u"boomControlButton")
        sizePolicy1.setHeightForWidth(self.boomControlButton.sizePolicy().hasHeightForWidth())
        self.boomControlButton.setSizePolicy(sizePolicy1)
        self.boomControlButton.setMinimumSize(QSize(180, 50))
        self.boomControlButton.setMaximumSize(QSize(180, 50))
        self.boomControlButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.boomControlButton)

        self.assistFunctionsButton = QPushButton(self.centralwidget)
        self.assistFunctionsButton.setObjectName(u"assistFunctionsButton")
        sizePolicy1.setHeightForWidth(self.assistFunctionsButton.sizePolicy().hasHeightForWidth())
        self.assistFunctionsButton.setSizePolicy(sizePolicy1)
        self.assistFunctionsButton.setMinimumSize(QSize(180, 50))
        self.assistFunctionsButton.setMaximumSize(QSize(180, 50))
        self.assistFunctionsButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.assistFunctionsButton)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.cctvPage = QWidget()
        self.cctvPage.setObjectName(u"cctvPage")
        self.gridLayout_2 = QGridLayout(self.cctvPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.craneEntranceButton = QPushButton(self.cctvPage)
        self.craneEntranceButton.setObjectName(u"craneEntranceButton")
        self.craneEntranceButton.setMinimumSize(QSize(150, 150))
        self.craneEntranceButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.craneEntranceButton, 0, 3, 1, 1)

        self.gantryRightWideButton = QPushButton(self.cctvPage)
        self.gantryRightWideButton.setObjectName(u"gantryRightWideButton")
        self.gantryRightWideButton.setMinimumSize(QSize(150, 150))
        self.gantryRightWideButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.gantryRightWideButton, 1, 3, 1, 1)

        self.boomMotionWideButton = QPushButton(self.cctvPage)
        self.boomMotionWideButton.setObjectName(u"boomMotionWideButton")
        self.boomMotionWideButton.setMinimumSize(QSize(150, 150))
        self.boomMotionWideButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.boomMotionWideButton, 0, 5, 1, 1)

        self.landingPlatformButton = QPushButton(self.cctvPage)
        self.landingPlatformButton.setObjectName(u"landingPlatformButton")
        self.landingPlatformButton.setMinimumSize(QSize(150, 150))
        self.landingPlatformButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.landingPlatformButton, 0, 6, 1, 1)

        self.boomMotionButton = QPushButton(self.cctvPage)
        self.boomMotionButton.setObjectName(u"boomMotionButton")
        self.boomMotionButton.setMinimumSize(QSize(150, 150))
        self.boomMotionButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.boomMotionButton, 0, 4, 1, 1)

        self.gantryRightButton = QPushButton(self.cctvPage)
        self.gantryRightButton.setObjectName(u"gantryRightButton")
        self.gantryRightButton.setMinimumSize(QSize(150, 150))
        self.gantryRightButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.gantryRightButton, 1, 2, 1, 1)

        self.highSpreaderButton = QPushButton(self.cctvPage)
        self.highSpreaderButton.setObjectName(u"highSpreaderButton")
        self.highSpreaderButton.setMinimumSize(QSize(150, 150))
        self.highSpreaderButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.highSpreaderButton, 0, 1, 1, 1)

        self.gantryLeftButton = QPushButton(self.cctvPage)
        self.gantryLeftButton.setObjectName(u"gantryLeftButton")
        self.gantryLeftButton.setMinimumSize(QSize(150, 150))
        self.gantryLeftButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.gantryLeftButton, 1, 0, 1, 1)

        self.landingPlatformWideButton = QPushButton(self.cctvPage)
        self.landingPlatformWideButton.setObjectName(u"landingPlatformWideButton")
        self.landingPlatformWideButton.setMinimumSize(QSize(150, 150))
        self.landingPlatformWideButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.landingPlatformWideButton, 1, 6, 1, 1)

        self.hatchCoverSingleButton = QPushButton(self.cctvPage)
        self.hatchCoverSingleButton.setObjectName(u"hatchCoverSingleButton")
        self.hatchCoverSingleButton.setMinimumSize(QSize(150, 150))
        self.hatchCoverSingleButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.hatchCoverSingleButton, 1, 4, 1, 1)

        self.hatchCoverSingleWideButton = QPushButton(self.cctvPage)
        self.hatchCoverSingleWideButton.setObjectName(u"hatchCoverSingleWideButton")
        self.hatchCoverSingleWideButton.setMinimumSize(QSize(150, 150))
        self.hatchCoverSingleWideButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.hatchCoverSingleWideButton, 1, 5, 1, 1)

        self.spreaderOverviewButton = QPushButton(self.cctvPage)
        self.spreaderOverviewButton.setObjectName(u"spreaderOverviewButton")
        self.spreaderOverviewButton.setMinimumSize(QSize(150, 150))
        self.spreaderOverviewButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.spreaderOverviewButton, 0, 2, 1, 1)

        self.gantryLeftWideButton = QPushButton(self.cctvPage)
        self.gantryLeftWideButton.setObjectName(u"gantryLeftWideButton")
        self.gantryLeftWideButton.setMinimumSize(QSize(150, 150))
        self.gantryLeftWideButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.gantryLeftWideButton, 1, 1, 1, 1)

        self.normalContainerButton = QPushButton(self.cctvPage)
        self.normalContainerButton.setObjectName(u"normalContainerButton")
        self.normalContainerButton.setMinimumSize(QSize(150, 150))
        self.normalContainerButton.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.normalContainerButton, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cctvPage)
        self.spreaderPage = QWidget()
        self.spreaderPage.setObjectName(u"spreaderPage")
        self.gridLayout_3 = QGridLayout(self.spreaderPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spHookModeButton = QPushButton(self.spreaderPage)
        self.spHookModeButton.setObjectName(u"spHookModeButton")
        self.spHookModeButton.setMinimumSize(QSize(150, 150))
        self.spHookModeButton.setMaximumSize(QSize(150, 150))
        self.spHookModeButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.spHookModeButton, 0, 0, 1, 1)

        self.overHeightModeButton = QPushButton(self.spreaderPage)
        self.overHeightModeButton.setObjectName(u"overHeightModeButton")
        self.overHeightModeButton.setMinimumSize(QSize(150, 150))
        self.overHeightModeButton.setMaximumSize(QSize(150, 150))
        self.overHeightModeButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.overHeightModeButton, 0, 1, 1, 1)

        self.overHeightIndicator = QToolButton(self.spreaderPage)
        self.overHeightIndicator.setObjectName(u"overHeightIndicator")
        self.overHeightIndicator.setEnabled(False)
        self.overHeightIndicator.setMinimumSize(QSize(120, 100))
        self.overHeightIndicator.setIcon(icon1)
        self.overHeightIndicator.setIconSize(QSize(80, 80))
        self.overHeightIndicator.setCheckable(True)
        self.overHeightIndicator.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.overHeightIndicator, 0, 2, 1, 1)

        self.ttdsFaultIndicator = QToolButton(self.spreaderPage)
        self.ttdsFaultIndicator.setObjectName(u"ttdsFaultIndicator")
        self.ttdsFaultIndicator.setEnabled(False)
        self.ttdsFaultIndicator.setMinimumSize(QSize(120, 100))
        self.ttdsFaultIndicator.setIcon(icon1)
        self.ttdsFaultIndicator.setIconSize(QSize(80, 80))
        self.ttdsFaultIndicator.setCheckable(True)
        self.ttdsFaultIndicator.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.ttdsFaultIndicator, 0, 3, 1, 1)

        self.lampTestButton = QPushButton(self.spreaderPage)
        self.lampTestButton.setObjectName(u"lampTestButton")
        self.lampTestButton.setMinimumSize(QSize(150, 150))
        self.lampTestButton.setMaximumSize(QSize(150, 150))
        self.lampTestButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.lampTestButton, 1, 0, 1, 1)

        self.hoistSnagLoadIndicator = QToolButton(self.spreaderPage)
        self.hoistSnagLoadIndicator.setObjectName(u"hoistSnagLoadIndicator")
        self.hoistSnagLoadIndicator.setEnabled(False)
        self.hoistSnagLoadIndicator.setMinimumSize(QSize(120, 100))
        self.hoistSnagLoadIndicator.setIcon(icon1)
        self.hoistSnagLoadIndicator.setIconSize(QSize(80, 80))
        self.hoistSnagLoadIndicator.setCheckable(True)
        self.hoistSnagLoadIndicator.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.hoistSnagLoadIndicator, 1, 2, 1, 1)

        self.highWindSpeedIndicator = QToolButton(self.spreaderPage)
        self.highWindSpeedIndicator.setObjectName(u"highWindSpeedIndicator")
        self.highWindSpeedIndicator.setEnabled(False)
        self.highWindSpeedIndicator.setMinimumSize(QSize(120, 100))
        self.highWindSpeedIndicator.setIcon(icon1)
        self.highWindSpeedIndicator.setIconSize(QSize(80, 80))
        self.highWindSpeedIndicator.setCheckable(True)
        self.highWindSpeedIndicator.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.highWindSpeedIndicator, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.spreaderPage)
        self.chassisPage = QWidget()
        self.chassisPage.setObjectName(u"chassisPage")
        self.gridLayout_4 = QGridLayout(self.chassisPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cpsAlignmentButton = QPushButton(self.chassisPage)
        self.cpsAlignmentButton.setObjectName(u"cpsAlignmentButton")
        self.cpsAlignmentButton.setMinimumSize(QSize(150, 150))
        self.cpsAlignmentButton.setMaximumSize(QSize(150, 150))
        self.cpsAlignmentButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.cpsAlignmentButton)

        self.cpsReverseDirectionButton = QPushButton(self.chassisPage)
        self.cpsReverseDirectionButton.setObjectName(u"cpsReverseDirectionButton")
        self.cpsReverseDirectionButton.setMinimumSize(QSize(150, 150))
        self.cpsReverseDirectionButton.setMaximumSize(QSize(150, 150))
        self.cpsReverseDirectionButton.setStyleSheet(u"")
        self.cpsReverseDirectionButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.cpsReverseDirectionButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(self.chassisPage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.cpsModeDial = QDial(self.chassisPage)
        self.cpsModeDial.setObjectName(u"cpsModeDial")
        sizePolicy2.setHeightForWidth(self.cpsModeDial.sizePolicy().hasHeightForWidth())
        self.cpsModeDial.setSizePolicy(sizePolicy2)
        self.cpsModeDial.setMinimumSize(QSize(150, 150))
        self.cpsModeDial.setMaximumSize(QSize(150, 150))
        self.cpsModeDial.setMinimum(-1)
        self.cpsModeDial.setMaximum(1)
        self.cpsModeDial.setValue(0)
        self.cpsModeDial.setSliderPosition(0)
        self.cpsModeDial.setInvertedAppearance(False)
        self.cpsModeDial.setInvertedControls(False)
        self.cpsModeDial.setNotchTarget(0.000000000000000)
        self.cpsModeDial.setNotchesVisible(True)

        self.verticalLayout_2.addWidget(self.cpsModeDial, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.chassisPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 35))
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setMargin(10)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.chassisPage)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.chassisPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 20))
        self.label_10.setMaximumSize(QSize(20, 20))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_12 = QLabel(self.chassisPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(20, 20))
        self.label_12.setMaximumSize(QSize(20, 20))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_11 = QLabel(self.chassisPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(20, 20))
        self.label_11.setMaximumSize(QSize(20, 20))
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_9 = QLabel(self.chassisPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(20, 20))
        self.label_9.setMaximumSize(QSize(20, 20))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_8 = QLabel(self.chassisPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(20, 20))
        self.label_8.setMaximumSize(QSize(20, 20))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_7 = QLabel(self.chassisPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setMaximumSize(QSize(20, 20))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.chassisPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 20))
        self.label_6.setMaximumSize(QSize(20, 20))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_17 = QLabel(self.chassisPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(20, 20))
        self.label_17.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.label_17)

        self.label_21 = QLabel(self.chassisPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(20, 20))
        self.label_21.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.label_21)

        self.label_20 = QLabel(self.chassisPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(20, 20))
        self.label_20.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.label_20)

        self.label_16 = QLabel(self.chassisPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(20, 20))
        self.label_16.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_18 = QLabel(self.chassisPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(20, 20))
        self.label_18.setMaximumSize(QSize(20, 20))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_18)

        self.label_15 = QLabel(self.chassisPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(20, 20))
        self.label_15.setMaximumSize(QSize(20, 20))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_19 = QLabel(self.chassisPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(20, 20))
        self.label_19.setMaximumSize(QSize(20, 20))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.label_14 = QLabel(self.chassisPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(20, 20))
        self.label_14.setMaximumSize(QSize(20, 20))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.label_13 = QLabel(self.chassisPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(20, 20))
        self.label_13.setMaximumSize(QSize(20, 20))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_13)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.windCompensationSlider = QSlider(self.chassisPage)
        self.windCompensationSlider.setObjectName(u"windCompensationSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.windCompensationSlider.sizePolicy().hasHeightForWidth())
        self.windCompensationSlider.setSizePolicy(sizePolicy4)
        self.windCompensationSlider.setMinimumSize(QSize(400, 50))
        self.windCompensationSlider.setMaximumSize(QSize(16777215, 50))
        self.windCompensationSlider.setMinimum(1)
        self.windCompensationSlider.setMaximum(7)
        self.windCompensationSlider.setSingleStep(1)
        self.windCompensationSlider.setPageStep(0)
        self.windCompensationSlider.setValue(4)
        self.windCompensationSlider.setOrientation(Qt.Horizontal)
        self.windCompensationSlider.setInvertedAppearance(False)
        self.windCompensationSlider.setTickPosition(QSlider.TicksAbove)
        self.windCompensationSlider.setTickInterval(1)

        self.gridLayout_4.addWidget(self.windCompensationSlider, 2, 0, 1, 1)

        self.laneSelectionSlider = QSlider(self.chassisPage)
        self.laneSelectionSlider.setObjectName(u"laneSelectionSlider")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.laneSelectionSlider.sizePolicy().hasHeightForWidth())
        self.laneSelectionSlider.setSizePolicy(sizePolicy5)
        self.laneSelectionSlider.setMinimumSize(QSize(400, 50))
        self.laneSelectionSlider.setMaximumSize(QSize(500, 50))
        self.laneSelectionSlider.setMinimum(1)
        self.laneSelectionSlider.setMaximum(9)
        self.laneSelectionSlider.setPageStep(0)
        self.laneSelectionSlider.setOrientation(Qt.Horizontal)
        self.laneSelectionSlider.setInvertedAppearance(False)
        self.laneSelectionSlider.setTickPosition(QSlider.TicksAbove)
        self.laneSelectionSlider.setTickInterval(1)

        self.gridLayout_4.addWidget(self.laneSelectionSlider, 2, 1, 1, 1)

        self.label_2 = QLabel(self.chassisPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(400, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.chassisPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.chassisPage)
        self.boomControlPage = QWidget()
        self.boomControlPage.setObjectName(u"boomControlPage")
        self.gridLayout_5 = QGridLayout(self.boomControlPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.boomUpButton = QPushButton(self.boomControlPage)
        self.boomUpButton.setObjectName(u"boomUpButton")
        self.boomUpButton.setMinimumSize(QSize(150, 150))
        self.boomUpButton.setMaximumSize(QSize(150, 150))
        self.boomUpButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.boomUpButton, 0, 0, 1, 1)

        self.boomUpFullButton = QPushButton(self.boomControlPage)
        self.boomUpFullButton.setObjectName(u"boomUpFullButton")
        self.boomUpFullButton.setMinimumSize(QSize(150, 150))
        self.boomUpFullButton.setMaximumSize(QSize(150, 150))
        self.boomUpFullButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.boomUpFullButton, 0, 1, 1, 1)

        self.gantryTieDownNotReleasedButton = QPushButton(self.boomControlPage)
        self.gantryTieDownNotReleasedButton.setObjectName(u"gantryTieDownNotReleasedButton")
        self.gantryTieDownNotReleasedButton.setMinimumSize(QSize(150, 150))
        self.gantryTieDownNotReleasedButton.setMaximumSize(QSize(150, 150))
        self.gantryTieDownNotReleasedButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.gantryTieDownNotReleasedButton, 0, 2, 1, 1)

        self.gantryMotorBrakesOpenButton = QPushButton(self.boomControlPage)
        self.gantryMotorBrakesOpenButton.setObjectName(u"gantryMotorBrakesOpenButton")
        self.gantryMotorBrakesOpenButton.setMinimumSize(QSize(150, 150))
        self.gantryMotorBrakesOpenButton.setMaximumSize(QSize(150, 150))
        self.gantryMotorBrakesOpenButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.gantryMotorBrakesOpenButton, 0, 3, 1, 1)

        self.boomUpFullIndication = QToolButton(self.boomControlPage)
        self.boomUpFullIndication.setObjectName(u"boomUpFullIndication")
        self.boomUpFullIndication.setEnabled(False)
        self.boomUpFullIndication.setMinimumSize(QSize(120, 100))
        self.boomUpFullIndication.setIcon(icon1)
        self.boomUpFullIndication.setIconSize(QSize(80, 80))
        self.boomUpFullIndication.setCheckable(True)
        self.boomUpFullIndication.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_5.addWidget(self.boomUpFullIndication, 0, 4, 1, 1)

        self.boomStopButton = QPushButton(self.boomControlPage)
        self.boomStopButton.setObjectName(u"boomStopButton")
        self.boomStopButton.setMinimumSize(QSize(150, 150))
        self.boomStopButton.setMaximumSize(QSize(150, 150))
        self.boomStopButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.boomStopButton, 1, 0, 1, 1)

        self.boomDownButton = QPushButton(self.boomControlPage)
        self.boomDownButton.setObjectName(u"boomDownButton")
        self.boomDownButton.setMinimumSize(QSize(150, 150))
        self.boomDownButton.setMaximumSize(QSize(150, 150))
        self.boomDownButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.boomDownButton, 1, 1, 1, 1)

        self.gantryStormPinNotReleasedButton = QPushButton(self.boomControlPage)
        self.gantryStormPinNotReleasedButton.setObjectName(u"gantryStormPinNotReleasedButton")
        self.gantryStormPinNotReleasedButton.setMinimumSize(QSize(150, 150))
        self.gantryStormPinNotReleasedButton.setMaximumSize(QSize(150, 150))
        self.gantryStormPinNotReleasedButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.gantryStormPinNotReleasedButton, 1, 2, 1, 1)

        self.bhCycleCompleteIndicator = QToolButton(self.boomControlPage)
        self.bhCycleCompleteIndicator.setObjectName(u"bhCycleCompleteIndicator")
        self.bhCycleCompleteIndicator.setEnabled(False)
        self.bhCycleCompleteIndicator.setMinimumSize(QSize(120, 100))
        self.bhCycleCompleteIndicator.setIcon(icon1)
        self.bhCycleCompleteIndicator.setIconSize(QSize(80, 80))
        self.bhCycleCompleteIndicator.setCheckable(True)
        self.bhCycleCompleteIndicator.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_5.addWidget(self.bhCycleCompleteIndicator, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.boomControlPage)
        self.assistFunctionsPage = QWidget()
        self.assistFunctionsPage.setObjectName(u"assistFunctionsPage")
        self.gridLayout_6 = QGridLayout(self.assistFunctionsPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.seeNotesButton_4 = QPushButton(self.assistFunctionsPage)
        self.seeNotesButton_4.setObjectName(u"seeNotesButton_4")
        self.seeNotesButton_4.setMinimumSize(QSize(150, 150))
        self.seeNotesButton_4.setMaximumSize(QSize(150, 150))
        self.seeNotesButton_4.setCheckable(True)

        self.gridLayout_6.addWidget(self.seeNotesButton_4, 0, 0, 1, 1)

        self.option5Button_4 = QPushButton(self.assistFunctionsPage)
        self.option5Button_4.setObjectName(u"option5Button_4")
        self.option5Button_4.setMinimumSize(QSize(150, 150))
        self.option5Button_4.setMaximumSize(QSize(150, 150))
        self.option5Button_4.setCheckable(True)

        self.gridLayout_6.addWidget(self.option5Button_4, 0, 1, 1, 1)

        self.option6Button_4 = QPushButton(self.assistFunctionsPage)
        self.option6Button_4.setObjectName(u"option6Button_4")
        self.option6Button_4.setMinimumSize(QSize(150, 150))
        self.option6Button_4.setMaximumSize(QSize(150, 150))
        self.option6Button_4.setCheckable(True)

        self.gridLayout_6.addWidget(self.option6Button_4, 1, 0, 1, 1)

        self.option7Button_4 = QPushButton(self.assistFunctionsPage)
        self.option7Button_4.setObjectName(u"option7Button_4")
        self.option7Button_4.setMinimumSize(QSize(150, 150))
        self.option7Button_4.setMaximumSize(QSize(150, 150))
        self.option7Button_4.setCheckable(True)

        self.gridLayout_6.addWidget(self.option7Button_4, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.assistFunctionsPage)

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)

        PLCApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(PLCApp)

        QMetaObject.connectSlotsByName(PLCApp)
    # setupUi

    def retranslateUi(self, PLCApp):
        PLCApp.setWindowTitle(QCoreApplication.translate("PLCApp", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        PLCApp.setAccessibleName(QCoreApplication.translate("PLCApp", u"mainwindow", None))
#endif // QT_CONFIG(accessibility)
        self.hoistLoad.setText(QCoreApplication.translate("PLCApp", u"0.6", None))
        self.hoistLoadLabel.setText(QCoreApplication.translate("PLCApp", u"Hoist Load", None))
        self.windSpeed.setText(QCoreApplication.translate("PLCApp", u"0.6", None))
        self.windSpeedLabel.setText(QCoreApplication.translate("PLCApp", u"Wind Speed", None))
        self.trimAngle.setText(QCoreApplication.translate("PLCApp", u"0.6", None))
        self.trimAngleLabel.setText(QCoreApplication.translate("PLCApp", u"Trim Angle", None))
        self.listAngle.setText(QCoreApplication.translate("PLCApp", u"0.6", None))
        self.listAngleLabel.setText(QCoreApplication.translate("PLCApp", u"List Angle", None))
        self.skewAngle.setText(QCoreApplication.translate("PLCApp", u"0.6", None))
        self.skewAngleLabel.setText(QCoreApplication.translate("PLCApp", u"Skew Angle", None))
        self.pageLabel.setText(QCoreApplication.translate("PLCApp", u"CCTV", None))
        self.spreaderTWLUnlocked.setText(QCoreApplication.translate("PLCApp", u"Spreader Twl \n"
"Unlocked", None))
        self.spreaderTWLLocked.setText(QCoreApplication.translate("PLCApp", u"Spreader Twl \n"
"Locked", None))
        self.spreaderLanded.setText(QCoreApplication.translate("PLCApp", u"Spreader\n"
"Landed", None))
        self.housingDown.setText(QCoreApplication.translate("PLCApp", u"Spreader twin\n"
"Housing Down", None))
        self.slackRobe.setText(QCoreApplication.translate("PLCApp", u"Slack Robe\n"
"HB", None))
        self.hoistOverload.setText(QCoreApplication.translate("PLCApp", u"Hoist\n"
"Overload", None))
        self.trolleyBlocking.setText(QCoreApplication.translate("PLCApp", u"Trolley\n"
"Blocking", None))
        self.cpsActive.setText(QCoreApplication.translate("PLCApp", u"CPS Active\n"
"", None))
        self.reloadButton.setText("")
        self.connectButton.setText("")
        self.cctvButton.setText(QCoreApplication.translate("PLCApp", u"CCTV", None))
        self.spreaderButton.setText(QCoreApplication.translate("PLCApp", u"Spreader", None))
        self.chassisButton.setText(QCoreApplication.translate("PLCApp", u"Chassis", None))
        self.boomControlButton.setText(QCoreApplication.translate("PLCApp", u"Boom Control", None))
        self.assistFunctionsButton.setText(QCoreApplication.translate("PLCApp", u"Assist Functions", None))
        self.craneEntranceButton.setText(QCoreApplication.translate("PLCApp", u"Crane\n"
"Entrance", None))
        self.gantryRightWideButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Right\n"
"Wide", None))
        self.boomMotionWideButton.setText(QCoreApplication.translate("PLCApp", u"Boom Motion\n"
"Wide", None))
        self.landingPlatformButton.setText(QCoreApplication.translate("PLCApp", u"Landing\n"
"Platform", None))
        self.boomMotionButton.setText(QCoreApplication.translate("PLCApp", u"Boom\n"
"Motion", None))
        self.gantryRightButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Right", None))
        self.highSpreaderButton.setText(QCoreApplication.translate("PLCApp", u"High\n"
"Spreader", None))
        self.gantryLeftButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Left", None))
        self.landingPlatformWideButton.setText(QCoreApplication.translate("PLCApp", u"Landing\n"
"Platform Wide", None))
        self.hatchCoverSingleButton.setText(QCoreApplication.translate("PLCApp", u"Hatch Cover\n"
"Single", None))
        self.hatchCoverSingleWideButton.setText(QCoreApplication.translate("PLCApp", u"Hatch Cover\n"
"Single Wide", None))
        self.spreaderOverviewButton.setText(QCoreApplication.translate("PLCApp", u"Spreader\n"
"Overview", None))
        self.gantryLeftWideButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Left\n"
"Wide", None))
        self.normalContainerButton.setText(QCoreApplication.translate("PLCApp", u"Normal\n"
"Container", None))
        self.spHookModeButton.setText(QCoreApplication.translate("PLCApp", u"Spreader/Hook\n"
"Mode", None))
        self.overHeightModeButton.setText(QCoreApplication.translate("PLCApp", u"Over Heigt Mode", None))
        self.overHeightIndicator.setText(QCoreApplication.translate("PLCApp", u"Over Height", None))
        self.ttdsFaultIndicator.setText(QCoreApplication.translate("PLCApp", u"TTDS Fault", None))
        self.lampTestButton.setText(QCoreApplication.translate("PLCApp", u"Lamp Test", None))
        self.hoistSnagLoadIndicator.setText(QCoreApplication.translate("PLCApp", u"Hoist Snag\n"
"Load", None))
        self.highWindSpeedIndicator.setText(QCoreApplication.translate("PLCApp", u"High Wind\n"
"Speed", None))
        self.cpsAlignmentButton.setText(QCoreApplication.translate("PLCApp", u"CPS Alignment", None))
        self.cpsReverseDirectionButton.setText(QCoreApplication.translate("PLCApp", u"CPS Reverse\n"
"Direction", None))
        self.label.setText(QCoreApplication.translate("PLCApp", u"0", None))
        self.label_3.setText(QCoreApplication.translate("PLCApp", u"T                   R", None))
        self.label_5.setText(QCoreApplication.translate("PLCApp", u"CPS Loading ", None))
        self.label_10.setText(QCoreApplication.translate("PLCApp", u"-3", None))
        self.label_12.setText(QCoreApplication.translate("PLCApp", u"-2", None))
        self.label_11.setText(QCoreApplication.translate("PLCApp", u"-1", None))
        self.label_9.setText(QCoreApplication.translate("PLCApp", u"0", None))
        self.label_8.setText(QCoreApplication.translate("PLCApp", u"1", None))
        self.label_7.setText(QCoreApplication.translate("PLCApp", u"2", None))
        self.label_6.setText(QCoreApplication.translate("PLCApp", u"3", None))
        self.label_17.setText(QCoreApplication.translate("PLCApp", u"1", None))
        self.label_21.setText(QCoreApplication.translate("PLCApp", u"2", None))
        self.label_20.setText(QCoreApplication.translate("PLCApp", u"3", None))
        self.label_16.setText(QCoreApplication.translate("PLCApp", u"4", None))
        self.label_18.setText(QCoreApplication.translate("PLCApp", u"5", None))
        self.label_15.setText(QCoreApplication.translate("PLCApp", u"6", None))
        self.label_19.setText(QCoreApplication.translate("PLCApp", u"7", None))
        self.label_14.setText(QCoreApplication.translate("PLCApp", u"8", None))
        self.label_13.setText(QCoreApplication.translate("PLCApp", u"9", None))
        self.label_2.setText(QCoreApplication.translate("PLCApp", u"CPS Wind Compensation", None))
        self.label_4.setText(QCoreApplication.translate("PLCApp", u"CPS Lane Selection", None))
        self.boomUpButton.setText(QCoreApplication.translate("PLCApp", u"Boom Up\n"
"60 Deg", None))
        self.boomUpFullButton.setText(QCoreApplication.translate("PLCApp", u"Boom Up\n"
"Full", None))
        self.gantryTieDownNotReleasedButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Tie Down\n"
"Not Released", None))
        self.gantryMotorBrakesOpenButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Motor\n"
"Brakes Open", None))
        self.boomUpFullIndication.setText(QCoreApplication.translate("PLCApp", u"Boom Up\n"
"Full", None))
        self.boomStopButton.setText(QCoreApplication.translate("PLCApp", u"Boom Stop", None))
        self.boomDownButton.setText(QCoreApplication.translate("PLCApp", u"Boom Down", None))
        self.gantryStormPinNotReleasedButton.setText(QCoreApplication.translate("PLCApp", u"Gantry Storm Pin\n"
"Not Released", None))
        self.bhCycleCompleteIndicator.setText(QCoreApplication.translate("PLCApp", u"BH Cycle\n"
"Complete", None))
        self.seeNotesButton_4.setText(QCoreApplication.translate("PLCApp", u"See Notes", None))
        self.option5Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 5", None))
        self.option6Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 6", None))
        self.option7Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 7", None))
    # retranslateUi

