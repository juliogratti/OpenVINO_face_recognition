from tkinter import *
from tkinter import ttk
import threading

class Application:
    def __init__(self,master=None):
        pass



class TelaPrincipal:
    def __init__ (self, master=None):

        self.root_principal = Tk()

        fonte_titulos = "Arial bold","15"


        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [50, 10],"font" : ('Arial', '13', 'bold')},}})
        s.theme_use("MyStyle")

        self.tab_control = ttk.Notebook(self.root_principal)
        self.aba_monitorar = Frame(self.tab_control)
        self.aba_cadastrar = Frame(self.tab_control)
        self.aba_consultar = Frame(self.tab_control)
        self.tab_control.add(self.aba_monitorar, text="MONITORAR")
        self.tab_control.add(self.aba_cadastrar, text="CADASTRAR")
        self.tab_control.add(self.aba_consultar, text="CONSULTAR")
        self.tab_control.pack(expand=1, fill="both")

        self.label_status_monitorar = Label(self.aba_monitorar, text="AAAAAAAAaa")
        self.label_status_monitorar.place(x=10,y=10)

        self.label_status_cadastrar = Label(self.aba_cadastrar, text="bbbbbbbbb")
        self.label_status_cadastrar.place(x=50,y=50)

        #=========================   MONITORAR  ============================================
        self.btn_iniciar  = Button(self.aba_monitorar, text="Iniciar", command=self.iniciarMonitoramento, fg="red")
        self.btn_iniciar.place(x=350,y=50)


        #=========================   CADASTRAR  ============================================

        #=========================   CONSULTAR  ============================================



        screen_width = self.root_principal.winfo_screenwidth()
        screen_height = self.root_principal.winfo_screenheight()
        x = (screen_width - 800)/2
        y = (screen_height - 700)/2
        self.root_principal.geometry('800x700+{}+{}'.format(int(x),int(y)))
        self.root_principal.title("Face Recognition")
        self.root_principal.mainloop()




    
    




def main():
    TelaPrincipal(master=None)

if __name__ == '__main__':
    main()