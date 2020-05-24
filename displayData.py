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

# Background/foreground color for GUI window.
widgetBG = "gray28"
widgetFG = "mint cream"

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

    def display_Provinces():

        def monitor_Province(*_):
            graph_Button.configure(state=tk.NORMAL)
            return province.get()

        provinceFG = 'lightgoldenrod'

        alpha = tk.Tk()

        # String variable to detect the selected province's radio button.
        province = tk.StringVar(alpha)

        # Set the default selected option to Alberta on display.
        province.set('Alberta')

        label1 = tk.Label(alpha, text="SELECT A PROVINCE:", bg="gray30", fg="light yellow",
                          font=("Courier", 24, "bold"))
        label1.grid(row=1, column=0, columnspan=2, pady=(20, 8))

        # Frame each province's stats.
        frame1 = tk.Frame(alpha, background=widgetBG, padx=18, pady=16)

        AB = interpreter.getCases(province='Alberta')
        r1 = tk.Radiobutton(frame1, variable=province, text='Alberta', value='Alberta',
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r1.grid(row=0, column=0)
        AB_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        AB_Confirmed.config(text="Confirmed Cases: " + str(format(AB['Confirmed'], ",d")), fg=widgetFG)
        AB_Confirmed.grid(row=1, column=0)
        AB_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        AB_Recovered.config(text="Recovered Cases: " + str(format(AB['Recovered'], ",d")), fg=widgetFG)
        AB_Recovered.grid(row=2, column=0)
        AB_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        AB_Death.config(text="Deaths: " + str(format(AB['Deaths'], ",d")), fg=widgetFG)
        AB_Death.grid(row=3, column=0)

        NS = interpreter.getCases(province='Nova Scotia')
        r2 = tk.Radiobutton(frame1, text='Nova Scotia',value="Nova Scotia", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r2.grid(row=4, column=0, padx=30, pady=(20,0))
        NS_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Confirmed.config(text="Confirmed Cases: " + str(format(NS['Confirmed'], ",d")), fg=widgetFG)
        NS_Confirmed.grid(row=5, column=0)
        NS_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Recovered.config(text="Recovered Cases: " + str(format(NS['Recovered'], ",d")), fg=widgetFG)
        NS_Recovered.grid(row=6, column=0)
        NS_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Death.config(text="Deaths: " + str(format(NS['Deaths'], ",d")), fg=widgetFG)
        NS_Death.grid(row=7, column=0)

        BC = interpreter.getCases(province='British Columbia')
        r4 = tk.Radiobutton(frame1, text='British Columbia', value="British Columbia", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r4.grid(row=8, column=0, pady=(20,0))
        BC_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Confirmed.config(text="Confirmed Cases: " + str(format(BC['Confirmed'], ",d")), fg=widgetFG)
        BC_Confirmed.grid(row=9, column=0)
        BC_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Recovered.config(text="Recovered Cases: " + str(format(BC['Recovered'], ",d")), fg=widgetFG)
        BC_Recovered.grid(row=10, column=0)
        BC_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Death.config(text="Deaths: " + str(format(BC['Deaths'], ",d")), fg=widgetFG)
        BC_Death.grid(row=11, column=0)

        NT = interpreter.getCases(province='Northwest Territories')
        r5 = tk.Radiobutton(frame1, text="Northwest Territories", value="Northwest Territories", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r5.grid(row=0, column=1)
        NT_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Confirmed.config(text="Confirmed Cases: " + str(format(NT['Confirmed'], ",d")), fg=widgetFG)
        NT_Confirmed.grid(row=1, column=1)
        NT_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Recovered.config(text="Recovered Cases: " + str(format(NT['Recovered'], ",d")), fg=widgetFG)
        NT_Recovered.grid(row=2, column=1)
        NT_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Death.config(text="Deaths: " + str(format(NT['Deaths'], ",d")), fg=widgetFG)
        NT_Death.grid(row=3, column=1)

        NL = interpreter.getCases(province='Newfoundland and Labrador')
        r8 = tk.Radiobutton(frame1, text='Newfoundland and Labrador', value="Newfoundland and Labrador", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r8.grid(row=4, column=1, padx=30, pady=(20,0))
        NL_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Confirmed.config(text="Confirmed Cases: " + str(format(NL['Confirmed'], ",d")), fg=widgetFG)
        NL_Confirmed.grid(row=5, column=1)
        NL_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Recovered.config(text="Recovered Cases: " + str(format(NL['Recovered'], ",d")), fg=widgetFG)
        NL_Recovered.grid(row=6, column=1)
        NL_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Death.config(text="Deaths: " + str(format(NL['Deaths'], ",d")), fg=widgetFG)
        NL_Death.grid(row=7, column=1)

        PE = interpreter.getCases(province='Prince Edward Island')
        r3 = tk.Radiobutton(frame1, text='Prince Edward Island', value="Prince Edward Island", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r3.grid(row=8, column=1, pady=(20,0))
        PE_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Confirmed.config(text="Confirmed Cases: " + str(format(PE['Confirmed'], ",d")), fg=widgetFG)
        PE_Confirmed.grid(row=9, column=1)
        PE_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Recovered.config(text="Recovered Cases: " + str(format(PE['Recovered'], ",d")), fg=widgetFG)
        PE_Recovered.grid(row=10, column=1)
        PE_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Death.config(text="Deaths: " + str(format(PE['Deaths'], ",d")), fg=widgetFG)
        PE_Death.grid(row=11, column=1)

        MB = interpreter.getCases(province='Manitoba')
        r7 = tk.Radiobutton(frame1, text='Manitoba', value="Manitoba", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r7.grid(row=0, column=2)
        MB_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Confirmed.config(text="Confirmed Cases: " + str(format(MB['Confirmed'], ",d")), fg=widgetFG)
        MB_Confirmed.grid(row=1, column=2)
        MB_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Recovered.config(text="Recovered Cases: " + str(format(MB['Recovered'], ",d")), fg=widgetFG)
        MB_Recovered.grid(row=2, column=2)
        MB_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Death.config(text="Deaths: " + str(format(MB['Deaths'], ",d")), fg=widgetFG)
        MB_Death.grid(row=3, column=2)

        ON = interpreter.getCases(province='Ontario')
        r11 = tk.Radiobutton(frame1, text='Ontario', value="Ontario", var=province,
                             font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r11.grid(row=4, column=2, padx=60, pady=(20,0))
        ON_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Confirmed.config(text="Confirmed Cases: " + str(format(ON['Confirmed'], ",d")), fg=widgetFG)
        ON_Confirmed.grid(row=5, column=2)
        ON_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Recovered.config(text="Recovered Cases: " + str(format(ON['Recovered'], ",d")), fg=widgetFG)
        ON_Recovered.grid(row=6, column=2)
        ON_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Death.config(text="Deaths: " + str(format(ON['Deaths'], ",d")), fg=widgetFG)
        ON_Death.grid(row=7, column=2)

        SK = interpreter.getCases(province='Saskatchewan')
        r9 = tk.Radiobutton(frame1, text='Saskatchewan', value="Saskatchewan", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r9.grid(row=8, column=2, pady=(20,0))
        SK_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Confirmed.config(text="Confirmed Cases: " + str(format(SK['Confirmed'], ",d")), fg=widgetFG)
        SK_Confirmed.grid(row=9, column=2)
        SK_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Recovered.config(text="Recovered Cases: " + str(format(SK['Recovered'], ",d")), fg=widgetFG)
        SK_Recovered.grid(row=10, column=2)
        SK_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Death.config(text="Deaths: " + str(format(SK['Deaths'], ",d")), fg=widgetFG)
        SK_Death.grid(row=11, column=2)

        NB = interpreter.getCases(province='New Brunswick')
        r10 = tk.Radiobutton(frame1, text='New Brunswick',value="New Brunswick", var=province,
                             font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r10.grid(row=0, column=3)
        NB_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Confirmed.config(text="Confirmed Cases: " + str(format(NB['Confirmed'], ",d")), fg=widgetFG)
        NB_Confirmed.grid(row=1, column=3)
        NB_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Recovered.config(text="Recovered Cases: " + str(format(NB['Recovered'], ",d")), fg=widgetFG)
        NB_Recovered.grid(row=2, column=3)
        NB_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Death.config(text="Deaths: " + str(format(NB['Deaths'], ",d")), fg=widgetFG)
        NB_Death.grid(row=3, column=3)

        YT = interpreter.getCases(province='Yukon')
        r12 = tk.Radiobutton(frame1, text='Yukon',value="Yukon", var=province,
                             font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r12.grid(row=4, column=3, padx=60, pady=(20,0))
        YT_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Confirmed.config(text="Confirmed Cases: " + str(format(YT['Confirmed'], ",d")), fg=widgetFG)
        YT_Confirmed.grid(row=5, column=3)
        YT_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Recovered.config(text="Recovered Cases: " + str(format(YT['Recovered'], ",d")), fg=widgetFG)
        YT_Recovered.grid(row=6, column=3)
        YT_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Death.config(text="Deaths: " + str(format(YT['Deaths'], ",d")), fg=widgetFG)
        YT_Death.grid(row=7, column=3)

        QC = interpreter.getCases(province='Quebec')
        r6 = tk.Radiobutton(frame1, text='Quebec', value="Quebec", var=province,
                            font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r6.grid(row=8, column=3, pady=(20,0))
        QC_Confirmed = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Confirmed.config(text="Confirmed Cases: " + str(format(QC['Confirmed'], ",d")), fg=widgetFG)
        QC_Confirmed.grid(row=9, column=3)
        QC_Recovered = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Recovered.config(text="Recovered Cases: " + str(format(QC['Recovered'], ",d")), fg=widgetFG)
        QC_Recovered.grid(row=10, column=3)
        QC_Death = tk.Label(frame1, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Death.config(text="Deaths: " + str(format(QC['Deaths'], ",d")), fg=widgetFG)
        QC_Death.grid(row=11, column=3)

        frame1.grid(padx=22, pady=16)

        graph_Button = tk.Button(alpha, text="Display Graph", height=2, width=30, fg="slate blue", font=("Courier", 20, "bold"))
        graph_Button.config(highlightbackground='pink', command=lambda: display_Graph(province.get()))
        graph_Button.grid(row=3, column=0, columnspan=3, padx=(200, 200))

        province.trace("w", monitor_Province)

        alpha.title('CANADIAN PROVINCIAL COVID-19 STATISTICS')
        alpha.geometry("940x500")
        alpha.resizable(False, False)
        alpha.configure(background="ivory2")
        alpha.mainloop()

    # Method displays the graph trend for the specific country/worldwide/province.
    def display_Graph(prov):

        # Get data depending on the radio button selection.
        # Worldwide is selected, fetch data for the world, else get specific country data.
        if worldwide is True:
            data = interpreter.getCasesList(worldwide=True)

        elif prov != 0:
            data = interpreter.getCasesList(province=prov)

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

        elif prov != 0:
            fig.canvas.set_window_title(prov + ' | COVID-19 TRACKER')

        else:
            fig.canvas.set_window_title(countryCode.upper() + ' | COVID-19 TRACKER')

        plt.show()

    # Create Graphical Window to display realtime statistics for country/worldwide selection.
    master = tk.Toplevel()

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
    graphButton.config(highlightbackground='pink', command=lambda: display_Graph(0))
    graphButton.pack(fill='x', padx=30, pady=10)

    # Button directs user to provincial COVID-19 data specifically for Canadian provinces.
    if countryCode == 'canada':
        stateButton = tk.Button(master, text="Province Data", height=2, fg="slate blue")
        stateButton.config(highlightbackground='pink', command=lambda: display_Provinces(), font=("Courier", 20, "bold"))
        stateButton.pack(fill='x', padx=30, pady=10)

    # Draw button to direct user to a graph trend of the selected country/worldwide COVID cases.
    newsButton = tk.Button(master, text="News", height=2, fg="slate blue", font=("Courier", 20, "bold"))
    newsButton.config(highlightbackground='pink', command=lambda: print('News Button'))
    newsButton.pack(fill='x', padx=30, pady=10)

    # GUI's attributes.
    master.resizable(False, False)
    master.configure(background="ivory2")
    master.geometry("600x600")
    master.mainloop()
