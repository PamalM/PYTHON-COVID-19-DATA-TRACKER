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

        label1 = tk.Label(alpha, text="SELECT A PROVINCE:", bg="gray30", fg="light yellow")
        label1.config(font=("Courier", 24, "bold"))
        label1.pack(pady=10)

        # Frame each province's stats.
        province_Frame = tk.Frame(alpha, background=widgetBG)

        AB = interpreter.getCases(province='Alberta')
        r1 = tk.Radiobutton(province_Frame, variable=province, text='Alberta', value='Alberta')
        r1.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r1.grid(row=0, column=0, sticky='nsew')
        AB_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"), bg="palegreen4")
        AB_Confirmed.config(text="Confirmed Cases: " + str(format(AB['Confirmed'], ",d")), fg=widgetFG)
        AB_Confirmed.grid(row=0, column=1)
        MB_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Active.config(text="Active Cases: " + str(format(AB['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        MB_Active.grid(row=0, column=2)
        AB_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        AB_Recovered.config(text="Recovered Cases: " + str(format(AB['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        AB_Recovered.grid(row=0, column=3)
        AB_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        AB_Death.config(text="Deaths: " + str(format(AB['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        AB_Death.grid(row=0, column=4)

        BC = interpreter.getCases(province='British Columbia')
        r2 = tk.Radiobutton(province_Frame, text='British Columbia', value="British Columbia", var=province)
        r2.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r2.grid(row=1, column=0, sticky='nsew')
        BC_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"), bg="palegreen4")
        BC_Confirmed.config(text="Confirmed Cases: " + str(format(BC['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        BC_Confirmed.grid(row=1, column=1)
        BC_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Active.config(text="Active Cases: " + str(format(BC['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        BC_Active.grid(row=1, column=2)
        BC_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Recovered.config(text="Recovered Cases: " + str(format(BC['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        BC_Recovered.grid(row=1, column=3)
        BC_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        BC_Death.config(text="Deaths: " + str(format(BC['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        BC_Death.grid(row=1, column=4)

        MB = interpreter.getCases(province='Manitoba')
        r3 = tk.Radiobutton(province_Frame, text='Manitoba', value="Manitoba", var=province)
        r3.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r3.grid(row=2, column=0, sticky='nsew')
        MB_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"), bg="palegreen4")
        MB_Confirmed.config(text="Confirmed Cases: " + str(format(MB['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        MB_Confirmed.grid(row=2, column=1)
        MB_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Active.config(text="Active Cases: " + str(format(MB['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        MB_Active.grid(row=2, column=2)
        MB_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Recovered.config(text="Recovered Cases: " + str(format(MB['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        MB_Recovered.grid(row=2, column=3)
        MB_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        MB_Death.config(text="Deaths: " + str(format(MB['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        MB_Death.grid(row=2, column=4)

        NB = interpreter.getCases(province='New Brunswick')
        r4 = tk.Radiobutton(province_Frame, text='New Brunswick',value="New Brunswick", var=province)
        r4.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r4.grid(row=3, column=0, sticky='nsew')
        NB_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Confirmed.config(text="Confirmed Cases: " + str(format(NB['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        NB_Confirmed.grid(row=3, column=1)
        NB_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Active.config(text="Active Cases: " + str(format(NB['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        NB_Active.grid(row=3, column=2)
        NB_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Recovered.config(text="Recovered Cases: " + str(format(NB['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        NB_Recovered.grid(row=3, column=3)
        NB_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NB_Death.config(text="Deaths: " + str(format(NB['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        NB_Death.grid(row=3, column=4)

        NL = interpreter.getCases(province='Newfoundland and Labrador')
        r5 = tk.Radiobutton(province_Frame, text='Newfoundland and Labrador', value="Newfoundland and Labrador", var=province)
        r5. config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r5.grid(row=4, column=0, sticky='nsew')
        NL_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Confirmed.config(text="Confirmed Cases: " + str(format(NL['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        NL_Confirmed.grid(row=4, column=1)
        NL_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Active.config(text="Active Cases: " + str(format(NL['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        NL_Active.grid(row=4, column=2)
        NL_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Recovered.config(text="Recovered Cases: " + str(format(NL['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        NL_Recovered.grid(row=4, column=3)
        NL_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NL_Death.config(text="Deaths: " + str(format(NL['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        NL_Death.grid(row=4, column=4)

        NT = interpreter.getCases(province='Northwest Territories')
        r6 = tk.Radiobutton(province_Frame, text='Northwest Territories', value="Northwest Territories", var=province)
        r6.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r6.grid(row=5, column=0, sticky='nsew')
        NT_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Confirmed.config(text="Confirmed Cases: " + str(format(NT['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        NT_Confirmed.grid(row=5, column=1)
        NT_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Active.config(text="Active Cases: " + str(format(NT['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        NT_Active.grid(row=5, column=2)
        NT_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Recovered.config(text="Recovered Cases: " + str(format(NT['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        NT_Recovered.grid(row=5, column=3)
        NT_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NT_Death.config(text="Deaths: " + str(format(NT['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        NT_Death.grid(row=5, column=4)

        NS = interpreter.getCases(province='Nova Scotia')
        r7 = tk.Radiobutton(province_Frame, text='Nova Scotia', value="Nova Scotia", var=province)
        r7.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r7.grid(row=6, column=0, sticky='nsew')
        NS_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Confirmed.config(text="Confirmed Cases: " + str(format(NS['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        NS_Confirmed.grid(row=6, column=1)
        NS_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Active.config(text="Active Cases: " + str(format(NS['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        NS_Active.grid(row=6, column=2)
        NS_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Recovered.config(text="Recovered Cases: " + str(format(NS['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        NS_Recovered.grid(row=6, column=3)
        NS_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NS_Death.config(text="Deaths: " + str(format(NS['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        NS_Death.grid(row=6, column=4)

        # Statistics not avaliable for Nunavut on API.
        #NU = interpreter.getCases(province='Nunavut')
        r8 = tk.Radiobutton(province_Frame, text='Nunavut (No API Data)', value="Nunavut", var=province)
        r8.config(font=("Courier", 14, "bold"), bg='gray93', fg='gray9', state=tk.DISABLED)
        r8.grid(row=12, column=0, sticky='nsew')
        NU_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"), bg="gray93")
        NU_Confirmed.config(text="Confirmed Cases: -", fg=widgetFG)
        NU_Confirmed.grid(row=12, column=1)
        NU_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NU_Active.config(text="Active Cases: -", fg=widgetFG, bg='gray93')
        NU_Active.grid(row=12, column=2)
        NU_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"), bg='gray93')
        NU_Recovered.config(text="Recovered Cases: -", fg=widgetFG)
        NU_Recovered.grid(row=12, column=3)
        NU_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        NU_Death.config(text="Deaths: -", fg=widgetFG, bg='gray93')
        NU_Death.grid(row=12, column=4)

        ON = interpreter.getCases(province='Ontario')
        r9 = tk.Radiobutton(province_Frame, text='Ontario', value="Ontario", var=province)
        r9.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r9.grid(row=7, column=0, sticky='nsew')
        ON_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Confirmed.config(text="Confirmed Cases: " + str(format(ON['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        ON_Confirmed.grid(row=7, column=1)
        ON_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Active.config(text="Active Cases: " + str(format(ON['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        ON_Active.grid(row=7, column=2)
        ON_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Recovered.config(text="Recovered Cases: " + str(format(ON['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        ON_Recovered.grid(row=7, column=3)
        ON_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        ON_Death.config(text="Deaths: " + str(format(ON['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        ON_Death.grid(row=7, column=4)

        PE = interpreter.getCases(province='Prince Edward Island')
        r10 = tk.Radiobutton(province_Frame, text='Prince Edward Island', value="Prince Edward Island", var=province)
        r10.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r10.grid(row=8, column=0, sticky='nsew')
        PE_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Confirmed.config(text="Confirmed Cases: " + str(format(PE['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        PE_Confirmed.grid(row=8, column=1)
        PE_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Active.config(text="Active Cases: " + str(format(PE['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        PE_Active.grid(row=8, column=2)
        PE_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Recovered.config(text="Recovered Cases: " + str(format(PE['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        PE_Recovered.grid(row=8, column=3)
        PE_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        PE_Death.config(text="Deaths: " + str(format(PE['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        PE_Death.grid(row=8, column=4)

        QC = interpreter.getCases(province='Quebec')
        r11 = tk.Radiobutton(province_Frame, text='Quebec', value="Quebec", var=province)
        r11.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r11.grid(row=9, column=0, sticky='nsew')
        QC_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Confirmed.config(text="Confirmed Cases: " + str(format(QC['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        QC_Confirmed.grid(row=9, column=1)
        QC_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Active.config(text="Active Cases: " + str(format(QC['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        QC_Active.grid(row=9, column=2)
        QC_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Recovered.config(text="Recovered Cases: " + str(format(QC['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        QC_Recovered.grid(row=9, column=3)
        QC_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        QC_Death.config(text="Deaths: " + str(format(QC['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        QC_Death.grid(row=9, column=4)

        SK = interpreter.getCases(province='Saskatchewan')
        r12 = tk.Radiobutton(province_Frame, text='Saskatchewan', value="Saskatchewan", var=province)
        r12.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r12.grid(row=10, column=0, sticky='nsew')
        SK_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Confirmed.config(text="Confirmed Cases: " + str(format(SK['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        SK_Confirmed.grid(row=10, column=1)
        SK_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Active.config(text="Active Cases: " + str(format(SK['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        SK_Active.grid(row=10, column=2)
        SK_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Recovered.config(text="Recovered Cases: " + str(format(SK['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        SK_Recovered.grid(row=10, column=3)
        SK_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        SK_Death.config(text="Deaths: " + str(format(SK['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        SK_Death.grid(row=10, column=4)

        YT = interpreter.getCases(province='Yukon')
        r13 = tk.Radiobutton(province_Frame, text='Yukon', value="Yukon", var=province)
        r13.config(font=("Courier", 14, "bold"), bg='lightyellow', fg='gray9')
        r13.grid(row=11, column=0, sticky='nsew')
        YT_Confirmed = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Confirmed.config(text="Confirmed Cases: " + str(format(YT['Confirmed'], ",d")), fg=widgetFG, bg="palegreen4")
        YT_Confirmed.grid(row=11, column=1)
        YT_Active = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Active.config(text="Active Cases: " + str(format(YT['Active'], ",d")), fg=widgetFG, bg='goldenrod3')
        YT_Active.grid(row=11, column=2)
        YT_Recovered = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Recovered.config(text="Recovered Cases: " + str(format(YT['Recovered'], ",d")), fg=widgetFG, bg='skyblue3')
        YT_Recovered.grid(row=11, column=3)
        YT_Death = tk.Label(province_Frame, background=widgetBG, font=("Courier", 12, "bold"))
        YT_Death.config(text="Deaths: " + str(format(YT['Deaths'], ",d")), fg=widgetFG, bg='salmon3')
        YT_Death.grid(row=11, column=4)

        province_Frame.pack(fill='x', padx=30, pady=5)
        province_Frame.grid_columnconfigure(0, weight=2)
        province_Frame.grid_columnconfigure(1, weight=2)
        province_Frame.grid_columnconfigure(2, weight=2)
        province_Frame.grid_columnconfigure(3, weight=2)
        province_Frame.grid_columnconfigure(4, weight=2)

        # Graph button directs user to graph trend of province COVID-19 trend.
        graph_Button = tk.Button(alpha, text="Display Graph", height=2, width=30, fg="slate blue", font=("Courier", 20, "bold"))
        graph_Button.config(highlightbackground='pink', command=lambda: display_Graph(province.get()))
        graph_Button.pack(fill='x', padx=30, pady=10)

        province.trace("w", monitor_Province)

        alpha.title('CANADIAN PROVINCIAL COVID-19 STATISTICS')
        alpha.geometry("1000x400")
        alpha.minsize(875, 400)
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
    # Also change window size depending on the selection.
    if countryCode == 'canada':
        stateButton = tk.Button(master, text="Province Data", height=2, fg="slate blue")
        stateButton.config(highlightbackground='pink', command=lambda: display_Provinces(), font=("Courier", 20, "bold"))
        stateButton.pack(fill='x', padx=30, pady=10)
        master.minsize(600, 575)
        master.geometry("600x600")

    else:
        master.minsize(600, 515)
        master.geometry("600x515")

    # GUI's attributes.
    master.configure(background="ivory2")
    master.mainloop()
