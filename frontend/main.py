from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def on_button_click(self, instance):
        # This will print the text of the button that was clicked
        print(f"{instance.text} button clicked!")

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create multiple buttons
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        button3 = Button(text="Button 3")

        # Bind the same method to all buttons
        button1.bind(on_press=self.on_button_click)
        button2.bind(on_press=self.on_button_click)
        button3.bind(on_press=self.on_button_click)

        # Add buttons to layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout

# Run the app
if __name__ == "__main__":
    MyApp().run()
