import SimpleMemoApp.View.MainView as mv
import SimpleMemoApp.Controller.MainController as mc
import SimpleMemoApp.Model.MainModel as md

def run():
    mainModel = md.MainModel()
    mainController = mc.MainController(mainModel)
    mainView = mv.MainView(mainController)
    mainView.mainloop()
