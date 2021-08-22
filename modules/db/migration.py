# STANDART KÜTÜPHANELER (MODÜLLER) İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
from sqlite3 import Cursor, Connection


class Migration:
    """todo: Migration sınıfı için dokümantasyon eklenecek"""

    MIGRATION_FILES = "modules/db/migrations/*.py"

    def __init__(self, conn: Connection, cur: Cursor):
        """Migration sınıfı yapıcı metodu"""

        self.conn = conn
        self.cur = cur

    # VERİ TABANI MIGRATION İŞLEMLERİNİ ÇALIŞTIRAN METOT
    # //////////////////////////////////////////////////////////////////////////
    def run(self):
        self.create_migrations_table()

    # MIGRATION İŞLEMLERİNİ TUTACAK OLAN TABLO EĞER YOKSA OLUŞTURULUR
    # //////////////////////////////////////////////////////////////////////////
    def create_migrations_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS "migrations" ('
                         '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                         '"migration" TEXT(191)'
                         ');')
        self.cur.execute('CREATE UNIQUE INDEX IF NOT EXISTS "migrations.PRIMARY" on migrations (id ASC);')
        self.conn.commit()

