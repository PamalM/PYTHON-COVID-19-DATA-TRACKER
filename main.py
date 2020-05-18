# This is the main python file. Run this (.py) to execute the program.

# Tkinter library will be utilized to create the Graphical User Interface (GUI).
import tkinter as tk

# PIL library will be utilized for image processing within the GUI.
from PIL import Image, ImageTk

# After selection is made in main.py, the selection is passed to displayData.py
import displayData


# GUI presents selections to user.
def selection_GUI():

    # Tracks and saves the selected country, and updates the stringvar().
    def monitorCountry(*_):
        # Enable next button state to allow user to proceed to next GUI.
        nextButton.configure(state=tk.NORMAL)
        return country.get()

    # After selection is made, direct user to next GUI with next button press.
    def nextGUI():
        if country.get() == "WORLDWIDE":
            displayData.display_World()

        else:
            displayData.display_Country(country.get())

    # Create tkinter GUI Window object.
    root = tk.Tk()

    # Background for frames containing list of countries, and worldwide selections.
    countryBG = "gray28"

    # String variable used hold the selected radio button's value. (countryCode)
    # This variable is passed through the various files in the application. We wil pass this to displayData.display()
    # This allows other GUIs/methods used throughout the application to display data relevant to the selected country.
    country = tk.StringVar()

    # Label at the top. ['Select A Country:']
    label1 = tk.Label(root, text="SELECT A COUNTRY:", bg="gray30", fg="light yellow", font=("Courier", 20, "bold"))
    label1.pack(pady=(20, 2))

    # Frame containing all the selection of countries to pick from, and their respective images.
    countries_Frame = tk.Frame(root, background=countryBG, padx=30, pady=16)

    # Draw United States Flag.
    usaFlag = ImageTk.PhotoImage(Image.open('Flags/united-states.png').resize((80, 40), Image.ANTIALIAS))
    usaLabel = tk.Label(countries_Frame, image=usaFlag, background=countryBG)
    usaLabel.grid(row=1, column=0, sticky=tk.W + tk.E)

    # Draw United States radio button.
    r1 = tk.Radiobutton(countries_Frame, text="USA", value="united-states", var=country, font=("Courier", 20, "bold"))
    r1.grid(row=1, column=1, sticky=tk.W + tk.E)

    # Draw Canada Flag.
    canadaFlag = ImageTk.PhotoImage(Image.open('Flags/canada.png').resize((80, 40), Image.ANTIALIAS))
    canadaLabel = tk.Label(countries_Frame, image=canadaFlag, background=countryBG)
    canadaLabel.grid(row=2, column=0, sticky=tk.W + tk.E)

    # Draw Canada radio button.
    r2 = tk.Radiobutton(countries_Frame, text="CANADA", value="canada", var=country, font=("Courier", 20, "bold"))
    r2.grid(row=2, column=1, sticky=tk.W + tk.E)

    # Draw france Flag.
    franceFlag = ImageTk.PhotoImage(Image.open('Flags/france.png').resize((80, 40), Image.ANTIALIAS))
    franceLabel = tk.Label(countries_Frame, image=franceFlag, background=countryBG)
    franceLabel.grid(row=1, column=2, sticky=tk.W + tk.E)

    # Draw France radio button.
    r3 = tk.Radiobutton(countries_Frame, text="FRANCE", value="france", var=country, font=("Courier", 20, "bold"))
    r3.grid(row=1, column=3, sticky=tk.W + tk.E)

    # Draw United Kingdom Flag.
    ukFlag = ImageTk.PhotoImage(Image.open('Flags/united-kingdom.png').resize((80, 40), Image.ANTIALIAS))
    ukLabel = tk.Label(countries_Frame, image=ukFlag, background=countryBG)
    ukLabel.grid(row=2, column=2, sticky=tk.W + tk.E)

    # Draw United Kingdom radio button.
    r4 = tk.Radiobutton(countries_Frame, text="U.K", value="united-kingdom", var=country, font=("Courier", 20, "bold"))
    r4.grid(row=2, column=3, sticky=tk.W + tk.E)

    # Draw Spain Flag.
    spainFlag = ImageTk.PhotoImage(Image.open('Flags/spain.png').resize((80, 40), Image.ANTIALIAS))
    spainLabel = tk.Label(countries_Frame, image=spainFlag, background=countryBG)
    spainLabel.grid(row=1, column=4, sticky=tk.W + tk.E)

    # Draw Spain radio button.
    r5 = tk.Radiobutton(countries_Frame, text="SPAIN", value="spain", var=country, font=("Courier", 20, "bold"))
    r5.grid(row=1, column=5, sticky=tk.W + tk.E)

    # Draw Italy Flag.
    italyFlag = ImageTk.PhotoImage(Image.open('Flags/italy.png').resize((80, 40), Image.ANTIALIAS))
    italyLabel = tk.Label(countries_Frame, image=italyFlag, background=countryBG)
    italyLabel.grid(row=2, column=4, sticky=tk.W + tk.E)

    # Draw Italy radio button.
    r6 = tk.Radiobutton(countries_Frame, text="ITALY", value="italy", var=country, font=("Courier", 20, "bold"))
    r6.grid(row=2, column=5, sticky=tk.W + tk.E)

    # Draw Next Button; Button directs user to the next GUI upon valid selection.
    nextButton = tk.Button(root, text="Next", width=10, height=2, fg="slate blue", font=("Courier", 20, "bold"),
                           highlightbackground='pink', state=tk.DISABLED, command=nextGUI)

    # Draw the frame containing the list of countries.
    # Provided proper padding, and equal column distribution to ensure equal spacing.
    countries_Frame.columnconfigure(0, weight=1)
    countries_Frame.columnconfigure(1, weight=1)
    countries_Frame.columnconfigure(2, weight=1)
    countries_Frame.columnconfigure(3, weight=1)
    countries_Frame.columnconfigure(4, weight=1)
    countries_Frame.columnconfigure(5, weight=1)
    countries_Frame.pack(fill='x', padx=30)

    # Label in the middle. ['Or, Select Worldwide:']
    label2 = tk.Label(root, text="OR, SELECT WORLDWIDE:", bg="gray30", fg="light yellow", font=("Courier", 20, "bold"))
    label2.pack(pady=(20, 2))

    # Frame containing the worldWide radio button and flag.
    worldwide_Frame = tk.Frame(root, background=countryBG, padx=30, pady=16)

    # Draw Worldwide Flag (Image).
    worldFlag = ImageTk.PhotoImage(Image.open('Flags/Earth.png').resize((76, 76), Image.ANTIALIAS))
    worldLabel = tk.Label(worldwide_Frame, image=worldFlag, background=countryBG)
    worldLabel.grid(row=0)

    # Draw Worldwide radio button.
    r7 = tk.Radiobutton(worldwide_Frame, text="WORLDWIDE", value="WORLDWIDE", var=country, font=("Courier", 20, "bold"))
    r7.grid(row=1, column=0)

    # Display worldwide Frame container.
    worldwide_Frame.rowconfigure(0, weight=1)
    worldwide_Frame.columnconfigure(0, weight=1)
    worldwide_Frame.pack(fill='x', padx=30)

    # Display the next button.
    nextButton.pack(fill='x', padx=120, pady=(10, 0))

    # Monitors when a valid radio button selection is made; Thus enabling the next button.
    country.trace("w", monitorCountry)

    # GUI attributes; (Window size, bg color, title, etc.)
    root.resizable(False, False)
    root.geometry("800x500")
    root.configure(background="ivory2")
    root.title("COVID-19 TRACKER")
    root.mainloop()


# Launch the selection GUI; Execute application.
selection_GUI()
