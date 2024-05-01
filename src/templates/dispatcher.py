from rest_framework.exceptions import APIException

from src.templates.scripts.resign import ResignScript


class Dispatcher:
    registry = {}

    def register(self, script_class):
        script_code = script_class.template.script_code
        self.registry[script_code] = script_class

    def get_script_class(self, template):
        if template.script_code not in self.registry:
            APIException("Not Found Script Class")
        return self.registry[template.script_code]


dispatcher = Dispatcher()
dispatcher.register(ResignScript)
