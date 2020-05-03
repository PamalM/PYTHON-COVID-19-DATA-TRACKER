# Main.py: User must run this file to launch the program. (Base-File)

# Tkinter library will be utilized to create the Graphical User Interface (GUI).
from tkinter import Label, Tk, Canvas, Button, Radiobutton, StringVar, DISABLED, NORMAL, CENTER, Frame, W, E, N, S

# PIL library handles the image processing in this applciation.
from PIL import Image, ImageTk

# Import displayData.py.
# User makes selection in this (.py) for specific country or worldwide data, which is passed onto displayData to display statistics.
import displayData

# Key-Value store used to convert radiobutton selection into integer values to pass onto displayData.py
# Alternatively, we could just assign an integer value to the radiobutton associated to each country,
# But keep a list of values for reference is a better practice for long-term solution.
countryCode = {"UNITED STATES OF AMERICA": 0,
               "CANADA": 1,
               "FRANCE": 2,
               "UNITED KINGDOM": 3,
               "SPAIN": 4,
               "ITALY": 5,
               "WORLDWIDE": 6}

# List containing filepaths for all images of associated country flags.
countriesDirectory = ['Flags/USA.png', 'Flags/CANADA.png', 'Flags/FRANCE.png', 'Flags/UK.png', 'Flags/SPAIN.png',
                      'Flags/ITALY.png', 'Flags/EARTH.png']


# Method will create and present the user with the selection page to select specific country or worldwide data preference.
def selection_GUI():
    # Method displays the selected radio button country/worldwide selection back to the user before entering next view.
    def selected_Country(*_):
        global selectedCountry
        selectedCountry = countryCode.get(country.get())

        # Valid radio button selection has been made, so make button visible. Allow user to proceed to next view.
        nextButton.configure(state=NORMAL)

        # Finally, return back the integer value associated with the country.
        return countryCode.get(country.get())

    def nextGUI():
        # Pass the country code to the displayData.py's display(countryCode) method to inititate the display of data.
        displayData.display(countryCode.get(country.get()))

    # Create tkinter window object.
    root = Tk()

    # Background for countries_Frame box and contents within it.
    countryBG = "gray28"

    # String variable used hold the selected radio button's value. (Country value)
    country = StringVar()

    # This frame will hold all the countries, radiobuttons and images; Think of it as a box.
    countries_Frame = Frame(root, background=countryBG, padx=30, pady=16)

    # Create ['Select A Country:'] label ontop of countries_Frame box.
    label1 = Label(root, text="SELECT A COUNTRY:", bg="gray30", fg="light yellow", font=("Courier", 20, "bold"))

    # Please note that, pady=(ytop, ybottom) paddings.
    # Alternatively, padx=(Left/Right) paddings.
    label1.pack(pady=(20, 2))

    # Insert all [6] country flag images, and the radio buttons associated with each, into the countries_Frame.
    usaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[0]).resize((80, 40), Image.ANTIALIAS))
    usaLabel = Label(countries_Frame, image=usaFlag, background=countryBG)
    usaLabel.grid(row=1, column=0, sticky=W + E)

    R1 = Radiobutton(countries_Frame, text="USA", value="UNITED STATES OF AMERICA", var=country,
                     font=("Courier", 20, "bold"))
    R1.grid(row=1, column=1, sticky=W + E)

    canadaFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[1]).resize((80, 40), Image.ANTIALIAS))
    canadaLabel = Label(countries_Frame, image=canadaFlag, background=countryBG)
    canadaLabel.grid(row=2, column=0, sticky=W + E)

    R2 = Radiobutton(countries_Frame, text="CANADA", value="CANADA", var=country, font=("Courier", 20, "bold"))
    R2.grid(row=2, column=1, sticky=W + E)

    franceFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[2]).resize((80, 40), Image.ANTIALIAS))
    franceLabel = Label(countries_Frame, image=franceFlag, background=countryBG)
    franceLabel.grid(row=1, column=2, sticky=W + E)

    R3 = Radiobutton(countries_Frame, text="FRANCE", value="FRANCE", var=country, font=("Courier", 20, "bold"))
    R3.grid(row=1, column=3, sticky=W + E)

    ukFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[3]).resize((80, 40), Image.ANTIALIAS))
    ukLabel = Label(countries_Frame, image=ukFlag, background=countryBG)
    ukLabel.grid(row=2, column=2, sticky=W + E)

    R4 = Radiobutton(countries_Frame, text="UK", value="UNITED KINGDOM", var=country, font=("Courier", 20, "bold"))
    R4.grid(row=2, column=3, sticky=W + E)

    spainFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[4]).resize((80, 40), Image.ANTIALIAS))
    spainLabel = Label(countries_Frame, image=spainFlag, background=countryBG)
    spainLabel.grid(row=1, column=4, sticky=W + E)

    R5 = Radiobutton(countries_Frame, text="SPAIN", value="SPAIN", var=country, font=("Courier", 20, "bold"))
    R5.grid(row=1, column=5, sticky=W + E)

    italyFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[5]).resize((80, 40), Image.ANTIALIAS))
    italyLabel = Label(countries_Frame, image=italyFlag, background=countryBG)
    italyLabel.grid(row=2, column=4, sticky=W + E)

    R6 = Radiobutton(countries_Frame, text="ITALY", value="ITALY", var=country, font=("Courier", 20, "bold"))
    R6.grid(row=2, column=5, sticky=W + E)

    # Draw ['Next'] button into box.
    # Button will direct user to the displayData script, and pass on the selected country to the file; Disable button until valid radiobutton selection is made.
    nextButton = Button(root, text="Next", width=10, height=2, fg="slate blue", font=("Courier", 20, "bold"),
                        highlightbackground='pink', state=DISABLED, command=nextGUI)

    # Draw the countries frame into window. Give it a padding of 20px, and fill in x direction.
    # Gave all the columns an equal padding size, to ensure equal distribution of space amongst the box frame.
    countries_Frame.columnconfigure(0, weight=1)
    countries_Frame.columnconfigure(1, weight=1)
    countries_Frame.columnconfigure(2, weight=1)
    countries_Frame.columnconfigure(3, weight=1)
    countries_Frame.columnconfigure(4, weight=1)
    countries_Frame.columnconfigure(5, weight=1)
    countries_Frame.pack(fill='x', padx=30)

    # Create ['SELECT WORLDWIDE:'] label ontop of worldwide_Frame box.
    label2 = Label(root, text="OR, SELECT WORLDWIDE:", bg="gray30", fg="light yellow", font=("Courier", 20, "bold"))
    label2.pack(pady=(20, 2))

    # This frame will hold the worldwide radiobutton and image; Think of it as another contianer box.
    worldwide_Frame = Frame(root, background=countryBG, padx=30, pady=16)

    # Insert worldwide image, and radiobutton into worldwide_Frame box container.
    worldFlag = ImageTk.PhotoImage(Image.open(countriesDirectory[6]).resize((76, 76), Image.ANTIALIAS))
    worldLabel = Label(worldwide_Frame, image=worldFlag, background=countryBG)
    worldLabel.grid(row=0)

    R7 = Radiobutton(worldwide_Frame, text="WORLDWIDE", value="WORLDWIDE", var=country, font=("Courier", 20, "bold"))
    R7.grid(row=1, column=0)

    # Draw in the worldwide frame box container.
    worldwide_Frame.rowconfigure(0, weight=1)
    worldwide_Frame.columnconfigure(0, weight=1)
    worldwide_Frame.pack(fill='x', padx=30)

    # Draw the next button in to allow user to proceed to next GUI.
    nextButton.pack(fill='x', padx=120, pady=(10, 0))

    # Window attributes for root; (Window size, bg color, title, etc. characteristics)
    # root.resizable(False, False)
    root.geometry("800x500")
    root.configure(background="ivory2")
    root.title("COVID-19 TRACKER")
    # Displays the selected country; Via the RadioButton.
    country.trace('w', selected_Country)
    root.mainloop()


# Launch the selection GUI.
# For debugging purposes we will launch directly into the selection GUI.
# A welcome screen GUI will reference the selection GUI when the user first launches into the application.
selection_GUI()
