# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.db.core import Core as DBCore
from modules.db.model import Model


class TeacherModel(Model):
    """todo: TeacherModel sınıfı için dokümantasyon eklenecek"""

    def __init__(self, db: DBCore):
        """TeacherModel sınıfı yapıcı metodu"""
        super(TeacherModel, self).__init__(db)

        self.TABLE_NAME = 'teachers'

    # ÖĞRETMENE ÖZEL KAYIT İŞLEMİ
    # //////////////////////////////////////////////////////////////////////////
    def save(self, data):
        # ÜST SINIF İLE KAYIT İŞLEMİ YAPILIR
        id = super(TeacherModel, self).save(data)

        # Kaydedilen öğretmen aktif öğretmen olarak seçildi
        # Diğer öğretmenler pasif yapılır
        self.update([['id', '!=', id]], {'is_active':0})
