
from datadog.dogstatsd.base import DogStatsd

class StatsClient(DogStatsd):
    def __init__(self, host='localhost', port=8125, prefix=None, namespace=None, **kwargs):
        assert prefix is None or namespace is None, "prefix is the same as namespace, so please leave None"
        if prefix is not None:
            namespace = prefix
        super(ProcessorWithInputCallback, self).__init__(host=host, port=port, namespace=namespace, **kwargs)

    timer = timed
    incr = increment
    decr = decrement

statsd = StatsClient()
