class CreateTeachersTable:

    @staticmethod
    def up():
        return [
            # TABLO OLUŞTUR
            'CREATE TABLE IF NOT EXISTS teachers ('
                'id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                'first_name VARCHAR(191) NOT NULL,'
                'last_name VARCHAR(191) NOT NULL,'
                'branch VARCHAR(191) NOT NULL,'
                'login_type VARCHAR(10),'
                'mebbis_username VARCHAR(11),'
                'mebbis_password VARCHAR(191),'
                'edevlet_tc VARCHAR(11),'
                'edevlet_password VARCHAR(191),'
                'is_active BOOLEAN(1) NOT NULL DEFAULT 1,'
                'created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
                'updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
                # is_active alanına sadece 0 ve 1 değerlerini kabul ediyoruz
                'CONSTRAINT teachers_is_active CHECK (is_active IN (0,1)),'
                # login_type alanına sadece "mebbis" ve "edevlet" değerlerini kabul ediyoruz
                'CONSTRAINT teachers_login_type CHECK (login_type IN ("mebbis", "edevlet"))'
            ');',
            # INDEX OLUŞTUR
            'CREATE UNIQUE INDEX IF NOT EXISTS teachers_id ON teachers (id ASC);',
            # GÜNCELLENDİĞİ TARİH İÇİN TRIGGER OLUŞTUR
            'CREATE TRIGGER IF NOT EXISTS teachers_updated_at '
            'AFTER UPDATE OF first_name, last_name, branch, login_type, mebbis_username, mebbis_password, edevlet_tc, edevlet_password ON teachers '
            'BEGIN '
                'UPDATE teachers SET updated_at=CURRENT_TIMESTAMP WHERE id=NEW.id; '
            'END'
        ]
