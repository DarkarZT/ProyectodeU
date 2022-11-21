
from ast import Try
from ctypes import alignment
from distutils.cmd import Command
from email import message
from email.mime import image
from msilib.schema import Icon
from tkinter import *
from tkinter import messagebox
from turtle import title
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk

class Login_Polimed:
    ####################### DIMENSIONES DE LA PANTALLA Y COLOR DEL FONDO ############
    def __init__(self,ventana):
        self.ventana = ventana
        self.NombreUsuario= StringVar()
        self.ContrasenaUsuario= StringVar()
        self.ventana.title("PoliMed")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+450+250"%(w/2,h/2))
        self.ventana.config(bg="#91B8C1") 
        self.ventana.resizable(0,0)
        self.ventana.attributes("-fullscreen", True)

        #################### IMAGEN DE LOGO TIPO ########################
    
        self.image = Image.open("hh.png")
        self.image = self.image.resize((150,150),Image.Resampling.LANCZOS)
        Lg_Polimed = ImageTk.PhotoImage(self.image)
        label_Logo = Label(ventana, image = Lg_Polimed, bg="#91B8C1")
        label_Logo.image = Lg_Polimed
        label_Logo.pack()

        ##################### TITULOS, ENTRADAS, BOTONES ######################
        self.Primer_titulo = Label (ventana, text= "Poli-Med", font=("Comic Sans MS",30,), bg="#91B8C1").pack()
        self.Titulo_De_Usuario = Label(ventana, text = "Usuario", font = ("Comic Sans MS",14,), bg = "#91B8C1").pack()
        self.Primera_Entrada = Entry(ventana, font = ("Comic Sans MS",12,), textvariable= self.NombreUsuario).pack()
        self.Espacio_Emergencia= Label(ventana, text = " ", font=("Comic Sans MS",14), bg = "#91B8C1").pack()
        self.Titulo_De_Password = Label (ventana, text = "Contraseña", font=("Comic Sans MS",14), bg = "#91B8C1").pack()
        self.Segunda_Entrada = Entry(ventana, font= ("Comic Sans MS",12,), show="*", textvariable= self.ContrasenaUsuario) 
        self.Segunda_Entrada.pack()  
        self.Espacio_Emergencia2= Label(ventana, text = " ", font=("Comic Sans MS",14), bg = "#91B8C1").pack()
        self.Boton_Ingreso = Button (ventana, text= "Ingresar", font = ("Comic Sans MS", 16), bg = "#91B8C1", command= self.Datos_Para_Validar).pack()
        self.Espacio_Emergencia3 = Label(ventana, text="", bg = "#91B8C1").pack()
        self.Boton_Registro = Button (ventana, text= "Registrarse", font = ("Comic Sans MS", 16), bg = "#91B8C1", command= self.Conexion).pack()
        ####################### CONEXION CON BASE DE DATOS ############################################
    def Conexion(self):
        self.bd = pymysql.connect(
            user = "root",
            host = "localhost",
            passwd= "",
            db = "usuariospoli"
        )
        self.fcursor = self.bd.cursor()
        
        self.sql = "INSERT INTO tablausuarios (Usuarios, Contra) VALUE ('{0}','{1}')".format(self.NombreUsuario.get(), self.ContrasenaUsuario.get())
        
        try:
            
            self.fcursor.execute(self.sql)
            self.bd.commit()
            messagebox.showinfo(message="Registro Realizado", title="Aviso")
            
        except:
            self.bd.rollback()
            messagebox.showinfo(message= "Registro NO Realizado", title= "Aviso")
        
        self.bd.close()
    ############################# VALIDACION DE DATOS DE USUARIO ####################################################    
    def Datos_Para_Validar(self):
        self.bd = pymysql.connect(
            user = "root",
            host = "localhost",
            passwd= "",
            db = "usuariospoli"
        )
        
        self.fcursor = self.bd.cursor()
        
        self.fcursor.execute("SELECT Contra FROM tablausuarios WHERE Usuarios='"+self.NombreUsuario.get()+"'and Contra='"+self.ContrasenaUsuario.get()+"'")
        
        if self.fcursor.fetchall():
            self.primer_toplevel()
            
            
        else:
            messagebox.showinfo(message="Contraseña o Usuarios Incorrectos", title= "Aviso de loggin")
            
        self.bd.close()
    
    def Cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana.quit()
    ################### VENTANA 3 #############################
    def Medicina_General(self):
        self.ventana2.withdraw()
        self.ventana3 = Toplevel()
        self.ventana3.iconbitmap("")
        self.ventana3.config(bg="light slate blue")
        altu, anch = self.ventana3.winfo_screenwidth(), self.ventana3.winfo_screenheight()
        self.ventana3.geometry("%dx%d+450+250"%(altu/2,anch/2))
        self.ventana3.title("Medicina General")
        self.ventana3.resizable(1,1)
        self.ventana3.attributes("-fullscreen", True)
        ############################################ Pestañas de Comunas#########################################
        self.panel2= ttk.Notebook(self.ventana3)
        self.pestana1 = Frame(self.panel2)
        self.pestana2 = Frame(self.panel2)
        self.pestana3 = Frame(self.panel2)
        self.pestana4 = Frame(self.panel2)
        self.pestana5 = Frame(self.panel2)
        self.pestana6 = Frame(self.panel2)
        self.pestana7 = Frame(self.panel2)
        self.pestana8 = Frame(self.panel2)
        self.pestana9 = Frame(self.panel2)
        self.pestana10 = Frame(self.panel2)
        self.pestana11 = Frame(self.panel2)
        self.pestana12 = Frame(self.panel2)        
        self.pestana13 = Frame(self.panel2)
        self.pestana14 = Frame(self.panel2)
        self.pestana15 = Frame(self.panel2)
        self.pestana16 = Frame(self.panel2)
        self.panel2.add(self.pestana1, text="Comuna 1")
        self.panel2.add(self.pestana2, text="Comuna 2")
        self.panel2.add(self.pestana3, text="Comuna 3")
        self.panel2.add(self.pestana4, text="Comuna 4")
        self.panel2.add(self.pestana5, text="Comuna 5")
        self.panel2.add(self.pestana6, text="Comuna 6")
        self.panel2.add(self.pestana7, text="Comuna 7")
        self.panel2.pack(expand=2, fill="both")
        ############################################### Pestaña 1 #############################################
        self.Titulo_de_Apartado = Label(self.pestana1, text="Bienvenido a Medicina General", bg = "light slate blue", font= ("Comic Sans MS", 18)).pack()
        
        self.Boton_Comuna1= Button (self.pestana1, text="Comuna 1", bg= "light slate blue", font=("Comic Sans MS", 14)).pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        #################################################### Pestaña 2 #########################################
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack(side="left")
        self.BotonVolver = Button(self.pestana2,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack(side="right")
        #################################################### Pestaña 3 #########################################
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack(side="left")
        self.BotonVolver = Button(self.pestana3,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack(side="right")
        #################################################### Pestaña 4 #########################################
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack(side="left")
        self.BotonVolver = Button(self.pestana4,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack(side="right")
        #################################################### Pestaña 5 #########################################
        self.BotonCerrar = Button(self.pestana5,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack(side="left")
        self.BotonVolver = Button(self.pestana5,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack(side="right")
        #################################################### Pestaña 6 #########################################
        self.BotonCerrar = Button(self.pestana6,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack(side="left")
        self.BotonVolver = Button(self.pestana6,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack(side="right")        
        self.ventana3.mainloop()
        
    def primer_toplevel(self):
        self.ventana2 = Toplevel()
        w, h = self.ventana2.winfo_screenwidth(), self.ventana2.winfo_screenheight()
        self.ventana2.geometry("%dx%d+450+260"%(w/2,h/2))
        self.ventana2.config(bg="#C7D8D9") 
        self.ventana2.title("Menú de Selección")
        self.ventana2.resizable(1,1)
        self.ventana2.attributes("-fullscreen", True)
        self.ventana.withdraw()
        self.panel = ttk.Notebook(self.ventana2) 
        self.pestana1 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel, bg ="#C7D8D9")
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.add(self.pestana4, text="Oftalmología")
        self.panel.pack(expand=2, fill="both")
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg = "light slate blue", font =("Comic Sans MS", 12)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="ESTO ES UN TEXTO DE EJEMPLO NECESITO IDEAS PARA PODER CONFORMAR DICHO TEXTO POR LO TANTO VAN A VER QUE REPITO MUCHO RESPECTO A LOS TEXTOS Y SIGO HACIENDO REFERENCIA A QUE ES UN TEXTO DE EJEMPLO PORQUE NECESITO IDEAS PARA RELLENAR DICHO APARTADO ASI QUE SI LEEN ESTO DEN IDEAS THANKS", wraplength= 350).pack()
        ################################################## Pestaña 1 #############################################
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 12), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()

        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Medicina_General).pack()        
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Boton_Optometria = Button (self.pestana3, text= "Optometria", bg = "light slate blue", font =("Comic Sans MS", 12,), command= self.optometria).pack()        
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 4 #############################################
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        self.ventana2.mainloop()
                
    def segundo_toplevel(self):
        self.ventana3.withdraw()
        self.ventana2 = Toplevel()
        w, h = self.ventana2.winfo_screenwidth(), self.ventana2.winfo_screenheight()
        self.ventana2.geometry("%dx%d+450+260"%(w/2,h/2))
        self.ventana2.config(bg="#C7D8D9") 
        self.ventana2.title("Menú de Selección")
        self.ventana2.resizable(1,1)
        self.ventana2.attributes("-fullscreen", True)
        self.ventana.withdraw()
        self.panel = ttk.Notebook(self.ventana2) 
        self.pestana1 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel, bg ="#C7D8D9")
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.add(self.pestana4, text="Oftalmología")
        self.panel.pack(expand=2, fill="both")
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg = "light slate blue", font =("Comic Sans MS", 12)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="ESTO ES UN TEXTO DE EJEMPLO NECESITO IDEAS PARA PODER CONFORMAR DICHO TEXTO POR LO TANTO VAN A VER QUE REPITO MUCHO RESPECTO A LOS TEXTOS Y SIGO HACIENDO REFERENCIA A QUE ES UN TEXTO DE EJEMPLO PORQUE NECESITO IDEAS PARA RELLENAR DICHO APARTADO ASI QUE SI LEEN ESTO DEN IDEAS THANKS", wraplength= 350).pack()
        ################################################## Pestaña 1 #############################################
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 12), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()

        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Medicina_General).pack()        
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Boton_Optometria = Button (self.pestana3, text= "Optometria", bg = "light slate blue", font =("Comic Sans MS", 12,), command= self.optometria).pack()        
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 4 #############################################
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        self.ventana2.mainloop()
########################################## 3re Toplevel ###############################
    def tercer_toplevel(self):
        self.ventana4.withdraw()
        self.ventana2 = Toplevel()
        w, h = self.ventana2.winfo_screenwidth(), self.ventana2.winfo_screenheight()
        self.ventana2.geometry("%dx%d+450+260"%(w/2,h/2))
        self.ventana2.config(bg="#C7D8D9") 
        self.ventana2.title("Menú de Selección")
        self.ventana2.resizable(1,1)
        self.ventana2.attributes("-fullscreen", True)
        self.ventana.withdraw()
        self.panel = ttk.Notebook(self.ventana2) 
        self.pestana1 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel, bg ="#C7D8D9")
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.add(self.pestana4, text="Oftalmología")
        self.panel.pack(expand=2, fill="both")
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg = "light slate blue", font =("Comic Sans MS", 12)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="ESTO ES UN TEXTO DE EJEMPLO NECESITO IDEAS PARA PODER CONFORMAR DICHO TEXTO POR LO TANTO VAN A VER QUE REPITO MUCHO RESPECTO A LOS TEXTOS Y SIGO HACIENDO REFERENCIA A QUE ES UN TEXTO DE EJEMPLO PORQUE NECESITO IDEAS PARA RELLENAR DICHO APARTADO ASI QUE SI LEEN ESTO DEN IDEAS THANKS", wraplength= 350).pack()
        ################################################## Pestaña 1 #############################################
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 12), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()

        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Medicina_General).pack()        
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Boton_Optometria = Button (self.pestana3, text= "Optometria", bg = "light slate blue", font =("Comic Sans MS", 12,), command= self.optometria).pack()        
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 4 #############################################
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        self.ventana2.mainloop()

       
########################################### Optometria ################################
    def optometria(self):
        self.ventana2.withdraw()
        self.ventana4 = Toplevel()
        self.ventana4.config(bg ="#C7D8D9")
        alto, anc = self.ventana4.winfo_screenwidth(), self.ventana4.winfo_screenheight()
        self.ventana4.geometry("%dx%d+450+250"%(alto/2,anc/2))
        self.ventana4.title("Optometria")
        self.ventana4.attributes("-fullscreen", True)
        self.panel3= ttk.Notebook(self.ventana4)
        self.pestana1 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana5 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana6 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana7 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana8 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana9 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana10 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana11 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana12 = Frame(self.panel3, bg ="#C7D8D9")        
        self.pestana13 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana14 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana15 = Frame(self.panel3, bg ="#C7D8D9")
        self.pestana16 = Frame(self.panel3, bg ="#C7D8D9")
        self.panel3.add(self.pestana1, text="Comuna 1")
        self.panel3.add(self.pestana2, text="Comuna 2")
        self.panel3.add(self.pestana3, text="Comuna 3")
        self.panel3.add(self.pestana4, text="Comuna 4")
        self.panel3.add(self.pestana5, text="Comuna 5")
        self.panel3.add(self.pestana6, text="Comuna 6")
        self.panel3.add(self.pestana7, text="Comuna 7")
        self.panel3.add(self.pestana8, text="Comuna 8")
        self.panel3.add(self.pestana9, text="Comuna 9")
        self.panel3.add(self.pestana10, text="Comuna 10")
        self.panel3.add(self.pestana11, text="Comuna 11")
        self.panel3.add(self.pestana12, text="Comuna 12")
        self.panel3.add(self.pestana13, text="Comuna 13")
        self.panel3.add(self.pestana14, text="Comuna 14")
        self.panel3.add(self.pestana15, text="Comuna 15")
        self.panel3.add(self.pestana16, text="Comuna 16")
        self.panel3.pack(expand=2, fill="both")
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack(side="right")
        self.ventana4.mainloop()
    def instrucctivo(self):
        self.ventana2.withdraw()
        self.ventana5 = Toplevel()
        self.ventana5.config(bg="#C7D8D9")
        alto, anc = self.ventana5.winfo_screenwidth(), self.ventana5.winfo_screenheight()
        self.ventana5.geometry("%dx%d+450+250"%(alto/2,anc/2))
        self.ventana5.title("Información")
        self.ventana5.resizable(1,1)
        self.ventana5.attributes("-fullscreen", True)
        self.panel4 = ttk.Notebook(self.ventana5)
        self.pestana1 = Frame(self.panel4, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel4, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel4, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel4, bg ="#C7D8D9")
        self.pestana16 = Frame(self.panel4, bg ="#C7D8D9")
        self.panel4.add(self.pestana1, text= "Navegacion de pestañas")
        self.panel4.add(self.pestana2, text= "Conoce  la interfaz")
        self.panel4.add(self.pestana3, text= "Ayudas visuales")
        self.panel4.add(self.pestana4, text= "Creditos")
        self.panel4.pack(expand=2, fill="both")
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.ventana5.mainloop()     
########################################### Inicio de Sesion ##########################
def inicio():
    ventana = Tk()
    Login_Polimed(ventana)

    ventana.mainloop()


##############
#################################
######################