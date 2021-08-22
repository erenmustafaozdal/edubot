# STANDART KÜTÜPHANELER (MODÜLLER) İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
import glob
import os
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

        # İŞLENMİŞ MIGRATION TABLOLARI VERİ TABANINDAN ALINIR
        migrations = self.get_migrations()

        # MIGRATION SINIFLARININ DOSYALARI ALINIR
        files = glob.glob(self.MIGRATION_FILES)

        # MIGRATION İŞLEMLERİ KONTROL EDİLİR VE YAPILMAMIŞ İŞLEMLER YAPILIR
        for file in files:
            migration_name = self.get_migration_name(file)
            if not migration_name in migrations:
                migration_class = self.get_migration_class(migration_name)
                sqls = migration_class.up()
                # MIGRATION SQLLERİ ÇALIŞTIRILIR
                for sql in sqls:
                    self.cur.execute(sql)

                self.save_migration(migration_name)

        self.conn.commit()

    # KAYITLI TÜM MIGRATION İŞLEMLERİNİ VERİ TABANINDAN ALIR
    # //////////////////////////////////////////////////////////////////////////////
    def get_migrations(self):
        self.cur.execute('SELECT * from migrations')
        migrations = self.cur.fetchall()
        return migrations

    # MIGRATION KAYDEDİLİR
    # //////////////////////////////////////////////////////////////////////////////
    def save_migration(self, migration_name):
        self.cur.execute(
            f'INSERT INTO "migrations" ("migration") VALUES ("{migration_name}")')

    # VERİLEN DOSYA YOLUNDAN, MIGRATION SINIFINI İÇERİ AKTARIR VE DÖNDÜRÜR
    # //////////////////////////////////////////////////////////////////////////////
    def get_migration_class(self, migration_name):
        class_name = self.filename_to_classname(migration_name)
        module = __import__(f"modules.db.migrations.{migration_name}",
                            fromlist=[class_name])
        migration_class = getattr(module, class_name)
        return migration_class

    def get_migration_name(self, file):
        migration_name = os.path.splitext(os.path.basename(file))[0]
        return migration_name

    # MIGRATION DOSYA ADINI SINIF ADINA ÇEVİRİR
    # //////////////////////////////////////////////////////////////////////////////
    def filename_to_classname(self, name):
        only_text = ''.join(i for i in name if not i.isdigit())
        text_parts = only_text.split('_')
        result = ''.join(ele.title() for ele in text_parts[1:])
        return result

    # MIGRATION İŞLEMLERİNİ TUTACAK OLAN TABLO EĞER YOKSA OLUŞTURULUR
    # //////////////////////////////////////////////////////////////////////////
    def create_migrations_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS "migrations" ('
                         '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                         '"migration" TEXT(191)'
                         ');')
        self.cur.execute('CREATE UNIQUE INDEX IF NOT EXISTS "migrations.PRIMARY" on migrations (id ASC);')
        self.conn.commit()

