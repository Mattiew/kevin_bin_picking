# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:07:49 2020

@author: Guill
"""


### IMPORTATION

import numpy as np
import matplotlib.pyplot as plt
import math as ma


#Méthode pour Tk + message (type alerte)
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as tks
from PIL import Image, ImageTk
#Méthode pour ouvrir et sauver un doc
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import cv2
import os
from functools import partial #exemple def set_time


### APPLICATION  
class Application:
    
    def __init__(self):
        #########################################
        #Fenêtre Tkinter de l'application
        self.root = Tk()
        self.root.title("LAB 4.2")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        
        #Bind de touches dans l'application²²
        self.root.bind('<KeyPress-q>',self.bind_start_segm)
        
        #########################################
        #MENU
        self.barremenu = Menu(self.root)
        
        #########################################
        #Création du menu Fichier
        self.fichier = Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = 'File', underline = 0, menu = self.fichier)
        self.fichier.add_command(label = 'Open', command = self.ouvrir_f)
        self.fichier.add_separator()
        self.fichier.add_command(label ='Quit', command = self.destructor)
        
        #Création du menu Edition
        self.edition = Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = 'Edition', underline = 0, menu = self.edition)
        self.edition.add_command(label = 'Start/Stop Face Detection', command = self.start_segm)
        self.edition.add_separator()
        
        #Afficher le Menu
        self.root.config(menu=self.barremenu)
        
        #########################################
        #Initialisation de la vidéo
        self.cap = None
        self.frame = None
        #self.output_path = output_path
        self.current_image = None
        self.resized = None
        self.start_segm = False
        
        #########################################
        #Zone d'affichage de la vidéo
        self.nb_faces = 0
        self.text = Label(self.root, text = 'Flux vidéo ')
        self.text.pack(padx=10, pady=10, fill=BOTH)
        self.panel = Label(self.root)
        self.panel.pack(padx=10, pady=10)
        
        #########################################
        #Variables utiles
        self.compt = 0
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        
        
        #########################################
        #Boutons de l'application
        display = Button(self.root, text = "Display", command = self.display)
        display.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)
        play = Button(self.root, text = "Play", command = self.video_loop)
        play.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)


###########################################################################################################################        
################################ METHODES DE L'APPLICATION


#BOUCLE LECTURE VIDEO
    def video_loop(self):
        ret, self.frame =  self.cap.read() #lecture
        width, height = int(self.cap.get(3)), int(self.cap.get(4))
        r_width, r_height = int(width*self.A/100), int(height*self.B/100)
        r_dim = (r_width, r_height)
        
        if self.start_segm:
            img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            r, g, b = cv2.split(img)
            hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
            h, s, v = cv2.split(hsv_img)
            
            #### DEFINITION DES BOUNDARIES POUR LE TRESHOLD
            #JAUNE
            low_y = (15, 150, 50)
            high_y = (30, 255, 255)
            #ROUGE
            low_r = (0, 150, 5)
            high_r = (4, 255, 255)
            #BLEU
            low_b = (95, 150, 5)
            high_b = (175, 255, 255)
            #VERT
            low_g = (60, 150, 50)
            high_g = (90, 255, 255)
            #ORANGE
            low_o = (5, 150, 100)
            high_o = (15, 255, 255)
            #VIOLET
            low_p = (150, 50, 50)
            high_p = (180, 150, 150)
            #BLANC
            low_w = (0, 0, 70)
            high_w = (180, 150, 255)
            
            #MASKS
            y_mask = cv2.inRange(hsv_img, low_y, high_y)
            r_mask = cv2.inRange(hsv_img, low_r, high_r)
            o_mask = cv2.inRange(hsv_img, low_o, high_o)
            b_mask = cv2.inRange(hsv_img, low_b, high_b)
            g_mask = cv2.inRange(hsv_img, low_g, high_g)
            p_mask = cv2.inRange(hsv_img, low_p, high_p)
            w_mask = cv2.inRange(hsv_img, low_w, high_w)
            
            #Results
            result_r = cv2.bitwise_and(img, img, mask= r_mask)
            result_y = cv2.bitwise_and(img, img, mask= y_mask)
            result_g = cv2.bitwise_and(img, img, mask= g_mask)
            result_b = cv2.bitwise_and(img, img, mask= b_mask)
            result_p = cv2.bitwise_and(img, img, mask= p_mask)
            result_o = cv2.bitwise_and(img, img, mask= o_mask)
            result_w = cv2.bitwise_and(img, img, mask= w_mask)
            mask_tot = r_mask + y_mask + b_mask + g_mask + o_mask + p_mask + w_mask
            r_tot = cv2.bitwise_and(img, img, mask= mask_tot)
            
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img = cv2.bitwise_and(img, img, mask= r_mask + y_mask + b_mask + g_mask + o_mask + p_mask)
            img = cv2.resize(img, r_dim)
            cv2.imshow("Segmentation", img)
            
        if not self.start_segm:
            self.text['text'] ='Flux vidéo :'
            
        self.resized = cv2.resize(self.frame, r_dim)
        
        if self.compt == 0:
            print('[VIDEO INFO] :')
            print('\t' + 'FPS :', int(self.cap.get(5)))
            print('\t' + 'Height :', height)
            print('\t' + 'Width :', width)
            
        if ret:
            cv2image = cv2.cvtColor(self.resized, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(master = self.root, image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
            self.compt += 1
            
        self.root.after(45, self.video_loop)
    
    
#OUVERTURE FICHIER VIDEO    
    def ouvrir_f(self):
        filepath = askopenfilename(title='Charger une vidéo', filetypes=[('Ficher MP4','.mp4'),('Tous les fichiers','.*')])
        self.cap = cv2.VideoCapture(filepath)
        print('\n'+"[INFO] :"+'\n'+'The file '+filepath+' is loaded, click on display')
    
    
#FERMETURE POP_UP    
    def close(self, pop_up):
        pop_up.destroy()
        
        
#FERMETURE DE L'APPLICATION
    def destructor(self):
        self.root.destroy()
        if self.cap is None:
            print('\n'+'No video loaded')
        else:
            self.cap.release()
            cv2.destroyAllWindows()   
        print('\n'+"[INFO] : Closing...")
  
    
#CHOIX D'AFFICHAGE      
    def display(self):
        pop_up = Toplevel(self.root)
        pop_up.title("""Display window""")
        pop_up.geometry('400x175')
        
        self.a = StringVar()
        self.b = StringVar()
        
        label = LabelFrame(pop_up, text = 'Modify dimensions :')
        label.pack()
        exp = Label(pop_up, text = 'It must be a percentage', font=("Comic Sans MS", 10, "italic"))
        exp.pack()
        cadre1 = LabelFrame(label, text = 'Width (%):')
        cadre1.pack()
        larg = Entry(cadre1, textvariable = self.a)
        larg.pack()
        
        cadre2 = LabelFrame(label, text = 'Height (%):')
        cadre2.pack()
        haut = Entry(cadre2, textvariable = self.b)
        haut.pack()
        
        Apply = Button(pop_up, text = 'Apply', command = self.readLabel)
        Apply.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)
        fermer = Button(pop_up, text = 'Close', command = partial(self.close, pop_up))
        fermer.pack(side = LEFT, fill = "both", expand = True, padx = 10, pady = 10)


#APPLICATION CHOIX D'AFFICHAGE   
    def readLabel(self):
        self.A = int(self.a.get())
        self.B = int(self.b.get())
        print('\n'+'[INFO] : '+'\n'+'Displaying the video at :' + '\n' 
              '\n'+'\t'+str(self.A)+'% of original width'+'\n'+'\t'+'           &'+
              '\n'+'\t'+str(self.B)+'% of original height')
        if self.A != self.B:
            print('\n'+'[WARNING] :'+'\n'+'You should choose same % to keep the proportions and prevent stretched videos')
            messagebox.showinfo('Warning', 'Not the best option, see Spyder console for details')
            

#LANCER/ARRETER LA DETECTION VISAGE    
    def start_segm(self):
        if self.start_segm == False:
            self.start_segm = True
            print('[INFO] : Starting segmentation...')
        else:
            self.start_segm = False
            print('[INFO] : Stopping segmentation...')
    
#LANCER/ARRETER LA DETECTION VISAGE BIND    
    def bind_start_segm(self, q):
        if self.start_segm == False:
            self.start_segm = True
            print('[INFO] : Starting detection...')
        else:
            self.start_segm = False
            print('[INFO] : Stopping detection...')
    
        

print("[INFO] : Starting...")
Application().root.mainloop()