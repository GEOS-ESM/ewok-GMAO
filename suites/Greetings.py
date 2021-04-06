from ewok.suite import Suite

class Greetings:

    @staticmethod
    def build():
        with Suite() as suite:
            hello = suite.add('HelloWorld')
            goodbye = suite.add('GoodbyeWorld')
        return suite
