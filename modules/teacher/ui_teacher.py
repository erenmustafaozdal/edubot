# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.db.core import Core as DBCore
from modules.db.model import Model
from modules.helpers import value_or_none
from modules.teacher.teacher_model import TeacherModel
from modules.ui.ui_core import UICore
from modules.ui.ui_main import Ui_MainWindow


class UITeacher(UICore):

    def __init__(self, window):
        super(UITeacher, self).__init__()

        # sınıfın değişkenleri tanımlanır
        # //////////////////////////////////////////////////////////////////////////////
        self.ui: Ui_MainWindow = window.ui
        self.db: DBCore = window.db
        self.model: Model = TeacherModel(self.db)

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

        # ÖĞRETMEN KAYDEDİLİR
        self.model.save({
            'first_name': self.ui.ledit_first_name.text(),
            'last_name': self.ui.ledit_last_name.text(),
            'branch': self.ui.combo_branch.currentText(),
            'login_type': self.get_login_type(),
            'mebbis_username': value_or_none(self.ui.ledit_mebbis_username.text()),
            'mebbis_password': value_or_none(self.ui.ledit_mebbis_password.text()),
            'edevlet_tc': value_or_none(self.ui.ledit_edevlet_tc.text()),
            'edevlet_password': value_or_none(self.ui.ledit_edevlet_password.text()),
        })

        # FORM ALANLARI RESETLENİR
        self.reset_form()

    # FORM ALANLARI RESETLEME İŞLEMİ YAPAR
    # //////////////////////////////////////////////////////////////////////////////
    def reset_form(self):
        self.ui.ledit_first_name.setText(None)
        self.ui.ledit_last_name.setText(None)
        self.ui.combo_branch.setCurrentIndex(0)
        self.ui.rad_eokul_login_mebbis.setChecked(False)
        self.ui.rad_eokul_login_edevlet.setChecked(False)
        self.ui.ledit_mebbis_username.setText(None)
        self.ui.ledit_mebbis_password.setText(None)
        self.ui.ledit_edevlet_tc.setText(None)
        self.ui.ledit_edevlet_password.setText(None)

    # E-OKUL GİRİŞ YÖNTEMİNİ VEREN METOT
    # //////////////////////////////////////////////////////////////////////////////
    def get_login_type(self):
        if self.ui.rad_eokul_login_mebbis.isChecked():
            login_type = "mebbis"
        elif self.ui.rad_eokul_login_edevlet.isChecked():
            login_type = "edevlet"
        else:
            login_type = None
        return login_type

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
