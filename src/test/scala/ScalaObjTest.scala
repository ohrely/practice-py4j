package practice

import org.apache.spark.sql.SparkSession
import org.scalatest.{FunSuite, Matchers}

import ScalaObj._

/**
  * Created by rely10 on 9/11/17.
  */
class ScalaObjTest extends FunSuite with Matchers {
  val spark: SparkSession = SparkSession.builder().config("spark.master", "local").getOrCreate()

  test("test basic method"){
    two() shouldEqual 2
  }

  test("test implicit method"){
    spark.read.three() shouldEqual 3
  }

}
