
import os

from PySide6 import QtWidgets
from mapclientplugins.userscriptstep.ui_configuredialog import Ui_ConfigureDialog


INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._workflow_location = None
        self._previous_location = ''

        self._make_connections()

    def _make_connections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)
        self._ui.lineEditScriptPath.textChanged.connect(self.validate)
        self._ui.pushButtonFileChooser.clicked.connect(self._open_file_chooser)

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.StandardButton.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration', 'This configuration is invalid.  Unpredictable behaviour '
                                                   'may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.StandardButton(QtWidgets.QMessageBox.StandardButton.Yes |
                                                                                        QtWidgets.QMessageBox.StandardButton.No),
                                                   QtWidgets.QMessageBox.StandardButton.No)

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        self._ui.lineEditIdentifier.setStyleSheet(
            DEFAULT_STYLE_SHEET if valid else INVALID_STYLE_SHEET)

        path = self._ui.lineEditScriptPath.text()
        path_valid = len(path) and os.path.isfile(path) and path.endswith(".py")
        self._ui.lineEditScriptPath.setStyleSheet(
            DEFAULT_STYLE_SHEET if path_valid else INVALID_STYLE_SHEET)

        return valid and path_valid

    def get_config(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {
            'identifier': self._ui.lineEditIdentifier.text(),
            'script_path': self._ui.lineEditScriptPath.text(),
            'input_port_count': self._ui.spinBoxNumberOfInputs.value(),
            'output_port_count': self._ui.spinBoxNumberOfOutputs.value()
        }
        return config

    def set_config(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.lineEditScriptPath.setText(config['script_path'])
        self._ui.spinBoxNumberOfInputs.setValue(config['input_port_count'])
        self._ui.spinBoxNumberOfOutputs.setValue(config['output_port_count'])

    def _open_file_chooser(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select File Location', self._previous_location)

        if path:
            self._previous_location = path
            self._ui.lineEditScriptPath.setText(path)
