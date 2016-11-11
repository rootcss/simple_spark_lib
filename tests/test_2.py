import sys
sys.path.append("../simple_spark_lib")

from SimpleSparkContext import SimpleSparkContext

cassandra_connection_config = {
  'host':     '192.168.56.101',
  'username': 'cassandra',
  'password': 'cassandra'
}
cassandra_config = {
  'cluster': 'rootCSSCluster',
  'tables': {
    'api_events': 'simpl_events_production.api_events',
    'transactions': 'simpl_events_production.transactions',
    'api_events2':'cequel_development.api_events',
  }
}

ssc = SimpleSparkContext()
ssc.setConf(cassandra_connection_config=cassandra_connection_config)
ssc.setContext()
ssc.setSqlContext()
ssc.cassandra_sql(cassandra_config=cassandra_config)
print ssc.execute("SELECT bucket_id, event_name FROM api_events").count()
print ssc.execute("SELECT * FROM transactions").count()
print ssc.execute("SELECT * FROM api_events2").count()
