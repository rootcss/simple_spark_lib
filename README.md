### Simple Spark Lib
<ol>
<li>Enables you to use the capability of Spark without actually writing the spark codes.</li>
<li>Includes many workflows; which helps in writing codes and get your results in just few lines.</li>
<li>For power user, it allows you to tweak every step in the flow.</li>
</ol>

### Prerequisite:
This assumes that you have access to Apache Spark and Cassandra clusters.

### Installation:
Clone the repo and build with the command:
```bash
python setup.py install
```

### Uninstallation:
```bash
sudo pip uninstall simple_spark_lib
```

### Usage:
#### Cassandra Workflow example:
```python
# First, import your libraries
from simple_spark_lib import SimpleSparkCassandraWorkflow

# Define connection configuration for cassandra
cassandra_connection_config = {
  'host':     '192.168.56.101',
  'username': 'cassandra',
  'password': 'cassandra'
}

# Define Cassandra Schema information
cassandra_config = {
  'keyspace':         'simple_events_production',
  'table_name':       'api_events',
  'cluster':          'rootCSSCluster',
  'temp_table_name':  'api_events'
}

# Initiate your workflow
workflow = SimpleSparkCassandraWorkflow(appName="Simple Example Worker")

# Setup the workflow with configurations
workflow.setup(cassandra_connection_config, cassandra_config)

# Run your favourite query
df = workflow.process(query="SELECT * FROM api_events")

print df.take(10)
```

Run this example with the command:
```bash
simple-runner filename.py -d cassandra
```
