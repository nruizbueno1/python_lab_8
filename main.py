# Author: Nicole Ruiz-Bueno
# Date:   03/07/2023
# File:   main.py
#
# Description:  Generate a list of Fahrenheit to Celsius temperature conversions using a while loop. The user will enter
#               the starting Fahrenheit temperature and the number of conversions. For each conversion increment the
#               temperature 2 degrees. Display the Fahrenheit and Celsius temperatures as follows:
#               0 Fahrenheit is -17.8 degrees Celsius
#
# Input:        Starting Fahrenheit and Number of Conversions
# Output:       RecyclerView with labels displaying Fahrenheit and equivalent Celsius degrees.
#
# Processing:   Use a while loop to display text in a RecyclerView
#               Convert Fahrenheit and Celsius to float
#               Add loop control variable ( x=1 )
#               Start while loop that calls on function FtoC with fahrenheit as its argument (self.FtoC(fahrenheit))
#                   while x <= conversions
#                   Increment fahrenheit ( fahrenheit = fahrenheit + 2 ) and the loop control variable (x = x + 1)
#                   Else function to print 'While loop finished'
#                   Except ValueError to display error message
#               Set up FtoC Function ( def FtoC(self, fahrenheit): )
#                   Conduct calculation: celsius = (((fahrenheit -32) * 5.0) / 9.0)
#                   Have results appear in RecylerView
#                       ( self.root.ids.output_list.data.append({'tex#t’: f'{kph} kph is {mph:.1f} mph'}) )
#               Exit button releases event function to close application


# import the Kivy library components
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

# imports for Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

# designate our .kv design file
# we are using gui.kv for the Graphical user Interface
Builder.load_file('gui.kv')


# A Widget is the base building block of GUI interfaces in Kivy.
# It provides a Canvas that can be used to draw on screen.
# It receives user events and reacts to them.
# MyLayout is the root window of the application
class MyLayout(Widget):
    pass


# Lab8 is the name of the Python application that will be using Kivy
class Lab8(App):
    # set the title of the window frame
    title = 'Lab8: FtoC Function Fahrenheit to Celsius by Ruiz-Bueno'

    # the build method is called when the application starts
    def build(self):
        print("build called")
        # when app starts, return main root window in the kivy gui file
        return MyLayout()

    # while button release event handler
    # this function is called by the Kivy event loop
    # when a user presses the While Loop button
    def generate_button(self):
        # get data from text inputs
        # self means this or the current object
        # root is the root window or MyLayout
        # ids is the id's of the widgets contained in the root window
        # start is the id of the first fahrenheit text input box
        # print the input for debugging
        print(f'generate_button start fahrenheit: {self.root.ids.start.text}')
        print(f'generate_button conversions: {self.root.ids.conversions.text}')

        # try the following code.
        # if int() or float() cannot convert the string,
        # a ValueError exception is raised. Execution jumps to except:
        try:
            # clear data in the recyclerView
            self.root.ids.output_list.data.clear()

            # declare variables starting fahrenheit and conversions
            # get input string from textInput and cast to integer
            fahrenheit = float(self.root.ids.start.text)
            conversions = int(self.root.ids.conversions.text)

            # loop control variable
            x = 1
            while x <= conversions:
                # calculate the conversion
                self.FtoC(fahrenheit)
                # increment fahrenheit
                fahrenheit = fahrenheit + 2
                # increment the loop control variable
                x = x + 1
            else:
                print('While loop finished')
                # print dictionary for debugging
                print(self.root.ids.output_list.data)

                # refresh the recyclerView from the data dictionary
                self.root.ids.output_list.refresh_from_data()

        # except catches the exception raised in the try block
        # display a Kivy message box with error message
        except ValueError:
            self.kivy_message_box('Input Error', 'Bad Input!')

    def FtoC(self, fahrenheit):

        celsius = (((fahrenheit - 32) * 5.0) / 9.0)
        print(f'FtoC called with fahrenheit: {fahrenheit}')
        self.root.ids.output_list.data.append({'text': f'{fahrenheit} Fahrenheit is {celsius:.1f} Celsius'})

    # exit button release event handler
    # this function is called by the Kivy event loop when a user presses the exit button
    def exit_button(self):
        # call the stop function in the app
        self.stop()

    # creates a kivy Message Box
    # it is a static method because self is not used
    @staticmethod
    def kivy_message_box(title, message):
        # create the button and label, add them to BoxLayout
        button = Button(text='Close',
                        size_hint=(.3, .3),
                        pos_hint={'right': 1}
                        )
        label = Label(text=message)
        box = BoxLayout(orientation='vertical')
        box.add_widget(label)
        box.add_widget(button)

        # create the popup object
        popup = Popup(title=title,
                      content=box,
                      size_hint=(None, None),
                      size=(dp(300), dp(200)),
                      auto_dismiss=False)
        # bind the on_press event of the button to the dismiss function
        button.bind(on_press=popup.dismiss)
        popup.open()


# If this Python file is called as the main starting point of the application
# start the Tutorial5 Python/Kivy app running.
if __name__ == '__main__':
    Lab8().run()
