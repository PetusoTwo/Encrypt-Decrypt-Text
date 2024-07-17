from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
#Autor: PetusoTwo
# Funcion para encriptar el texto
def encriptador_cesar(texto, desplazamiento):
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    texto_encriptado = ''
    
    for letra in texto.lower():
        if letra in alphabet:
            index = alphabet.find(letra)
            new_index = (index + desplazamiento) % len(alphabet)
            texto_encriptado += alphabet[new_index]
        else:
            texto_encriptado += letra
    
    return texto_encriptado

# Funcion para desencriptar el texto
def desencriptador_cesar(texto, desplazamiento):
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    texto_desencriptado = ''
    
    for letra in texto.lower():
        if letra in alphabet:
            index = alphabet.find(letra)
            new_index = (index - desplazamiento) % len(alphabet)
            texto_desencriptado += alphabet[new_index]
        else:
            texto_desencriptado += letra
    
    return texto_desencriptado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        
        # Configuraciones de ventana
        self.setWindowTitle("Encriptador Cesar | PetusoTwo")
        self.setWindowOpacity(1)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Conexion de los Botones
        self.encriptar.clicked.connect(self.encriptar_texto)
        self.desencriptar.clicked.connect(self.desencriptar_texto)
        self.copiaText.clicked.connect(self.copiar_texto)
        self.copiaText.clicked.connect(self.clearData)
        self.btnClose.clicked.connect(lambda: self.close())
        
    def clearData(self):
        self.textEncriptar.clear()
        self.textDesencriptar.clear()
        
    def encriptar_texto(self):
        texto = self.textEncriptar.toPlainText()
        if not texto:
            QMessageBox.warning(self, "Error | PetusoTwo", "No hay texto para encriptar. Ingrese un texto")
            return
        else:
            desplazamiento = 3  # Desplazamiento
            texto_encriptado = encriptador_cesar(texto, desplazamiento)
            self.textDesencriptar.setPlainText(texto_encriptado)
    
    def desencriptar_texto(self):
        texto = self.textEncriptar.toPlainText()
        if not texto:
            QMessageBox.warning(self, "Error | PetusoTwo", "No hay texto para desencriptar. Ingrese un texto")
            return
        else:
            desplazamiento = 3  # Desplazamiento
            texto_desencriptado = desencriptador_cesar(texto, desplazamiento)
            self.textDesencriptar.setPlainText(texto_desencriptado)
    
    def copiar_texto(self):
        texto_encriptado = self.textDesencriptar.toPlainText()
        if texto_encriptado:
            clipboard = QApplication.clipboard()
            clipboard.setText(texto_encriptado)
            QMessageBox.information(self, "Exito | PetusoTwo", "Texto copiado al portapapeles")
        else:
            QMessageBox.warning(self, "Error | PetusoTwo", "No hay texto para copiar")
    #Autor PetusoTwo
    #Funciones para que la ventana se pueda mover#
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_position = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.click_position is not None:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_position)
            self.click_position = event.globalPosition().toPoint()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_position = None

# Inicializar la aplicación
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
#Autor PetusoTwo
