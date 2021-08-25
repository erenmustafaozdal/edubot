# YEREL MODÜLLERİ VE ARAÇLARI İÇERİ AKTAR
# //////////////////////////////////////////////////////////////////////////////
from modules.db.core import Core as DBCore


class Model:
    """todo: Model sınıfı için dokümantasyon eklenecek"""

    # MODELİN VERİ TABANINDAKİ TABLO ADINI TUTAN DEĞİŞKEN
    # //////////////////////////////////////////////////////////////////////////
    TABLE_NAME = None

    def __init__(self, db: DBCore):
        """Model sınıfı yapıcı metodu"""

        self.db = db
        self.conn = db.conn
        self.cur = db.cur

    # KAYIT İŞLEMİ
    # //////////////////////////////////////////////////////////////////////////
    def save(self, data: dict):
        """
        Dictionary tipinde gelen verileri veri tabanına kaydeder.

        :param data: dict | { "key": "value" }
        :return: id: int
        """

        # VERİ AYIKLANIR
        keys = ", ".join(data.keys())
        values = data.values()
        value_placers = ", ".join(['?'] * len(values))

        # VERİ KAYDEDİLİR
        self.cur.execute(
            f'INSERT INTO {self.TABLE_NAME} ({keys}) VALUES ({value_placers})',
            tuple(values)
        )
        self.conn.commit()

        # KAYDEDİLEN VERİNİN ID'Sİ GERİ DÖNDÜRÜLÜR
        return self.cur.lastrowid

    # GÜNCELLEME İŞLEMİ
    # //////////////////////////////////////////////////////////////////////////
    def update(self, where: list, values: dict, limit: int = None, offset: int = None):
        """
        Dictionary tipinde gelen where (koşul) bilgilerini kullanarak, eşleşen verileri dictionary tipinde değerler ile günceller

        :param where: list | [ ['is_active', '!=', 1], 'AND', ['name', 'Eren'] ]
        :param values: dict | {'key':'value'}
        :param limit: int|None
        :param offset: int|None
        :return: None
        """

        # VERİ AYIKLANIR
        set_placers = ', '.join(f"{key}={values[key]}" for key in values)

        # SORGU OLUŞTURULUR VE SONRA EKLEMELER YAPILIR
        sql = f"UPDATE {self.TABLE_NAME} SET {set_placers}"
        sql += self.get_where_sql(where)

        # limit ve offset varsa sorguya eklenir
        sql += self.get_limit_sql(limit)
        sql += self.get_offset_sql(offset)

        # VERİ GÜNCELLENİR
        self.cur.execute(sql)
        self.conn.commit()

    def get_offset_sql(self, offset: int = None):
        """
        :param offset: int|None
        :return: srt
        """
        if offset:
            return f" OFFSET {offset}"

        return ""

    def get_limit_sql(self, limit: int = None):
        """
        :param limit: int|None
        :return: srt
        """
        if limit:
            return f" LIMIT {limit}"

        return ""

    # SQL WHERE KOŞULLARINI OLUŞTURUR
    # //////////////////////////////////////////////////////////////////////////
    def get_where_sql(self, where: list):
        """
        Liste şeklinde gelen koşulları durumuna göre sorguya dahil eder.
            1. yöntem: 'AND'
            2. yöntem: ['name', 'Eren']
            3. yöntem: ['is_active', '!=', 1]

        :param where: list | [ ['is_active', '!=', 1], 'AND', ['name', 'Eren'] ]
        :return: str
        """
        sql = " WHERE"
        for w in where:
            # LİSTE DEĞİLSE (STRİNG İSE) DİREKT SORGUYA DAHİL ET
            if type(w) is str:
                sql += f" {w}"
                continue

            # 2 ELEMANLI LİSTE İSE; 1. ALAN, 2. DEĞERE EŞİTLİK ŞARTI ŞEKLİNDE EKLE
            if len(w) == 2:
                sql += f" {w[0]} = {w[1]}"
                continue

            # 3 ELEMANLI LİSTE İSE; 1. ALAN, 2. ŞART VE 3. DEĞER ŞEKLİNDE EKLE
            sql += f" {w[0]} {w[1]} {w[2]}"

        return sql
