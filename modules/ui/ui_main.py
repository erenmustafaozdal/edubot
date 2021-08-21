# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.styleSheet.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"APP STYLES - DARK THEME\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"    color: #dddddd;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid #2c313a;\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid #6F99CB; /* A\u00e7\u0131k Mavi */\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {    \n"
"    background-color: #282c"
                        "34;\n"
"    border: 1px solid #2c313a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {   \n"
"    background-color: #21252b;\n"
"}\n"
"#topLogo {\n"
"    background-color: #21252b;\n"
"    background-image: url(:/images/images/images/edubot_kare_logo.png);\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 20pt \"Bahn Pro\", 12pt \"Segoe UI\";\n"
"    letter-spacing: 4px;\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 12pt \"Caveat Brush\", 8pt \"Segoe UI\";\n"
"    letter-spacing: 0.5px;\n"
"    color: #F96A76; /* K\u0131rm\u0131z\u0131 */\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton { \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#t"
                        "opMenu .QPushButton:hover {\n"
"    background-color: #282c34;\n"
"}\n"
"#topMenu .QPushButton:pressed { \n"
"    background-color: #3F72AF; /* Mavi */\n"
"    color: #FFFFFF;\n"
"}\n"
"#bottomMenu .QPushButton {  \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: #282c34;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {  \n"
"    background-color: #3F72AF; /* Mavi */\n"
"    color: #FFFFFF;\n"
"}\n"
"#leftMenuFrame{\n"
"    border-top: 3px solid #2C313A;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: #252930;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #717E"
                        "95;\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: #282C34;\n"
"}\n"
"#toggleButton:pressed {\n"
"    background-color: #3F72AF; /* Mavi */\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#teachersBox { \n"
"    background-color: #2C313A;\n"
"}\n"
"#extraTopBg{    \n"
"    background-color: #3F72AF /* Mavi */\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/icons/images/icons/people-fill.svg);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: #FFFFFF; }\n"
"\n"
"/* Btn Close */\n"
"#teachersBoxCloseBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#teachersBoxCloseBtn:hover { background-color: #6F99CB; border-style: solid; border-radius: 4px; } /* A\u00e7\u0131k Mavi */\n"
"#teachersBoxCloseBtn:pressed {"
                        " background-color: #38669D; border-style: solid; border-radius: 4px; } /* Mavi (Bir t\u0131k koyu) */\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"    border-top: 3px solid #282C34;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: #282C34;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {    \n"
"    background-color: #3F72AF; /* Mavi */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* Add Teacher Button */\n"
"#btn_add_teacher {\n"
"    border: 2px solid #112D4E;\n"
"    border-radius: 5px; \n"
"    background-color: #3F72AF;\n"
"	padding: 3px;\n"
"	margin: 5px 15px 20px 15px;\n"
"}\n"
"#btn_add_teacher:hover {\n"
"    background-color: #6F99CB;\n"
"    border: 2px solid #3F72AF;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
                        "\n"
"Content App */\n"
"#contentTopBg{  \n"
"    background-color: #21252B;\n"
"}\n"
"#contentBottom{\n"
"    border-top: 3px solid #2C313A;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #2C3139; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #171A1E; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #2C313A; }\n"
"#themeSettingsTopDetail { background-color: #3F72AF; } /* Mavi */\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #2C313A; }\n"
"#bottomBar QLabel { font-size: 11px; color: #717E95; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* Frame Size Grip */\n"
"#frame_size_grip {\n"
"    background-image: url(:/icons/images/icons/cil-size-grip.png);\n"
"    background-position: right bottom;\n"
"    "
                        "background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton { \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: #282C34;\n"
"}\n"
"#contentSettings .QPushButton:pressed { \n"
"    background-color: #3F72AF; /* Mavi */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {  \n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: #2C313A;\n"
"    border-bottom: 1px solid #2C313C;\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: #2C313C;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color:"
                        " #2C313C;\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: #3F72AF; /* Mavi */\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: #21252B;\n"
"    max-width: 30px;\n"
"    border: 1px solid #2C313A;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #2C313C;\n"
"    border-right: 1px solid #2C313C;\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: #21252B;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #21252B;\n"
"    background-color: #21252B;\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #2C313C;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"    background-color: #21252B;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #21252B;\n"
"    padding-left: 10px;\n"
"    selection-color: #FFFFFF;\n"
"  "
                        "  selection-background-color: #6F99CB;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid #404758;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #5B657C;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #1B1D23;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #6F99CB;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid #404758;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #5B657C;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #343B48;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0"
                        " 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3F72AF; /* Mavi */\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #373F4D;\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #373F4D;\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #343B48;\n"
"    width: 8px;\n"
" "
                        "   margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {  \n"
"    background: #3F72AF; /* Mavi */\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #373F4D;\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #373F4D;\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* //////////////////////////////////////////////////////////////////"
                        "///////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #343B48;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: #2C313C;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #3A4251;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #343B48;\n"
"    border: 3px solid #343B48;  \n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #343B48;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: #2C313C;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid #3A4251;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #5E6A82;\n"
"    border: 3px solid #343B48;  \n"
"}\n"
"\n"
"/* ////////////////////////////////////"
                        "/////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"    background-color: #1B1D23;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #21252B;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid #404758;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: #6F99CB;  \n"
"    background-color: #21252B;\n"
"    padding: 10px;\n"
"    selection-background-color: #272C36;\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////"
                        "///////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: #343B48;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: #373E4C;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #3F72AF; /* Mavi */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #5280B7; /* Mavi (Bir t\u0131k a\u00e7\u0131k)  */\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #6F99CB;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: #343B48;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: #373E4C;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #3F72AF; /* Mavi */\n"
"    border: none;\n"
"    height"
                        ": 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #5280B7; /* Mavi (Bir t\u0131k a\u00e7\u0131k)  */\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #6F99CB;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {    \n"
"    color: #6F99CB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #6F99CB; /* A\u00e7\u0131k Mavi */\n"
"}\n"
"QCommandLinkButton:hover {  \n"
"    color: #6F99CB; /* A\u00e7\u0131k Mavi */\n"
"    background-color: #2C313C;\n"
"}\n"
"QCommandLinkButton:pressed {    \n"
"    color: #3F72AF; /* Mavi */\n"
"    background-color: #343A47;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QGroupBox */\n"
"QGroupBox {\n"
"    border: 1px solid #5B657C;\n"
"    border-radius: 9px;\n"
""
                        "    margin-top: 10px;\n"
"    margin-bottom: 20px;\n"
"	font-size: 13px;\n"
"    font-weight: bold;\n"
"	background-color: #21252b;\n"
"	color: #F96A76;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Pages */\n"
"\n"
"/* Line */\n"
"Line {\n"
"	color: #5B657C;\n"
"}\n"
"\n"
"/* Page Title */\n"
"QLabel[class=\"page_title\"] {\n"
"	margin: 0 0 15px 0;\n"
"}\n"
"\n"
"/* Page Description */\n"
"QLabel[class=\"page_description\"] {\n"
"	margin: 0 0 5px 0;\n"
"}\n"
"\n"
"/* Form Description */\n"
"QLabel[class=\"form_description\"] {\n"
"	margin: 0 0 5px 0;\n"
"	color: #717E95;\n"
"}\n"
"\n"
"/* Field Description */\n"
"QLabel[class=\"field_description\"] {\n"
"	margin: 0 0 5px 0;\n"
"	color: #717E95;\n"
"	font-size: 11px;\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(240, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 5, 160, 25))
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 28, 160, 20))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 20))
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/list.svg);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/house-door-fill.svg);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_students = QPushButton(self.topMenu)
        self.btn_students.setObjectName(u"btn_students")
        sizePolicy.setHeightForWidth(self.btn_students.sizePolicy().hasHeightForWidth())
        self.btn_students.setSizePolicy(sizePolicy)
        self.btn_students.setMinimumSize(QSize(0, 45))
        self.btn_students.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_students.setStyleSheet(u"background-image: url(:/icons/images/icons/file-earmark-person-fill.svg);")

        self.verticalLayout_8.addWidget(self.btn_students)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMaximumSize(QSize(16777215, 16777215))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleTeachersBox = QPushButton(self.bottomMenu)
        self.toggleTeachersBox.setObjectName(u"toggleTeachersBox")
        sizePolicy.setHeightForWidth(self.toggleTeachersBox.sizePolicy().hasHeightForWidth())
        self.toggleTeachersBox.setSizePolicy(sizePolicy)
        self.toggleTeachersBox.setMinimumSize(QSize(0, 45))
        self.toggleTeachersBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleTeachersBox.setStyleSheet(u"background-image: url(:/icons/images/icons/people-fill.svg);")

        self.verticalLayout_9.addWidget(self.toggleTeachersBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.teachersBox = QFrame(self.bgApp)
        self.teachersBox.setObjectName(u"teachersBox")
        self.teachersBox.setMaximumSize(QSize(0, 16777215))
        self.teachersBox.setFrameShape(QFrame.NoFrame)
        self.teachersBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.teachersBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.teachersBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.teachersBoxCloseBtn = QPushButton(self.extraTopBg)
        self.teachersBoxCloseBtn.setObjectName(u"teachersBoxCloseBtn")
        self.teachersBoxCloseBtn.setMinimumSize(QSize(28, 28))
        self.teachersBoxCloseBtn.setMaximumSize(QSize(28, 28))
        self.teachersBoxCloseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.teachersBoxCloseBtn.setIcon(icon)
        self.teachersBoxCloseBtn.setIconSize(QSize(25, 25))

        self.extraTopLayout.addWidget(self.teachersBoxCloseBtn, 0, 2, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.teachersBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.teacher2 = QFrame(self.extraTopMenu)
        self.teacher2.setObjectName(u"teacher2")
        self.teacher2.setMinimumSize(QSize(0, 45))
        self.teacher2.setFrameShape(QFrame.NoFrame)
        self.teacher2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.teacher2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.teacherName2 = QPushButton(self.teacher2)
        self.teacherName2.setObjectName(u"teacherName2")
        self.teacherName2.setMinimumSize(QSize(0, 45))
        self.teacherName2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.teacherName2)

        self.teacherSelect2 = QRadioButton(self.teacher2)
        self.teacherRadioGroup = QButtonGroup(MainWindow)
        self.teacherRadioGroup.setObjectName(u"teacherRadioGroup")
        self.teacherRadioGroup.addButton(self.teacherSelect2)
        self.teacherSelect2.setObjectName(u"teacherSelect2")
        self.teacherSelect2.setMinimumSize(QSize(45, 45))
        self.teacherSelect2.setMaximumSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.teacherSelect2)


        self.verticalLayout_11.addWidget(self.teacher2)

        self.teacher1 = QFrame(self.extraTopMenu)
        self.teacher1.setObjectName(u"teacher1")
        self.teacher1.setMinimumSize(QSize(0, 45))
        self.teacher1.setFrameShape(QFrame.NoFrame)
        self.teacher1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.teacher1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.teacherName1 = QPushButton(self.teacher1)
        self.teacherName1.setObjectName(u"teacherName1")
        self.teacherName1.setMinimumSize(QSize(0, 45))
        self.teacherName1.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.teacherName1)

        self.teacherSelect1 = QRadioButton(self.teacher1)
        self.teacherRadioGroup.addButton(self.teacherSelect1)
        self.teacherSelect1.setObjectName(u"teacherSelect1")
        self.teacherSelect1.setMinimumSize(QSize(45, 45))
        self.teacherSelect1.setMaximumSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.teacherSelect1)


        self.verticalLayout_11.addWidget(self.teacher1, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.btn_add_teacher = QPushButton(self.extraContent)
        self.btn_add_teacher.setObjectName(u"btn_add_teacher")
        self.btn_add_teacher.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/person-plus-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_teacher.setIcon(icon1)

        self.verticalLayout_12.addWidget(self.btn_add_teacher)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.teachersBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setCursor(QCursor(Qt.SizeAllCursor))

        self.horizontalLayout_4.addWidget(self.titleRightInfo)


        self.horizontalLayout_3.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/gear-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/dash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/fullscreen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.content)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy2)
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/robot_hello.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.teacher = QWidget()
        self.teacher.setObjectName(u"teacher")
        self.verticalLayout = QVBoxLayout(self.teacher)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.teacher)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 290, 727))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 15, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.teacher_title = QLabel(self.frame)
        self.teacher_title.setObjectName(u"teacher_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.teacher_title.sizePolicy().hasHeightForWidth())
        self.teacher_title.setSizePolicy(sizePolicy3)
        self.teacher_title.setTextFormat(Qt.RichText)

        self.verticalLayout_13.addWidget(self.teacher_title)

        self.teacher_description = QLabel(self.frame)
        self.teacher_description.setObjectName(u"teacher_description")
        sizePolicy3.setHeightForWidth(self.teacher_description.sizePolicy().hasHeightForWidth())
        self.teacher_description.setSizePolicy(sizePolicy3)
        self.teacher_description.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.teacher_description)

        self.teacherPersonalInfo = QGroupBox(self.frame)
        self.teacherPersonalInfo.setObjectName(u"teacherPersonalInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.teacherPersonalInfo.sizePolicy().hasHeightForWidth())
        self.teacherPersonalInfo.setSizePolicy(sizePolicy4)
        self.teacherPersonalInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.teacherPersonalInfo.setFlat(False)
        self.teacherPersonalInfo.setCheckable(False)
        self.teacherPersonalInfo.setChecked(False)
        self._2 = QVBoxLayout(self.teacherPersonalInfo)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, 15, -1, -1)
        self.label = QLabel(self.teacherPersonalInfo)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self._2.addWidget(self.label)

        self.line = QFrame(self.teacherPersonalInfo)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self._2.addWidget(self.line)

        self.personalInfoFormLayout = QFormLayout()
        self.personalInfoFormLayout.setObjectName(u"personalInfoFormLayout")
        self.personalInfoFormLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_name = QLabel(self.teacherPersonalInfo)
        self.lbl_name.setObjectName(u"lbl_name")

        self.personalInfoFormLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.ledit_name = QLineEdit(self.teacherPersonalInfo)
        self.ledit_name.setObjectName(u"ledit_name")

        self.personalInfoFormLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_name)

        self.lbl_surname = QLabel(self.teacherPersonalInfo)
        self.lbl_surname.setObjectName(u"lbl_surname")

        self.personalInfoFormLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_surname)

        self.ledit_surname = QLineEdit(self.teacherPersonalInfo)
        self.ledit_surname.setObjectName(u"ledit_surname")

        self.personalInfoFormLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_surname)


        self._2.addLayout(self.personalInfoFormLayout)


        self.verticalLayout_13.addWidget(self.teacherPersonalInfo)

        self.teacherLoginInfo = QGroupBox(self.frame)
        self.teacherLoginInfo.setObjectName(u"teacherLoginInfo")
        sizePolicy4.setHeightForWidth(self.teacherLoginInfo.sizePolicy().hasHeightForWidth())
        self.teacherLoginInfo.setSizePolicy(sizePolicy4)
        self.teacherLoginInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.teacherLoginInfo.setFlat(False)
        self.teacherLoginInfo.setCheckable(False)
        self.teacherLoginInfo.setChecked(False)
        self._3 = QVBoxLayout(self.teacherLoginInfo)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(-1, 15, -1, -1)
        self.label_2 = QLabel(self.teacherLoginInfo)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setLineWidth(1)
        self.label_2.setWordWrap(True)

        self._3.addWidget(self.label_2)

        self.line_2 = QFrame(self.teacherLoginInfo)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self._3.addWidget(self.line_2)

        self.loginFormLayout = QFormLayout()
        self.loginFormLayout.setObjectName(u"loginFormLayout")
        self.loginFormLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_eokul_login_type = QLabel(self.teacherLoginInfo)
        self.lbl_eokul_login_type.setObjectName(u"lbl_eokul_login_type")

        self.loginFormLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_eokul_login_type)

        self.rad_eokul_login_mebbis = QRadioButton(self.teacherLoginInfo)
        self.rad_eokul_login_mebbis.setObjectName(u"rad_eokul_login_mebbis")

        self.loginFormLayout.setWidget(1, QFormLayout.FieldRole, self.rad_eokul_login_mebbis)

        self.rad_eokul_login_edevlet = QRadioButton(self.teacherLoginInfo)
        self.rad_eokul_login_edevlet.setObjectName(u"rad_eokul_login_edevlet")

        self.loginFormLayout.setWidget(2, QFormLayout.FieldRole, self.rad_eokul_login_edevlet)

        self.label_3 = QLabel(self.teacherLoginInfo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setLineWidth(1)
        self.label_3.setWordWrap(True)

        self.loginFormLayout.setWidget(4, QFormLayout.FieldRole, self.label_3)

        self.lbl_mebbis_username = QLabel(self.teacherLoginInfo)
        self.lbl_mebbis_username.setObjectName(u"lbl_mebbis_username")

        self.loginFormLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_mebbis_username)

        self.ledit_mebbis_username = QLineEdit(self.teacherLoginInfo)
        self.ledit_mebbis_username.setObjectName(u"ledit_mebbis_username")

        self.loginFormLayout.setWidget(5, QFormLayout.FieldRole, self.ledit_mebbis_username)

        self.lbl_mebbis_password = QLabel(self.teacherLoginInfo)
        self.lbl_mebbis_password.setObjectName(u"lbl_mebbis_password")

        self.loginFormLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_mebbis_password)

        self.ledit_mebbis_password = QLineEdit(self.teacherLoginInfo)
        self.ledit_mebbis_password.setObjectName(u"ledit_mebbis_password")
        self.ledit_mebbis_password.setEchoMode(QLineEdit.Password)

        self.loginFormLayout.setWidget(6, QFormLayout.FieldRole, self.ledit_mebbis_password)

        self.lbl_edevlet_tc = QLabel(self.teacherLoginInfo)
        self.lbl_edevlet_tc.setObjectName(u"lbl_edevlet_tc")

        self.loginFormLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_edevlet_tc)

        self.ledit_edevlet_tc = QLineEdit(self.teacherLoginInfo)
        self.ledit_edevlet_tc.setObjectName(u"ledit_edevlet_tc")

        self.loginFormLayout.setWidget(7, QFormLayout.FieldRole, self.ledit_edevlet_tc)

        self.lbl_edevlet_password = QLabel(self.teacherLoginInfo)
        self.lbl_edevlet_password.setObjectName(u"lbl_edevlet_password")

        self.loginFormLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_edevlet_password)

        self.ledit_edevlet_password = QLineEdit(self.teacherLoginInfo)
        self.ledit_edevlet_password.setObjectName(u"ledit_edevlet_password")
        self.ledit_edevlet_password.setEchoMode(QLineEdit.Password)

        self.loginFormLayout.setWidget(8, QFormLayout.FieldRole, self.ledit_edevlet_password)


        self._3.addLayout(self.loginFormLayout)


        self.verticalLayout_13.addWidget(self.teacherLoginInfo)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.teacher)
        self.students = QWidget()
        self.students.setObjectName(u"students")
        self.stackedWidget.addWidget(self.students)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setFrameShape(QFrame.NoFrame)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_students)
        QWidget.setTabOrder(self.btn_students, self.toggleTeachersBox)
        QWidget.setTabOrder(self.toggleTeachersBox, self.teachersBoxCloseBtn)
        QWidget.setTabOrder(self.teachersBoxCloseBtn, self.teacherName2)
        QWidget.setTabOrder(self.teacherName2, self.teacherSelect2)
        QWidget.setTabOrder(self.teacherSelect2, self.teacherName1)
        QWidget.setTabOrder(self.teacherName1, self.teacherSelect1)
        QWidget.setTabOrder(self.teacherSelect1, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.btn_add_teacher)
        QWidget.setTabOrder(self.btn_add_teacher, self.settingsTopBtn)
        QWidget.setTabOrder(self.settingsTopBtn, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.ledit_name)
        QWidget.setTabOrder(self.ledit_name, self.ledit_surname)
        QWidget.setTabOrder(self.ledit_surname, self.rad_eokul_login_mebbis)
        QWidget.setTabOrder(self.rad_eokul_login_mebbis, self.rad_eokul_login_edevlet)
        QWidget.setTabOrder(self.rad_eokul_login_edevlet, self.ledit_mebbis_username)
        QWidget.setTabOrder(self.ledit_mebbis_username, self.ledit_mebbis_password)

        self.retranslateUi(MainWindow)
        self.rad_eokul_login_edevlet.toggled.connect(self.ledit_mebbis_username.setDisabled)
        self.rad_eokul_login_edevlet.toggled.connect(self.ledit_mebbis_password.setDisabled)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"EduBot", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmene yard\u0131mc\u0131 BOT", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Gizle", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Ana Sayfa", None))
        self.btn_students.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011frenciler", None))
#if QT_CONFIG(tooltip)
        self.toggleTeachersBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toggleTeachersBox.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmenler", None))
#if QT_CONFIG(tooltip)
        self.teachersBoxCloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmenler kutusunu kapat", None))
#endif // QT_CONFIG(tooltip)
        self.teachersBoxCloseBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmenler", None))
        self.teacherName2.setText(QCoreApplication.translate("MainWindow", u"Eren Mustafa \u00d6zdal", None))
#if QT_CONFIG(tooltip)
        self.teacherSelect2.setToolTip(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmeni se\u00e7", None))
#endif // QT_CONFIG(tooltip)
        self.teacherSelect2.setText("")
        self.teacherName1.setText(QCoreApplication.translate("MainWindow", u"Sultan \u00d6zdal", None))
#if QT_CONFIG(tooltip)
        self.teacherSelect1.setToolTip(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmeni se\u00e7", None))
#endif // QT_CONFIG(tooltip)
        self.teacherSelect1.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#f96a76;\">Hen\u00fcz \u00f6\u011fretmen eklemediniz!</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00d6\u011fretmen ekleyerek <span style=\" font-style:italic;\">EduBot</span>'un i\u015flerinizde size yard\u0131mc\u0131 olmas\u0131n\u0131 sa\u011flayabilirsiniz.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><img src=\":/images/images/images/robot_not_found.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hemen a\u015fa\u011f\u0131daki <span style=\" font-weight:600; font-style:italic;\">&quot;\u00d6\u011fretmen Ekle&quot;</span> tu\u015fu ile ba\u015flayabilirsiniz.</p></body></html>", None))
        self.btn_add_teacher.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011fretmen Ekle", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"EduBot'a ho\u015f geldiniz!..", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"K\u00fc\u00e7\u00fclt", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Tam ekran yap", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Kapat", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.teacher_title.setText(QCoreApplication.translate("MainWindow", u"<h2>Yeni \u00d6\u011fretmen Ekleyin</h2>", None))
        self.teacher_title.setProperty("class", QCoreApplication.translate("MainWindow", u"page_title", None))
        self.teacher_description.setText(QCoreApplication.translate("MainWindow", u"EduBot'u kullanacak \u00f6\u011fretmen ekleyin.", None))
        self.teacher_description.setProperty("class", QCoreApplication.translate("MainWindow", u"page_description", None))
        self.teacherPersonalInfo.setTitle(QCoreApplication.translate("MainWindow", u"Ki\u015fisel Bilgiler", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EduBot \u00fczerinde g\u00f6r\u00fcnecek olan \u00f6\u011fretmen bilgileri. Bu bilgileri sadece EduBot i\u00e7inde \u00f6\u011fretmen se\u00e7imi yapmak i\u00e7in kullanacaks\u0131n\u0131z.", None))
        self.label.setProperty("class", QCoreApplication.translate("MainWindow", u"form_description", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Ad", None))
        self.lbl_surname.setText(QCoreApplication.translate("MainWindow", u"Soyad", None))
        self.teacherLoginInfo.setTitle(QCoreApplication.translate("MainWindow", u"Oturum A\u00e7ma Bilgileri", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"e-Okul ve EBA'da oturum a\u00e7ma bilgileri. Bu bilgiler bilgisayar\u0131n\u0131zdaki EduBot veritaban\u0131nda saklanacakt\u0131r. Bu bilgiler ile EduBot hesaplar\u0131n\u0131za otomatik giri\u015f yap\u0131p i\u015flem yapabilir. Bu bilgileri vermedi\u011finiz takdirde giri\u015f i\u015flemlerini manuel yapman\u0131z gerekecek.", None))
        self.label_2.setProperty("class", QCoreApplication.translate("MainWindow", u"form_description", None))
        self.lbl_eokul_login_type.setText(QCoreApplication.translate("MainWindow", u"e-Okul'a nas\u0131l giri\u015f yap\u0131ls\u0131n?", None))
        self.rad_eokul_login_mebbis.setText(QCoreApplication.translate("MainWindow", u"Mebbis", None))
        self.rad_eokul_login_edevlet.setText(QCoreApplication.translate("MainWindow", u"e-Devlet", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"e-Okul'a giri\u015f yaparken burada se\u00e7ti\u011finiz y\u00f6ntem kullan\u0131lacak.", None))
        self.label_3.setProperty("class", QCoreApplication.translate("MainWindow", u"field_description", None))
        self.lbl_mebbis_username.setText(QCoreApplication.translate("MainWindow", u"Mebbis Kullan\u0131c\u0131 Ad\u0131", None))
        self.ledit_mebbis_username.setInputMask(QCoreApplication.translate("MainWindow", u"99999999999", None))
        self.ledit_mebbis_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mebbis kullan\u0131c\u0131 ad\u0131 olarak kulland\u0131\u011f\u0131n\u0131z T.C. Kimlik No", None))
        self.lbl_mebbis_password.setText(QCoreApplication.translate("MainWindow", u"Mebbis \u015eifresi", None))
        self.ledit_mebbis_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mebbis kullan\u0131c\u0131 ad\u0131n\u0131za tan\u0131mlad\u0131\u011f\u0131n\u0131z \u015fifreniz", None))
        self.lbl_edevlet_tc.setText(QCoreApplication.translate("MainWindow", u"e-Devlet T.C. Kimlik No", None))
        self.ledit_edevlet_tc.setInputMask(QCoreApplication.translate("MainWindow", u"99999999999", None))
        self.ledit_edevlet_tc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"11 haneli e-Devlet T.C. Kimlik No", None))
        self.lbl_edevlet_password.setText(QCoreApplication.translate("MainWindow", u"e-Devlet \u015eifresi", None))
        self.ledit_edevlet_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e-Devlet i\u00e7in tan\u0131mlad\u0131\u011f\u0131n\u0131z \u015fifreniz", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Eren Mustafa \u00d6zdal taraf\u0131ndan geli\u015ftirilmi\u015ftir.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

