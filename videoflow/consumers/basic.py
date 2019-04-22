from ..core.node import ConsumerNode

class CommandlineConsumer(ConsumerNode):
    def __init__(self, sep = ' ', end = '\n'):
        self._end = end
        self._sep = sep
        super(CommandlineConsumer, self).__init__()
    
    def consume(self, item):
        print(item, sep = self._sep, end = self._end)