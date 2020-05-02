#Main.py: This is the base-file for the application. User must run this (.py) to launch the program. 

#Tkinter library will be utilized to create the GUI.
from tkinter import Label, Tk, Canvas, Button, Radiobutton, CENTER, StringVar, DISABLED, NORMAL

#PIL library will be utilized to resize and display the images used within our application.
from PIL import Image, ImageTk

#Import the other python file that will be used to display the data after a country/worldwide option is selected.
import displayData

#After the welcome screen, the user is presented with the selection page.
#Here they will select whether they wish to view worldwide COVID-19 data, or particular to one of the provided countries. 
def selection_GUI():
    
    #Method displays the selected radio button country/worldwide selection back to the user in top right. 
    def selected_Country(*_):

        #We will attempt to catch any errors that arise that may cause error messages to show if image can't be displayed due to program exit. 
        try:
            global selectionPicture
            global cc
            
            #Save country code as integer.
            cc = countryCode.get(country.get())

            #Make canvas visible; Updated with the selected country.
            selectionPicture = ImageTk.PhotoImage(Image.open(countriesDirectory[cc]).resize((64, 42), Image.ANTIALIAS))
            selection_Canvas.configure(bg="gray24", highlightbackground="gray24")
            selection_Canvas.itemconfigure(baseSelection, image=selectionPicture)

            #When the selected country has been displayed for user confirmation in bottom right corner. Enable the button allow them to proceed to next view (GUI).
            nextButton.configure(state=NORMAL)
            
            return countryCode.get(country.get())

        #We will be handling unexpected user exits from the application.
        #To limit error messages, if user quits randomly instead of printing an error, just print ('APPLICATION HAS BEEN CLOSED!')
        except (TypeError, RuntimeError) as E:
            print("[APPLICAITON HAS BEEN CLOSED!]")

    #Method invoked upon ['NEXT'] button press. This method passes the selected country/worldwide selection as an integer to another python file to handle the data displayal. 
    def nextGUI():
        #Pass the country code to the displayData.py's display(countryCode) method to inititate the display of data.
        displayData.display(cc)

        
        
    #Create reference of home window. 
    root = Tk()

    #Countries = keys, Values = Country codes.
    #We will pass countries as integers between GUI's, instead of Strings.
    countryCode = {"UNITED STATES OF AMERICA": 0,
                   "CANADA": 1,
                   "FRANCE" : 2,
                   "UNITED KINGDOM" : 3,
                   "SPAIN" : 4,
                   "ITALY" : 5,
                   "WORLDWIDE" : 6}

    #Draw: ['Select Country'] label.
    label1 = Label(root, text="SELECT COUNTRY:", bg="light yellow", fg="gray24", font=("Courier", 20, "bold"))
    label1.place(x=37, y=148)

    #Draw: ['Worldwide:'] label.
    label2 = Label(root, text="Worldwide:", bg="light yellow", fg="gray24", font=("Courier", 20, "bold"))
    label2.place(x=37, y=348)

    #Draw box containing selection of countries. 
    countries_Canvas = Canvas(root, width=720, height=140, bg="gray28")
    countries_Canvas.place(x=37, y=170)

    #Draw box containing wordwide radio button. 
    worldwide_Canvas = Canvas(root, width=300, height=80, bg="gray28")
    worldwide_Canvas.place(x=37, y=370)

    #List containing folder references to countries flags.
    countriesDirectory = ['Flags/USA.png','Flags/CANADA.png','Flags/FRANCE.png','Flags/UK.png','Flags/SPAIN.png','Flags/ITALY.png', 'Flags/EARTH.png']

    #Insert flags/countries into canvas as images.
    usaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[0]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(70,48, anchor=CENTER, image=usaFlag)

    canadaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[1]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(70,110, anchor=CENTER, image=canadaFlag)

    franceFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[2]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(304,48, anchor=CENTER, image=franceFlag)

    ukFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[3]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(304,110, anchor=CENTER, image=ukFlag)

    spainFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[4]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(550,48, anchor=CENTER, image=spainFlag)

    italyFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[5]).resize((80, 40), Image.ANTIALIAS))
    countries_Canvas.create_image(550,110, anchor=CENTER, image=italyFlag)

    #Insert earth picture into worldwide canvas as image.
    earthPicture = ImageTk.PhotoImage(Image.open(countriesDirectory[6]).resize((64, 64), Image.ANTIALIAS))
    worldwide_Canvas.create_image(54,44, anchor=CENTER, image=earthPicture)

    #String variable to hold the selected country.
    country = StringVar()

    #Insert radio buttons to the right of country flags.
    R1 = Radiobutton(root, text="USA", value="UNITED STATES OF AMERICA", var=country, font=("Courier", 20, "bold"))
    R1.place(x=160, y=202)

    R2 = Radiobutton(root, text="CANADA", value="CANADA", var=country, font=("Courier", 20, "bold"))
    R2.place(x=160, y=266)

    R3 = Radiobutton(root, text="FRANCE", value="FRANCE", var=country, font=("Courier", 20, "bold"))
    R3.place(x=395, y=202)

    R4 = Radiobutton(root, text="UK", value="UNITED KINGDOM", var=country, font=("Courier", 20, "bold"))
    R4.place(x=395, y=266)

    R5 = Radiobutton(root, text="SPAIN", value="SPAIN", var=country, font=("Courier", 20, "bold"))
    R5.place(x=640, y=202)

    R6 = Radiobutton(root, text="ITALY", value="ITALY", var=country, font=("Courier", 20, "bold"))
    R6.place(x=640, y=266)

    #Insert radio button to the right of the earth logo. 
    R7 = Radiobutton(root, text="WORLDWIDE", value="WORLDWIDE", var=country, font=("Courier", 20, "bold"))
    R7.place(x=130, y=400)

    #Draw ['Next'] Button.
    #Disable the button until a valid radiobutton has been selected.
    nextButton = Button(root, text="Next", width=8, height=2, fg="slate blue", font=("Courier", 20, "bold"), highlightbackground='pink', state=DISABLED, command=nextGUI)
    nextButton.place(x=654, y=430)
    
    #Displays the selected country; Via the RadioButton.
    country.trace('w', selected_Country)

    #Draw invisible box that will be used to show user's radio button selection.
    #Initially it will be invisible, but set to visible upon radiobutton selection.
    selection_Canvas = Canvas(root, width=100, height=50, bg="medium slate blue", highlightbackground="medium slate blue")
    baseSelection = selection_Canvas.create_image((52,28), image=None, anchor=CENTER)
    selection_Canvas.place(x=654, y=360)

    #Window's attributes. (Size, title, other characteristics etc.)
    root.title("PYTHON COVID-19 DATA TRACKER")
    root.geometry("800x500")
    root.resizable(False, False)
    root.configure(bg="medium slate blue")
    root.mainloop()
    selected_Country()

#For testing purposes, we will launch directly into the selection page. (We will implement the welcome screen last.)
#The Welcome screen will call the selection_GUI() method.
selection_GUI()
