class AbstractProcessor:
    parameters_schema = None
    allowed_parameters = []
    default_parameters = {}

    def __init__(self, image, name, input_parameters=None):
        self.image = image
        self.filename = name
        self.parameters = {**self.default_parameters}

        input_parameters = input_parameters or {}

        for parameter in self.allowed_parameters:
            if parameter in input_parameters:
                self.parameters[parameter] = input_parameters[parameter]

    def process(self):
        pass

