package practice

import org.apache.spark.sql.DataFrameReader
/**
  * Created by ohrely on 9/11/17.
  */
object ScalaObj {
  def two(): Int = 2

  implicit class DFR(dfr: DataFrameReader) {
    def three(): Int = 3
  }
}
