class CreateTeachersTable:

    @staticmethod
    def up():
        return [
            'CREATE TABLE IF NOT EXISTS "teachers" ('
                '"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                '"first_name"  TEXT NOT NULL,'
                '"last_name"  TEXT NOT NULL,'
                '"login_type"  TEXT(10),'
                '"mebbis_user_name"  TEXT(11),'
                '"mebbis_password"  TEXT,'
                '"edevlet_tc"  TEXT(11),'
                '"edevlet_password"  TEXT'
            ');',
            'CREATE UNIQUE INDEX IF NOT EXISTS "teachers.PRIMARY" ON "teachers" ("id" ASC);'
        ]
