class ConfigExceptions(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class InvalidExtention(ConfigExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class DefaultPathIsFile(ConfigExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class DefaultPathDoesNotExist(ConfigExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)