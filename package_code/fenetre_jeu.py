from tkinter import *

from fonc_pions import*
from gerer_plateau import*
from fonc_contraintes import*
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
window.geometry("900x900")
window.minsize(900, 900)
window.config(bg='#C0C0C0')
window.iconbitmap('images pions/logo.ico')
window.title(" Projet NSI n°1  -  Jeu d'Echec")

frame = Frame(window)

case = ""
    
def button1():
    global case 
    case = "A1"
def button2():
    global case 
    case = "A2"
def button3():
    global case 
    case = "A3"
def button4():
    global case 
    case = "A4"
def button5():
    global case 
    case = "A5"
def button6():
    global case
    case = "A6"
def button7():
    global case
    case = "A7"
def button8():
    global case
    case = "A8"
def button9():
    global case
    case = "B1"
def button10():
    global case
    case = "B2"
def button11():
    global case
    case = "B3"
def button12():
    global case
    case = "B4"
def button13():
    global case
    case = "B5"
def button14():
    global case
    case = "B6"
def button15():
    global case
    case = "B7"
def button16():
    global case
    case = "B8"
def button17():
    global case
    case = "C1"
def button18():
    global case
    case = "C2"
def button19():
    global case
    case = "C3"
def button20():
    global case
    case = "C4"
def button21():
    global case
    case = "C5"
def button22():
    global case
    case = "C6"
def button23():
    global case
    case = "C7"
def button24():
    global case
    case = "C8"
def button25():
    global case
    case = "D1"
def button26():
    global case
    case = "D2"
def button27():
    global case
    case = "D3"
def button28():
    global case
    case = "D4"
def button29():
    global case
    case = "D5"
def button30():
    global case
    case = "D6"
def button31():
    global case
    case = "D7"
def button32():
    global case
    case = "D8"
def button33():
    global case
    case = "E1"
def button34():
    global case
    case = "E2"
def button35():
    global case
    case = "E3"
def button36():
    global case
    case = "E4"
def button37():
    global case
    case = "E5"
def button38():
    global case
    case = "E6"
def button39():
    global case
    case = "E7"
def button40():
    global case
    case = "E8"
def button41():
    global case
    case = "F1"
def button42():
    global case
    case = "F2"
def button43():
    global case
    case = "F3"
def button44():
    global case
    case = "F4"
def button45():
    global case
    case = "F5"
def button46():
    global case
    case = "F6"
def button47():
    global case
    case = "F7"
def button48():
    global case
    case = "F8"
def button49():
    global case
    case = "G1"
def button50():
    global case
    case = "G2"
def button51():
    global case
    case = "G3"
def button52():
    global case
    case = "G4"
def button53():
    global case
    case = "G5"
def button54():
    global case
    case = "G6"
def button55():
    global case
    case = "G7"
def button56():
    global case
    case = "G8"
def button57():
    global case
    case = "H1"
def button58():
    global case
    case = "H2"
def button59():
    global case
    case = "H3"
def button60():
    global case
    case = "H4"
def button61():
    global case
    case = "H5"
def button62():
    global case
    case = "H6"
def button63():
    global case
    case = "H7"
def button64():
    global case
    case = "H8"

button1 = Button(frame, bg="#8B4513", width=100, height= 100, command = button1, image = photo_pions_noir)
button2 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button2, image = photo_pions_noir)
button3 = Button(frame, bg="#8B4513", width=100, height= 100, command = button3, image = photo_pions_noir)
button4 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button4, image = photo_pions_noir)
button5 = Button(frame, bg="#8B4513", width=100, height= 100, command = button5, image = photo_pions_noir)
button6 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button6, image = photo_pions_noir)
button7 = Button(frame, bg="#8B4513", width=100, height= 100, command = button7, image = photo_pions_noir)
button8 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button8, image = photo_pions_noir)
button9 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button9, image = photo_pions_noir)
button10 = Button(frame, bg="#8B4513", width=100, height= 100, command = button10, image = photo_pions_noir)
button11 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button11, image = photo_pions_noir)
button12 = Button(frame, bg="#8B4513", width=100, height= 100, command = button12, image = photo_pions_noir)
button13 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button13, image = photo_pions_noir)
button14 = Button(frame, bg="#8B4513", width=100, height= 100, command = button14, image = photo_pions_noir)
button15 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button15, image = photo_pions_noir)
button16 = Button(frame, bg="#8B4513", width=100, height= 100, command = button16, image = photo_pions_noir)
button17 = Button(frame, bg="#8B4513", width=100, height= 100, command = button17, image = photo_vide)
button18 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button18, image = photo_vide)
button19 = Button(frame, bg="#8B4513", width=100, height= 100, command = button19, image = photo_vide)
button20 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button20, image = photo_vide)
button21 = Button(frame, bg="#8B4513", width=100, height= 100, command = button21, image = photo_vide)
button22 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button22, image = photo_vide)
button23 = Button(frame, bg="#8B4513", width=100, height= 100, command = button23, image = photo_vide)
button24 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button24, image = photo_vide)
button25 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button25, image = photo_vide)
button26 = Button(frame, bg="#8B4513", width=100, height= 100, command = button26, image = photo_vide)
button27 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button27, image = photo_vide)
button28 = Button(frame, bg="#8B4513", width=100, height= 100, command = button28, image = photo_vide)
button29 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button29, image = photo_vide)
button30 = Button(frame, bg="#8B4513", width=100, height= 100, command = button30, image = photo_vide)
button31 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button31, image = photo_vide)
button32 = Button(frame, bg="#8B4513", width=100, height= 100, command = button32, image = photo_vide)
button33 = Button(frame, bg="#8B4513", width=100, height= 100, command = button33, image = photo_vide)
button34 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button34, image = photo_vide)
button35 = Button(frame, bg="#8B4513", width=100, height= 100, command = button35, image = photo_vide)
button36 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button36, image = photo_vide)
button37 = Button(frame, bg="#8B4513", width=100, height= 100, command = button37, image = photo_vide)
button38 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button38, image = photo_vide)
button39 = Button(frame, bg="#8B4513", width=100, height= 100, command = button39, image = photo_vide)
button40 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button40, image = photo_vide)
button41 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button41, image = photo_vide)
button42 = Button(frame, bg="#8B4513", width=100, height= 100, command = button42, image = photo_vide)
button43 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button43, image = photo_vide)
button44 = Button(frame, bg="#8B4513", width=100, height= 100, command = button44, image = photo_vide)
button45 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button45, image = photo_vide)
button46 = Button(frame, bg="#8B4513", width=100, height= 100, command = button46, image = photo_vide)
button47 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button47, image = photo_vide)
button48 = Button(frame, bg="#8B4513", width=100, height= 100, command = button48, image = photo_vide)
button49 = Button(frame, bg="#8B4513", width=100, height= 100, command = button49, image = photo_pions_blanc)
button50 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button50, image = photo_pions_blanc)
button51 = Button(frame, bg="#8B4513", width=100, height= 100, command = button51, image = photo_pions_blanc)
button52 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button52, image = photo_pions_blanc)
button53 = Button(frame, bg="#8B4513", width=100, height= 100, command = button53, image = photo_pions_blanc)
button54 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button54, image = photo_pions_blanc)
button55 = Button(frame, bg="#8B4513", width=100, height= 100, command = button55, image = photo_pions_blanc)
button56 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button56, image = photo_pions_blanc)
button57 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button57, image = photo_pions_blanc)
button58 = Button(frame, bg="#8B4513", width=100, height= 100, command = button58, image = photo_pions_blanc)
button59 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button59, image = photo_pions_blanc)
button60 = Button(frame, bg="#8B4513", width=100, height= 100, command = button60, image = photo_pions_blanc)
button61 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button61, image = photo_pions_blanc)
button62 = Button(frame, bg="#8B4513", width=100, height= 100, command = button62, image = photo_pions_blanc)
button63 = Button(frame, bg="#FFDEAD", width=100, height= 100, command = button63, image = photo_pions_blanc)
button64 = Button(frame, bg="#8B4513", width=100, height= 100, command = button64, image = photo_pions_blanc)

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=2, row=0)
button4.grid(column=3, row=0)
button5.grid(column=4, row=0)
button6.grid(column=5, row=0)
button7.grid(column=6, row=0)
button8.grid(column=7, row=0)
button9.grid(column=0, row=1)
button10.grid(column=1, row=1)
button11.grid(column=2, row=1)
button12.grid(column=3, row=1)
button13.grid(column=4, row=1)
button14.grid(column=5, row=1)
button15.grid(column=6, row=1)
button16.grid(column=7, row=1)
button17.grid(column=0, row=2)
button18.grid(column=1, row=2)
button19.grid(column=2, row=2)
button20.grid(column=3, row=2)
button21.grid(column=4, row=2)
button22.grid(column=5, row=2)
button23.grid(column=6, row=2)
button24.grid(column=7, row=2)
button25.grid(column=0, row=3)
button26.grid(column=1, row=3)
button27.grid(column=2, row=3)
button28.grid(column=3, row=3)
button29.grid(column=4, row=3)
button30.grid(column=5, row=3)
button31.grid(column=6, row=3)
button32.grid(column=7, row=3)
button33.grid(column=0, row=4)
button34.grid(column=1, row=4)
button35.grid(column=2, row=4)
button36.grid(column=3, row=4)
button37.grid(column=4, row=4)
button38.grid(column=5, row=4)
button39.grid(column=6, row=4)
button40.grid(column=7, row=4)
button41.grid(column=0, row=5)
button42.grid(column=1, row=5)
button43.grid(column=2, row=5)
button44.grid(column=3, row=5)
button45.grid(column=4, row=5)
button46.grid(column=5, row=5)
button47.grid(column=6, row=5)
button48.grid(column=7, row=5)
button49.grid(column=0, row=6)
button50.grid(column=1, row=6)
button51.grid(column=2, row=6)
button52.grid(column=3, row=6)
button53.grid(column=4, row=6)
button54.grid(column=5, row=6)
button55.grid(column=6, row=6)
button56.grid(column=7, row=6)
button57.grid(column=0, row=7)
button58.grid(column=1, row=7)
button59.grid(column=2, row=7)
button60.grid(column=3, row=7)
button61.grid(column=4, row=7)
button62.grid(column=5, row=7)
button63.grid(column=6, row=7)
button64.grid(column=7, row=7)

frame.pack(expand=YES)

window.mainloop()