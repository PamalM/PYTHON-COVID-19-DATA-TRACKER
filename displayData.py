# This (.py) handles the display of data.
# We will make the API request and fetch information as needed, if it is out of date.
# When user makes a selection on the main.py, they are directed to this script upon the ['Next'] button click.
# The statistics will be displayed, and stored in a JSON folder locally for the user to access if they wish.

from tkinter import *

from PIL import Image, ImageTk
import APIInterpreter as interpreter
import matplotlib.pyplot as plt

def display(countryCode):

    # Display the selected country, and populate the displayValues dictionary with the statistics.
    print("Selected: " + countryCode)
    displayValues = interpreter.getCases(countryCode)
    print("[Fetch Complete]")

    # Grab the respective stats from the dictionary that are of interest to us.
    # Store them into variables, they will be displayed in the tkinter window.
    global confirmed, deaths, recovered, active
    confirmed = displayValues['confirmed']
    deaths = displayValues['deaths']
    recovered = displayValues['recovered']
    active = displayValues['active']

    #Dictionary to convert countrySlug values into pretty string format.
    convCountryName = {'united-states': "U.S.A",
                       'canada': 'CANADA',
                       'united-kingdom': 'UNITED KINGDOM',
                       'france': 'FRANCE',
                       'spain': 'SPAIN',
                       'italy': 'ITALY'}

    #Creates a GUI to display statistics for today's COVID-19 cases.
    def display_GUI():
        master = Toplevel()

        # Background for widgets in window.
        countryBG = "gray28"

        # Image url for the countries' flag.
        imgUrl = "Flags/" + countryCode + ".png"

        # Frame to hold widgets and buttons within the window.
        frame = Frame(master, background=countryBG, padx=30, pady=16)

        #  Draw the clicked countries' flag into window.
        flag = ImageTk.PhotoImage(Image.open(imgUrl).resize((80, 40), Image.ANTIALIAS))
        label = Label(frame, image=flag, background=countryBG)
        label.pack()

        # Draw countries name next to flag.
        label1 = Label(frame, text=convCountryName.get(countryCode),
                       background=countryBG, font=("Courier", 26, "bold"))
        label1.config(fg='mint cream')
        label1.pack()

        frame.pack(fill='x', padx=30, pady=(20, 30))

        # Frame to display COVID-19 statistics.
        frame2 = Frame(master, background=countryBG, padx=30, pady=16)

        confirmedLabel = Label(frame2, text="Confirmed Cases: " + str(format(confirmed, ",d")),
                       background=countryBG, font=("Courier", 24, "bold"))
        confirmedLabel.config(fg='mint cream')
        confirmedLabel.pack()

        frame2.pack(fill='x', padx=30, pady=10)

        frame3 = Frame(master, background=countryBG, padx=30, pady=16)

        recoveredLabel = Label(frame3, text="Recovered Cases: " + str(format(recovered, ",d")),
                               background=countryBG, font=("Courier", 24, "bold"))
        recoveredLabel.config(fg='mint cream')
        recoveredLabel.pack()

        frame3.pack(fill='x', padx=30, pady=5)

        frame4 = Frame(master, background=countryBG, padx=30, pady=16)

        deathLabel = Label(frame4, text="Death count: " + str(format(deaths, ",d")),
                               background=countryBG, font=("Courier", 24, "bold"))
        deathLabel.config(fg='mint cream')
        deathLabel.pack()

        frame4.pack(fill='x', padx=30, pady=5)

        #Button directs user to the matplotlib graph trend.
        graphButton = Button(master, text="Display Graph", height=2, fg="slate blue", font=("Courier", 20, "bold"),
                            highlightbackground='pink', command=display_Graph)
        graphButton.pack(fill='x', padx=30, pady=10)

        # Window's attributes.
        master.resizable(False, False)
        master.configure(background="ivory2")
        master.geometry("600x600")
        master.title(convCountryName.get(countryCode) + " COVID-19 STATISTICS")
        master.mainloop()


    #Method displays the graph trend for the specific country.
    def display_Graph():

        # Return the data for the specific country from April 13th - Present.
        data = interpreter.getCasesList(countryCode)

        # List to hold all the dates from April 13th-Present.
        dates = []

        # List to hold all the death count from the dates from April 13th-Present.
        deathCount = []

        #List to hold all the confirmed cases count from the dates from April 13-Present.
        confirmedCount = []

        #List to hold all the recovered cases count from the dates from April 13th-Present.
        recoveredCount = []

        # List to hold all the active cases count from the dates from April 13th-Present.
        activeCount = []

        for item in data:
            dates.append(item['date'])
            deathCount.append(item['cases']['deaths'])
            confirmedCount.append(item['cases']['confirmed'])
            recoveredCount.append(item['cases']['recovered'])
            activeCount.append(item['cases']['active'])


        for index in dates, deathCount, confirmedCount, recoveredCount, activeCount:
            print(index)


        plt.plot(dates, deathCount)
        plt.show()


    display_GUI()
