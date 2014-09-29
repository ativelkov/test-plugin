from common import BasePlugin


class Foo(BasePlugin):
    def execute(self):
        print "FOO: " + self.name
