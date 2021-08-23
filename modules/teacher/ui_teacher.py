# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.db.core import Core as DBCore
from modules.ui.ui_core import UICore
from modules.ui.ui_main import Ui_MainWindow


class UITeacher(UICore):

    def __init__(self, window):
        super(UITeacher, self).__init__()

        self.ui: Ui_MainWindow = window.ui
        self.db: DBCore = window.db

        # HATA MESAJI KUTUSUNU GİZLE
        self.reset_error_box(self.ui.teacher_error_box)

        # TUŞLARA TIKLAMA
        # ///////////////////////////////////////////////////////////////

        # ÖĞRETMEN EKLEME TUŞU İLE SAYFA GÖSTERİLİR
        self.ui.btn_add_teacher.clicked.connect(self.show_teacher)

        # kaydet tuşuna tıklandığında öğretmen kaydedilir
        self.ui.teacher_save_btn.clicked.connect(self.save)

    # ÖĞRETMEN KAYDETME İŞLEMİ
    # ///////////////////////////////////////////////////////////////////
    def save(self):
        self.reset_error_box(self.ui.teacher_error_box)

        # ALANLAR KONTROL EDİLİR
        if not self.validate():
            return

        # öğretmen kaydedilir


    # ALANLAR KONTROL EDİLİR
    # ///////////////////////////////////////////////////////////////////
    def validate(self):
        """
        Form alanları kontrol edilir. Eğer sorun yoksa True, sorun varsa False değeri döndürülür

        :return: Boolean [True,False]
        """
        # ÖĞRETMEN ADI ZORUNLU
        if not self.ui.ledit_first_name.text():
            self.flash_error_box(
                self.ui.teacher_error_box,
                self.trans.validation['teacher']['name']['required']
            )
            return False

        # ÖĞRETMEN SOYADI ZORUNLU
        if not self.ui.ledit_last_name.text():
            self.flash_error_box(
                self.ui.teacher_error_box,
                self.trans.validation['teacher']['surname']['required']
            )
            return False

        # ÖĞRETMEN BRANŞI ZORUNLU
        if not self.ui.combo_branch.currentText():
            self.flash_error_box(
                self.ui.teacher_error_box,
                self.trans.validation['teacher']['branch']['required']
            )
            return False

        return True

    # SHOW TEACHER PAGE
    # ///////////////////////////////////////////////////////////////////
    def show_teacher(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.teacher)
