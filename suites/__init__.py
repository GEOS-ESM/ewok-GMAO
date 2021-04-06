from solo.factory import create_factory
from .Greetings import Greetings

suite_factory = create_factory("Suite")
suite_factory.register('Greetings', Greetings)
