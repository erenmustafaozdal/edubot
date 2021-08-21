class UITeacher():

    def __init__(self, window):
        self.window = window

        # ÖĞRETMEN EKLEME TUŞU İLE SAYFA GÖSTERİLİR
        # ///////////////////////////////////////////////////////////////
        self.window.ui.btn_add_teacher.clicked.connect(self.show_teacher)

    # SHOW TEACHER PAGE
    # ///////////////////////////////////////////////////////////////
    def show_teacher(self):
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.teacher)
