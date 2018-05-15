import jsonschema


class Validator:
    schema = {}

    def __init__(self, data):
        self.data = data
        self.errors = []

    def is_valid(self):
        errors = list(jsonschema
                      .Draft4Validator(self.schema).iter_errors(self.data))
        if errors:
            for error in errors:
                self.errors.append(error.message)
            return False
        return True


class TaskValidator(Validator):
    schema = {
        "type": "object",
        "properties": {
            "bucket": {
                "type": "object",
                "properties": {
                    "region": {"type": "string"},
                    "name": {"type": "string"}
                },
                "required": ["region", "name"]
            },
            "filename": {"type": "string"},
            "parameters": {"type": "object"}
        },
        "required": ["bucket", "filename"]
    }