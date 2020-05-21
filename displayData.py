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


# Method displays the current confirmed, recovered, death count for a specific country, or worldwide.
def display(countryCode, worldwide):

    # Display selected country slug to terminal.
    print("Selected: " + countryCode.upper())

    # Fetch data from appropriate API depending on selection.
    if worldwide is True:
        displayValues = interpreter.getCases(worldwide=True)

    else:
        displayValues = interpreter.getCases(country=countryCode)

    print("[Fetch Complete]\n")

    # Store the fetched data into dictionaries for us to utilize.
    confirmed = displayValues['Confirmed']
    deaths = displayValues['Deaths']
    recovered = displayValues['Recovered']
    active = displayValues['Active']

    # Method displays the graph trend for the specific country/worldwide.
    def display_Graph():

        # Get data depending on the radio button selection.
        # Worldwide is selected, fetch data for the world, else get specific country data.
        if worldwide is True:
            data = interpreter.getCasesList(worldwide=True)

        else:
            data = interpreter.getCasesList(country=countryCode)

        # Theme for the graph plot.
        style.use('bmh')

        # List to hold all the dates from today's date to when the API has info available.
        # Create empty lists to hold confirmed, deaths, recovered, active cases for each date.
        dates, deathCount, confirmedCount, recoveredCount, activeCount = [], [], [], [], []

        # Iterate through the fetched data, and populate the lists above.
        for item in data:
            dates.append(item['date'])
            deathCount.append(item['cases']['Deaths'])
            confirmedCount.append(item['cases']['Confirmed'])
            recoveredCount.append(item['cases']['Recovered'])
            activeCount.append(item['cases']['Active'])

        # Dictionary used to format Dates into human-readable format.
        month_Conversion = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
                            5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
                            9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

        # List containing the dates in the format we want them in to show on the graph.
        formattedDates = []
        for date in dates:
            formattedDates.append(month_Conversion.get(int(date[5:7])) + "/" + date[8:10] + "/" + date[0:4])

        # Plot above list onto graph.
        plt.plot(formattedDates, confirmedCount, label='Confirmed Cases', color='b', marker='.')
        plt.plot(formattedDates, recoveredCount, label='Recoveries', color='g', marker='.')
        plt.plot(formattedDates, activeCount, label='Active Cases', color='k', marker='.')
        plt.plot(formattedDates, deathCount, label='Deaths', color='r', marker='.')

        # Create ref. for graph axis.
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

        # Change title for matplotlib window.
        fig = plt.gcf()

        if worldwide is True:
            fig.canvas.set_window_title('WORLDWIDE | COVID-19 TRACKER')

        else:
            fig.canvas.set_window_title(countryCode.upper() + ' | COVID-19 TRACKER')

        plt.show()

    # Create Graphical Window to display realtime statistics for country/worldwide selection.
    master = tk.Toplevel()

    # Background/foreground color for GUI window.
    widgetBG = "gray28"
    widgetFG = "mint cream"

    # Frame to hold country/worldwide image/flag.
    frame = tk.Frame(master, background=widgetBG, padx=30, pady=16)

    # Change title of window, and image url for country depending on arguments passed (Selection).
    # Some aspects of the window such as title, imageURl need to be changed depending on radio button selection.
    if worldwide is True:
        imgUrl = "Flags/EARTH.png"
        master.title("WORLDWIDE | COVID-19 TRACKER")
        flag = ImageTk.PhotoImage(Image.open("Flags/EARTH.png").resize((80, 60), Image.ANTIALIAS))

    else:
        imgUrl = "Flags/" + countryCode + ".png"
        master.title(countryCode.upper() + " | COVID-19 TRACKER")
        flag = ImageTk.PhotoImage(Image.open(imgUrl).resize((80, 40), Image.ANTIALIAS))

    # Label to hold country/worldwide flag into frame.
    flagLabel = tk.Label(frame, image=flag, background=widgetBG)
    flagLabel.pack()

    # Label writes country name/worldwide text under the image above in frame.
    countryText = tk.Label(frame, text=countryCode.upper(), background=widgetBG, font=("Courier", 26, "bold"))
    countryText.config(fg=widgetFG)
    countryText.pack()
    frame.pack(fill='x', padx=30, pady=(20, 30))

    # Frame displays the confirmed number of cases.
    confirmedFrame = tk.Frame(master, background=widgetBG, padx=30, pady=16)
    confirmedLabel = tk.Label(confirmedFrame, background=widgetBG, font=("Courier", 24, "bold"))
    confirmedLabel.config(text="Confirmed Cases: " + str(format(confirmed, ",d")), fg=widgetFG)
    confirmedLabel.pack()
    confirmedFrame.pack(fill='x', padx=30, pady=10)

    # Frame displays the recovered number of cases.
    recoveredFrame = tk.Frame(master, background=widgetBG, padx=30, pady=16)
    recoveredLabel = tk.Label(recoveredFrame, background=widgetBG, font=("Courier", 24, "bold"))
    recoveredLabel.config(text="Recovered Cases: " + str(format(recovered, ",d")), fg=widgetFG)
    recoveredLabel.pack()
    recoveredFrame.pack(fill='x', padx=30, pady=5)

    # Frame displays the Death number of cases.
    deathFrame = tk.Frame(master, background=widgetBG, padx=30, pady=16)
    deathLabel = tk.Label(deathFrame, background=widgetBG, font=("Courier", 24, "bold"))
    deathLabel.config(text="Deaths: " + str(format(deaths, ",d")), fg=widgetFG)
    deathLabel.pack()
    deathFrame.pack(fill='x', padx=30, pady=5)

    # Button directs user to a graphical trend of the COVID-19 statistics; Particular to that radio button selection.
    graphButton = tk.Button(master, text="Display Graph", height=2, fg="slate blue", font=("Courier", 20, "bold"))
    graphButton.config(highlightbackground='pink', command=lambda:display_Graph())
    graphButton.pack(fill='x', padx=30, pady=10)

    # Display a button to show individual state/province data for countries; Don't show button if worldwide is selected.
    if worldwide is False:
        stateButton = tk.Button(master, text="State/Province Data", height=2, fg="slate blue")
        stateButton.config(highlightbackground='pink', command=lambda:print('state Button'), font=("Courier", 20, "bold"))
        stateButton.pack(fill='x', padx=30, pady=10)

    # Draw button to direct user to a graph trend of the selected country/worldwide COVID cases.
    newsButton = tk.Button(master, text="News", height=2, fg="slate blue", font=("Courier", 20, "bold"))
    newsButton.config(highlightbackground='pink', command=lambda:print('News Button'))
    newsButton.pack(fill='x', padx=30, pady=10)

    # GUI's attributes.
    master.resizable(False, False)
    master.configure(background="ivory2")
    master.geometry("600x600")
    master.mainloop()
