from ewok.suite import Suite

class CycleGreetings:

    @staticmethod
    def build():
        with Suite() as suite:
            start = 'config.init_cycle'
            stop = 'config.last_cycle'
            step = 'config.step_cycle'
            with suite.add('helloCycle', start=start, stop=stop, step=step) as cycle:	
                hello = cycle.add('HelloWorld')
                goodbye = cycle.add('GoodbyeWorld', hello)
        return suite
