# This python file displays the data for the selected radio button country/worldWide value.

import tkinter as tk
from PIL import Image, ImageTk

# Python file containing all the methods for data manipulation/fetching/parsing, etc.
import APIInterpreter as interpreter

# Matplotlib library will be utilized to display the graph trend of COVID-19 statistics for selected country.
import matplotlib.pyplot as plt
from matplotlib import style

# Suppressing a matplotlib warning during runtime. Not a critical warning, just a suggestion.
import warnings
warnings.filterwarnings("ignore")


# Method displays the confirmed, deaths, recovered cases for the selected country; Display additional features too.
def display(countryCode):

    # Display the selected country, and populate the displayValues dictionary with the statistics.
    print("Selected: " + countryCode)
    displayValues = interpreter.getCases(country=countryCode)
    print("[Fetch Complete]")

    # Grab the respective stats from the dictionary that are of interest to us.
    # Store them into variables, they will be displayed in the tkinter window.
    global confirmed, deaths, recovered, active
    confirmed = displayValues['Confirmed']
    deaths = displayValues['Deaths']
    recovered = displayValues['Recovered']
    active = displayValues['Active']

    # Minor formatting to the country names when displaying in title of GUI.
    convCountryName = {'united-states': "U.S.A",
                       'canada': 'CANADA',
                       'united-kingdom': 'UNITED KINGDOM',
                       'france': 'FRANCE',
                       'spain': 'SPAIN',
                       'italy': 'ITALY'}

    # Create GUI to display above information.
    def display_GUI():
        master = tk.Toplevel()

        # Background for widgets in GUI window.
        countryBG = "gray28"

        # Image url for the selected countries' flag.
        imgUrl = "Flags/" + countryCode + ".png"

        # Draw the clicked countries' flag and name into its own frame.
        frame = tk.Frame(master, background=countryBG, padx=30, pady=16)
        flag = ImageTk.PhotoImage(Image.open(imgUrl).resize((80, 40), Image.ANTIALIAS))
        label = tk.Label(frame, image=flag, background=countryBG)
        label.pack()
        label1 = tk.Label(frame, text=convCountryName.get(countryCode),
                          background=countryBG, font=("Courier", 26, "bold"))
        label1.config(fg='mint cream')
        label1.pack()
        frame.pack(fill='x', padx=30, pady=(20, 30))

        # Display the confirmed number of cases in its own frame.
        frame2 = tk.Frame(master, background=countryBG, padx=30, pady=16)
        confirmedLabel = tk.Label(frame2, text="Confirmed Cases: " + str(format(confirmed, ",d")),
                                  background=countryBG, font=("Courier", 24, "bold"))
        confirmedLabel.config(fg='mint cream')
        confirmedLabel.pack()
        frame2.pack(fill='x', padx=30, pady=10)

        # Display the recovered number of cases in its own frame.
        frame3 = tk.Frame(master, background=countryBG, padx=30, pady=16)

        recoveredLabel = tk.Label(frame3, text="",
                                  background=countryBG, font=("Courier", 24, "bold"), fg='mint cream')

        # The API was having trouble fetching recovered information for some countries.
        # So if the issue does occur that recovered Cases = 0, we will just display something else.
        if recovered != 0:
            recoveredLabel.config(text="Recovered Cases: " + str(format(recovered, ",d")))

        else:
            recoveredLabel.config(text="Recovered Cases: " + "N/A")

        recoveredLabel.pack()
        frame3.pack(fill='x', padx=30, pady=5)

        recoveredLabel.config(fg='mint cream')
        recoveredLabel.pack()
        frame3.pack(fill='x', padx=30, pady=5)

        # Display the death number in its own frame.
        frame4 = tk.Frame(master, background=countryBG, padx=30, pady=16)
        deathLabel = tk.Label(frame4, text="Death count: " + str(format(deaths, ",d")),
                              background=countryBG, font=("Courier", 24, "bold"))
        deathLabel.config(fg='mint cream')
        deathLabel.pack()
        frame4.pack(fill='x', padx=30, pady=5)

        # Draw button to direct user to a graph trend of the selected country's COVID cases.
        graphButton = tk.Button(master, text="Display Graph", height=2, fg="slate blue", font=("Courier", 20, "bold"),
                                highlightbackground='pink', command=display_Graph)
        graphButton.pack(fill='x', padx=30, pady=10)

        # Draw button to direct user to a graph trend of the selected country's COVID cases.
        newsButton = tk.Button(master, text="News", height=2, fg="slate blue", font=("Courier", 20, "bold"),
                                highlightbackground='pink', command=display_Graph)
        newsButton.pack(fill='x', padx=30, pady=10)

        # GUI's attributes.
        master.resizable(False, False)
        master.configure(background="ivory2")
        master.geometry("600x600")
        master.title(convCountryName.get(countryCode) + " | COVID-19 TRACKER")
        master.mainloop()

    # Method displays the graph trend for the specific country.
    def display_Graph():

        # Return the data for the specific country, up until the present date.
        data = interpreter.getCasesList(country=countryCode)

        # Theme for the plot.
        style.use('bmh')

        # List to hold all the dates from April 13th-Present.
        dates = []

        # List to hold all the death count from the dates from April 13th-Present.
        deathCount = []

        # List to hold all the confirmed cases count from the dates from April 13-Present.
        confirmedCount = []

        # List to hold all the recovered cases count from the dates from April 13th-Present.
        recoveredCount = []

        # List to hold all the active cases count from the dates from April 13th-Present.
        activeCount = []

        # Iterate through the fetched data, and populate the individual lists.
        for item in data:
            dates.append(item['date'])
            deathCount.append(item['cases']['Deaths'])
            confirmedCount.append(item['cases']['Confirmed'])
            recoveredCount.append(item['cases']['Recovered'])
            activeCount.append(item['cases']['Active'])

        # Dictionary used to convert date format from yyyy-mm-dd, month/dd.
        monthConv = {1: 'Jan', 2: 'Feb',
                     3: 'Mar', 4: 'Apr',
                     5: 'May', 6: 'Jun',
                     7: 'Jul', 8: 'Aug',
                     9: 'Sep', 10: 'Oct',
                     11: 'Nov', 12: 'Dec'}

        # List containing the dates in the format we want them in to show on the graph.
        formatedDates = []
        for date in dates:
            formatedDates.append(monthConv.get(int(date[5:7])) + "/" + date[8:10] + "\n" + date[0:4])

        # Plot lists onto graph.
        plt.plot(formatedDates, confirmedCount, label='Confirmed Cases', color='b', marker='.')

        if recovered != 0:
            plt.plot(formatedDates, recoveredCount, label='Recoveries', color='g', marker='.')

        plt.plot(formatedDates, activeCount, label='Active Cases', color='k', marker='.')
        plt.plot(formatedDates, deathCount, label='Deaths', color='r', marker='.')

        ax = plt.axes()

        # Display the x,y title labels for the graph.
        plt.xlabel('Dates')

        # Change the scale of the y axis depending on the confirmed case total.
        if confirmed > 1000000:
            plt.ylabel('#Cases (million)')

        else:
            plt.ylabel('# Cases')

        plt.title('COVID-19 TREND')
        plt.legend()

        # Sets the spacing for the xlabel ticks. (To prevent overlapping of xlabels on graph. )
        ax.xaxis.set_major_locator(plt.MultipleLocator(30))

        def onclick(event):
            print(event.xdata, event.ydata)

        # Change title for matplotlib window.
        fig = plt.gcf()
        fig.canvas.set_window_title(convCountryName.get(countryCode) + ' | COVID-19 TRACKER')


        plt.show()

    display_GUI()
