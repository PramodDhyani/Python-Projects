from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.label import Label

class MyTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Call the parent class constructor
        self.size_hint = (0.8, 0.8)  # Set size of the TabbedPanel
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Positioning the TabbedPanel

        # Add first tab
        tab1 = TabbedPanelItem(text="Tab 1")  # Create a Tab
        tab1.content = Label(text="This is content for Tab 1")  # Set content for Tab 1
        self.add_widget(tab1)  # Add the tab to TabbedPanel

        # Add second tab
        tab2 = TabbedPanelItem(text="Tab 2")
        tab2.content = Label(text="This is content for Tab 2")
        self.add_widget(tab2)

        # Add third tab
        tab3 = TabbedPanelItem(text="Tab 3")
        tab3.content = Label(text="This is content for Tab 3")
        self.add_widget(tab3)

class MyApp(App):
    def build(self):
        return MyTabbedPanel()  # Return the TabbedPanel widget to be displayed

if __name__ == "__main__":
    MyApp().run()  # Run the application
