
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
        self.ventana3.config(bg="#C7D8D9")
        altu, anch = self.ventana3.winfo_screenwidth(), self.ventana3.winfo_screenheight()
        self.ventana3.geometry("%dx%d+450+250"%(altu/2,anch/2))
        self.ventana3.title("Medicina General")
        self.ventana3.resizable(1,1)
        self.ventana3.attributes("-fullscreen", True)
        ############################################ Pestañas de Comunas#########################################
        self.panel2= ttk.Notebook(self.ventana3)
        self.pestana1 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana2 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana3 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana4 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana5 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana6 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana7 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana8 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana9 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana10 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana11 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana12 = Frame(self.panel2, bg ="#C7D8D9")        
        self.pestana13 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana14 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana15 = Frame(self.panel2, bg ="#C7D8D9")
        self.pestana16 = Frame(self.panel2, bg ="#C7D8D9")
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
        self.Titulo_de_Apartado = Label(self.pestana1, text="Bienvenido a Medicina General", bg = "#C7D8D9", font= ("Comic Sans MS", 18)).pack()

        ################################# PESTAÑA 1 COMUNA 1 #################################################
        self.texto_Comunas = Label(self.pestana1, text = "Cra.43b #108 - 6  Centro de salud popular 1 \n 3138313938",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana1, text = "Cra. 42 #20-92 Hospital Zamora \n 60444482030",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ################################# PESTAÑA 2 COMUNA2 ###############################################
        self.texto_Comunas = Label(self.pestana2, text = "Cra.51A #100-50 Unidad intermedia santa cruz \n 300443322",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana2, text = "Cl. 105 #49-45 Centro de salud villa del socorro \n 6044756565",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana2, text = "Cra. 25 #1 Puesto de salud la cruz \n 604565430",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana2,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ############################# PESTAÑA 3 COMUNA 3 ################################################
        
        self.texto_Comunas = Label(self.pestana3, text = "Cl. 71c #32-65 Centro de salud el raizal \n 4767574",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana3, text = "Cl. 66f #43-81 Unidad hospitalaria Manrique \n 6044446570",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana3, text = "Cll. 95A con Cra. 38 Hospital Pablo Tobon \n 604565740",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana3, text = "Cll 89 con Cra 36A Centro de salud San Blas \n 604354070",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana3, text = "Cra. 45 #83-42 Centro medico la samaritana \n 60444087027",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana3,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
               
        ############################ PESTAÑA 4 COMUNA 4 ###################################################
        
        self.texto_Comunas = Label(self.pestana4, text = "Cra. 51 #91 Consultorio medico San Cayetano \n 60442364076",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana4, text = "Cra. 50A #93-39 Centro de salud Aranjuez \n 604354233",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana4,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ########################## PESTAÑA 5 COMUNA 5 ####################################################
        
        self.texto_Comunas = Label(self.pestana5, text = "Cra. 65 #97-5 Copsana Ips sede norte \n 6044440051",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana5, text = "Cl. 98a #65-120 Unidad Intermedia Castilla \n 60444256440",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana5, text = "Cra. 65 #98-115 Metrosalud \n 6044543215",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana5, text = "Cll. 92ee #67-61 Hospital la María E.S.E \n 60444447192",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana5, text = "Cra. 70a #91-17 Centro de salud Alfonso Lopez \n 604564739",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()   
        self.BotonVolver = Button(self.pestana5,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana5,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ###################### PESTAÑA 6 COMUNA 6 #######################################################
        
        self.texto_Comunas = Label(self.pestana6, text = "Clle 108BB # 78-10 Unidad hospitalaria doce de octubre \n 60444782800",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana6, text = "Cl. 102 #83-99 Intermedia del doce \n 604657877",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana6, text = "83a-80, Cl. 104dd #83a-2 Salud total \n 6044508877",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana6,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana6,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ###################### PESTAÑA 7 COMUNA 7 #########################################################
        
        self.texto_Comunas = Label(self.pestana7, text = "Cll.82 #87-100 Centro de salud San Camilo \n 3014110358",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana7, text = "Cl. 78b #72 A-220 Clinica VID \n 3126543387",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana7, text = "Cra. 72A #78b - 50 Clina Universitaria bolivariana \n 6044455900",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana7, text = "Cl.78b #69-240 Hospital pablo tobon Uribe \n 6044459000",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana7, text = "Cl. 75 #75-29 Metrosalud centro de salud robledo \n 60442340070",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana7,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana7,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ####################### PESTAÑA 8 COMUNA 8 ########################################################
        
        self.texto_Comunas = Label(self.pestana8, text = "Cra. 17b#56e-61 Centro de salud sol de oriente \n 3106452233",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana8, text = "Cra.23 #56eh-1 Metro salud enciso \n 604456570",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana8, text = "Cra. 30 #58-100 Centro de salud enciso \n 604345423",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana8, text = "Cra.17a #54-63 Centro de salud villatina \n 604354657",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana8, text = "Cll.63 / Darien #41-27 Clinica Rosario \n 604453245",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana8,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana8,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ###################### PESTAÑA 9 COMUNA 9 ##########################################################
        
        self.texto_Comunas = Label(self.pestana9, text = "Cl.49a ##582 San ignacio 604567843",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana9, text = "Cra. 28a #38F Centro de salud loreto",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana9, text = "Cra. 29 #4215 Consultorio la milagrosa \n 6044448318",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana9, text = "Cl. 49 #35 - 61 Nueva clinica sagrado corazón \n 6042151000",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana9, text = "Cra. 36 #40 a-30 Centro de salud el salvador \n 60442173194  ",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana9,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana9,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ###################### PESTAÑA 10 COMUNA 10 #########################################################
        
        self.texto_Comunas = Label(self.pestana10, text = "Cl 50 N°46B-60 Coosalud EPS \n 60448372880 ",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana10, text = "Cl 50 #46 36 colmedicos S.A.S \n 60445100500",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana10, text = "Cra. 46 #47-66 IPS Esalud \n 3016569147",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana10, text = "Cl. 51 #45-93 Clinica Soma \n 6045768400",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana10, text = "Cra. 45 #5063 Nueva Eps \n 6044335540",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas6 = Label(self.pestana10, text = "a 49-124, Av carabobo #492 Congracion Mariana",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas7 = Label(self.pestana10, text = "Cra. 49 #58-19 Clinica Victoriana",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas8 = Label(self.pestana10, text = "Cra.56c #50-56 Fundacion Medico preventiva sede colombia \n 314220870",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana10,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana10,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ##################### PESTAÑA 11 COMUNA 11 ############################################################
        
        self.texto_Comunas = Label(self.pestana11, text = "Cl. 47D #70-155 IPS \n 604543422",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana11, text = "Cra.72 #44-57 Florida Nueva \n 604432244",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana11, text = "a 34-156,Dg. 66A #34-2 Santa lucia \n 604454454",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana11, text = "Calle 66b #34A-76 Local 242 DR.Angel Contreras \n 3008828295",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana11, text = "Cl. 44A #79-145 Salud total \n 018000114524",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas6 = Label(self.pestana11, text = "Av. 80 #49a-68 Coopsana IPS \n 6044440051",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()        
        self.BotonVolver = Button(self.pestana11,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana11,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        #################### PESTAÑA 12 COMUNA 12 #################################################################
        
        self.texto_Comunas = Label(self.pestana12, text = "Cra. 70 #1-141 Clinica las americas \n 604434455",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana12, text = "Dg.75B #2 A - 80 Torre 2 Torre Medica las americas \n 6043417070",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana12, text = "Dg. 75B #2A-80/140 Clinica Las Americas Auna \n 6043421010",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana12, text = "Diagonal 75 Dra.Clemencia Duque Vera \n 3136460299",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()        
        self.BotonVolver = Button(self.pestana12,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana12,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ######################## PESTAÑA 13 COMUNA 13 ##############################################
        
        self.texto_Comunas = Label(self.pestana13, text = "Cra.105b #34bb-30 Centro de salud villa laura \n 60444920838",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana13, text = "a 39a-7, Cra. 118 #39a1 Centro de salud cuatro esquinas, la Esperanza \n 3004103000",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana13, text = "Cl. 40 veinte de julio Centro de salud San Javier \n 60442520100",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana13, text = "39b-64, Cra.109 #39b-2 Consultorio medico San vicente \n 60442537417",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()      
        self.BotonVolver = Button(self.pestana13,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana13,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ########################## PESTAÑA 14 COMUNA 14 ############################################
        
        self.texto_Comunas = Label(self.pestana14, text = "Cra. 46 #27-35 Colsanitas IPS \n 60443548871",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana14, text = "Cra. 43 Colsanitas Av.poblado \n 6045675544",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana14, text = "Cl. 19a #44-25 Torre medica salud y servicios \n 3102576598",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana14, text = "Cra. 48 #10-45 Botero sanin \n 6044445523 ",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana14, text = "Cl. 17 #40b-300 coomeva \n 60444157700",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas6 = Label(self.pestana14, text = "Cra. 43B #16-95 local 2 y 5 Centro medico Manila 6046044191",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas7 = Label(self.pestana14, text = "Cl. 14 #43b-9 Metrosalud \n 60445117505",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas8 = Label(self.pestana14, text = "Cl. 7 #39-290 Clinica medellin \n 6043112800",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas9 = Label(self.pestana14, text = "Cl. 7 #39 - 290 piso 3 CediMed S.A.S \n 60446040138",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()      
        self.BotonVolver = Button(self.pestana14,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana14,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ######################### PESTAÑA 15 COMUNA 15 ############################################
        
        self.texto_Comunas = Label(self.pestana15, text = "Cl. 1 sur #51B-36 Consult. medico \n 60442852682",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana15, text = "Cl. 1 #53 - 57 Centro de salud Sura \n 604443434",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana15, text = "Cl. 1c #65-85 EPS Guayabal \n 6044335533",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana15, text = "Cl. 78 #52d-141 Comfama Santa María IPS \n 604564433",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana15, text = "Carrera 55, Cl. 78 Sura EPS Comfama \n 604432244",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana15,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana15,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        
        ####################### PESTAÑA 16 COMUNA 16 ################################################
        
        self.texto_Comunas = Label(self.pestana16, text = "#75,cq. 5 #42 centro medico la mota \n 6042565075 ",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas2 = Label(self.pestana16, text = "Dg. 75B #5-106 Coomeva EPS \n 60444156000",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas3 = Label(self.pestana16, text = "Cl. 2b #100 Centro de salud Belen Rincón \n 6042388000",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas4 = Label(self.pestana16, text = "Cra. 84a #15A - 15 Consultorio medico \n 60443415509",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas5 = Label(self.pestana16, text = "Cra. 83 # 27 consultorio medico \n 3162064037",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas6 = Label(self.pestana16, text = "Cll 28 entre Cra 79A Centro de salud belen \n 60443332439 ",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.texto_Comunas7 = Label(self.pestana16, text = "Dg. 74B belen Ips sevid \n 60444116592",wraplength= 350, font =("", 16), bg="#C7D8D9").pack()
        self.BotonVolver = Button(self.pestana16,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.segundo_toplevel).pack()
        self.BotonCerrar = Button(self.pestana16,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()   
             
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
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.pack(expand=2, fill="both")
        ################################################## Pestaña 1 #############################################
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg ="#C7D8D9", font =("Comic Sans MS", 30)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="Bienvenidos,\n Es un placer para el equipo de PoliMed que puedan estar con nosotros en este momento para navegar por medio de nuestra aplicación. En esta aplicación van a encontrar Textos de ayuda para poder reconocer los diversos sectores de las comunas. Polimed, es una aplicación que permite encontrar centros médicos por medio de un esquema de directorio para que de esta manera el usuario pueda tener facilidad de acceder información de manera rápida y oportuna.", wraplength= 800, font=("",25), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia7 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 16), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Espacio_Emergencia1= Label(self.pestana2, text = " ", font=("Comic Sans MS",28), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="Medicina General", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia2= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="La medicina general constituye el primer nivel de atención médica y es imprescindible para la prevención, detección, tratamiento y seguimiento de las enfermedades crónicas estabilizadas, responsabilizándose del paciente en su conjunto, para decidir su derivación a los especialistas cuando alguna patología se descompense.", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia3= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia4= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura4.PNG")
        self.image = self.image.resize((323,437),Image.Resampling.LANCZOS)
        Medicina_Logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana2, image = Medicina_Logo, bg="#C7D8D9")
        label_Logo.image = Medicina_Logo
        label_Logo.pack()
        self.Espacio_Emergencia5= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Medicina_General).pack()
        self.Espacio_Emergencia7= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Espacio_Emergencia1= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio3 = Label(self.pestana3, text="La optometría es la ciencia sanitaria no médica que estudia el sistema visual, sus alteraciones no patológicas y su solución, así como las normas de salud e higiene visual a cargo del optometrista. La optometría presta especial atención precisamente a defectos visuales que pueden tener su origen en malos hábitos sobre la postura y distancia, por ejemplo, en la lectura, escritura o sobre el tipo de iluminación en nuestro entorno durante el trabajo, etc., y que pudieran provocar casos de fatiga visual.", bg = "#C7D8D9", font= ("Comic Sans MS", 16),wraplength= 700).pack()      
        self.Espacio_Emergencia2= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura5.PNG")
        self.image = self.image.resize((512,512),Image.Resampling.LANCZOS)
        Optometria_logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana3, image = Optometria_logo, bg="#C7D8D9")
        label_Logo.image = Optometria_logo
        label_Logo.pack()
        self.Espacio_Emergencia3= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana3, text="Optometria", bg= "#C7D8D9", font=("Comic Sans MS", 18), command= self.optometria).pack()
        self.Espacio_Emergencia4= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
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
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.pack(expand=2, fill="both")
        ################################################## Pestaña 1 #############################################
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg ="#C7D8D9", font =("Comic Sans MS", 30)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="Bienvenidos,\n Es un placer para el equipo de PoliMed que puedan estar con nosotros en este momento para navegar por medio de nuestra aplicación. En esta aplicación van a encontrar Textos de ayuda para poder reconocer los diversos sectores de las comunas. Polimed, es una aplicación que permite encontrar centros médicos por medio de un esquema de directorio para que de esta manera el usuario pueda tener facilidad de acceder información de manera rápida y oportuna.", wraplength= 800, font=("",25), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia7 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 16), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Espacio_Emergencia1= Label(self.pestana2, text = " ", font=("Comic Sans MS",28), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="Medicina General", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia2= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="La medicina general constituye el primer nivel de atención médica y es imprescindible para la prevención, detección, tratamiento y seguimiento de las enfermedades crónicas estabilizadas, responsabilizándose del paciente en su conjunto, para decidir su derivación a los especialistas cuando alguna patología se descompense.", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia3= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia4= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura4.PNG")
        self.image = self.image.resize((323,437),Image.Resampling.LANCZOS)
        Medicina_Logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana2, image = Medicina_Logo, bg="#C7D8D9")
        label_Logo.image = Medicina_Logo
        label_Logo.pack()
        self.Espacio_Emergencia5= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Medicina_General).pack()
        self.Espacio_Emergencia7= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Espacio_Emergencia1= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio3 = Label(self.pestana3, text="La optometría es la ciencia sanitaria no médica que estudia el sistema visual, sus alteraciones no patológicas y su solución, así como las normas de salud e higiene visual a cargo del optometrista. La optometría presta especial atención precisamente a defectos visuales que pueden tener su origen en malos hábitos sobre la postura y distancia, por ejemplo, en la lectura, escritura o sobre el tipo de iluminación en nuestro entorno durante el trabajo, etc., y que pudieran provocar casos de fatiga visual.", bg = "#C7D8D9", font= ("Comic Sans MS", 16),wraplength= 700).pack()      
        self.Espacio_Emergencia2= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura5.PNG")
        self.image = self.image.resize((512,512),Image.Resampling.LANCZOS)
        Optometria_logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana3, image = Optometria_logo, bg="#C7D8D9")
        label_Logo.image = Optometria_logo
        label_Logo.pack()
        self.Espacio_Emergencia3= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana3, text="Optometria", bg= "#C7D8D9", font=("Comic Sans MS", 18), command= self.optometria).pack()
        self.Espacio_Emergencia4= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
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
        self.panel.add(self.pestana1, text="Acercamiento")
        self.panel.add(self.pestana2, text="Medicina General")
        self.panel.add(self.pestana3, text="Optometria")
        self.panel.pack(expand=2, fill="both")
        ################################################## Pestaña 1 #############################################
        self.Label_Instruccion = Label (self.pestana1, text= "Instrucción de Navegación", bg ="#C7D8D9", font =("Comic Sans MS", 30)).pack()
        self.Espacio_Emergencia4 = Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Texto_explicacion = Label (self.pestana1, text="Bienvenidos,\n Es un placer para el equipo de PoliMed que puedan estar con nosotros en este momento para navegar por medio de nuestra aplicación. En esta aplicación van a encontrar Textos de ayuda para poder reconocer los diversos sectores de las comunas. Polimed, es una aplicación que permite encontrar centros médicos por medio de un esquema de directorio para que de esta manera el usuario pueda tener facilidad de acceder información de manera rápida y oportuna.", wraplength= 800, font=("",25), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia7 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana1, text="Información", bg= "#C7D8D9", font=("Comic Sans MS", 16), command= self.instrucctivo).pack()
        self.Espacio_Emergencia5 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6 =Label(self.pestana1, text="", bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 2 #############################################
        self.Espacio_Emergencia1= Label(self.pestana2, text = " ", font=("Comic Sans MS",28), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="Medicina General", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia2= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio = Label(self.pestana2, text="La medicina general constituye el primer nivel de atención médica y es imprescindible para la prevención, detección, tratamiento y seguimiento de las enfermedades crónicas estabilizadas, responsabilizándose del paciente en su conjunto, para decidir su derivación a los especialistas cuando alguna patología se descompense.", bg = "#C7D8D9", font= ("Comic Sans MS", 18),wraplength= 700).pack()
        self.Espacio_Emergencia3= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia4= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura4.PNG")
        self.image = self.image.resize((323,437),Image.Resampling.LANCZOS)
        Medicina_Logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana2, image = Medicina_Logo, bg="#C7D8D9")
        label_Logo.image = Medicina_Logo
        label_Logo.pack()
        self.Espacio_Emergencia5= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_MedicinaGeneral = Button (self.pestana2, text= "Medicina General", bg = "#C7D8D9", font =("Comic Sans MS", 16), command= self.Medicina_General).pack()
        self.Espacio_Emergencia7= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ##################################################### Pestaña 3 #############################################
        self.Espacio_Emergencia1= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_Introductorio3 = Label(self.pestana3, text="La optometría es la ciencia sanitaria no médica que estudia el sistema visual, sus alteraciones no patológicas y su solución, así como las normas de salud e higiene visual a cargo del optometrista. La optometría presta especial atención precisamente a defectos visuales que pueden tener su origen en malos hábitos sobre la postura y distancia, por ejemplo, en la lectura, escritura o sobre el tipo de iluminación en nuestro entorno durante el trabajo, etc., y que pudieran provocar casos de fatiga visual.", bg = "#C7D8D9", font= ("Comic Sans MS", 16),wraplength= 700).pack()      
        self.Espacio_Emergencia2= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura5.PNG")
        self.image = self.image.resize((512,512),Image.Resampling.LANCZOS)
        Optometria_logo = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana3, image = Optometria_logo, bg="#C7D8D9")
        label_Logo.image = Optometria_logo
        label_Logo.pack()
        self.Espacio_Emergencia3= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Boton_Navegacion = Button(self.pestana3, text="Optometria", bg= "#C7D8D9", font=("Comic Sans MS", 18), command= self.optometria).pack()
        self.Espacio_Emergencia4= Label(self.pestana3, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
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
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana1,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana2,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana3,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana3,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
               
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
        self.BotonCerrar = Button(self.pestana4,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana4,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana5,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana5,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana6,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana6,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana7,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana7,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 8 COMUNA 8 ########################################################
        
        self.texto_Comunas = Label(self.pestana8, text = "Cl. 40 #65aa-45 Óptica Villa hermosa \n 3153025644",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana8, text = "Calle 57 # 49 44 Local 237 Oftalvision \n 44481760",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana8, text = "Cra. 46 #47-36 Óptica vision clara \n 44236218",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana8, text = "Cra 49 # 57 - 51 Centro Óptico villanueva \n 3186423693",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas8 = Label(self.pestana8, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana8,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana8,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ###################### PESTAÑA 9 COMUNA 9 ##########################################################
        
        self.texto_Comunas = Label(self.pestana9, text = "Cl. 49 #38-28 Óptica Ayacucho \n 3003102017",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana9, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana9,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana9,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana10,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana10,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
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
        self.BotonCerrar = Button(self.pestana11,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana11,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        #################### PESTAÑA 12 COMUNA 12 #################################################################
        
        self.texto_Comunas = Label(self.pestana12, text = "Cra. 87 # 47-32 Optilux \n 3134840521",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana12, text = "Cl. 47DD #87-4 Infocus optica \n 4088407",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana12, text = "Cl.46 #5310 Gran visual optica \n 3204253397",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana12, text = "Calle 50 #46-41 local 105 visual confort \n 3013802734",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana12, text = "Cra. 44 #48-71 Opti servicios \n 6042390680",wraplength= 350).pack()
        self.texto_Comunas6 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.texto_Comunas7 = Label(self.pestana12, text = "sadlkasjdsa",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana12,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana12,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ######################## PESTAÑA 13 COMUNA 13 ##############################################
        
        self.texto_Comunas = Label(self.pestana13, text = "Cl. 42 # 101114 Óptica Servisalud \n 3157204455",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana13, text = "",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana13,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana13,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ########################## PESTAÑA 14 COMUNA 14 ############################################
        
        self.texto_Comunas = Label(self.pestana14, text = "Cra. 42 #7a Sur-143 Óptica colombiana S.A.S loc 1214 \n 43217025",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana14, text = "Sur 170,Carrera 43 A #7 Multiopticas \n 43213339",wraplength= 350).pack()
        self.texto_Comunas3 = Label(self.pestana14, text = "Cra. 48 #19 A-40 Doctoralia \n 320332244 ",wraplength= 350).pack()
        self.texto_Comunas4 = Label(self.pestana14, text = "Carrera 43, Cl. 9 Sur # 36 HD Ópticas Poblado \n 6045017102",wraplength= 350).pack()
        self.texto_Comunas5 = Label(self.pestana14, text = "Cll 9 A # 29 62 Apto 804 Optica el tercer ojo \n 3505476571",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana14,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana14,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        ######################### PESTAÑA 15 COMUNA 15 ############################################
        
        self.texto_Comunas = Label(self.pestana15, text = "Cra. 52 #1-19 Optivisual \n 46062226",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana15, text = "Calle 13 A sur 52 A 61 Optidubra \n 3227682772",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana15,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana15,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack()
        
        ####################### PESTAÑA 16 COMUNA 16 ################################################
        
        self.texto_Comunas = Label(self.pestana16, text = "Cra. 70 #1 - 18 Local 377 Lafam-Arkadia \n 316349",wraplength= 350).pack()
        self.texto_Comunas2 = Label(self.pestana16, text = "",wraplength= 350).pack()
        self.BotonCerrar = Button(self.pestana16,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        self.BotonVolver = Button(self.pestana16,text= "Regresar", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.tercer_toplevel).pack() 
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
        self.panel4.add(self.pestana1, text= "Navegacion de pestañas")
        self.panel4.add(self.pestana2, text= "Conoce la interfaz")
        self.panel4.add(self.pestana3, text= "Creditos")
        self.panel4.pack(expand=2, fill="both")
        ############################## Logo pestaña 1 y funciones pestaña 1 #########################
        self.Texto_pestana_ = Label(self.pestana1, text = "1. Debemos aprender principalmente la navegación de POLIMED, en el siguiente material te proporcionaremos instrucciones a partir de imágenes y textos con la finalidad de que puedas aprender a interactuar con la plataforma.",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.Texto_pestana1 = Label(self.pestana1, text = "2. En la siguiente imagen podremos observar las pestañas de navegación en la ventana de nuestra aplicación. Estas ventanas permitirán la navegación del Usuario para conocer un poco mas acerca de POLIMED",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.Espacio_Emergencia1= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia2= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura2.PNG")
        self.image = self.image.resize((421,131),Image.Resampling.LANCZOS)
        Ayuda_Img = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana1, image = Ayuda_Img, bg="#91B8C1")
        label_Logo.image = Ayuda_Img
        label_Logo.pack()
        self.Espacio_Emergencia3= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia4= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_pestana2 = Label(self.pestana1, text = "3. La siguiente imagen te incita a que toques en las diferentes pestañas para que puedas observar mas acerca de la navegación en el aplicativo.",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.Espacio_Emergencia5= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia6= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura2.PNG")
        self.image = self.image.resize((421,131),Image.Resampling.LANCZOS)
        Ayuda_Img2 = ImageTk.PhotoImage(self.image)
        label_Logo2 = Label(self.pestana1, image = Ayuda_Img2, bg="#91B8C1")
        label_Logo2.image = Ayuda_Img2
        label_Logo2.pack()
        self.Espacio_Emergencia1= Label(self.pestana1, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana1,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ################################### Pestaña 2 Conoce la aplicación ############################
        self.Texto_pestana_ = Label(self.pestana2, text = "Como ya pudiste observar POLIMED es una aplicación de escritorio que está realizada en el lenguaje de programación Python. Esta aplicación, permite la navegación entre ventanas de manera facil mediante la implementación de una interfaz gráfica. Sin embargo, no es difícil de manejar. A continuación, se mostrará una imagen en relación al contenido de la aplicación.",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.Espacio_Emergencia1= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Espacio_Emergencia2= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.image = Image.open("Captura3.PNG")
        self.image = self.image.resize((421,131),Image.Resampling.LANCZOS)
        Ayuda_Img = ImageTk.PhotoImage(self.image)
        label_Logo = Label(self.pestana2, image = Ayuda_Img, bg="#91B8C1")
        label_Logo.image = Ayuda_Img
        label_Logo.pack()
        self.Espacio_Emergencia3= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.Texto_pestana_ = Label(self.pestana2, text = "Esta imagen nos esta indicando que deberás utilizar las pestañas para navegar en la búsqueda de los centros médicos comuna a comuna. No obstante, sabemos que en algunas ocasiones no se sabe con certeza a cuál comuna de la ciudad de Medellín pertenece un sector. Por lo tanto, Optamos por Anexar pequeños textos e imágenes ilustrativas para que puedas reconocer los sectores y familiarizarte.",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.Espacio_Emergencia4= Label(self.pestana2, text = " ", font=("Comic Sans MS",14), bg = "#C7D8D9").pack()
        self.BotonCerrar = Button(self.pestana2,text= "Salir", bg = "#C7D8D9", font =("Comic Sans MS", 12), command= self.Cerrar_ventana).pack()
        ############################### Pestaña 3 Creditos de la APP #########################################
        self.Texto_pestana_ = Label(self.pestana3, text ="ANA \n Yhojan \n Milton",wraplength= 700, font=( "", 20), bg="#C7D8D9").pack()
        self.ventana5.mainloop() 
########################################### Inicio de Sesion ##########################
def inicio():
    ventana = Tk()
    Login_Polimed(ventana)

    ventana.mainloop()

