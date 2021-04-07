from solo.factory import create_factory
from .Greetings import Greetings
from .CycleGreetings import CycleGreetings

suite_factory = create_factory("Suite")
suite_factory.register('Greetings', Greetings)
suite_factory.register('CycleGreetings', CycleGreetings)
