class CreateTeachersTable:

    @staticmethod
    def up():
        return [
            'CREATE TABLE IF NOT EXISTS "teachers" ('
                '"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                '"first_name" VARCHAR(191) NOT NULL,'
                '"last_name" VARCHAR(191) NOT NULL,'
                '"branch" VARCHAR(191) NOT NULL,'
                '"login_type" VARCHAR(10),'
                '"mebbis_user_name" VARCHAR(11),'
                '"mebbis_password" VARCHAR(191),'
                '"edevlet_tc" VARCHAR(11),'
                '"edevlet_password" VARCHAR(191),'
                '"is_active" BOOLEAN(1) NOT NULL DEFAULT 0,'
                '"created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
                '"updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
                # is_active alanına sadece 0 ve 1 değerlerini kabul ediyoruz
                'CONSTRAINT "teachers.is_active" CHECK ("is_active" IN (0,1)),'
                # login_type alanına sadece "mebbis" ve "edevlet" değerlerini kabul ediyoruz
                'CONSTRAINT "teachers.login_type" CHECK ("login_type" IN ("mebbis", "edevlet"))'
            ');',
            'CREATE UNIQUE INDEX IF NOT EXISTS "teachers.PRIMARY" ON "teachers" ("id" ASC);'
        ]
