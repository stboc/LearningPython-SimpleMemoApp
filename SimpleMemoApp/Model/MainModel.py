class MainModel():
    SAVED_MEMO_FILE = "SimpleMemoApp_SavedText.txt"
    
    def __init__(self):
        return
    
    def save_memo(self, contents):
        print("Save")
        with open(self.SAVED_MEMO_FILE, "w") as writer:
            writer.write(contents)

    def load_memo(self) -> str:
        print("Load")
        with open(self.SAVED_MEMO_FILE, "r") as reader:
            return reader.read()