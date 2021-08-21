# //////////////////////////////////////////////////////////////////////////////
#
# BY: EREN M. ÖZDAL
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# //////////////////////////////////////////////////////////////////////////////

# STANDART KÜTÜPHANELER (MODÜLLER) İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
import sys
import os
import platform

# ÜÇÜNCÜ PARTİ ARAYÜZ MODÜLLERİ VE ARAÇLARI İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

# YEREL ARAYÜZ MODÜLLERİ VE ARAÇLARI İÇERİ AKTARILIR
# //////////////////////////////////////////////////////////////////////////////
from modules.ui.ui_window_main import UIWindowMain
os.environ["QT_FONT_DPI"] = "96" # Yüksek DPI ve %100'ün üzerinde ölçek için sorun düzeltme

if __name__ == "__main__":
    edubot = QApplication(sys.argv)
    edubot.setWindowIcon(QIcon("icon.ico"))
    window = UIWindowMain()
    sys.exit(edubot.exec())
