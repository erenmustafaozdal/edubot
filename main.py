# //////////////////////////////////////////////////////////////////////////////
#
# BY: EREN M. ÖZDAL
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# //////////////////////////////////////////////////////////////////////////////

import sys

# ARAYÜZÜ, MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.ui.ui_main import Ui_MainWindow
from modules.ui.app_settings import Settings
from modules.ui.ui_functions import *

# EVRENSEL ARAÇLAR AYARLANIR
# //////////////////////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # EVRENSEL ARAÇLAR AYARLANIR
        # //////////////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # ÖZEL BAŞLIK ÇUBUĞU
        # ///////////////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # UYGULAMA ADI VE AÇIKLAMASI
        # ///////////////////////////////////////////////////////////////////////
        title = "EduBot - Öğretmene yardımcı BOT"
        description = "EduBot'a hoş geldiniz!.."
        # METİNLERİ EKLE
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # MENU GEÇİŞİ
        # ///////////////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggle_menu(self, True))

        # UI TANIMLAMALARINI AYARLA
        # //////////////////////////////////////////////////////////////////////
        UIFunctions.ui_definations(self)

    # MOUSE TIKLAMA OLAYLARI
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # PENCERENİN  SÜRÜKLENME POZİSYONUNU AYARLA
        self.dragPos = event.globalPosition().toPoint()

        # MOUSE OLAYINI YAZDIR
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    edubot = QApplication(sys.argv)
    edubot.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()
    sys.exit(edubot.exec())
