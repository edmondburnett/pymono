

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Settings(Borg):
    """ Borg/Singleton class for service settings. Insert methods for loading by service_name from /conf """
    pass