#!/usr/bin/env bash

export SPARK_HOME="/Users/rely10/spark-2.1.1-bin-hadoop2.7"
export TARGET_PATH="/Users/rely10/bloomberg/spark/extratests/practice_py4j/target"

${SPARK_HOME}/bin/spark-submit \
--master local \
--jars ${TARGET_PATH}/practice_py4j-1.0_s2.2.0-SNAPSHOT.jar \
--conf spark.driver.extraClassPath="protobuf-java-2.6.1.jar" \
--conf spark.sql.warehouse.dir="/tmp" \
/Users/rely10/bloomberg/spark/extratests/practice_py4j/src/main/python/practice/PythonGatewayTest.py