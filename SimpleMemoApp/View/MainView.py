import tkinter as tk
import SimpleMemoApp.Controller.MainController as mc

class MainView(tk.Tk):
    def __init__(self, mainController:mc.MainController):
        super().__init__()
        self._mainController = mainController
        
        # Set title and window size.
        self.title("Simple memo app")
        self.geometry("300x400")
        
        # Create label
        label = tk.Label(self, text="Simple memo app")
        label.pack()

        self._textBox = tk.Text(bd=1, relief="solid")
        self._textBox.pack()

        self._saveButton = tk.Button(text="Save", command=self.save_button_click)
        self._saveButton.pack()
        
        self._loadButton = tk.Button(text="Load", command=self.load_button_click)
        self._loadButton.pack()
        

    def save_button_click(self):
        print("Save button clicked")
        contents = self._textBox.get("1.0", tk.END)
        self._mainController.save_memo(contents=contents)

    def load_button_click(self):
        print("Load button clicked")
        loaded_memo = self._mainController.load_memo()
        self._textBox.delete("1.0", tk.END)
        self._textBox.insert("1.0", loaded_memo)

