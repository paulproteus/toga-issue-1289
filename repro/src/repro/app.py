"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Repro(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        label = toga.Label("App started")
        def change_label(*args):
            label.text = "New text"
        button = toga.Button(label="Click to change label", on_press=change_label)
        main_box = toga.Box(children=[label, button])

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Repro()
