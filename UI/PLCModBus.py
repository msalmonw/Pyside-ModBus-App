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
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_PLCApp(object):
    def setupUi(self, PLCApp):
        if not PLCApp.objectName():
            PLCApp.setObjectName(u"PLCApp")
        PLCApp.resize(1280, 720)
        PLCApp.setMinimumSize(QSize(1280, 720))
        PLCApp.setMaximumSize(QSize(16777215, 16777215))
        PLCApp.setStyleSheet(u"")
        PLCApp.setIconSize(QSize(32, 48))
        self.centralwidget = QWidget(PLCApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background:rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 6px solid;\n"
"border-color: rgb(255, 0, 0);\n"
"}\n"
"QWidget{\n"
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
"QPushButton#reloadButton{\n"
"background: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#reloadButton:pressed{\n"
"border: 3px solid grey;\n"
"}\n"
"QLabel#hoistLoad, #windSpeed, #trimAngle, #listAngle, #skewAngle{\n"
"background: rgb(255, 204, 188);\n"
"color: rgb(255, 61, 0);\n"
"font-size: 22px;\n"
""
                        "}\n"
"QLabel#pageLabel{\n"
"font-size: 22px;\n"
"}\n"
"QDial{\n"
"background: rgb(0, 70, 100);\n"
"color: rbg(0, 0, 0);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"height: 20px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background: rgb(0, 70, 100);\n"
"border-radius: 3px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 20, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.reloadButton = QPushButton(self.centralwidget)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setMinimumSize(QSize(50, 50))
        self.reloadButton.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u"UI/resources/reloading.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadButton.setIcon(icon)
        self.reloadButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.reloadButton)

        self.cctvButton = QPushButton(self.centralwidget)
        self.cctvButton.setObjectName(u"cctvButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cctvButton.sizePolicy().hasHeightForWidth())
        self.cctvButton.setSizePolicy(sizePolicy)
        self.cctvButton.setMinimumSize(QSize(180, 50))
        self.cctvButton.setMaximumSize(QSize(180, 50))
        self.cctvButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.cctvButton)

        self.spreaderButton = QPushButton(self.centralwidget)
        self.spreaderButton.setObjectName(u"spreaderButton")
        sizePolicy.setHeightForWidth(self.spreaderButton.sizePolicy().hasHeightForWidth())
        self.spreaderButton.setSizePolicy(sizePolicy)
        self.spreaderButton.setMinimumSize(QSize(180, 50))
        self.spreaderButton.setMaximumSize(QSize(180, 50))
        self.spreaderButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.spreaderButton)

        self.chassisButton = QPushButton(self.centralwidget)
        self.chassisButton.setObjectName(u"chassisButton")
        sizePolicy.setHeightForWidth(self.chassisButton.sizePolicy().hasHeightForWidth())
        self.chassisButton.setSizePolicy(sizePolicy)
        self.chassisButton.setMinimumSize(QSize(180, 50))
        self.chassisButton.setMaximumSize(QSize(180, 50))
        self.chassisButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.chassisButton)

        self.boomControlButton = QPushButton(self.centralwidget)
        self.boomControlButton.setObjectName(u"boomControlButton")
        sizePolicy.setHeightForWidth(self.boomControlButton.sizePolicy().hasHeightForWidth())
        self.boomControlButton.setSizePolicy(sizePolicy)
        self.boomControlButton.setMinimumSize(QSize(180, 50))
        self.boomControlButton.setMaximumSize(QSize(180, 50))
        self.boomControlButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.boomControlButton)

        self.assistFunctionsButton = QPushButton(self.centralwidget)
        self.assistFunctionsButton.setObjectName(u"assistFunctionsButton")
        sizePolicy.setHeightForWidth(self.assistFunctionsButton.sizePolicy().hasHeightForWidth())
        self.assistFunctionsButton.setSizePolicy(sizePolicy)
        self.assistFunctionsButton.setMinimumSize(QSize(180, 50))
        self.assistFunctionsButton.setMaximumSize(QSize(180, 50))
        self.assistFunctionsButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.assistFunctionsButton)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.sideInfoWidget = QWidget(self.centralwidget)
        self.sideInfoWidget.setObjectName(u"sideInfoWidget")
        self.sideInfoWidget.setMinimumSize(QSize(120, 0))
        self.verticalLayout = QVBoxLayout(self.sideInfoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hoistLoad = QLabel(self.sideInfoWidget)
        self.hoistLoad.setObjectName(u"hoistLoad")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hoistLoad.sizePolicy().hasHeightForWidth())
        self.hoistLoad.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.windSpeed.sizePolicy().hasHeightForWidth())
        self.windSpeed.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.trimAngle.sizePolicy().hasHeightForWidth())
        self.trimAngle.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.listAngle.sizePolicy().hasHeightForWidth())
        self.listAngle.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.skewAngle.sizePolicy().hasHeightForWidth())
        self.skewAngle.setSizePolicy(sizePolicy1)
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
        icon1 = QIcon()
        icon1.addFile(u"UI/resources/redlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spreaderTWLUnlocked.setIcon(icon1)
        self.spreaderTWLUnlocked.setIconSize(QSize(80, 80))
        self.spreaderTWLUnlocked.setCheckable(True)
        self.spreaderTWLUnlocked.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderTWLUnlocked)

        self.spreaderTWLLocked = QToolButton(self.topInfoWidget)
        self.spreaderTWLLocked.setObjectName(u"spreaderTWLLocked")
        self.spreaderTWLLocked.setMinimumSize(QSize(120, 100))
        icon2 = QIcon()
        icon2.addFile(u"UI/resources/greenlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spreaderTWLLocked.setIcon(icon2)
        self.spreaderTWLLocked.setIconSize(QSize(80, 80))
        self.spreaderTWLLocked.setCheckable(True)
        self.spreaderTWLLocked.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderTWLLocked)

        self.spreaderLanded = QToolButton(self.topInfoWidget)
        self.spreaderLanded.setObjectName(u"spreaderLanded")
        self.spreaderLanded.setMinimumSize(QSize(120, 100))
        self.spreaderLanded.setIcon(icon2)
        self.spreaderLanded.setIconSize(QSize(80, 80))
        self.spreaderLanded.setCheckable(True)
        self.spreaderLanded.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.spreaderLanded)

        self.housingDown = QToolButton(self.topInfoWidget)
        self.housingDown.setObjectName(u"housingDown")
        self.housingDown.setMinimumSize(QSize(120, 100))
        icon3 = QIcon()
        icon3.addFile(u"UI/resources/yellowlight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.housingDown.setIcon(icon3)
        self.housingDown.setIconSize(QSize(80, 80))
        self.housingDown.setCheckable(True)
        self.housingDown.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.housingDown)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.slackRobe = QToolButton(self.topInfoWidget)
        self.slackRobe.setObjectName(u"slackRobe")
        self.slackRobe.setMinimumSize(QSize(120, 100))
        self.slackRobe.setIcon(icon3)
        self.slackRobe.setIconSize(QSize(80, 80))
        self.slackRobe.setCheckable(True)
        self.slackRobe.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.slackRobe)

        self.hoistOverload = QToolButton(self.topInfoWidget)
        self.hoistOverload.setObjectName(u"hoistOverload")
        self.hoistOverload.setMinimumSize(QSize(120, 100))
        self.hoistOverload.setIcon(icon3)
        self.hoistOverload.setIconSize(QSize(80, 80))
        self.hoistOverload.setCheckable(True)
        self.hoistOverload.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.hoistOverload)

        self.trolleyBlocking = QToolButton(self.topInfoWidget)
        self.trolleyBlocking.setObjectName(u"trolleyBlocking")
        self.trolleyBlocking.setMinimumSize(QSize(120, 100))
        self.trolleyBlocking.setIcon(icon3)
        self.trolleyBlocking.setIconSize(QSize(80, 80))
        self.trolleyBlocking.setCheckable(True)
        self.trolleyBlocking.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.trolleyBlocking)

        self.cpsActive = QToolButton(self.topInfoWidget)
        self.cpsActive.setObjectName(u"cpsActive")
        self.cpsActive.setMinimumSize(QSize(120, 100))
        self.cpsActive.setIcon(icon2)
        self.cpsActive.setIconSize(QSize(80, 80))
        self.cpsActive.setCheckable(True)
        self.cpsActive.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.cpsActive)


        self.gridLayout.addWidget(self.topInfoWidget, 0, 1, 1, 1)

        self.pageLabel = QLabel(self.centralwidget)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setMinimumSize(QSize(0, 50))
        self.pageLabel.setMaximumSize(QSize(16777215, 50))
        self.pageLabel.setMargin(10)

        self.gridLayout.addWidget(self.pageLabel, 1, 1, 1, 1)

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
        self.seeNotesButton = QPushButton(self.spreaderPage)
        self.seeNotesButton.setObjectName(u"seeNotesButton")
        self.seeNotesButton.setMinimumSize(QSize(150, 150))
        self.seeNotesButton.setMaximumSize(QSize(150, 150))
        self.seeNotesButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.seeNotesButton, 0, 0, 1, 1)

        self.option5Button = QPushButton(self.spreaderPage)
        self.option5Button.setObjectName(u"option5Button")
        self.option5Button.setMinimumSize(QSize(150, 150))
        self.option5Button.setMaximumSize(QSize(150, 150))
        self.option5Button.setCheckable(True)

        self.gridLayout_3.addWidget(self.option5Button, 0, 1, 1, 1)

        self.option6Button = QPushButton(self.spreaderPage)
        self.option6Button.setObjectName(u"option6Button")
        self.option6Button.setMinimumSize(QSize(150, 150))
        self.option6Button.setMaximumSize(QSize(150, 150))
        self.option6Button.setCheckable(True)

        self.gridLayout_3.addWidget(self.option6Button, 1, 0, 1, 1)

        self.option7Button = QPushButton(self.spreaderPage)
        self.option7Button.setObjectName(u"option7Button")
        self.option7Button.setMinimumSize(QSize(150, 150))
        self.option7Button.setMaximumSize(QSize(150, 150))
        self.option7Button.setCheckable(True)

        self.gridLayout_3.addWidget(self.option7Button, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.spreaderPage)
        self.chassisPage = QWidget()
        self.chassisPage.setObjectName(u"chassisPage")
        self.gridLayout_4 = QGridLayout(self.chassisPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.seeNotesButton_2 = QPushButton(self.chassisPage)
        self.seeNotesButton_2.setObjectName(u"seeNotesButton_2")
        self.seeNotesButton_2.setMinimumSize(QSize(150, 150))
        self.seeNotesButton_2.setMaximumSize(QSize(150, 150))
        self.seeNotesButton_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.seeNotesButton_2, 0, 0, 1, 1)

        self.option5Button_2 = QPushButton(self.chassisPage)
        self.option5Button_2.setObjectName(u"option5Button_2")
        self.option5Button_2.setMinimumSize(QSize(150, 150))
        self.option5Button_2.setMaximumSize(QSize(150, 150))
        self.option5Button_2.setStyleSheet(u"")
        self.option5Button_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.option5Button_2, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(self.chassisPage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.dialOne = QDial(self.chassisPage)
        self.dialOne.setObjectName(u"dialOne")
        self.dialOne.setMinimumSize(QSize(150, 150))
        self.dialOne.setMaximumSize(QSize(150, 150))
        self.dialOne.setMinimum(-1)
        self.dialOne.setMaximum(1)
        self.dialOne.setValue(0)
        self.dialOne.setSliderPosition(0)
        self.dialOne.setInvertedAppearance(False)
        self.dialOne.setInvertedControls(False)
        self.dialOne.setNotchTarget(0.000000000000000)
        self.dialOne.setNotchesVisible(True)

        self.verticalLayout_2.addWidget(self.dialOne, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.chassisPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setMargin(10)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.option6Button_2 = QPushButton(self.chassisPage)
        self.option6Button_2.setObjectName(u"option6Button_2")
        self.option6Button_2.setMinimumSize(QSize(150, 150))
        self.option6Button_2.setMaximumSize(QSize(150, 150))
        self.option6Button_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.option6Button_2, 1, 0, 1, 1)

        self.option7Button_2 = QPushButton(self.chassisPage)
        self.option7Button_2.setObjectName(u"option7Button_2")
        self.option7Button_2.setMinimumSize(QSize(150, 150))
        self.option7Button_2.setMaximumSize(QSize(150, 150))
        self.option7Button_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.option7Button_2, 1, 1, 1, 1)

        self.horizontalSlider = QSlider(self.chassisPage)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(600, 50))
        self.horizontalSlider.setMaximumSize(QSize(600, 50))
        self.horizontalSlider.setMinimum(-3)
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)

        self.gridLayout_4.addWidget(self.horizontalSlider, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.chassisPage)
        self.boomControlPage = QWidget()
        self.boomControlPage.setObjectName(u"boomControlPage")
        self.gridLayout_5 = QGridLayout(self.boomControlPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.seeNotesButton_3 = QPushButton(self.boomControlPage)
        self.seeNotesButton_3.setObjectName(u"seeNotesButton_3")
        self.seeNotesButton_3.setMinimumSize(QSize(150, 150))
        self.seeNotesButton_3.setMaximumSize(QSize(150, 150))
        self.seeNotesButton_3.setCheckable(True)

        self.gridLayout_5.addWidget(self.seeNotesButton_3, 0, 0, 1, 1)

        self.option5Button_3 = QPushButton(self.boomControlPage)
        self.option5Button_3.setObjectName(u"option5Button_3")
        self.option5Button_3.setMinimumSize(QSize(150, 150))
        self.option5Button_3.setMaximumSize(QSize(150, 150))
        self.option5Button_3.setCheckable(True)

        self.gridLayout_5.addWidget(self.option5Button_3, 0, 1, 1, 1)

        self.option6Button_3 = QPushButton(self.boomControlPage)
        self.option6Button_3.setObjectName(u"option6Button_3")
        self.option6Button_3.setMinimumSize(QSize(150, 150))
        self.option6Button_3.setMaximumSize(QSize(150, 150))
        self.option6Button_3.setCheckable(True)

        self.gridLayout_5.addWidget(self.option6Button_3, 1, 0, 1, 1)

        self.option7Button_3 = QPushButton(self.boomControlPage)
        self.option7Button_3.setObjectName(u"option7Button_3")
        self.option7Button_3.setMinimumSize(QSize(150, 150))
        self.option7Button_3.setMaximumSize(QSize(150, 150))
        self.option7Button_3.setCheckable(True)

        self.gridLayout_5.addWidget(self.option7Button_3, 1, 1, 1, 1)

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
        self.reloadButton.setText("")
        self.cctvButton.setText(QCoreApplication.translate("PLCApp", u"CCTV", None))
        self.spreaderButton.setText(QCoreApplication.translate("PLCApp", u"Spreader", None))
        self.chassisButton.setText(QCoreApplication.translate("PLCApp", u"Chassis", None))
        self.boomControlButton.setText(QCoreApplication.translate("PLCApp", u"Boom Control", None))
        self.assistFunctionsButton.setText(QCoreApplication.translate("PLCApp", u"Assist Functions", None))
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
        self.pageLabel.setText(QCoreApplication.translate("PLCApp", u"CCTV", None))
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
        self.seeNotesButton.setText(QCoreApplication.translate("PLCApp", u"See Notes", None))
        self.option5Button.setText(QCoreApplication.translate("PLCApp", u"Option 5", None))
        self.option6Button.setText(QCoreApplication.translate("PLCApp", u"Option 6", None))
        self.option7Button.setText(QCoreApplication.translate("PLCApp", u"Option 7", None))
        self.seeNotesButton_2.setText(QCoreApplication.translate("PLCApp", u"See Notes", None))
        self.option5Button_2.setText(QCoreApplication.translate("PLCApp", u"Option 5", None))
        self.label.setText(QCoreApplication.translate("PLCApp", u"0", None))
        self.label_3.setText(QCoreApplication.translate("PLCApp", u"T                   R", None))
        self.option6Button_2.setText(QCoreApplication.translate("PLCApp", u"Option 6", None))
        self.option7Button_2.setText(QCoreApplication.translate("PLCApp", u"Option 7", None))
        self.seeNotesButton_3.setText(QCoreApplication.translate("PLCApp", u"See Notes", None))
        self.option5Button_3.setText(QCoreApplication.translate("PLCApp", u"Option 5", None))
        self.option6Button_3.setText(QCoreApplication.translate("PLCApp", u"Option 6", None))
        self.option7Button_3.setText(QCoreApplication.translate("PLCApp", u"Option 7", None))
        self.seeNotesButton_4.setText(QCoreApplication.translate("PLCApp", u"See Notes", None))
        self.option5Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 5", None))
        self.option6Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 6", None))
        self.option7Button_4.setText(QCoreApplication.translate("PLCApp", u"Option 7", None))
    # retranslateUi

