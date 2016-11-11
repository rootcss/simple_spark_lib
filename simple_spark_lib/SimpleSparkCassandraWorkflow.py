from SimpleSparkContext import SimpleSparkContext

class SimpleSparkCassandraWorkflow(SimpleSparkContext):
  simple_sc = None
  appName = None
  master = None

  def __init__(self, appName=None, master=None):
    self.appName = appName
    self.master = master

  def setup(self, cassandra_connection_config=None, cassandra_config=None):
    self.simple_sc = SimpleSparkContext()
    self.simple_sc.setConf(appName=self.appName, cassandra_connection_config=cassandra_connection_config)
    self.simple_sc.setContext(master=self.master)
    self.simple_sc.setSqlContext()
    self.simple_sc.cassandra_sql(cassandra_config=cassandra_config)

  def process(self, query=None):
    return self.simple_sc.execute(query=query)
