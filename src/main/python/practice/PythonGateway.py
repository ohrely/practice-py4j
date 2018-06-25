from pyspark import SparkContext
import pprint
import imp
import sys

__all__ = []
def _create_function(name, doc=""):
    """ Create a function for aggregator by name"""
    def _(asdf):
        sc = SparkContext._active_spark_context
        jc = getattr(sc._jvm.practice.ScalaObj, name)()
        return jc
    _.__name__ = name
    _.__doc__ = doc
    return _

_functions = {
    'three': 'Calculate the kurtosis, maybe!',
    'two': 'basic method'
}

print("bah")

class Foo:
    def __init__(self):
        pass

a = Foo()

def create_funcs():
    print("creating funcs")
    for _name, _doc in _functions.items():
        print("foo {}".format(_name))
        name = "stest." + _name
        a.two = _create_function(_name, _doc)

#    pprint.pprint(globals())