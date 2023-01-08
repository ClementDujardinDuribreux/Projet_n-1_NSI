from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

from fonc_pions import*
from gerer_plateau import*
from fonc_contraintes import*
import time

##from jeu import*

## ---------------------------- JEU UI ------------------------------ ##

window = Tk()

photo_vide = PhotoImage(file="images pions/vide.png")
photo_pions_noir = PhotoImage(file="images pions/pions_noir.png")
photo_pions_blanc = PhotoImage(file="images pions/pions blanc.png")
photo_tour_noir = PhotoImage(file="images pions/tours noir.png")
photo_tour_blanc = PhotoImage(file="images pions/tours blanc.png")
photo_cavalier_noir = PhotoImage(file="images pions/dada noir.png")
photo_cavalier_blanc = PhotoImage(file="images pions/dada blanc.png")
photo_fou_noir = PhotoImage(file="images pions/fou noir .png")
photo_fou_blanc = PhotoImage(file="images pions/fou blanc.png")
photo_dame_noir = PhotoImage(file="images pions/reine noir .png")
photo_dame_blanc = PhotoImage(file="images pions/reine blanc.png")
photo_roi_noir = PhotoImage(file="images pions/roi noir .png")
photo_roi_blanc = PhotoImage(file="images pions/roi blanc.png")

window.title("Jeu")
window.geometry("900x940")
window.minsize(900, 940)
window.config(bg='#C0C0C0')
window.iconbitmap('images pions/logo.ico')
window.title(" Projet NSI n°1  -  Jeu d'Echec")

frame = Frame(window)

case_1 = ""
case_2 = ""
isClicked = False
joueur = 1
dico_plateau = placement_pion_depart(generer_plateau(8,8))
dico_button = {}
    
def button1():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A1"
        affichage(dico_button)

def button2():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A2"
        affichage(dico_button)

def button3():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A3"
        affichage(dico_button)

def button4():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A4"
        affichage(dico_button)

def button5():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A5"
        affichage(dico_button)

def button6():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A6"
        affichage(dico_button)

def button7():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A7"
        affichage(dico_button)
        
def button8():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "A8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "A8"
        affichage(dico_button)
        
def button9():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B1"
        affichage(dico_button)
        
def button10():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B2"
        affichage(dico_button)
        
def button11():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B3"
        affichage(dico_button)
        
def button12():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B4"
        affichage(dico_button)
        
def button13():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B5"
        affichage(dico_button)
        
def button14():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B6"
        affichage(dico_button)
        
def button15():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B7"
        affichage(dico_button)
        
def button16():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "B8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "B8"
        affichage(dico_button)   

def button17():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C1"
        affichage(dico_button)

def button18():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C2"
        affichage(dico_button)
        
def button19():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C3"
        affichage(dico_button)
        
def button20():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C4"
        affichage(dico_button)
        
def button21():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C5"
        affichage(dico_button)
        
def button22():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C6"
        affichage(dico_button)
        
def button23():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C7"
        affichage(dico_button)
        
def button24():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "C8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "C8"
        affichage(dico_button)
        
def button25():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D1"
        affichage(dico_button)
        
def button26():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D2"
        affichage(dico_button)
        
def button27():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D3"
        affichage(dico_button)
        
def button28():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D4"
        affichage(dico_button)
        
def button29():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D5"
        affichage(dico_button)
        
def button30():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D6"
        affichage(dico_button)
        
def button31():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D7"
        affichage(dico_button)
        
def button32():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "D8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "D8"
        affichage(dico_button)
        
def button33():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E1"
        affichage(dico_button)
        
def button34():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E2"
        affichage(dico_button)
        
def button35():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E3"
        affichage(dico_button)
        
def button36():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E4"
        affichage(dico_button)
        
def button37():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E5"
        affichage(dico_button)
        
def button38():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E6"
        affichage(dico_button)
        
def button39():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E7"
        affichage(dico_button)
        
def button40():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "E8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "E8"
        affichage(dico_button)
        
def button41():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F1"
        affichage(dico_button)
        
def button42():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F2"
        affichage(dico_button)
        
def button43():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F3"
        affichage(dico_button)
        
def button44():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F4"
        affichage(dico_button)
        
def button45():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F5"
        affichage(dico_button)
        
def button46():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F6"
        affichage(dico_button)
        
def button47():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F7"
        affichage(dico_button)
        
def button48():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "F8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "F8"
        affichage(dico_button)
        
def button49():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G1"
        affichage(dico_button)
        
def button50():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G2"
        affichage(dico_button)
        
def button51():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G3"
        affichage(dico_button)
        
def button52():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G4"
        affichage(dico_button)
        
def button53():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G5"
        affichage(dico_button)
        
def button54():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G6"
        affichage(dico_button)
        
def button55():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G7"
        affichage(dico_button)
        
def button56():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "G8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "G8"
        affichage(dico_button)
        
def button57():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H1"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H1"
        affichage(dico_button)
        
def button58():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H2"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H2"
        affichage(dico_button)
        
def button59():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H3"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H3"
        affichage(dico_button)
        
def button60():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H4"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H4"
        affichage(dico_button)
        
def button61():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H5"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H5"
        affichage(dico_button)
        
def button62():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H6"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H6"
        affichage(dico_button)
        
def button63():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H7"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H7"
        affichage(dico_button)
        
def button64():
    global case_1
    global case_2
    global isClicked
    global dico_button

    if isClicked:
        case_2 = "H8"
        affichage(dico_button)
        isClicked = False
    else:
        case_1 = "H8"
        affichage(dico_button)

label = Label(window, bg = '#C0C0C0', font=("Arial", 20))
label.pack(pady=10)
        
def intialiser_plateau():

    global case_1
    global case_2
    global isClicked
    global joueur
    global dico_plateau
    global dico_button
    global label

    case_1 = ""
    case_2 = ""
    isClicked = False
    joueur = 1
    dico_plateau = placement_pion_depart(generer_plateau(8,8))

    button_1 = Button(frame, bg="#8B4513", width=100, height= 100, command = button1, image = photo_tour_noir)
    button_2 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button2, image = photo_cavalier_noir)
    button_3 = Button(frame, bg="#8B4513", width=100, height= 100, command = button3, image = photo_fou_noir)
    button_4 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button4, image = photo_dame_noir)
    button_5 = Button(frame, bg="#8B4513", width=100, height= 100, command = button5, image = photo_roi_noir)
    button_6 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button6, image = photo_fou_noir)
    button_7 = Button(frame, bg="#8B4513", width=100, height= 100, command = button7, image = photo_cavalier_noir)
    button_8 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button8, image = photo_tour_noir)
    button_9 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button9, image = photo_pions_noir)
    button_10 = Button(frame, bg="#8B4513", width=100, height= 100, command = button10, image = photo_pions_noir)
    button_11 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button11, image = photo_pions_noir)
    button_12 = Button(frame, bg="#8B4513", width=100, height= 100, command = button12, image = photo_pions_noir)
    button_13 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button13, image = photo_pions_noir)
    button_14 = Button(frame, bg="#8B4513", width=100, height= 100, command = button14, image = photo_pions_noir)
    button_15 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button15, image = photo_pions_noir)
    button_16 = Button(frame, bg="#8B4513", width=100, height= 100, command = button16, image = photo_pions_noir)
    button_17 = Button(frame, bg="#8B4513", width=100, height= 100, command = button17, image = photo_vide)
    button_18 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button18, image = photo_vide)
    button_19 = Button(frame, bg="#8B4513", width=100, height= 100, command = button19, image = photo_vide)
    button_20 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button20, image = photo_vide)
    button_21 = Button(frame, bg="#8B4513", width=100, height= 100, command = button21, image = photo_vide)
    button_22 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button22, image = photo_vide)
    button_23 = Button(frame, bg="#8B4513", width=100, height= 100, command = button23, image = photo_vide)
    button_24 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button24, image = photo_vide)
    button_25 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button25, image = photo_vide)
    button_26 = Button(frame, bg="#8B4513", width=100, height= 100, command = button26, image = photo_vide)
    button_27 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button27, image = photo_vide)
    button_28 = Button(frame, bg="#8B4513", width=100, height= 100, command = button28, image = photo_vide)
    button_29 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button29, image = photo_vide)
    button_30 = Button(frame, bg="#8B4513", width=100, height= 100, command = button30, image = photo_vide)
    button_31 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button31, image = photo_vide)
    button_32 = Button(frame, bg="#8B4513", width=100, height= 100, command = button32, image = photo_vide)
    button_33 = Button(frame, bg="#8B4513", width=100, height= 100, command = button33, image = photo_vide)
    button_34 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button34, image = photo_vide)
    button_35 = Button(frame, bg="#8B4513", width=100, height= 100, command = button35, image = photo_vide)
    button_36 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button36, image = photo_vide)
    button_37 = Button(frame, bg="#8B4513", width=100, height= 100, command = button37, image = photo_vide)
    button_38 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button38, image = photo_vide)
    button_39 = Button(frame, bg="#8B4513", width=100, height= 100, command = button39, image = photo_vide)
    button_40 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button40, image = photo_vide)
    button_41 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button41, image = photo_vide)
    button_42 = Button(frame, bg="#8B4513", width=100, height= 100, command = button42, image = photo_vide)
    button_43 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button43, image = photo_vide)
    button_44 = Button(frame, bg="#8B4513", width=100, height= 100, command = button44, image = photo_vide)
    button_45 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button45, image = photo_vide)
    button_46 = Button(frame, bg="#8B4513", width=100, height= 100, command = button46, image = photo_vide)
    button_47 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button47, image = photo_vide)
    button_48 = Button(frame, bg="#8B4513", width=100, height= 100, command = button48, image = photo_vide)
    button_49 = Button(frame, bg="#8B4513", width=100, height= 100, command = button49, image = photo_pions_blanc)
    button_50 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button50, image = photo_pions_blanc)
    button_51 = Button(frame, bg="#8B4513", width=100, height= 100, command = button51, image = photo_pions_blanc)
    button_52 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button52, image = photo_pions_blanc)
    button_53 = Button(frame, bg="#8B4513", width=100, height= 100, command = button53, image = photo_pions_blanc)
    button_54 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button54, image = photo_pions_blanc)
    button_55 = Button(frame, bg="#8B4513", width=100, height= 100, command = button55, image = photo_pions_blanc)
    button_56 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button56, image = photo_pions_blanc)
    button_57 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button57, image = photo_tour_blanc)
    button_58 = Button(frame, bg="#8B4513", width=100, height= 100, command = button58, image = photo_cavalier_blanc)
    button_59 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button59, image = photo_fou_blanc)
    button_60 = Button(frame, bg="#8B4513", width=100, height= 100, command = button60, image = photo_roi_blanc)
    button_61 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button61, image = photo_dame_blanc)
    button_62 = Button(frame, bg="#8B4513", width=100, height= 100, command = button62, image = photo_fou_blanc)
    button_63 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button63, image = photo_cavalier_blanc)
    button_64 = Button(frame, bg="#8B4513", width=100, height= 100, command = button64, image = photo_tour_blanc)

    button_1.grid(column=0, row=0)
    button_2.grid(column=1, row=0)
    button_3.grid(column=2, row=0)
    button_4.grid(column=3, row=0)
    button_5.grid(column=4, row=0)
    button_6.grid(column=5, row=0)
    button_7.grid(column=6, row=0)
    button_8.grid(column=7, row=0)
    button_9.grid(column=0, row=1)
    button_10.grid(column=1, row=1)
    button_11.grid(column=2, row=1)
    button_12.grid(column=3, row=1)
    button_13.grid(column=4, row=1)
    button_14.grid(column=5, row=1)
    button_15.grid(column=6, row=1)
    button_16.grid(column=7, row=1)
    button_17.grid(column=0, row=2)
    button_18.grid(column=1, row=2)
    button_19.grid(column=2, row=2)
    button_20.grid(column=3, row=2)
    button_21.grid(column=4, row=2)
    button_22.grid(column=5, row=2)
    button_23.grid(column=6, row=2)
    button_24.grid(column=7, row=2)
    button_25.grid(column=0, row=3)
    button_26.grid(column=1, row=3)
    button_27.grid(column=2, row=3)
    button_28.grid(column=3, row=3)
    button_29.grid(column=4, row=3)
    button_30.grid(column=5, row=3)
    button_31.grid(column=6, row=3)
    button_32.grid(column=7, row=3)
    button_33.grid(column=0, row=4)
    button_34.grid(column=1, row=4)
    button_35.grid(column=2, row=4)
    button_36.grid(column=3, row=4)
    button_37.grid(column=4, row=4)
    button_38.grid(column=5, row=4)
    button_39.grid(column=6, row=4)
    button_40.grid(column=7, row=4)
    button_41.grid(column=0, row=5)
    button_42.grid(column=1, row=5)
    button_43.grid(column=2, row=5)
    button_44.grid(column=3, row=5)
    button_45.grid(column=4, row=5)
    button_46.grid(column=5, row=5)
    button_47.grid(column=6, row=5)
    button_48.grid(column=7, row=5)
    button_49.grid(column=0, row=6)
    button_50.grid(column=1, row=6)
    button_51.grid(column=2, row=6)
    button_52.grid(column=3, row=6)
    button_53.grid(column=4, row=6)
    button_54.grid(column=5, row=6)
    button_55.grid(column=6, row=6)
    button_56.grid(column=7, row=6)
    button_57.grid(column=0, row=7)
    button_58.grid(column=1, row=7)
    button_59.grid(column=2, row=7)
    button_60.grid(column=3, row=7)
    button_61.grid(column=4, row=7)
    button_62.grid(column=5, row=7)
    button_63.grid(column=6, row=7)
    button_64.grid(column=7, row=7)

    frame.pack(expand=YES)

    label_joueur(joueur, label)

    dico_button = {"A1": [button_1, button1, 0, 0], "A2": [button_2, button2, 1, 0], "A3": [button_3, button3, 2, 0], "A4": [button_4, button4, 3, 0],
               "A5": [button_5, button5, 4, 0], "A6": [button_6, button6, 5, 0], "A7": [button_7, button7, 6, 0], "A8": [button_8, button8, 7, 0],
               "B1": [button_9, button9, 0, 1], "B2": [button_10, button10, 1, 1], "B3": [button_11, button11, 2, 1], "B4": [button_12, button12, 3, 1],
               "B5": [button_13, button13, 4, 1], "B6": [button_14, button14, 5, 1], "B7": [button_15, button15, 6, 1], "B8": [button_16, button16, 7, 1],
               "C1": [button_17, button17, 0, 2], "C2": [button_18, button18, 1, 2], "C3": [button_19, button19, 2, 2], "C4": [button_20, button20, 3, 2],
               "C5": [button_21, button21, 4, 2], "C6": [button_22, button22, 5, 2], "C7": [button_23, button23, 6, 2], "C8": [button_24, button24, 7, 2],
               "D1": [button_25, button25, 0, 3], "D2": [button_26, button26, 1, 3], "D3": [button_27, button27, 2, 3], "D4": [button_28, button28, 3, 3],
               "D5": [button_29, button29, 4, 3], "D6": [button_30, button30, 5, 3], "D7": [button_31, button31, 6, 3], "D8": [button_32, button32, 7, 3],
               "E1": [button_33, button33, 0, 4], "E2": [button_34, button34, 1, 4], "E3": [button_35, button35, 2, 4], "E4": [button_36, button36, 3, 4],
               "E5": [button_37, button37, 4, 4], "E6": [button_38, button38, 5, 4], "E7": [button_39, button39, 6, 4], "E8": [button_40, button40, 7, 4],
               "F1": [button_41, button41, 0, 5], "F2": [button_42, button42, 1, 5], "F3": [button_43, button43, 2, 5], "F4": [button_44, button44, 3, 5],
               "F5": [button_45, button45, 4, 5], "F6": [button_46, button46, 5, 5], "F7": [button_47, button47, 6, 5], "F8": [button_48, button48, 7, 5],
               "G1": [button_49, button49, 0, 6], "G2": [button_50, button50, 1, 6], "G3": [button_51, button51, 2, 6], "G4": [button_52, button52, 3, 6],
               "G5": [button_53, button53, 4, 6], "G6": [button_54, button54, 5, 6], "G7": [button_55, button55, 6, 6], "G8": [button_56, button56, 7, 6],
               "H1": [button_57, button57, 0, 7], "H2": [button_58, button58, 1, 7], "H3": [button_59, button59, 2, 7], "H4": [button_60, button60, 3, 7],
               "H5": [button_61, button61, 4, 7], "H6": [button_62, button62, 5, 7], "H7": [button_63, button63, 6, 7], "H8": [button_64, button64, 7, 7]}

def label_joueur(joueur:int, label:Label):
    if joueur == 1:
        label.config(text="C'est aux pions blancs", fg = 'white')
    else:
        label.config(text="C'est aux pions noirs", fg = 'black')

intialiser_plateau()

def menu_quit():
    avert_quit = messagebox.askyesno("Quitter", "Êtes-vous sur de vouloir quitter ?")
    if avert_quit:
        window.quit()

def menu_retry():
    avert_retry = messagebox.askretrycancel('Recommencer', 'Voulez-vous vraiment recommencer ?')
    if avert_retry:
        intialiser_plateau()

menu_bar = Menu(window)
lancer_menu = Menu(menu_bar, tearoff=0)
lancer_menu.add_command(label='Relancer', command= menu_retry)
lancer_menu.add_command(label='Quitter', command= menu_quit)
menu_bar.add_cascade(label='Jeu', menu= lancer_menu)

j1 = simpledialog.askstring("Nom du joueur 1", "Entre ton nom", parent=window)
j2 = simpledialog.askstring("Nom du joueur 2", "Entre ton nom", parent=window)

if j1 == None:
    j1 = "Joueur 1"
if j2 == None:
    j2 = "Joueur 2"

def change_color(couleur:str, bouton:Button):

    color_base = bouton.cget('bg')
    bouton.configure(bg = couleur)
    window.update()
    time.sleep(1)
    bouton.configure(bg = color_base)

def affichage(dico_button):

    global isClicked
    global case_1
    global case_2
    global joueur
    global dico_plateau
    global j1
    global label

    pion_a_bouger = verifier_case(dico_plateau, pos(case_1))

    if isClicked and contraintes_global(dico_plateau, pion_a_bouger, pos(case_1), pos(case_2), joueur)[0]:
    
        color1 = dico_button[case_1][0].cget("bg")
        image = dico_button[case_1][0].cget('image')
        dico_button[case_1][0] = Button(frame, bg= color1, width=100, height= 100, command = dico_button[case_1][1], image = photo_vide)
        dico_button[case_1][0].grid(column= dico_button[case_1][2], row= dico_button[case_1][3])
        color2 = dico_button[case_2][0].cget("bg")
        dico_button[case_2][0] = Button(frame, bg= color2, width=100, height= 100, command = dico_button[case_2][1], image = image)
        dico_button[case_2][0].grid(column= dico_button[case_2][2], row= dico_button[case_2][3])

        dico_plateau = deplacer_pion(dico_plateau, pion_a_bouger, pos(case_2))

        joueur += 1

        if joueur % 2 == 0:
            joueur = 2
        else:
            joueur = 1

        label_joueur(joueur, label)

        if roi_en_vie_J1(dico_plateau) == False or roi_en_vie_J2(dico_plateau) == False:
            if roi_en_vie_J1(dico_plateau) == False:
                gagnant = j2
            else:
                gagnant = j1
            ficher = open('historique_parties.txt', 'a')
            ficher.write(' - ' + j1 + '\n' + ' - ' + j2 + '\n' + 'Le gagnant de cette partie est : ' + gagnant +'\n' + '\n')
            ficher.close()
            message_fin = messagebox.askyesno("Recommencer", "Voulez-vous relancer une partie ?")
            if message_fin:
                intialiser_plateau()
            else:
                window.quit()
    
    elif isClicked and contraintes_global(dico_plateau, pion_a_bouger, pos_pion(dico_plateau,pion_a_bouger), pos(case_2), joueur)[0] == False:
        change_color("#FE3939", dico_button[case_2][0])  

    if pion_a_bouger == 'None':
        case_1 = ""
        isClicked = False
    else:
        isClicked = True

window.config(menu= menu_bar)

window.mainloop()
