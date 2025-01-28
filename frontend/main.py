from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Create a layout that arranges widgets vertically
        layout = BoxLayout(orientation='vertical')

        # Create a label widget
        label = Label(text="Welcome to Kivy!")

        # Create a button widget
        button = Button(text="Click Me!")

        # Add the label and button to the layout
        layout.add_widget(label)
        layout.add_widget(button)

        # Return the layout to be displayed
        return layout

# Run the app
if __name__ == "__main__":
    MyApp().run()
