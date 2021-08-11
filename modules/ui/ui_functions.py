# ARAYÜZÜ, MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from main import *

# EVRENSELLER
# //////////////////////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class UIFunctions(MainWindow):
    # TAM EKRAN BÜYÜT VE GERİ DÖNDÜR
    # //////////////////////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Küçült")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/fullscreen-exit.svg"))
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.maximizeRestoreAppBtn.setToolTip("Tam ekran yap")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/fullscreen.svg"))
            self.ui.frame_size_grip.show()
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

    # UI TANIMLAMALARI
    # //////////////////////////////////////////////////////////////////////////////
    def ui_definations(self):

        # ÇİFT TIKLAMA İLE TAM EKRAN YAPMA
        def double_click_maximize(event):
            # EĞER ÇİFT TIKLAMA YAPILDIYSA DURUMU DEĞİŞTİR
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = double_click_maximize

        # STANDART BAŞLIK ÇUBUĞU KALDIR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # PENCEREYİ TAŞIMA / TAM EKRAN YAPMA / GERİ KÜÇÜLTME
        def move_window(event):
            # EĞER TAM EKRAN İSE NORMALE ÇEVİR
            if UIFunctions.return_status(self):
                UIFunctions.maximize_restore(self)

            # PENCEREYİ TAŞI
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = move_window

        # GÖLGE
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # PENCEREYİ YENİDEN BOYUTLANDIR
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

    # EVRENSEL DURUMU DÖNDÜRÜR
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def return_status(self):
        return GLOBAL_STATE
