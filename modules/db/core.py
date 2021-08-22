# STANDART KÜTÜPHANELER (MODÜLLER) İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
import sqlite3


class Core:
    """todo: DBCore sınıfı için dokümantasyon eklenecek"""

    DB_PATH = "data/edubot.db"

    def __init__(self):
        """DBCore sınıfı yapıcı metodu"""

        self.conn = sqlite3.connect(self.DB_PATH)
        self.cur = self.conn.cursor()

