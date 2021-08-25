# GELEN DEĞERİ VEYA DEĞER YOKSA NONE DÖNDÜREN METOT
# //////////////////////////////////////////////////////////////////////////////
def value_or_none(value: str):
    """
    Form alanlarından alınan değeri veya boş geldiyse None değerini döndürür

    :param value: str
    :return: str|None
    """
    return value if value else None
