
"""
MAP Client Plugin Step
"""
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.userscriptstep.configuredialog import ConfigureDialog, import_plugin_main


class UserScriptStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(UserScriptStep, self).__init__('User Script', location)
        self._configured = False
        self._category = 'General'

        # Ports:
        self._skeleton_input_triple_individual = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
             '<not-set>']
        self._skeleton_input_triple_list = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#uses-list-of',
             '<not-set>']
        self._skeleton_output_triple_individual = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
             '<not-set>']
        self._skeleton_output_triple_list = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#provides-list-of',
             '<not-set>']
        self.addPort([tuple(self._skeleton_input_triple_individual),
                      tuple(self._skeleton_input_triple_list)])
        self.addPort([tuple(self._skeleton_output_triple_individual),
                      tuple(self._skeleton_output_triple_list)])

        # Port data:
        self._input_data = [None]
        self._output_data = [None]

        # Config:
        self._config = {
            'identifier': '',
            'script_path': '',
            'input_port_count': 1,
            'output_port_count': 1,
        }

    def _process_config(self):
        self._ports.clear()

        input_port_count = self._config['input_port_count']
        self._input_data = [None] * input_port_count
        input_port_triple_individual = self._skeleton_input_triple_individual
        input_port_triple_list = self._skeleton_input_triple_list
        for i in range(input_port_count):
            self.addPort([tuple(input_port_triple_individual), tuple(input_port_triple_list)])

        output_port_count = self._config['output_port_count']
        self._output_data = [None] * output_port_count
        output_port_triple_individual = self._skeleton_output_triple_individual
        output_port_triple_list = self._skeleton_output_triple_list
        for i in range(output_port_count):
            self.addPort([tuple(output_port_triple_individual), tuple(output_port_triple_list)])

    def execute(self):
        """
        The plugin will call the `plugin_main` function defined in the user script and pass in the
        input port data as arguments. The user script must define the `plugin_main` function.
        """
        plugin_main = import_plugin_main(self._config['script_path'])
        self._output_data = list(plugin_main(*self._input_data))

        self._doneExecution()

    def setPortData(self, index, data_in):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param data_in: The data to set for the port at the given index.
        """
        self._input_data[index] = data_in

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        output_index = index - self._config['input_port_count']
        return self._output_data[output_index]

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.set_config(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.get_config()
            self._process_config()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.set_config(self._config)
        self._configured = d.validate()
        self._process_config()
