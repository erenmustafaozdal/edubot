# ÜÇÜNCÜ PARTİ MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt

# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.ui.ui_core import UICore
from modules.teacher.ui_teacher import UITeacher


class UIWindowMain(UICore):

    def __init__(self):
        """UIWindowMain sınıfı yapıcı metodu"""
        super(UIWindowMain, self).__init__()

        # ÇEKİRDEK SINIFI YÜKLEME İŞLEMİ YAPILIR
        # //////////////////////////////////////////////////////////////////////
        self.setup_core()

        # UI TANIMLAMALARINI AYARLA
        # //////////////////////////////////////////////////////////////////////
        self.ui_definations()

        # MENU GEÇİŞİ
        # //////////////////////////////////////////////////////////////////////
        self.ui.toggleButton.clicked.connect(lambda: self.toggle_menu())

        # TUŞLARA TIKLAMA
        # //////////////////////////////////////////////////////////////////////

        # SOL MENÜ
        self.ui.btn_home.clicked.connect(self.button_click)
        self.ui.btn_students.clicked.connect(self.button_click)

        # ÖĞRETMENLER KUTUSU AÇILMASI VE KAPANMASI
        # //////////////////////////////////////////////////////////////////////
        self.ui.toggleTeachersBox.clicked.connect(self.toggle_teachers_box)
        self.ui.teachersBoxCloseBtn.clicked.connect(self.toggle_teachers_box)

        # ANA SAYFAYI AYARLA VE STİLLERİ DEĞİŞTİR
        # //////////////////////////////////////////////////////////////////////
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(self.select_menu(self.ui.btn_home.styleSheet()))

        # UYGULAMAYI GÖSTER
        # //////////////////////////////////////////////////////////////////////
        self.show()

        # ÖĞRETMEN ARAYÜZ MODÜLÜ ÇALIŞTIRILIR
        # //////////////////////////////////////////////////////////////////////
        self.teacher = UITeacher(self)

    # TUŞLARA TIKLAMA
    # ///////////////////////////////////////////////////////////////
    def button_click(self):
        # TIKLANAN TUŞU AL
        btn = self.sender()
        btn_name = btn.objectName()

        # ANA SAYFAYI GÖSTER
        if btn_name == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # ÖĞRENCİLERİ GÖSTER
        if btn_name == "btn_students":
            self.ui.stackedWidget.setCurrentWidget(self.ui.students)

        # TUŞ STİLLERİNİ DEĞİŞTİR
        self.reset_style(btn_name)
        btn.setStyleSheet(self.select_menu(btn.styleSheet()))

        # TUŞ ADINI YAZDIR
        print(f'"{btn_name}" tuşu basıldı!')

    # MOUSE TIKLAMA OLAYLARI
    # Ana sınıfın (UICore) üzerine yazılan method
    # //////////////////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        # MOUSE OLAYINI YAZDIR
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
