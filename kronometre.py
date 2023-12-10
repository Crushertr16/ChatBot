import sys
import time
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)




main_window = QtWidgets.QWidget()
main_window.setGeometry(100, 100, 200, 50)
main_window.setWindowTitle("Başlat Durdur Uygulaması")





start_button = QtWidgets.QPushButton("Başlat", main_window)
start_button.setGeometry(10, 10, 75, 30)

def on_start():
    print("Uygulama Başlatıldı!")
    
start_button.clicked.connect(on_start)





stop_button = QtWidgets.QPushButton("Durdur", main_window)
stop_button.setGeometry(110, 10, 75, 30)

def on_stop():
    print("Uygulama Durduruldu!")
    app.quit()
    
stop_button.clicked.connect(on_stop)




main_window.show()
sys.exit(app.exec_())




