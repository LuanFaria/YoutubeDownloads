import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar
from interface import *
from pytube import YouTube
from time import sleep



class Youtube_Download(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)
        super().setupUi(self)

        # Fixar nesse tamanho
        self.setFixedSize(460, 369)

        # CSS

        self.titulo.setStyleSheet(
            '* {background: Red; color: White; font-weight: bold; font-size: 25px; border-radius: 20px}'
        )
        #
        self.setStyleSheet(
            '* {background: PeachPuff}'  # Formatação em CSS
        )
        self.listView.setStyleSheet(
            '* {background:  white}'  # Formatação em CSS
        )
        self.resultado.setStyleSheet(
            '* {background: white}'  # Formatação em CSS
        )
        self.download_andamento.setStyleSheet(
            '* {background: white}'
        )
        self.bt_mp4.setStyleSheet(
            '* {background:   	white}'
        )
        self.bt_mp3.setStyleSheet(
            '* {background:  	 white}'
        )
        self.tempo.setStyleSheet(
            '* {background:  	white}'
        )
        self.input.setStyleSheet(
            '* {background:  	white}'
        )


        self.bt_mp3.clicked.connect(self.mp3)
        self.bt_mp4.clicked.connect(self.mp4)


    def mp4(self):
        try:
            self.download_andamento.setText(' ')
            self.resultado.setText(' ')
            self._link = self.input.text()
            self._yt = YouTube(self._link)
            self.listView.setStyleSheet(
                '* {background:   	#98FB98}'  # Formatação em CSS
            )
            self.resultado.setStyleSheet(
                '* {background:   	 	#98FB98; color:green; font-weight: bold; font-size:20px}'  # Formatação em CSS
            )
            self.download_andamento.setStyleSheet(
                '* {background:  #98FB98;color:green;font-weight: bold; font-size: 14px}'  # Formatação em CSS
            )
            self.download_andamento.setText('O Mp4 {} está sendo baixado...'.format(self._yt.title))

            # Barra de Download...
            n = 100
            for i in range(n):
                sleep(0.05)
                self.tempo.setValue(i + 1)
                ##########################

            video = self._yt.streams.first()
            video.download()
            self.resultado.setText('Download com sucesso!')

        except:
            self.listView.setStyleSheet(
                '* {background:  #FA8072}'  # Formatação em CSS
            )
            self.download_andamento.setStyleSheet(
                '* {background:  #FA8072;color:red;font-weight: bold; font-size: 14px}'  # Formatação em CSS
            )
            self.download_andamento.setText('-'*110)
            self.resultado.setStyleSheet(
                '* {background:  #FA8072; color:red; font-weight: bold; font-size:20px}'  # Formatação em CSS
            )
            self.resultado.setText('Download Falhou!')


    def mp3(self):
        try:
            self.download_andamento.setText(' ')
            self.resultado.setText(' ')
            self._link = self.input.text()
            self._yt = YouTube(self._link)

            self.listView.setStyleSheet(
                '* {background:   	#98FB98}'  # Formatação em CSS
            )
            self.resultado.setStyleSheet(
                '* {background:   	 	#98FB98; color:green; font-weight: bold; font-size:20px}'  # Formatação em CSS
            )
            self.download_andamento.setStyleSheet(
                '* {background:  #98FB98;color:green;font-weight: bold; font-size: 14px}'  # Formatação em CSS
            )
            self.download_andamento.setText('O Mp3 {} está sendo baixado...'.format(self._yt.title))

            # Barra de Download...
            n = 100
            for i in range(n):
                sleep(0.05)
                self.tempo.setValue(i + 1)
                ##########################

            audio = self._yt.streams.get_audio_only()
            audio.download()
            self.resultado.setText('Download com sucesso!')


        except:
            self.listView.setStyleSheet(
                '* {background:  #FA8072}'  # Formatação em CSS
            )
            self.download_andamento.setStyleSheet(
                '* {background:  #FA8072;color:red;font-weight: bold; font-size: 14px}'  # Formatação em CSS
            )
            self.download_andamento.setText('-'*110)
            self.resultado.setStyleSheet(
                '* {background:  #FA8072; color:red; font-weight: bold; font-size:20px}'  # Formatação em CSS
            )
            self.resultado.setText('Download Falhou!')








if __name__ == '__main__':
    qt = QApplication(sys.argv)
    you = Youtube_Download()
    you.show()
    qt.exec_()
