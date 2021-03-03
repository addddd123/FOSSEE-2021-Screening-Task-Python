from PyQt5.QtWidgets import QApplication 
import sys
import view
import model
class control():
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view = view.window()
        self._model=model.model1()
    def run(self):
        self._view.show()
        return self._app.exec_()

    
if __name__=="__main__":
    obj=control()
    obj.run()