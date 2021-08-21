# ÜÇÜNCÜ PARTİ MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtCore import QEvent, QTimer, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsDropShadowEffect,
    QSizeGrip,
    QPushButton
)

# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.ui.ui_main import Ui_MainWindow
from modules.ui.ui_settings import UISettings
from modules.ui.ui_translation import UITranslation

# EVRENSELLER
# //////////////////////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class UICore(QMainWindow):

    def __init__(self):
        """UICore sınıfı yapıcı metodu"""
        super(UICore, self).__init__()

    def setup_core(self):
        # EVRENSEL ARAÇLAR VE DEĞİŞKENLER AYARLANIR
        # //////////////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()  # nesneler
        self.ui.setupUi(self)
        self.settings = UISettings  # uygulama ayarları
        self.trans = UITranslation  # uygulama metinleri

        # METİNLERİ EKLE
        self.setWindowTitle(self.trans.app_title)
        self.ui.titleRightInfo.setText(self.trans.app_description)

    # TAM EKRAN BÜYÜT VE GERİ DÖNDÜR
    # //////////////////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip(self.trans.app_minimize)
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(self.settings.FULLSCREEN_EXIT_ICON))
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.maximizeRestoreAppBtn.setToolTip(self.trans.app_maximize)
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(self.settings.FULLSCREEN_ICON))
            self.ui.frame_size_grip.show()

    # ÇİFT TIKLAMA İLE TAM EKRAN YAPMA
    # //////////////////////////////////////////////////////////////////////////
    def double_click_maximize(self, event):
        # EĞER ÇİFT TIKLAMA YAPILDIYSA DURUMU DEĞİŞTİR
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximize_restore())

    # PENCEREYİ TAŞIMA / TAM EKRAN YAPMA / GERİ KÜÇÜLTME
    # //////////////////////////////////////////////////////////////////////////
    def move_window(self, event):
        # EĞER TAM EKRAN İSE NORMALE ÇEVİR
        if self.return_status():
            self.maximize_restore()

        # PENCEREYİ TAŞI
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    # UYGULAMANIN GÖLGESİNİ AYARLA
    # //////////////////////////////////////////////////////////////////////////////
    def app_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

    # UI TANIMLAMALARI
    # //////////////////////////////////////////////////////////////////////////
    def ui_definations(self):
        # ÇİFT TIKLAMA İLE TAM EKRAN YAPMA
        self.ui.titleRightInfo.mouseDoubleClickEvent = self.double_click_maximize

        # STANDART BAŞLIK ÇUBUĞU KALDIR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # PENCEREYİ TAŞIMA / TAM EKRAN YAPMA / GERİ KÜÇÜLTME
        self.ui.titleRightInfo.mouseMoveEvent = self.move_window

        # GÖLGE
        self.app_shadow()

        # PENCEREYİ YENİDEN BOYUTLANDIR
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # ÖZEL TUŞ İLE SİMGE DURUMUNA KÜÇÜLTME
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # ÖZEL TUŞ İLE TAM EKRAN BÜYÜT VE GERİ DÖNDÜR
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        # özel tuş ile uygulamayı kapat
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    # EVRENSEL DURUMU DÖNDÜRÜR
    # //////////////////////////////////////////////////////////////////////////
    @staticmethod
    def return_status():
        return GLOBAL_STATE

    # MOUSE TIKLAMA OLAYLARI
    # Ana sınıfın (QMainWindow) üzerine yazılan method
    # //////////////////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # PENCERENİN  SÜRÜKLENME POZİSYONUNU AYARLA
        self.dragPos = event.globalPosition().toPoint()

    # KUTU AÇILMA VE KAPANMA ANİMASYONU
    # //////////////////////////////////////////////////////////////////////////
    def box_animation(self, box, width, width_extended, is_hide = True):
        type = b"minimumWidth" if is_hide else b"maximumWidth"

        # ANİMASYON
        self.animation = QPropertyAnimation(box, type)
        self.animation.setDuration(self.settings.TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    # MENÜ SEÇ VE SEÇİMİ KALDIR
    # ///////////////////////////////////////////////////////////////

    # SEÇ
    def select_menu(self, getStyle):
        select = getStyle + self.settings.MENU_SELECTED_STYLESHEET
        return select

    # SEÇİMİ KALDIR
    def deselect_menu(self, getStyle):
        deselect = getStyle.replace(self.settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # SEÇİMİ BAŞLAT
    def select_standard_menu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(self.select_menu(w.styleSheet()))

    # SEÇİMİ RESETLE
    def reset_style(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselect_menu(w.styleSheet()))

    # MENÜ GEÇİŞİ
    # //////////////////////////////////////////////////////////////////////////
    def toggle_menu(self):
        # GENİŞLİK ALINIR
        width = self.ui.leftMenuBg.width()
        menu_width = self.settings.MENU_WIDTH
        minimize = 60

        # MENÜ GENİŞLİĞİ AYARLANIR
        if width == 60:
            width_extended = menu_width
        else:
            width_extended = minimize

        self.box_animation(self.ui.leftMenuBg, width, width_extended, is_hide=False)

    # ÖĞRETMENLER KUTUSU GEÇİŞİ
    # //////////////////////////////////////////////////////////////////////
    def toggle_teachers_box(self):
        # GENİŞLİĞİ AL
        width = self.ui.teachersBox.width()
        max_extend = self.settings.TEACHERS_BOX_WIDTH
        color = self.settings.BTN_TEACHERS_BOX_COLOR
        standard = 0

        # TUŞ STİLİNİ AL
        style = self.ui.toggleTeachersBox.styleSheet()

        # GENİŞLİĞİ AYARLA
        if width == 0:
            width_extended = max_extend
            # TUŞU SEÇ
            self.ui.toggleTeachersBox.setStyleSheet(style + color)
        else:
            width_extended = standard
            # TUŞU RESETLE
            self.ui.toggleTeachersBox.setStyleSheet(style.replace(color, ''))

        self.box_animation(self.ui.teachersBox, width, width_extended)
