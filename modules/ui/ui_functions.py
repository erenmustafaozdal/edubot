# MAIN DOSYASI
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from main import *


class UIFunctions(MainWindow):
    # MENÜ GEÇİŞİ
    # //////////////////////////////////////////////////////////////////////////
    def toggle_menu(self, enable):
        if enable:
            # GENİŞLİK ALINIR
            width = self.ui.leftMenuBg.width()
            menu_width = Settings.MENU_WIDTH
            standart = 60

            # MENÜ GENİŞLİĞİ AYARLANIR
            if width == 60:
                width_extended = menu_width
            else:
                width_extended = standart

            # ANİMASYON
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
