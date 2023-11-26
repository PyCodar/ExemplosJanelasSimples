import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Criando a aplicação
app = QApplication(sys.argv)

# Criando a janela
janela = QWidget()
janela.setWindowTitle("Janela Vazia")

# Exibindo a janela
janela.show()

# Iniciando o loop principal
sys.exit(app.exec_())
