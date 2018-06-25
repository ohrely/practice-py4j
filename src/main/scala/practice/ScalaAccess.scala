package practice

import py4j.GatewayServer

/**
  * Created by rely10 on 9/11/17.
  */
class ScalaAccess {
  def main(args: Array[String]) = {
    val gs: GatewayServer = new GatewayServer(new ScalaAccess)
    gs.start
  }
}
