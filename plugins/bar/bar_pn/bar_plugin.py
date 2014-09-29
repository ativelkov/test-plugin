from common import BasePlugin


class Bar(BasePlugin):
    def execute(self):
        print "BAR: " + self.name
