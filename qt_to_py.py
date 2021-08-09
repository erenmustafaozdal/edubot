import os

path = 'modules/ui'

# KLASÖR YOKSA OLUŞTUR
# //////////////////////////////////////////////////////////////////////////////
if not os.path.exists(path):
    os.makedirs(path)

# "UI TO PY" VE "QRC TO PY" İŞLEMLERİ
# //////////////////////////////////////////////////////////////////////////////
os.system("pyside6-uic main.ui > modules/ui/ui_main.py")
os.system("pyside6-rcc resources.qrc > modules/ui/resources_rc.py")

# ui_main.py İÇİNDEKİ resources_rc.py İÇERİ AKTARMA KODUNUN DEĞİŞTİRİLMESİ
# //////////////////////////////////////////////////////////////////////////////
file_path = f"{path}/ui_main.py"
file = open(file_path, "rt")
data = file.read()
data = data.replace('import resources_rc', 'from . resources_rc import *')
file.close()


file = open(file_path, "wt")
file.write(data)
file.close()
