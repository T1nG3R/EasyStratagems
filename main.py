import sys
import time

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from pynput.keyboard import Key, Controller, Listener

from MainWindow import Ui_MainWindow
from stratagems import stratagems


class StratagemExecutor:
    """
    Facilitates the execution of predefined stratagems using keyboard input.

    The `StratagemExecutor` class provides a mechanism to execute specific
    actions corresponding to stratagems, by simulating keyboard events. It
    utilizes a controller to emulate key presses for a sequence of keys
    associated with a given stratagem.

    :ivar keyboard: Controller object used for simulating keyboard input.
    :type keyboard: Controller
    :ivar stratagems: Dictionary that contains stratagem names as keys and
        their associated sequences of key presses as values.
    :type stratagems: dict
    """

    def __init__(self):
        self.keyboard = Controller()
        self.stratagems = stratagems

    def execute_stratagem(self, stratagem_name):
        """
        Executes a given stratagem by simulating the required keyboard input.
        The function checks if the provided stratagem exists and triggers the
        key presses in the sequence associated with the given stratagem.

        :param stratagem_name: Name of the stratagem to execute
        :type stratagem_name: str
        :return: None
        """
        if stratagem_name not in self.stratagems:
            return

        self.keyboard.press(Key.ctrl)
        time.sleep(0.1)

        for key in self.stratagems[stratagem_name][0]:
            self.keyboard.press(key)
            time.sleep(0.05)
            self.keyboard.release(key)
            time.sleep(0.05)

        self.keyboard.release(Key.ctrl)


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    MainWindow class provides a user interface for managing strategic controls and
    listening to keyboard inputs with actions triggered on specific keys.

    This class integrates functionalities for configuring combo boxes with stratagems,
    associating keyboard keys with corresponding combo boxes, and managing the listening
    state for handling keyboard inputs. It uses an external module for executing the
    selected stratagems based on user inputs and updates the UI in response to state changes.

    :ivar listener: Instance of a keyboard listener that listens for keypress events
        and invokes the associated actions.
    :type listener: pynput.keyboard.Listener or None
    :ivar is_listening: Indicates whether the application is currently listening for
        keyboard inputs.
    :type is_listening: bool
    :ivar stratagem_executor: Executor instance responsible for executing stratagems
        as defined and selected in the UI.
    :type stratagem_executor: StratagemExecutor
    :ivar key_to_combo: Mapping of keyboard keys to the associated combo box widgets.
    :type key_to_combo: dict[str, QComboBox]
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.listener = None
        self.is_listening = False
        self.stratagem_executor = StratagemExecutor()

        self.key_to_combo = {'o': self.comboBox, 'p': self.comboBox_2, '[': self.comboBox_3, ']': self.comboBox_4}

        self._setup_combo_boxes()
        self.is_listening_Button.clicked.connect(self.toggle_listening)

    def _setup_combo_boxes(self):
        """
        Populates multiple combo boxes with items representing stratagems.

        This method populates specified combo boxes with items using data from
        the `stratagem_executor` attribute's `stratagems` dictionary. Each item
        consists of a key as the display text and an associated icon from the
        value tuple. Icons and keys are added to every combo box in the provided
        list.

        :param self: The instance of the class on which this method is called.

        :return: None
        """
        for key, value in self.stratagem_executor.stratagems.items():
            for combo_box in [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4]:
                combo_box.addItem(QIcon(value[1]), key)

    def on_key_press(self, key):
        """
        Handles the event when a key is pressed by executing a corresponding
        stratagem based on the key pressed. If the key corresponds to a combo
        box, retrieves the selected value from the combo box and executes the
        associated stratagem using the `stratagem_executor`.

        :param key: The key that was pressed. This object may include a 'char'
                    attribute representing the character of the key pressed.
        :type key: Any
        :return: None
        """
        try:
            if hasattr(key, 'char') and key.char in self.key_to_combo:
                combo_box = self.key_to_combo[key.char]
                selected_stratagem = combo_box.currentText()
                self.stratagem_executor.execute_stratagem(selected_stratagem)
        except AttributeError:
            pass

    def toggle_listening(self):
        """
        Toggles the listening state of the Listener instance.

        When this method is called, it checks the current state of the `is_listening`
        flag. If `is_listening` is `False`, it initializes a Listener instance, sets
        up the key press callback, and starts the listener, which begins capturing
        keyboard events. Additionally, it updates the user interface to reflect the
        active listening state.

        If `is_listening` is `True`, the method stops the active Listener instance,
        releases resources associated with it, and updates the user interface to
        reflect that listening has been disabled.

        :rtype: None
        :return: This method does not return any value, it only alters the state of
            the Listener and the user interface.
        """
        if not self.is_listening:
            self.listener = Listener(on_press=self.on_key_press)
            self.listener.start()
            self.is_listening = True
            self._update_ui_state(True)
        else:
            if self.listener:
                self.listener.stop()
            self.is_listening = False
            self._update_ui_state(False)

    def _update_ui_state(self, is_listening):
        """
        Updates the UI state of a listening button and status label in the application.

        This method modifies the button text, label text, and label color based on the
        listening state passed as an argument.

        :param is_listening: A boolean value indicating whether the system is currently
            in a listening state or not.
        :return: None
        """
        button_text = "Stop listening" if is_listening else "Start listening"
        label_color = "#00ff00" if is_listening else "#ff0000"
        status_text = "listening" if is_listening else "not listening"

        self.is_listening_Button.setText(button_text)
        self.is_listening_label.setText(QApplication.translate("MainWindow",
                                                               f'<html><head/><body><p><span style=" color:{label_color};">Status: {status_text}</span></p></body></html>',
                                                               None))

    def closeEvent(self, event):
        """
        Handles the window close event by stopping the listener if it exists, and then
        delegates the event to the parent class's close event handler.

        This function ensures that any active listener is properly stopped before
        the application closes to release resources or perform any cleanup.

        :param event: The close event to handle.
        :type event: QCloseEvent
        :return: None.
        """
        if self.listener:
            self.listener.stop()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
