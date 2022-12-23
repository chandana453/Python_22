class Editor:
    def execute(self):
        print("Compiling")
        print("Running")

class Notepad:
    def execute(self):
        print("SpellCheck")
        print("Compiling")
        print("Running")

class Program:
    def code(self,ide):
        ide.execute()

#ide=Editor()
ide=Notepad()

p=Program()
p.code(ide)