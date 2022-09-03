import PySimpleGUI as sg
from selenium_fetch_stats import selenium
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from kittehs import kitteh
from offdays import days_off
import calcs

sg.theme('DarkGrey7')  # please make your windows colorful

layout = [
    [sg.Push(), sg.Text("*Motivational quote*"), sg.Push()],
    [sg.Text('Number of photos:'), sg.Input(key='-IN-P-', size=25), sg.Text('And videos:'), sg.Input(key='-IN-V-', size=25)],
    [sg.Text(text=f"", key='-OUT1-', expand_x=True)],
    [sg.Text(text=f"", key='-OUT2-', expand_x=True)],
    [sg.Push(), sg.Text(text=f"Waiting for input", key='-OUT3-'), sg.Push()],
    [sg.Text(text=f"", key='-OUT4-', expand_x=True)],
    [sg.Text(text=f"", key='-OUT5-', expand_x=True)],
    [sg.Text(text=f"", key='-OUT6-', expand_x=True)],
    [sg.Push(), sg.Button('Calculate'), sg.Push(), sg.Button('Fetch automatically'), sg.Push(), sg.Button('Kitties!'), sg.Push()],
]
window = sg.Window('Py Point Calculator', layout, element_justification='m')

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Fetch automatically':
        try:
            photos, videos = selenium()
            window['-IN-P-'].update(photos)
            window['-IN-V-'].update(videos)
            window['-OUT3-'].update('Fetch successful')
        except ElementNotInteractableException:
            window['-OUT3-'].update('Please press that button again')
        except NoSuchElementException:
            window['-OUT3-'].update('Check login credentials and try again')

    if event == 'Kitties!':
        kitteh()

    if event == 'Calculate':
        photos, videos = values['-IN-P-'], values['-IN-V-']
        if photos == '':
            photos = 0
        if videos == '':
            videos = 0
        try:
            total = int(photos) + (int(videos) * 2)
            calculated = calcs.Pointer(total, days_off)
            window['-OUT1-'].update(
                f"You've processed {calculated.p_total} total points. That was approx. {calculated.average_daily} points per weekday.")
            window['-OUT2-'].update(
                f"You've already earned {calculated.money_now} roubles, that's {calculated.tier} roubles per point.")
            window['-OUT3-'].update(
                f"So, by my humble estimates, you'll get {calculated.money_prediction} roubles by the end of the current month, {calculated.tier_prediction} roubles per point.")
            window['-OUT4-'].update(
                f"And, converted to points, that'd be {calculated.prognosis} points.")
            window['-OUT5-'].update(
                f"You'd have to process {calculated.tier_diff_by_end_of_month} more points per weekday for the next tier.")
            window['-OUT6-'].update(
                f"You have worked {calculated.worked_days} days out of {calculated.month_workdays} this month.")
        except ValueError:
            window['-OUT3-'].update(f"Try again")
