
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
        self.panel2.add(self.pestana8, text="Comuna 8")
        self.panel2.add(self.pestana9, text="Comuna 9")
        self.panel2.add(self.pestana10, text="Comuna 10")
        self.panel2.add(self.pestana11, text="Comuna 11")
        self.panel2.add(self.pestana12, text="Comuna 12")
        self.panel2.add(self.pestana13, text="Comuna 13")
        self.panel2.add(self.pestana14, text="Comuna 14")
        self.panel2.add(self.pestana15, text="Comuna 15")
        self.panel2.add(self.pestana16, text="Comuna 16")
        self.panel2.pack(expand=2, fill="both")
        ############################################### Pestaña 1 #############################################
        self.Titulo_de_Apartado = Label(self.pestana1, text="Bienvenido a Medicina General", bg = "light slate blue", font= ("Comic Sans MS", 18)).pack()
        ################################# PESTAÑA 1 COMUNA 1 #################################################
        self.texto_Comunas = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ################################# PESTAÑA 2 COMUNA2 ###############################################
        self.texto_Comunas = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana2,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ############################# PESTAÑA 3 COMUNA 3 ################################################
        
        self.texto_Comunas = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana3,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
               
        ############################ PESTAÑA 4 COMUNA 4 ###################################################
        
        self.texto_Comunas = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana4,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ########################## PESTAÑA 5 COMUNA 5 ####################################################
        
        self.texto_Comunas = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana5,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana5,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 6 COMUNA 6 #######################################################
        
        self.texto_Comunas = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana6,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana6,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 7 COMUNA 7 #########################################################
        
        self.texto_Comunas = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana7,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana7,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 8 COMUNA 8 ########################################################
        
        self.texto_Comunas = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana8,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana8,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 9 COMUNA 9 ##########################################################
        
        self.texto_Comunas = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana9,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana9,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 10 COMUNA 10 #########################################################
        
        self.texto_Comunas = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana10,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana10,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ##################### PESTAÑA 11 COMUNA 11 ############################################################
        
        self.texto_Comunas = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana11,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana11,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        #################### PESTAÑA 12 COMUNA 12 #################################################################
        
        self.texto_Comunas = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana12,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana12,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ######################## PESTAÑA 13 COMUNA 13 ##############################################
        
        self.texto_Comunas = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana13,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana13,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ########################## PESTAÑA 14 COMUNA 14 ############################################
        
        self.texto_Comunas = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana14,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana14,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ######################### PESTAÑA 15 COMUNA 15 ############################################
        
        self.texto_Comunas = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana15,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana15,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 16 COMUNA 16 ################################################
        
        self.texto_Comunas = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana16,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana16,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
                
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
        ################################# PESTAÑA 1 COMUNA 1 #################################################
        self.texto_Comunas = Label(self.pestana1, text = "Cr 32 #102 b - 03 - Óptical Visual New\n 3012549724",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana1, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ################################# PESTAÑA 2 COMUNA2 ###############################################
        self.texto_Comunas = Label(self.pestana2, text = "Cra. 50A # 41-42 - OPTICALIA\n 43739111",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana2, text = "",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana2, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana2,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ############################# PESTAÑA 3 COMUNA 3 ################################################
        
        self.texto_Comunas = Label(self.pestana3, text = "Calle 72 # 44-105 CC Gardel Plaza L-131 Optiplus \n 3105997940",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana3, text = "Cl. 80 #44-79 Optica la 45 \n 75026476",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana3, text = "Cra. 45 #78-66 Optica Digital Max \n 63018102",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana3, text = "Cra. 47 #49 69 Ips Optica la plazuela \n 5129146",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana3, text = "Cl. 78 #44-88 Focus Optical \n 3175231522",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana3, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana3,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
               
        ############################ PESTAÑA 4 COMUNA 4 ###################################################
        
        self.texto_Comunas = Label(self.pestana4, text = "Cra. 47 # 52 - 143 Optica Veo Veo \n 4253397",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana4, text = "Cra. 49A #30 Óptica Aranjuez \n 44489091",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana4, text = "Calle 92 # 50d-44 Óptica Comfort Visual aranjuez \n 3136932597",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana4, text = "Cra. 47 #48-82 Óptica Vision Forte \n 3127502867",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana4, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana4,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ########################## PESTAÑA 5 COMUNA 5 ####################################################
        
        self.texto_Comunas = Label(self.pestana5, text = "Cl.46 #5310 Gran Visual Optica \n 310410560",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana5, text = "Cra. 51a #4648 Óptica imperio \n 3013423002",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana5, text = "Cra. 47 #54-32 Óptica Lentisol \n 3123969996",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana5, text = "Cra. 47 #52-153 Ópticalia express \n 3052420794",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana5, text = "Cra 47 49 59 Somos la Óptica \n 3122697300",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana5, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana5,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana5,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 6 COMUNA 6 #######################################################
        
        self.texto_Comunas = Label(self.pestana6, text = "Cl. 104 #7453 Optica mas cercana \n 3024402307",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana6, text = "Cra. 82e #102a \n 3218118969",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana6, text = "weffrf",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana6, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana6,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana6,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 7 COMUNA 7 #########################################################
        
        self.texto_Comunas = Label(self.pestana7, text = "Cra. 85b #77c-40 Óptica espejo visual \n 3217901122",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana7, text = "Cl. 80 # 72a-201 Óptica Vision estelar \n 3105427136 ",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana7, text = "Cr91B, Cl. 77 cc #42 Óptica vision infinita \n 3116127485",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana7, text = "Cra. 68 #91-20 optica San Judas \n 6042677450",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana7, text = "Cra. 74 #106a18  Óptica soluciones visuales medellin \n 6042677450 ",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana7, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana7,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana7,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 8 COMUNA 8 ########################################################
        
        self.texto_Comunas = Label(self.pestana8, text = "Cl. 40 #65aa-45 Óptica Villa hermosa \n 3153025644",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana8, text = "Calle 57 # 49 44 Local 237 Oftalvision \n 44481760",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana8, text = "Cra. 46 #47-36 Óptica vision clara \n 44236218",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana8, text = "Cra 49 # 57 - 51 Centro Óptico villanueva \n 3186423693",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana8,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana8,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 9 COMUNA 9 ##########################################################
        
        self.texto_Comunas = Label(self.pestana9, text = "Cl. 49 #38-28 Óptica Ayacucho \n 3003102017",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana9,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana9,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 10 COMUNA 10 #########################################################
        
        self.texto_Comunas = Label(self.pestana10, text = "Cl. 46 #5310 Gran Visual Optica \n 3204338764",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana10, text = "Cra. 47 #49-79 Optica Maxigafas \n 3177366621",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana10, text = "Cra. 49 #48-64 Optica Nacional \n 6044446359",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana10, text = "Cra. 51a #4648 Optica imperio \n 3013423002",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana10, text = "Cra. 47 #52-46 CrediOptica.IPS \n 45118882",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana10, text = "Cl. 53 #47-55 Medi Óptica \n 3104522868",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana10, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana10,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana10,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ##################### PESTAÑA 11 COMUNA 11 ############################################################
        
        self.texto_Comunas = Label(self.pestana11, text = "CC unicentro, Carrera 66B # 34A - 76 Local 365 Neuta Caro Optometria Especializada \n 3118818604",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana11, text = "Cra. 65 #48 C - 18 Su vision ideal \n 42307017",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana11, text = "Cra. 65 #65-20 Center vision \n 45815259",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana11, text = "Cl. 47 #No. 70 - 31 Visso-Omni \n 3004567644",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana11, text = "Cra. 66 #48D-24 Óptica Alta Vista \n 3166362513",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana11, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana11,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana11,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        #################### PESTAÑA 12 COMUNA 12 #################################################################
        
        self.texto_Comunas = Label(self.pestana12, text = "Cra. 87 # 47-32 Optilux \n 3134840521",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana12, text = "Cl. 47DD #87-4 Infocus optica \n 4088407",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana12,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana12,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ######################## PESTAÑA 13 COMUNA 13 ##############################################
        
        self.texto_Comunas = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana13, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana13,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana13,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ########################## PESTAÑA 14 COMUNA 14 ############################################
        
        self.texto_Comunas = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana14, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana14,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana14,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ######################### PESTAÑA 15 COMUNA 15 ############################################
        
        self.texto_Comunas = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana15, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana15,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana15,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 16 COMUNA 16 ################################################
        
        self.texto_Comunas = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas9 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas10 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas11 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas12 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas13 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas14 = Label(self.pestana16, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana16,text= "Salir", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana16,text= "Regresar", bg = "light slate blue", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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

###
###
##############
#################################
######################