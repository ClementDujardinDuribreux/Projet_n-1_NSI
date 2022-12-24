from tkinter import *
from fonc_pions import*
from gerer_plateau import*
from fonc_contraintes import*
import time

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
window.geometry("900x900")
window.minsize(900, 900)
window.config(bg='#C0C0C0')
window.iconbitmap('images pions/logo.ico')
window.title(" Projet NSI n°1  -  Jeu d'Echec")

frame = Frame(window)

case_1 = StringVar()
case_2 = StringVar()
clicked = False
    
def button1():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A1')
    elif clicked == True:
        case_2.set('A1')
        clicked = False

def button2():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A2')
    elif clicked == True:
        case_2.set('A2')
        clicked = False

def button3():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A3')
    elif clicked == True:
        case_2.set('A3')
        clicked = False
        
def button4():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A4')
    elif clicked == True:
        case_2.set('A4')
        clicked = False
        
def button5():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A5')
    elif clicked == True:
        case_2.set('A5')
        clicked = False
        
def button6():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A6')
    elif clicked == True:
        case_2.set('A6')
        clicked = False
        
def button7():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A7')
    elif clicked == True:
        case_2.set('A7')
        clicked = False
        
def button8():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('A8')
    elif clicked == True:
        case_2.set('A8')
        clicked = False
        
def button9():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B1')
    elif clicked == True:
        case_2.set('B1')
        clicked = False
        
def button10():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B2')
    elif clicked == True:
        case_2.set('B2')
        clicked = False
        
def button11():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B3')
    elif clicked == True:
        case_2.set('B3')
        clicked = False
        
def button12():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B4')
    elif clicked == True:
        case_2.set('B4')
        clicked = False
        
def button13():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B5')
    elif clicked == True:
        case_2.set('B5')
        clicked = False
        
def button14():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B6')
    elif clicked == True:
        case_2.set('B6')
        clicked = False
        
def button15():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B7')
    elif clicked == True:
        case_2.set('B7')
        clicked = False
        
def button16():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('B8')
    elif clicked == True:
        case_2.set('B8')
        clicked = False
        
def button17():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C1')
    elif clicked == True:
        case_2.set('C1')
        clicked = False
        
def button18():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C2')
    elif clicked == True:
        case_2.set('C2')
        clicked = False
        
def button19():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C3')
    elif clicked == True:
        case_2.set('C3')
        clicked = False
        
def button20():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C4')
    elif clicked == True:
        case_2.set('C4')
        clicked = False
        
def button21():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C5')
    elif clicked == True:
        case_2.set('C5')
        clicked = False
        
def button22():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C6')
    elif clicked == True:
        case_2.set('C6')
        clicked = False
        
def button23():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C7')
    elif clicked == True:
        case_2.set('C7')
        clicked = False
        
def button24():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('C8')
    elif clicked == True:
        case_2.set('C8')
        clicked = False
        
def button25():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D1')
    elif clicked == True:
        case_2.set('D1')
        clicked = False
        
def button26():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D2')
    elif clicked == True:
        case_2.set('D2')
        clicked = False
        
def button27():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D3')
    elif clicked == True:
        case_2.set('D3')
        clicked = False
        
def button28():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D4')
    elif clicked == True:
        case_2.set('D4')
        clicked = False
        
def button29():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D5')
    elif clicked == True:
        case_2.set('D5')
        clicked = False
        
def button30():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D6')
    elif clicked == True:
        case_2.set('D6')
        clicked = False
        
def button31():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D7')
    elif clicked == True:
        case_2.set('D7')
        clicked = False
        
def button32():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('D8')
    elif clicked == True:
        case_2.set('D8')
        clicked = False
        
def button33():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E1')
    elif clicked == True:
        case_2.set('E1')
        clicked = False
        
def button34():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E2')
    elif clicked == True:
        case_2.set('E2')
        clicked = False

def button35():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E3')
    elif clicked == True:
        case_2.set('E3')
        clicked = False

def button36():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E4')
    elif clicked == True:
        case_2.set('E4')
        clicked = False

def button37():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E5')
    elif clicked == True:
        case_2.set('E5')
        clicked = False

def button38():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E6')
    elif clicked == True:
        case_2.set('E6')
        clicked = False

def button39():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E7')
    elif clicked == True:
        case_2.set('E7')
        clicked = False

def button40():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('E8')
    elif clicked == True:
        case_2.set('E8')
        clicked = False

def button41():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F1')
    elif clicked == True:
        case_2.set('F1')
        clicked = False

def button42():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F2')
    elif clicked == True:
        case_2.set('F2')
        clicked = False

def button43():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F3')
    elif clicked == True:
        case_2.set('F3')
        clicked = False

def button44():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F4')
    elif clicked == True:
        case_2.set('F4')
        clicked = False

def button45():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F5')
    elif clicked == True:
        case_2.set('F5')
        clicked = False

def button46():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F6')
    elif clicked == True:
        case_2.set('F6')
        clicked = False

def button47():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F7')
    elif clicked == True:
        case_2.set('F7')
        clicked = False

def button48():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('F8')
    elif clicked == True:
        case_2.set('F8')
        clicked = False

def button49():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G1')
    elif clicked == True:
        case_2.set('G1')
        clicked = False
        
def button50():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G2')
    elif clicked == True:
        case_2.set('G2')
        clicked = False
        
def button51():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G3')
    elif clicked == True:
        case_2.set('G3')
        clicked = False
        
def button52():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G4')
    elif clicked == True:
        case_2.set('G4')
        clicked = False
        
def button53():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G5')
    elif clicked == True:
        case_2.set('G5')
        clicked = False
        
def button54():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G6')
    elif clicked == True:
        case_2.set('G6')
        clicked = False
        
def button55():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G7')
    elif clicked == True:
        case_2.set('G7')
        clicked = False
        
def button56():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('G8')
    elif clicked == True:
        case_2.set('G8')
        clicked = False
        
def button57():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H1')
    elif clicked == True:
        case_2.set('H1')
        clicked = False
        
def button58():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H2')
    elif clicked == True:
        case_2.set('H2')
        clicked = False
        
def button59():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H3')
    elif clicked == True:
        case_2.set('H3')
        clicked = False
        
def button60():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H4')
    elif clicked == True:
        case_2.set('H4')
        clicked = False
        
def button61():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H5')
    elif clicked == True:
        case_2.set('H5')
        clicked = False
        
def button62():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H6')
    elif clicked == True:
        case_2.set('H6')
        clicked = False
        
def button63():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H7')
    elif clicked == True:
        case_2.set('H7')
        clicked = False
        
def button64():
    global case_1
    global case_2
    global clicked

    if clicked == False:
        clicked = True
        case_1.set('H8')
    elif clicked == True:
        case_2.set('H8')
        clicked = False
        

## --- Initialisation --- ##

button_1 = Button(frame, bg="#8B4513", width=100, height= 100, command = button1, image = photo_vide)
button_2 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button2, image = photo_vide)
button_3 = Button(frame, bg="#8B4513", width=100, height= 100, command = button3, image = photo_vide)
button_4 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button4, image = photo_vide)
button_5 = Button(frame, bg="#8B4513", width=100, height= 100, command = button5, image = photo_vide)
button_6 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button6, image = photo_vide)
button_7 = Button(frame, bg="#8B4513", width=100, height= 100, command = button7, image = photo_vide)
button_8 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button8, image = photo_vide)
button_9 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button9, image = photo_vide)
button_10 = Button(frame, bg="#8B4513", width=100, height= 100, command = button10, image = photo_vide)
button_11 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button11, image = photo_vide)
button_12 = Button(frame, bg="#8B4513", width=100, height= 100, command = button12, image = photo_vide)
button_13 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button13, image = photo_vide)
button_14 = Button(frame, bg="#8B4513", width=100, height= 100, command = button14, image = photo_vide)
button_15 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button15, image = photo_vide)
button_16 = Button(frame, bg="#8B4513", width=100, height= 100, command = button16, image = photo_vide)
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
button_49 = Button(frame, bg="#8B4513", width=100, height= 100, command = button49, image = photo_vide)
button_50 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button50, image = photo_vide)
button_51 = Button(frame, bg="#8B4513", width=100, height= 100, command = button51, image = photo_vide)
button_52 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button52, image = photo_vide)
button_53 = Button(frame, bg="#8B4513", width=100, height= 100, command = button53, image = photo_vide)
button_54 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button54, image = photo_vide)
button_55 = Button(frame, bg="#8B4513", width=100, height= 100, command = button55, image = photo_vide)
button_56 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button56, image = photo_vide)
button_57 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button57, image = photo_vide)
button_58 = Button(frame, bg="#8B4513", width=100, height= 100, command = button58, image = photo_vide)
button_59 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button59, image = photo_vide)
button_60 = Button(frame, bg="#8B4513", width=100, height= 100, command = button60, image = photo_vide)
button_61 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button61, image = photo_vide)
button_62 = Button(frame, bg="#8B4513", width=100, height= 100, command = button62, image = photo_vide)
button_63 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button63, image = photo_vide)
button_64 = Button(frame, bg="#8B4513", width=100, height= 100, command = button64, image = photo_vide)

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

## --------------------------------------------------------------------------------------------------------- ##

def chaque_case():
    liste_case_tuple = []
    liste_case = [  
                    'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
                    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
                    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
                    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
                    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
                    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8',
                ]
    for case in liste_case:
        liste_case_tuple.append(pos(case))
    return liste_case_tuple


def reinitilaliser_plateau(dico_plateau:dict):
    liste_image = []
    liste_fonctions = [
        button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
        button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40,
        button41, button42, button43, button44, button45, button46, button47, button48, button49, button50, button51, button52, button53, button54, button55, button56, button57, button58, button59, button60,
        button61, button62, button63, button64
    ]
    liste_bouttons = [
        button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20,
        button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40,
        button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_58, button_59, button_60,
        button_61, button_62, button_63, button_64
    ]


    for case in chaque_case():
        pion_case = verifier_case(dico_plateau, case)
        
        if pion_case == 'None':
            liste_image.append(photo_vide)

        elif pion_case  == 1 or pion_case == 6:
            liste_image.append(photo_tour_blanc)
        elif pion_case == 2 or pion_case == 7:
            liste_image.append(photo_cavalier_blanc)
        elif pion_case == 3 or pion_case == 8:
            liste_image.append(photo_fou_blanc)
        elif pion_case == 5:
            liste_image.append(photo_dame_blanc)
        elif pion_case == 4:
            liste_image.append(photo_roi_blanc)
        elif pion_case == 9 or pion_case == 10 or pion_case == 11 or pion_case == 12 or pion_case == 13 or pion_case == 14 or pion_case == 15 or pion_case == 16:
            liste_image.append(photo_pions_blanc)
        
        elif pion_case == 100 or pion_case == 150:
            liste_image.append(photo_tour_noir)
        elif pion_case == 110 or pion_case == 160:
            liste_image.append(photo_cavalier_noir)
        elif pion_case == 120 or pion_case == 170:
            liste_image.append(photo_fou_noir)
        elif pion_case == 130:
            liste_image.append(photo_dame_noir)
        elif pion_case == 140:
            liste_image.append(photo_roi_noir)
        elif pion_case == 180 or pion_case == 190 or pion_case == 200 or pion_case == 210 or pion_case == 220 or pion_case == 230 or pion_case == 240 or pion_case == 250:
            liste_image.append(photo_pions_noir)

    a = 0
    b = 0
    for i in range(0,64):
        if (i + b) % 2 == 0:
            couleur = "#8B4513"
        else:
            couleur = "#FFDEAD"

        liste_bouttons[i] = Button(frame, bg=couleur, width=100, height= 100, command = liste_fonctions[i], image = liste_image[i])
        liste_bouttons[i].grid(column=a, row=b)

        a += 1
        if a == 8:
            a = 0
            b += 1

    return None

def lancer(J1:str, J2:str) -> None:

    global clicked
    global case_1
    global case_2

    dico_plateau = placement_pion_depart(generer_plateau(8,8))
    tour = 1
    ficher = open('historique_parties.txt', 'a')

    reinitilaliser_plateau(dico_plateau)

    while roi_en_vie_J1(dico_plateau) == True and roi_en_vie_J2(dico_plateau) == True:
        if tour % 2 == 0:
            joueur = 2
        else:
            joueur = 1
        
        window.wait_variable(case_1)
        case_ini = case_1.get()

        while verifier_case(dico_plateau, pos(case_ini)) == 'None':
            window.wait_variable(case_1)
            case_ini = case_1.get()

        window.wait_variable(case_2)
        case_final = case_2.get()

        while contraintes_global(dico_plateau, verifier_case(dico_plateau, pos(case_ini)), pos(case_ini), pos(case_final), joueur)[0] != True:
            case_1 = StringVar()
            case_2 = StringVar()
            window.wait_variable(case_1)
            case_ini = case_1.get()
            window.wait_variable(case_2)
            case_final = case_2.get()

        tour += 1
        dico_plateau = deplacer_pion(dico_plateau, verifier_case(dico_plateau, pos(case_ini)), pos(case_final))
        case_1 = StringVar()
        case_2 = StringVar()
        reinitilaliser_plateau(dico_plateau)
        afficher_plateau(dico_plateau)

    if roi_en_vie_J1(dico_plateau) == True:
        gagnant = J1
    else:
        gagnant = J2

    ficher.write(' - ' + J1 + '\n' + ' - ' + J2 + '\n' + 'Le gagnant de cette partie est : ' + gagnant + ' en ' + str(tour) + 'tours' +'\n' + '\n')
    ficher.close()

    time.sleep(2)
    window.destroy()

    return 

lancer("1", "2")

window.mainloop()