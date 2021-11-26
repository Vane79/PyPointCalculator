import PySimpleGUI as sg
from selenium_fetch_stats import selenium
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import calcs

sg.theme('DarkGrey7')  # please make your windows colorful

column1 = [
    [sg.Text('Number of your photos:')],
    [sg.Input(key='-IN-P-', size=(45, 1))]
]
column2 = [
    [sg.Text('And videos:')],
    [sg.Input(key='-IN-V-', size=(45, 1))],

]
layout = [
    [sg.Column(column1, element_justification='left'), sg.Column(column2, element_justification='right')],
    [sg.Text(size=(90, 1), text=f"", key='-OUT1-')],
    [sg.Text(size=(90, 1), text=f"", key='-OUT2-')],
    [sg.Text(size=(90, 1), text=f"                                                                      Waiting for input", key='-OUT3-')],
    [sg.Text(size=(90, 1), text="", key='-OUT4-')],
    [sg.Text(size=(90, 1), text=f"", key='-OUT5-')],
    [sg.Button('Calculate'), sg.Button('Fetch automatically')]
]

window = sg.Window('Py Point Calculator', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Fetch automatically':
        try:
            photos, videos = selenium()
            window['-IN-P-'].update(photos)
            window['-IN-V-'].update(videos)
        except ElementNotInteractableException:
            window['-OUT3-'].update('                                                               Please press that button again')
        except NoSuchElementException:
            window['-OUT3-'].update('                                                               Check login credentials and try again')


    if event == 'Calculate':
        photos, videos = values['-IN-P-'], values['-IN-V-']
        if photos == '':
            photos = 0
        if videos == '':
            videos = 0
        try:
            total = int(photos) + (int(videos) * 2)
            calculated = calcs.Pointer(total)
            window['-OUT1-'].update(
                f"You've processed {calculated.p_total} total points. That was approx. {calculated.average_daily} points per weekday.")
            window['-OUT2-'].update(
                f"You've already earned {calculated.money_now} roubles, that's {calculated.tier} roubles per point.")
            window['-OUT3-'].update(
                f"So, by my humble estimates, you'll get {calculated.money_prediction} roubles by the end of the current month, {calculated.tier_prediction} roubles per point.")
            window['-OUT4-'].update(
                f"You'd have to process {calculated.tier_diff_by_end_of_month} more points per weekday for the next tier.")
            window['-OUT5-'].update(
                f"By the way, there's only a bit of time left. Only {calculated.workdays_left} days, to be exact.")
        except ValueError:
            window['-OUT3-'].update(
                f"                                                                          Try again")
