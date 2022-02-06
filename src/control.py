from PyQt5 import uic, QtWidgets
def func_principal():

    linha1 = style.lineEdit.text()
    linha2 = style.lineEdit_2.text()
    linha3 = style.lineEdit_3.text()

    if style.radioButton.isChecked() :
        print("Categoria Eletrónicos selecionada")
    elif style.radioButton_2.isChecked() :
        print("Categoria Informática selecionada")
    else :
        print("Categoria Alimentos selecionada")

    print("Código:",linha1)
    print("Descrição:",linha2)
    print("Preço",linha3)


app=QtWidgets.QApplication([])
style=uic.loadUi("style.ui")
style.pushButton.clicked.connect(func_principal)

style.show()
app.exec()
