import SimpleMemoApp.Model.MainModel as md

class MainController():
    def __init__(self, mainModel:md.MainModel):
        self._mainModel = mainModel

    def save_memo(self, contents):
        self._mainModel.save_memo(contents=contents)
        
    def load_memo(self) -> str:
        return self._mainModel.load_memo()


