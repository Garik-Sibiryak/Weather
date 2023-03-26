# >>>>>>>>>>>>>>> --- TITLE --- <<<<<<<<<<<<<<<<
#           This is my first program           #
# >>>>>>>>>>>>>>> ------------- <<<<<<<<<<<<<<<<

import requests as req
from tkinter import *
import ctypes
from cities_database import file_read

root = Tk()


# <<<<<<<<<<<<<<<<<<<<<<< - FUNCTIONS FIELD START - >>>>>>>>>>>>>>>>>>>>>>>>>>

# //////////////////// Language check function \\\\\\\\\\\\\\\\\\\\
def get_keyboard_layout():
    """
    Detecting keyboard layout for language option
    in application`s text.
    :param:
    :return: 'ru' or 'en'
    """
    library = ctypes.windll.LoadLibrary("user32.dll")
    keyboard_layout = getattr(library, "GetKeyboardLayout")
    if hex(keyboard_layout(0)) == '0x4190419':
        return 'ru'
    if hex(keyboard_layout(0)) == '0x4090409':
        return 'en'
# \\\\\\\\\\\\\\\\\\\\__________________________////////////////////


# ////////////////////// Activation function \\\\\\\\\\\\\\\\\\\\\\
def activation_function(event):
    """
    This function is used as an activator
    when user presses the "ENTER" button.
    It runs "request" function and passes
    arguments to it.
    :param:
    :return: request(city, par_1, par_2)
    """
    return request(value.get(), 2, '')
# \\\\\\\\\\\\\\\\\\\\\\____________________//////////////////////


# /////////////////////// Request function \\\\\\\\\\\\\\\\\\\\\\\
def request(city, par_1, par_2):
    """
    This function sends request to the server.
    It processes the result and passes it to the program body.
    :param city: name of a city
    :param par_1: format of the weather forecast text
    (1 - fallout, temperature; 2 - fallout, temperature,
    wind speed; 3 - city name, fallout, temperature;
    4 - city name, fallout, temperature, wind speed)
    !!!Window size doesn't support the 4th version!!!
    :param par_2: wind speed format ('' - m/s; '1' - km/h)
    :return: None
    """
    url = f'https://wttr.in/{city}'
    parameters = {
        'format': par_1,
        'M': par_2
    }
    try:
        # - Tries to get response from the server -
        response = req.get(url, parameters)

        # - Activates the "weather" functions -
        weather_in()

        # - Activates the "in_city" functions -
        in_city()

        # - Passes the positive result of request
        # in text format to the "forecast" field -
        forecast['text'] = response.text

        # - Passes the "text color" parameter
        # to the "forecast" field in relation
        # of the temperature in response -
        if '+0' in response.text:
            forecast['fg'] = 'black'
        elif '-0' in response.text:
            forecast['fg'] = 'black'
        elif '+' in response.text:
            forecast['fg'] = 'red'
        elif '-' in response.text:
            forecast['fg'] = 'blue'
    # - Passes the negative result of request
    # to the "error field" -
    except:
        # - Language check -
        if get_keyboard_layout() == 'ru':
            error['text'] = 'Что-то сломалось...\n¯\_(⊙_ʖ⊙)_/¯'
        else:
            error['text'] = 'Something broke...\n¯\_(⊙_ʖ⊙)_/¯'
# \\\\\\\\\\\\\\\\\\\\\\\__________________///////////////////////


# /////////////////////// Text function №1 \\\\\\\\\\\\\\\\\\\\\\\
def weather_in():
    """
    This function activates the "weather_in_text" field
    by transmitting coordinates. Also, it passes the text
    :param:
    :return: None
    """
    # - Language check -
    if get_keyboard_layout() == 'ru':
        weather_in_text['text'] = 'Погода в'
    else:
        weather_in_text['text'] = 'Weather in'
    weather_in_text.place(relx=0.03, rely=0.6)
# \\\\\\\\\\\\\\\\\\\\\\\__________________///////////////////////


# /////////////////////// Text function №2 \\\\\\\\\\\\\\\\\\\\\\\
def in_city():
    """
    This function activates the "in_city" field
    :param:
    :return: None
    """

    # - Getting a value from "input" field -
    name = value.get()

    # - Language check -
    if get_keyboard_layout() == 'ru':
        # - Runs the function from the module
        # and passes the received value to the
        # "city_name" field -
        result = file_read(name)
        city_name['text'] = next(result)
    else:
        city_name['text'] = name

    # - Clearing the "input" field -
    city_name_input.delete(0, END)
# \\\\\\\\\\\\\\\\\\\\\\\__________________///////////////////////

# <<<<<<<<<<<<<<<<<<<<<<<< - FUNCTIONS FIELD END - >>>>>>>>>>>>>>>>>>>>>>>>>>>


# <<<<<<<<<<<<<<<<<<<<<<<<<< - MAIN WINDOW START - >>>>>>>>>>>>>>>>>>>>>>>>>>>

# /////////////////////// Main parameters \\\\\\\\\\\\\\\\\\\\\\\
root.geometry('460x300+400+200')
root.resizable(False, False)

# - Language check -
if get_keyboard_layout() == 'ru':
    root.title('Прогноз погоды')
else:
    root.title('Weather forecast')
img = PhotoImage(file='cloudy.png')
root.iconphoto(False, img)
root.configure(bg='white')
# \\\\\\\\\\\\\\\\\\\\\\__________________///////////////////////

# <<<<<<<<<<<<<<<<<<<<<<<<< - MAIN WINDOW END - >>>>>>>>>>>>>>>>>>>>>>>>>


# <<<<<<<<<<<<<<<<<<<<<<< - PROGRAM BODY START - >>>>>>>>>>>>>>>>>>>>>>>>

# //////////////////// Image on background \\\\\\\\\\\\\\\\\\\\\
canvas = Canvas(root,
                width=460,
                height=300,
                bg='white'
                )
canvas.place(relx=0, rely=0)
bg_image = canvas.create_image(320, 130,
                               anchor=CENTER,
                               image=img
                               )
# \\\\\\\\\\\\\\\\\\\\\______________________////////////////////

# ////////////////////// Text input area \\\\\\\\\\\\\\\\\\\\\\\\
# - Language check -
if get_keyboard_layout() == 'ru':
    # - "City name" text -
    city_name = Label(root,
                      text='Название города',
                      bg='white',
                      fg='#ffae00',
                      font=('Times New Roman', 17, 'bold')
                      )
else:
    city_name = Label(root,
                      text='City name',
                      bg='white',
                      fg='#ffae00',
                      font=('Times New Roman', 20, 'bold')
                      )
city_name.place(relx=0.01, rely=0.04)

# - Variable for data from the "text input" field -
value = StringVar()

# - "Text input" field -
city_name_input = Entry(root,
                        width=25,
                        textvariable=value
                        )

# - Automatic cursor placement in the "text input" field -
city_name_input.focus()

# - Language check -
if get_keyboard_layout() == 'ru':
    city_name_input.place(relx=0.015, rely=0.16)
else:
    city_name_input.place(relx=0.32, rely=0.074)

# - "Text input" field activation by "ENTER" button pressing
# and "activation_function" running -
city_name_input.bind('<Return>', activation_function)
# \\\\\\\\\\\\\\\\\\\\\\\_________________///////////////////////

# /////////////////// Forecast result area \\\\\\\\\\\\\\\\\\\\\\
# - "weather in" text -
weather_in_text = Label(root,
                        text='',
                        bg='white',
                        fg='#76c0ff',
                        font=('Times New Roman', 15, 'bold')
                        )

# - "city name" text -
city_name = Label(root,
                  bg='white',
                  fg='#4682B4',
                  text='',
                  font=('times New Roman', 20, 'bold')
                  )
city_name.place(relx=0.03, rely=0.7)

# - Weather forecast text -
forecast = Label(root,
                 text='',
                 bg='white',
                 fg='white',
                 font=('Times New Roman', 20, 'bold')
                 )
forecast.place(relx=0.02, rely=0.84)
# \\\\\\\\\\\\\\\\\\\\\______________________////////////////////

# //////////////////////// Error area \\\\\\\\\\\\\\\\\\\\\\\\\\\
# - Text with an error -
error = Label(root,
              text='',
              bg='white',
              fg='red',
              font=('Times New Roman', 15, 'bold')
              )
error.place(relx=0.02, rely=0.65)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\____________////////////////////////

# <<<<<<<<<<<<<<<<<<<<<<<< - PROGRAM BODY END - >>>>>>>>>>>>>>>>>>>>>>>>>

root.mainloop()
