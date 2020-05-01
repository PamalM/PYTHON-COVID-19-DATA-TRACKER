#main.py is the index file. This is the file that user will execute to run the project. (Base-File)

#Tkinter library will be used to create graphical user interface.
from tkinter import *
from PIL import Image, ImageTk

#Method displays the selected country. 
def display_Selected_Country(*_):
    print(country.get())

#Create reference of home window. 
root = Tk()

#Draw: ['Select Country'] label.
label1 = Label(root, text="SELECT COUNTRY:", bg="light yellow", fg="gray24", font=("Courier", 20, "bold"))
label1.place(x=30, y=20)

#Draw box containing selection of countries. 
countries_Canvas = Canvas(root, width=720, height=140, bg="gray28")
countries_Canvas.place(x=30, y=50)

#List containing folder references to countries flags.
countriesDirectory = ['Flags/USA.png',
                      'Flags/CANADA.png',
                      'Flags/FRANCE.png',
                      'Flags/UK.png',
                      'Flags/SPAIN.png',
                      'Flags/ITALY.png']

#Insert flags/countries into canvas as images.
usaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[0]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(70,44, anchor=CENTER, image=usaFlag)

canadaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[1]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(70,106, anchor=CENTER, image=canadaFlag)

franceFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[2]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(304,44, anchor=CENTER, image=franceFlag)

ukFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[3]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(304,106, anchor=CENTER, image=ukFlag)

spainFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[4]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(550,44, anchor=CENTER, image=spainFlag)

italyFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[5]).resize((80, 40), Image.ANTIALIAS))
countries_Canvas.create_image(550,106, anchor=CENTER, image=italyFlag)

#String variable to hold the selected country.
country = StringVar()

#Insert radio buttons to the right of country flags.
R1 = Radiobutton(root, text="USA", value="UNITED STATES OF AMERICA", var=country, font=("Courier", 20, "bold"))
R1.place(x=150, y=80)

R2 = Radiobutton(root, text="CANADA", value="CANADA", var=country, font=("Courier", 20, "bold"))
R2.place(x=150, y=142)

R3 = Radiobutton(root, text="FRANCE", value="FRANCE", var=country, font=("Courier", 20, "bold"))
R3.place(x=386, y=80)

R4 = Radiobutton(root, text="UK", value="UNITED KINGDOM", var=country, font=("Courier", 20, "bold"))
R4.place(x=386, y=142)

R5 = Radiobutton(root, text="SPAIN", value="SPAIN", var=country, font=("Courier", 20, "bold"))
R5.place(x=630, y=80)

R6 = Radiobutton(root, text="ITALY", value="ITALY", var=country, font=("Courier", 20, "bold"))
R6.place(x=630, y=142)

#Displays the selected country; Via the RadioButton.
country.trace('w', display_Selected_Country)

#Window's attributes. (Size, title, other characteristics etc.)
root.title("PYTHON COVID-19 DATA TRACKER")
root.geometry("800x500")
root.resizable(False, False)
root.configure(bg="medium slate blue")
root.mainloop()
