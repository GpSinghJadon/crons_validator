
class Alert:

    def __init__(self, *args, **kwargs):
        self.logger = kwargs.pop('logger',None)

    def raiseAlert(self, message):
        self.logger.critical('ALERT!, %s'%message)