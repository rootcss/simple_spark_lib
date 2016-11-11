from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.functions import col

class SimpleSparkContext(object):
  conf = None
  sc = None
  sqlContext = None
  appName = "Simple PySpark Lib Example"
  master = "local[*]"

  def __init__(self):
    print "initializing.."

  def setConf(self, appName=None, cassandra_connection_config=None):
    if appName is not None:
      self.appName = appName

    if cassandra_connection_config is not None:
      self.conf = SparkConf().setAppName(self.appName)\
                  .set('spark.cassandra.connection.host', cassandra_connection_config['host'])\
                  .set('spark.cassandra.auth.username', cassandra_connection_config['username'])\
                  .set('spark.cassandra.auth.password', cassandra_connection_config['password'])
    else:
      self.conf = SparkConf().setAppName(self.appName)


  def setContext(self, master=None):
    if master is not None:
      self.master = master

    self.sc = SparkContext(master=self.master, conf=self.conf)

  def setSqlContext(self):
    self.sqlContext = SQLContext(self.sc)

  def cassandra_sql(self, cassandra_config=None):
    cluster = cassandra_config['cluster']
    all_tables = cassandra_config['tables']
    for temp_table_name in all_tables:
      keyspace, table_name = all_tables[temp_table_name].split('.')
      cmd = """
            CREATE TEMPORARY TABLE %s
            USING org.apache.spark.sql.cassandra
            OPTIONS ( table "%s",
                      keyspace "%s",
                      cluster "%s",
                      pushdown "True")
            """ % (temp_table_name, table_name, keyspace, cluster)
      print cmd
      self.sqlContext.sql(cmd)

  def execute(self, query):
    return self.sqlContext.sql(query)

  def getSparkContext(self):
    return self.sc

  def getSqlContext(self):
    return self.sqlContext

  def printConfig(self):
    print self.conf
    print self.sc
    print self.sqlContext
    print self.appName
    print self.master
