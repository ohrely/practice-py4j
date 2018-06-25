import unittest


from pyspark.sql import SparkSession
from pyspark.sql import Row
import pprint
from pyspark import SparkContext

import PythonGateway
from PythonGateway import Foo, a

PythonGateway.create_funcs()

class ScalaObjTest(unittest.TestCase):
    spark = SparkSession.builder.config("spark.master", "local").getOrCreate()

    rdd = spark.sparkContext.parallelize([Row(4)])
    df = rdd.toDF()

    def test_basic_method(self):
        print("new globals")
        pprint.pprint(globals())
        self.assertEqual(self.df.foreach(a.two), 2)

    def test_implicit_method(self):
        # self.assertEqual(three(), 3)
        pass


if __name__ == '__main__':
    unittest.main()
