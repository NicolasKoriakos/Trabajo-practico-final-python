import os
import tkinter as tk
import pickle
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import time

os.system('cls')

class App:

    def __init__(self):

        #Lista

        self.datos = []

        self.lista_canciones = []

        self.lista_artistas = []

        self.info_artistas = []

        #Creamos la ventana

        self.window = tk.Tk()
        self.window.title('TRABAJO PRACTICO NICOLAS KORIAKOS')
        self.window.geometry('760x422')

        #Creamos el cuaderno

        self.notepad = ttk.Notebook(self.window)
        self.notepad.grid(column = 0, row = 0, padx = 10, pady = 10)

        #Mainloop   

        self.agregar_disco()
        self.actualizar_catalogo()
        self.agregar_tema()
        self.filtrar()
        self.listar()
        self.filtrar_genero()
        self.carga_artistas()
        self.window.mainloop()

 #INTERFAZ GRAFICA

  #Funcion para añadir discos al catalogo  
    
    def agregar_disco(self):

        #Creamos la primer hoja

        self.sheet1 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet1, text = 'Añadir disco')

        #labels

        self.labelframe1 = ttk.Labelframe(self.sheet1, text = 'Discos')
        self.labelframe1.grid(column = 0, row = 0, padx = 5, pady = 10)
        
        self.label1 = ttk.Label(self.labelframe1, text = 'TITULO:')
        self.label1.grid(column = 0, row = 0, padx = 4 , pady = 4)

        self.label2 = ttk.Label(self.labelframe1, text = 'FECHA DE LANZAMIENTO:')
        self.label2.grid(column = 0, row = 1, padx = 4 , pady = 4)

        self.label3 = ttk.Label(self.labelframe1, text = 'GENERO:')
        self.label3.grid(column = 0, row = 2, padx = 4 , pady = 4)

        self.label4 = ttk.Label(self.labelframe1, text = 'GENERO SECUNDARIO(OPCIONAL):')
        self.label4.grid(column = 0, row = 3, padx = 4 , pady = 4)

        self.label4 = ttk.Label(self.labelframe1, text = 'MUSICO/BANDA:')
        self.label4.grid(column = 0, row = 4, padx = 4 , pady = 4)

        self.label5 = ttk.Label(self.labelframe1, text = 'DISCOGRAFICA:')
        self.label5.grid(column = 0, row = 5, padx = 4 , pady = 4)

        self.label6 = ttk.Label(self.labelframe1, text = 'CANTIDAD DE CANCIONES:')
        self.label6.grid(column = 0, row = 6, padx = 4 , pady = 4)

        self.label7 = ttk.Label(self.labelframe1, text = 'DURACION TOTAL EN MINUTOS:')
        self.label7.grid(column = 0, row = 7, padx = 4, pady = 4)

        self.label8 = ttk.Label(self.labelframe1, text = 'NACIONALIDAD:')
        self.label8.grid(column = 0, row = 8, padx = 4, pady = 4)

        self.label9 = ttk.Label(self.labelframe1, text = 'CANTIDAD DE MIEMBROS:')
        self.label9.grid(column = 0, row = 9, padx = 4, pady = 4)

        #Entry

        self.tituloentry = tk.StringVar()
        self.titulo = ttk.Entry(self.labelframe1, textvariable = self.tituloentry)
        self.titulo.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.fechaentry = tk.StringVar()
        self.fecha = ttk.Entry(self.labelframe1, textvariable = self.fechaentry)
        self.fecha.grid(column = 1, row = 1, padx = 4, pady = 4)

        self.genero1entry = tk.StringVar()
        self.genero1 = ttk.Entry(self.labelframe1, textvariable = self.genero1entry)
        self.genero1.grid(column = 1, row = 2, padx = 4, pady = 4)

        self.genero2entry = tk.StringVar()
        self.genero2 = ttk.Entry(self.labelframe1, textvariable = self.genero2entry)
        self.genero2.grid(column = 1, row = 3, padx = 4, pady = 4)

        self.artistaentry = tk.StringVar()
        self.artista = ttk.Entry(self.labelframe1, textvariable = self.artistaentry)
        self.artista.grid(column = 1, row = 4, padx = 4, pady = 4)

        self.discograficaentry = tk.StringVar()
        self.discografica = ttk.Entry(self.labelframe1, textvariable = self.discograficaentry)
        self.discografica.grid(column = 1, row = 5, padx = 4, pady = 4)

        self.cantidadentry = tk.IntVar()
        self.cantidad = ttk.Entry(self.labelframe1, textvariable = self.cantidadentry)
        self.cantidad.grid(column = 1, row = 6, padx = 4, pady = 4)

        self.duracionentry = tk.IntVar()
        self.duracion = ttk.Entry(self.labelframe1, textvariable = self.duracionentry)
        self.duracion.grid(column = 1, row = 7, padx = 4, pady = 4)

        self.nacionalidadenty = tk.StringVar()
        self.nacionalidad = ttk.Entry(self.labelframe1, textvariable = self.nacionalidadenty)
        self.nacionalidad.grid(column = 1, row = 8, padx = 4, pady = 4)

        self.miembrosentry = tk.IntVar()
        self.miembrosentry.set(1)
        self.miembros = ttk.Entry(self.labelframe1, textvariable = self.miembrosentry)
        self.miembros.grid(column = 1, row = 9, padx = 4, pady = 4)
        
        #Button

        self.seleccion2 = tk.IntVar()
        self.seleccion2.set(2)

        self.radiob = ttk.Radiobutton(self.labelframe1, text = 'BANDA', variable = self.seleccion2, value = 1)
        self.radiob.grid(column = 0, row = 10, padx = 4, pady = 4)

        self.radiob2 = ttk.Radiobutton(self.labelframe1, text = 'SOLISTA', variable = self.seleccion2, value = 2)
        self.radiob2.grid(column = 1, row = 10, padx = 4, pady = 4)

        self.boton1 = ttk.Button(self.labelframe1, text = 'Confirmar', command = self.agregar)
        self.boton1.grid(column = 0, row = 11, padx = 4, pady = 4)

  #Cargar los datos nuevos al catalogo

    def actualizar_catalogo(self):

        #Creamos la segunda hoja

        self.sheet2 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet2, text = 'Cargar / Actualizar catalogo')

        #Labels 

        self.labelframe2 = ttk.Labelframe(self.sheet2, text = 'Catalogo:')
        self.labelframe2.grid(column = 0, row = 0, padx = 5, pady = 10)

        #Buton

        boton1 = ttk.Button(self.labelframe2, text = 'ACTUALIZAR CATALOGO', command = self.guardar)
        boton1.grid(column = 0, row = 0, padx = 4, pady = 4)

        boton2 = ttk.Button(self.labelframe2, text = 'CARGAR CATALOGO', command = self.cargar)
        boton2.grid(column = 1, row = 0, padx = 4, pady = 4)

  #Agregar musica al catalogo
  
    def agregar_tema(self):

        #Creamos la 3er hoja

        self.sheet3 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet3, text = 'Añadir/mostrar temas')    
        
        #Labels

        self.labelframe3 = ttk.Labelframe(self.sheet3, text = 'Canciones:')
        self.labelframe3.grid(column = 0, row = 0, padx = 5, pady = 10)

        self.label2_1 = ttk.Label(self.labelframe3, text = 'DISCO:')
        self.label2_1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.label2_2 = ttk.Label(self.labelframe3, text = 'CANCION:')
        self.label2_2.grid(column = 0, row = 1, padx = 4, pady = 4)

        self.label2_3 = ttk.Label(self.labelframe3, text = 'ARTISTA:')
        self.label2_3.grid(column = 0, row = 2, padx = 4 ,pady = 4)
       
        #Entry

        self.discoentry = tk.StringVar()
        self.disco_check = ttk.Entry(self.labelframe3, textvariable = self.discoentry)
        self.disco_check.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.cancionentry = tk.StringVar()
        self.cancion = ttk.Entry(self.labelframe3, textvariable = self.cancionentry)
        self.cancion.grid(column = 1, row = 1, padx = 4, pady = 4)

        self.musicoentry = tk.StringVar()
        self.muscio = ttk.Entry(self.labelframe3, textvariable = self.musicoentry)
        self.muscio.grid(column = 1, row = 2,padx = 4, pady = 4)

        #Buttons

        self.boton2 = ttk.Button(self.labelframe3, text = 'CONFIRMAR', command = self.catalogo_añadir_tema)
        self.boton2.grid(column = 0, row = 3, padx = 4, pady = 4)

        self.boton3 = ttk.Button(self.labelframe3, text = 'INFORMACION', command = self.info)
        self.boton3.grid(column = 0, row = 4, padx = 4, pady = 4)

        self.boton4 = ttk.Button(self.labelframe3, text = 'MOSTRAR LISTA', command = self.cargar_lista)
        self.boton4.grid(column = 0, row = 5, padx = 4 ,pady = 4)



        #SCROLLED TEXT

        self.scroll = st.ScrolledText(self.labelframe3, width = 30, height = 10)
        self.scroll.grid(column = 1, row = 5, padx = 4, pady = 4 )
  
  #Filtrar

    def filtrar(self):

        #Creamos la 4ta hoja

        self.sheet4 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet4, text = 'Filtrar')

        #Labels

        self.labelframe4 = ttk.LabelFrame(self.sheet4, text = 'Filtros:')
        self.labelframe4.grid(column = 0, row = 0, padx = 5, pady = 10)

        self.label3_1 = ttk.Label(self.labelframe4, text = 'BANDA/ARTISTA:')
        self.label3_1.grid(column = 0, row = 0, padx = 4 ,pady = 4)

        self.label3_2 = ttk.Label(self.labelframe4, text = 'DISCO:')
        self.label3_2.grid(column = 0, row = 1, padx = 4 ,pady = 4)

        self.label3_3 = ttk.Label(self.labelframe4, text = 'FILTRAR POR:')
        self.label3_3.grid(column = 0, row = 2, padx = 4 , pady = 4)

        #Entry

        self.artistafiltro_entry = tk.StringVar()
        self.artistafiltro = ttk.Entry(self.labelframe4, textvariable = self.artistafiltro_entry)
        self.artistafiltro.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.discofiltro_entry = tk.StringVar()
        self.discofiltro = ttk.Entry(self.labelframe4, textvariable = self.discofiltro_entry)
        self.discofiltro.grid(column = 1, row = 1, padx = 4, pady = 4)

        #Button

        self.boton = ttk.Button(self.labelframe4, text = 'FILTRAR', command =self.filtrarmusico)
        self.boton.grid(column = 0, row = 5, padx = 4 , pady = 4)

        #Radio button

        self.seleccion = tk.IntVar()
        self.seleccion.set(3)

        self.rb = ttk.Radiobutton(self.labelframe4, text = 'ARTISTA/BANDA', variable = self.seleccion, value = 1)
        self.rb.grid(column = 1, row = 2, padx = 4, pady = 4)

        self.rb1 = ttk.Radiobutton(self.labelframe4, text = 'DISCO', variable = self.seleccion, value = 2)
        self.rb1.grid(column = 1, row = 3, padx = 4, pady = 4)

        self.rb2 = ttk.Radiobutton(self.labelframe4, text = 'AMBOS', variable = self.seleccion, value = 3)
        self.rb2.grid(column = 1, row = 4, padx = 4, pady = 4)
        
        #SCROLLED TEXT

        self.scroll2 = st.ScrolledText(self.labelframe4, width = 30, height = 10)
        self.scroll2.grid(column = 1, row = 5, padx = 4, pady = 4 )

  #Listar por duracion

    def listar(self):

        #Creamos la 5ta hoja

        self.sheet5 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet5, text = 'Listar')

        #Labels

        self.labelframe5 = ttk.LabelFrame(self.sheet5, text = 'Listar:')
        self.labelframe5.grid(column = 0, row = 0, padx = 4 ,pady = 5)

        #Buttons

        self.button4_1 = ttk.Button(self.labelframe5, text = 'Listar discos por duracion', command = self.listar_duracion)
        self.button4_1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.button4_2 = ttk.Button(self.labelframe5, text = 'Listar artistas por nacionalidad', command = self.listar_artistas)
        self.button4_2.grid(column = 1, row = 0, padx = 4, pady = 4)

        #Scrolled Text

        self.scroll3 = st.ScrolledText(self.labelframe5, width = 40, height = 15)
        self.scroll3.grid(column = 1, row = 1, padx = 4, pady = 4)
  
  #Filtrar por genero

    def filtrar_genero(self):

        #Cargamos la 6ta hoja
        
        self.sheet6 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet6, text = 'Filtrar por genero/discografica')

        #labels

        self.labelframe6 = ttk.Labelframe(self.sheet6, text = 'Filtrar:')
        self.labelframe6.grid(column = 0, row = 0, padx = 4, pady = 5)

        self.label6_1 = ttk.Label(self.labelframe6, text = 'GENERO:')
        self.label6_1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.label6_2 = ttk.Label(self.labelframe6, text = 'DISCOGRAFICA:')
        self.label6_2.grid(column = 0, row = 1, padx = 4, pady = 4)

        #Entry

        self.genero = tk.StringVar()
        self.generoentry = ttk.Entry(self.labelframe6, textvariable = self.genero)
        self.generoentry.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.discografica2 = tk.StringVar()
        self.discografica2entry = ttk.Entry(self.labelframe6, textvariable = self.discografica2)
        self.discografica2entry.grid(column = 1, row = 1)

        #Buttons

        self.button6_1 = ttk.Button(self.labelframe6, text = 'FILTRAR POR GENERO', command = self.filtrar_por_genero)
        self.button6_1.grid(column = 0, row = 3, padx = 4, pady = 4)

        self.button6_2 = ttk.Button(self.labelframe6, text = 'FILTRAR POR DISCOGRAFICA', command = self.filtrar_discografica)
        self.button6_2.grid(column = 1, row = 3, padx = 4, pady = 4)

        #Scrolled Text

        self.scroll4 = st.ScrolledText(self.labelframe6, width = 35, height = 12)
        self.scroll4.grid(column = 1, row = 4, padx = 4, pady = 4)

  #Cargar informacion BANDA

    def carga_artistas(self):
        
        #septima hoja

        self.sheet7 = ttk.Frame(self.notepad)
        self.notepad.add(self.sheet7, text = 'cargar Informacion bandas')

        #labels

        self.labelframe7 = ttk.Labelframe(self.sheet7, text = 'Añadir miembros a la banda:')
        self.labelframe7.grid(column = 0, row = 0, padx = 4, pady = 5)

        self.label7_1 = ttk.Label(self.labelframe7, text = 'nombre de la banda:')
        self.label7_1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.label7_2 = ttk.Label(self.labelframe7, text = 'nombre del artista:')
        self.label7_2.grid(column = 0, row = 1, padx = 4, pady = 4)

        self.label7_3 = ttk.Label(self.labelframe7, text = 'nacionalidad:')
        self.label7_3.grid(column = 0, row = 2, padx = 4, pady = 4)

        self.labelframe8 = ttk.Labelframe(self.sheet7, text = 'Mostrar informacion de la banda:')
        self.labelframe8.grid(column = 0, row = 4, padx = 4 , pady = 4)

        self.label8_1 = ttk.Label(self.labelframe8, text = 'nombre de la banda:')
        self.label8_1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.label8_2 = ttk.Label(self.labelframe8, text = 'nombre del artista:')
        self.label8_2.grid(column = 0, row = 1, padx = 4, pady = 4)

        self.labelframe9 = ttk.Labelframe(self.sheet7)
        self.labelframe9.grid(column = 4, row = 0, padx = 4, pady = 4)
        
        #Entry

        self.nombrebanda2entry = tk.StringVar()
        self.nombrebanda2 = ttk.Entry(self.labelframe7, textvariable = self.nombrebanda2entry)
        self.nombrebanda2.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.nombreartistaentry = tk.StringVar()
        self.nombreartista = ttk.Entry(self.labelframe7, textvariable = self.nombreartistaentry)
        self.nombreartista.grid(column = 1, row = 1, padx = 4 , pady = 4)

        self.nacionalidadartistaentry = tk.StringVar()
        self.nacionalidadartista = ttk.Entry(self.labelframe7, textvariable = self.nacionalidadartistaentry)
        self.nacionalidadartista.grid(column = 1, row = 2, padx = 4, pady = 4)

        self.nombrebandaentry = tk.StringVar()
        self.nombrebanda = ttk.Entry(self.labelframe8, textvariable = self.nombrebandaentry)
        self.nombrebanda.grid(column = 1, row = 0, padx = 4, pady = 4)

        self.nombreartista2entry = tk.StringVar()
        self.nombreartista2 = ttk.Entry(self.labelframe8, textvariable = self.nombreartista2entry)
        self.nombreartista2.grid(column = 1, row = 1, padx = 4, pady = 4)

        #buttons

        self.button = ttk.Button(self.labelframe7, text = 'añadir artista', command = self.añadir_artista)
        self.button.grid(column = 0 , row = 5, padx = 4, pady = 4)

        self.button2 = ttk.Button(self.labelframe8, text = 'buscar artista', command = self.filtrar_artista)
        self.button2.grid(column = 0, row = 3, padx = 4, pady = 4)

        self.button3 = ttk.Button(self.labelframe8, text = 'mostrar todos los artistas', command = self.mostrar_artistas)
        self.button3.grid(column = 1, row = 3, padx = 4, pady = 4)

        #scrolled text

        self.scroll5 = st.ScrolledText(self.labelframe9, width = 35, height = 12)
        self.scroll5.grid(column = 1, row = 0, padx = 4, pady = 4)

 #Modulos

    def agregar(self):

        #cargamos la info
 
        try:

            self.datos = pickle.load(open('info.txt', 'rb'))

        except (OSError,IOError,AttributeError):
                   
            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos,archivo)
            
            self.datos = pickle.load(open('info.txt', 'rb'))

        #Nos aseguramos que no se repita el disco

        repeticion = False

        if self.duracionentry.get() <= 0:

            mb.showerror('ERROR!','LA DURACION DEL DISCO NO PUEDE SER MENOR O IGUAL A 0')
        
        else:

            if self.cantidadentry.get() <= 0:

                mb.showerror('ERROR!','LA CANTIDAD DE CANCIONES DEBE SER MAYOR A 0')

            else:

                for x in range(len(self.datos)):

                    if self.tituloentry.get() == self.datos[x]['TITULO'] and self.artistaentry.get() == self.datos[x]['MUSICO/BANDA']:

                        repeticion = True

                #Nos aseguramos de que haya un segundo genero
        
                if not repeticion:

                    vacio = False

                    if self.genero2entry.get() == '':

                        vacio = True

                    if not vacio:

                        genero = [str(self.genero1entry.get()) , str(self.genero2entry.get())]
        
                    else:

                        genero = [str(self.genero1.get())]
        
                    self.infodisco = {

                              'TITULO': str(self.tituloentry.get()) ,
                              'FECHA DE LANZAMIENTO': str(self.fechaentry.get()) ,
                              'GENERO': genero ,
                              'MUSICO/BANDA': str(self.artistaentry.get()) ,
                              'DISCOGRAFICA': str(self.discograficaentry.get()) ,
                              'CANTIDAD DE CANCIONES': int(self.cantidadentry.get()),
                              'LISTA DE CANCIONES': [],
                              'DURACION': int(self.duracionentry.get()),
                              'NACIONALIDAD': str(self.nacionalidadenty.get()),
                              'CANTIDAD DE MIEMBROS': int(self.miembrosentry.get()),
                              'CODIGO': int(self.seleccion2.get()),
                              'MIEMBROS': []
                         
                                    }
 
                    self.datos.append(self.infodisco)

                    with open('info.txt', 'wb') as archivo:

                        pickle.dump(self.datos,archivo)

                    mb.showinfo('INFORMACION','SE HA CARGADO CON EXTIO EL DISCO.')
        
                else:

                    mb.showerror('ERROR!','ESTE ARTISTA YA TIENE UN DISCO CARGADO CON ESE NOMBRE')
        
    def guardar(self):

        with open('info.txt', 'wb') as archivo:

            pickle.dump(self.datos,archivo)
        
        mb.showinfo('INFORMACION','SE HA ACTUALIZADO CON EXITO EL CATALOGO')
    
    def cargar(self):

        with open('info.txt', 'rb') as archivo:

            self.datos = pickle.load(archivo)

        mb.showinfo('INFORMACION','SE HA CARGADO CON EXITO EL CATALOGO')

    def catalogo_añadir_tema(self):
        
        #Nos aseguramos de que exista un archivo para almacenar la informacion

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))

        except (OSError,IOError,AttributeError):
                   
            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos,archivo)
            
            self.datos = pickle.load(open('info.txt', 'rb'))
            
        filtro_disco = self.discoentry.get()
        tema = self.cancionentry.get()
        artista = self.musicoentry.get()
        info = [artista,filtro_disco,tema]
        disco = False
              
        repeticion = False

        #Nos aseguramos de que exista un archivo para almacenar la informacion

        try:

            self.lista_canciones = pickle.load(open('info_canciones.dat','rb'))
        
        except (OSError,IOError):

            with open('info_canciones.dat', 'wb') as archivo:

                pickle.dump(self.lista_canciones,archivo)

        #Chequeo para asegurarnos de que el disco haya sido previamente cargado al catalogo
        
        if len(self.datos) == 0:

            mb.showerror('ERROR!','ERROR! DEBES CARGAR UN DISCO PRIMERO')
        else:

            for x in range(len(self.datos)):

                if filtro_disco == self.datos[x]['TITULO']:

                    limite = int(self.datos[x]['CANTIDAD DE CANCIONES'])
                    tamaño = len(self.datos[x]['LISTA DE CANCIONES'])
                    disco = True

                    if tamaño >= limite:

                        mb.showerror('ERROR!','SE ALCANZO EL MAXIMO DE CANCIONES EN ESTE DISCO')
                
                    else:
                
                    #Nos aseguramos de que no se repita la cancion

                        for f in range(len(self.lista_canciones)):
      
                            if tema == self.lista_canciones[f][2]:

                                repeticion = True
        
                        if repeticion:

                            mb.showerror('ERROR!','LA CANCION YA ESTA EN LA LISTA!')
        
                        else:

                            mb.showinfo('INFORMACION','LA CANCION HA SIDO AÑADIDA A LA LISTA!')
            
                            self.lista_canciones.append(info)

                            with open('info_canciones.dat', 'wb') as archivo:

                                pickle.dump(self.lista_canciones,archivo)

                            self.datos[x]['LISTA DE CANCIONES'].append(tema)

                            tamaño = len(self.datos[x]['LISTA DE CANCIONES'])

                            with open('info.txt', 'wb') as archivo:

                                pickle.dump(self.datos,archivo)

                            mb.showinfo('INFO',f'hay {tamaño} canciones en el disco, el maximo de temas disponibles es: {limite}')

        if not disco:

            mb.showerror('ERROR!','NO SE ENCONTRO UN DISCO CON ESE NOMBRE EN LA BASE DE DATOS')
      
    def info(self):

        try:

            self.lista_canciones = pickle.load(open('info_canciones.dat','rb'))
        
        except (OSError,IOError):

            with open('info_canciones.dat', 'wb') as archivo:

                pickle.dump(self.lista_canciones,archivo)

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))
        
        except (OSError,IOError):

            with open('info.txt', 'wb') as archivo2:

                pickle.dump(self.datos,archivo2)

        cantidad = len(self.lista_canciones)
        cantidad2 = len(self.datos)

        mb.showinfo('INFORMACION',f'Hay {cantidad} canciones distintas en el catalogo.')
        mb.showinfo('INFORMACION',f'Hay {cantidad2} discos distintos en el catalogo.')
      
    def cargar_lista(self):

        with open('info_canciones.dat', 'rb') as archivo:

            self.datos_canciones = pickle.load(archivo)

        mb.showinfo('INFORMACION','SE HA CARGADO CON EXITO LA LISTA DE TEMAS DEL CATALOGO')

        self.scroll.delete("1.0", tk.END)

        for x in range(len(self.datos_canciones)):

            self.scroll.insert(tk.END, f'MUSICO/BANDA: {self.datos_canciones[x][0]}\n' +
                                       f'DISCO: {self.datos_canciones[x][1]} \n' +
                                       f'CANCION: {self.datos_canciones[x][2]}\n\n')

    def filtrarmusico(self):

        with open('info_canciones.dat', 'rb') as archivo:

            self.datos_canciones = pickle.load(archivo)
        
        filtro_artista = self.artistafiltro.get()
        filtro_disco = self.discofiltro.get()
        valor = self.seleccion.get()
        Filtro = False
        self.datos = pickle.load(open('info.txt', 'rb'))
      
        if valor == 1:

            self.scroll2.delete("1.0", tk.END)    

            for x in range(len(self.datos_canciones)):

                if filtro_artista == self.datos_canciones[x][0]:
                    
                    for f in range(len(self.datos)):

                            if filtro_artista == self.datos[f]['MUSICO/BANDA']:

                                Filtro = True
                                discografica = self.datos[f]['DISCOGRAFICA']

                                self.scroll2.insert(tk.END, f'MUSICO/BANDA: {self.datos_canciones[x][0]}\n' +
                                                            f'DISCO: {self.datos_canciones[x][1]} \n' +
                                                            f'CANCION: {self.datos_canciones[x][2]}\n' +
                                                            f'DISCOGRAFICA: {discografica}\n\n')
          
            if Filtro:
                
                mb.showinfo('INFORMACION', 'SE HA APLICADO CON EXITO EL FILTRO SOLICITADO')
            
            else:

                mb.showerror('ERROR!','NO SE ENCONTRO UNA CANCION CON EL FILTRO SOLICITADO')
         
        elif valor == 2:
            
            self.scroll2.delete("1.0", tk.END)
            
            for x in range(len(self.datos_canciones)):

                if filtro_disco == self.datos_canciones[x][1]:

                    for f in range(len(self.datos)):

                            if filtro_disco == self.datos[f]['TITULO']:

                                Filtro = True
                                discografica = self.datos[f]['DISCOGRAFICA']

                                self.scroll2.insert(tk.END, f'MUSICO/BANDA: {self.datos_canciones[x][0]}\n' +
                                                            f'DISCO: {self.datos_canciones[x][1]} \n' +
                                                            f'CANCION: {self.datos_canciones[x][2]}\n' +
                                                            f'DISCOGRAFICA: {discografica}\n\n')
           
            if Filtro:
                
                mb.showinfo('INFORMACION', 'SE HA APLICADO CON EXITO EL FILTRO SOLICITADO')
            
            else:

                mb.showerror('ERROR!','NO SE ENCONTRO UNA CANCION CON EL FILTRO SOLICITADO')
         
        elif valor == 3:
            
            self.scroll2.delete("1.0", tk.END)
            
            for x in range(len(self.datos_canciones)):

                if filtro_disco == self.datos_canciones[x][1]:

                        if filtro_artista == self.datos_canciones[x][0]:

                            for f in range(len(self.datos)):

                                if filtro_artista == self.datos[f]['MUSICO/BANDA']:

                                    Filtro = True
                                    discografica = self.datos[f]['DISCOGRAFICA']

                                    self.scroll2.insert(tk.END, f'MUSICO/BANDA: {self.datos_canciones[x][0]}\n' +
                                                                f'DISCO: {self.datos_canciones[x][1]} \n' +
                                                                f'CANCION: {self.datos_canciones[x][2]}\n' +
                                                                f'DISCOGRAFICA: {discografica}\n\n')
                                    
                                    break
           
            if Filtro:
                
                mb.showinfo('INFORMACION', 'SE HA APLICADO CON EXITO EL FILTRO SOLICITADO')
            
            else:

                mb.showerror('ERROR!','NO SE ENCONTRO UNA CANCION CON EL FILTRO SOLICITADO')               

    def listar_artistas(self):

        #cargamos la info

        try:

            self.lista_artistas = pickle.load(open('artistas.txt', 'rb'))
        
        except (OSError, IOError, AttributeError):

            with open('artistas.txt', 'wb') as archivo:

                pickle.dump(self.lista_artistas,archivo)
                
                self.lista_artistas = pickle.load(open('artistas.txt','rb'))           

        
        #Nos aseguramos de que tenga datos la informacion

        contenido = True

        if len(self.lista_artistas) == 0:

            contenido = False

            mb.showerror('ERROR!','ERROR! NO HAY ARTISTAS CARGADOS')  
        
        else:
    
            if contenido:

                lista_ordenada = sorted(self.lista_artistas, key = lambda x: x[1])

                mb.showinfo('INFORMACION','LISTA CARGADA!')

                self.scroll3.delete("1.0", tk.END)  

                for x in range(len(lista_ordenada)):

                    self.scroll3.insert(tk.END,f'ARTISTA: {lista_ordenada[x][0]}\n'+
                                               f'NACIONALIDAD: {lista_ordenada[x][1]}\n\n')

    def listar_duracion(self):

        #cargamos la info

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))
        
        except (OSError, IOError, AttributeError):

            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos,archivo)
                
                self.datos = pickle.load(open('info.txt','rb'))
      
        if len(self.datos) == 0:

            mb.showerror('ERROR!','ERROR! NO HAY NINGUN DISCO CARGADO A LA LISTA.')

        else:

            lista_ordenada = sorted(self.datos,key = lambda i: i['DURACION'])

            mb.showinfo('INFORMACION','LISTA CARGADA!')

            self.scroll3.delete("1.0", tk.END)  

            for x in range(len(lista_ordenada)):

                    titulo = lista_ordenada[x]['TITULO']
                    fecha = lista_ordenada[x]['FECHA DE LANZAMIENTO']
                    genero = lista_ordenada[x]['GENERO']
                    artista = lista_ordenada[x]['MUSICO/BANDA']
                    discografica = lista_ordenada[x]['DISCOGRAFICA']
                    cantidad = str(lista_ordenada[x]['CANTIDAD DE CANCIONES'])
                    duracion = str(lista_ordenada[x]['DURACION'])
                    nacionalidad = lista_ordenada[x]['NACIONALIDAD']

                    self.scroll3.insert(tk.END, f'TITULO: {titulo}\n' +
                                                f'FECHA DE LANZAMIENTO: {fecha}\n' +
                                                f'GENERO: {genero}\n' +
                                                f'MUSICO/BANDA: {artista}\n' +
                                                f'DISCOGRAFICA: {discografica}\n' +
                                                f'CANTIDAD DE CANCIONES: {cantidad}\n' +
                                                f'DURACION: {duracion} minutos\n' +
                                                f'NACIONALIDAD: {nacionalidad}\n\n'
                                        )

    def filtrar_por_genero(self):

        genero = self.genero.get()

        self.scroll4.delete('1.0', tk.END)

        vacio = False

        match = False
       
        #nos aseguramos de que el programa tenga de donde cargar los datos

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))
        
        except (IOError,OSError):

            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos, archivo)

        if self.datos == 0:

            vacio = True

        if not vacio:

            for x in range(len(self.datos)):

                genero_cargado = self.datos[x]['GENERO']

                if genero in genero_cargado:

                    match = True

                    titulo = self.datos[x]['TITULO']
                    fecha = self.datos[x]['FECHA DE LANZAMIENTO']
                    genero3 = self.datos[x]['GENERO']
                    artista = self.datos[x]['MUSICO/BANDA']
                    discografica = self.datos[x]['DISCOGRAFICA']
                    cantidad = str(self.datos[x]['CANTIDAD DE CANCIONES'])
                    duracion = str(self.datos[x]['DURACION'])
                    nacionalidad = self.datos[x]['NACIONALIDAD']

                    self.scroll4.insert(tk.END, f'TITULO: {titulo}\n' +
                                                f'FECHA DE LANZAMIENTO: {fecha}\n' +
                                                f'GENERO: {genero3}\n' +
                                                f'MUSICO/BANDA: {artista}\n' +
                                                f'DISCOGRAFICA: {discografica}\n' +
                                                f'CANTIDAD DE CANCIONES: {cantidad}\n' +
                                                f'DURACION: {duracion} minutos\n' +
                                                f'NACIONALIDAD: {nacionalidad}\n\n'
                                        )

        else:

            mb.showerror('ERROR!','ERROR! NO HAY INFORMACION CARGADA EN EL CATALOGO')

        if not match:

            mb.showerror('ERROR!','ERROR! NO SE ENCONTRO UN DISCO CON ESE GENERO')
        
        else: 

            mb.showinfo('INFORMACION!','SE HA CARGADO CON EXITO LOS DISCOS CON EL FILTRO SOLICITADO')

    def filtrar_discografica(self):

        discografica = self.discografica2.get()

        self.scroll4.delete('1.0', tk.END)

        vacio = False

        match = False
       
        #nos aseguramos de que el programa tenga de donde cargar los datos

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))
        
        except (IOError,OSError):

            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos, archivo)

        if self.datos == 0:

            vacio = True
        
        if not vacio:

            for x in range(len(self.datos)):

                discografica_cargada = self.datos[x]['DISCOGRAFICA']

                if discografica in discografica_cargada:

                    match = True

                    titulo = self.datos[x]['TITULO']
                    fecha = self.datos[x]['FECHA DE LANZAMIENTO']
                    genero3 = self.datos[x]['GENERO']
                    artista = self.datos[x]['MUSICO/BANDA']
                    discografica = self.datos[x]['DISCOGRAFICA']
                    cantidad = str(self.datos[x]['CANTIDAD DE CANCIONES'])
                    duracion = str(self.datos[x]['DURACION'])
                    nacionalidad = self.datos[x]['NACIONALIDAD']

                    self.scroll4.insert(tk.END, f'TITULO: {titulo}\n' +
                                                f'FECHA DE LANZAMIENTO: {fecha}\n' +
                                                f'GENERO: {genero3}\n' +
                                                f'MUSICO/BANDA: {artista}\n' +
                                                f'DISCOGRAFICA: {discografica}\n' +
                                                f'CANTIDAD DE CANCIONES: {cantidad}\n' +
                                                f'DURACION: {duracion} minutos\n' +
                                                f'NACIONALIDAD: {nacionalidad}\n\n'
                                        )
            
        else:

            mb.showerror('ERROR!','ERROR! NO HAY INFORMACION CARGADA EN EL CATALOGO')

        if not match:

            mb.showerror('ERROR!','ERROR! NO SE ENCONTRO UN DISCO CON ESE GENERO')
        
        else: 

            mb.showinfo('INFORMACION!','SE HA CARGADO CON EXITO LOS DISCOS CON EL FILTRO SOLICITADO')

    def añadir_artista(self):

        banda = self.nombrebanda2entry.get()

        repetido = False

        artista = self.nombreartistaentry.get()

        nacionalidad = self.nacionalidadartistaentry.get()

        vacio = False

        try:

            self.info_artistas = pickle.load(open('artistas.txt','rb'))
        
        except (IOError,EOFError):

            with open('artistas.txt', 'wb') as archivo:

                pickle.dump(self.info_artistas,archivo)

            self.info_artistas = pickle.load(open('artistas.txt','rb'))

        #Nos aseguramos de que exista un archivo para almacenar la informacion

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))

        except (OSError,IOError,AttributeError):
                   
            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos,archivo)
            
            self.datos = pickle.load(open('info.txt', 'rb'))
        
        if len(self.datos) == 0:

            vacio = True
        
        if vacio:

            mb.showerror('ERROR!','NO HAY NINGUNA BANDA CARGADA EN EL SISTEMA')
            time.sleep(1)
            mb.showinfo('INFORMACION!','PARA CARGAR UNA BANDA SE DEBE CARGAR UN DISCO PRIMERO')
 
        else:

            for x in range(len(self.datos)):

                banda_cargada = self.datos[x]['MUSICO/BANDA']
                codigo = self.datos[x]['CODIGO']
                miembros = self.datos[x]['MIEMBROS']
                cantidad = self.datos[x]['CANTIDAD DE MIEMBROS']

                if banda_cargada == banda:

                    if codigo == 2:

                        mb.showerror('ERROR','SE INGRESO UN SOLISTA, NO UNA BANDA')
                    
                    else:

                        if len(miembros) == cantidad:

                            mb.showerror('ERROR!','YA SE CARGARON TODOS LOS MIEMBROS DE ESTA BANDA')
                        
                        else:

                            for f in range(len(miembros)):

                                if artista in miembros[f]:
                                    
                                    repetido = True
                                    
                            if repetido:

                                mb.showerror('ERROR!','ESTE MUSICO YA HA SIDO CARGADO A ESTA BANDA')
                                
                            else:
                                    
                                info = [artista,nacionalidad]
                                info2 = [artista,nacionalidad,banda]
                                self.datos[x]['MIEMBROS'].append(info)
                                self.info_artistas.append(info2)

                                miembros = self.datos[x]['MIEMBROS']

                                mb.showinfo('INFORMACION','SE HA CARGADO CON EXITO EL MUSICO')
                                time.sleep(0.5)
                                mb.showinfo('INFORMACION',f'HAY {len(miembros)} artistas cargados en esta banda')

                                with open('info.txt', 'wb') as archivo:

                                    pickle.dump(self.datos,archivo)
                                    
                                with open('artistas.txt', 'wb') as archivo2:

                                    pickle.dump(self.info_artistas,archivo2)
                
                else:

                    mb.showerror('ERROR!','NO SE ENCONTRO UNA BANDA CON ESE NOMBRE')

    def mostrar_artistas(self):

        self.scroll5.delete('1.0', tk.END)

        try:

            self.info_artistas = pickle.load(open('artistas.txt','rb'))
        
        except (IOError,EOFError):

            with open('artistas.txt', 'wb') as archivo:

                pickle.dump(self.info_artistas,archivo)

            self.info_artistas = pickle.load(open('artistas.txt','rb'))

        if self.info_artistas == 0:

            mb.showerror('ERROR!','NO HAY NINGUN ARTISTA CARGADO')

        else:

            for x in range(len(self.info_artistas)):

                artista = self.info_artistas[x][0]
                nacionalidad = self.info_artistas[x][1]
                banda = self.info_artistas[x][2]

                self.scroll5.insert(tk.END, f'ARTISTA: {artista} \n'
                                            f'NACIONALIDAD: {nacionalidad} \n'
                                            f'BANDA: {banda} \n\n')
            
            mb.showinfo('INFORMACION','SE HA CARGADO CON EXITO LA LISTA DE ARTISTAS')

    def filtrar_artista(self):

        self.scroll5.delete('1.0', tk.END)
        
        #usamos esta variable para asegurarnos de que haya informacion en el programa

        vacio = False

        #Cargamos los datos necesarios

        artista = self.nombreartista2entry.get()
        banda = self.nombrebandaentry.get()
        
        #variable para chequear si se aplico correctamente el filtro

        match = False
        
        try:

            self.info_artistas = pickle.load(open('artistas.txt','rb'))
        
        except (IOError,EOFError):

            with open('artistas.txt', 'wb') as archivo:

                pickle.dump(self.info_artistas,archivo)

            self.info_artistas = pickle.load(open('artistas.txt','rb'))

        try:

            self.datos = pickle.load(open('info.txt', 'rb'))

        except (OSError,IOError,AttributeError):
                   
            with open('info.txt', 'wb') as archivo:

                pickle.dump(self.datos,archivo)
            
            self.datos = pickle.load(open('info.txt', 'rb'))

        if self.datos == 0:

            vacio = True

        elif self.info_artistas == 0:

            vacio = True

        if vacio:

            mb.showerror('ERROR!','ERROR! NO HAY UN ARTISTA CARGADO')
        
        else:

            for x in range(len(self.info_artistas)):

                artista2 = self.info_artistas[x][0]
                banda2 = self.info_artistas[x][2]
                nacionalidad = self.info_artistas[x][1]

                if banda2 == banda and artista == artista2:

                    match = True

                    self.scroll5.insert(tk.END,f'ARTISTA: {artista2} \n'
                                               f'NACIONALIDAD: {nacionalidad} \n'
                                               f'BANDA: {banda2} \n\n' )
            
            if match:

                mb.showinfo('INFORMACION','SE ENCONTRO EL ARTISTA SOLICITADO')
            
            else:

                mb.showerror('ERROR!','ERROR! NO SE ENCONTRO UN ARTISTA CON LOS VALORES INGRESADOS')

#Bloque principal

app = App()