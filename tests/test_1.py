import sys
sys.path.append("../simple_spark_lib")

from SimpleSparkCassandraWorkflow import SimpleSparkCassandraWorkflow
import json

cassandra_connection_config = {
  'host':     '192.168.56.101',
  'username': 'cassandra',
  'password': 'cassandra'
}
cassandra_config = {
  'cluster': 'rootCSSCluster',
  'tables': {
    'api_events': 'simpl_events_production.api_events'
  }
}

workflow = SimpleSparkCassandraWorkflow(appName="Simple Example Worker")
workflow.setup(cassandra_connection_config, cassandra_config)

query = "SELECT * FROM api_events WHERE event_name = 'UserApprovedEvent'"
df_payload = workflow.process(query=query)

def mapper(bbb):
  return (bbb['merchant']['id'], bbb['user']['id'], bbb['user']['first_name'])

zzz = df_payload\
        .select("payload")\
        .flatMap(lambda p: p)\
        .map(lambda a: json.loads(a))

abc1 = zzz\
          .map(lambda bbb: mapper(bbb))

print abc1.take(10)
