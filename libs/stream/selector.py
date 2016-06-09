from collections import Iterable

from libs.stream.processor import Processor


class Selector(Processor):
    def __init__(self, streams):
        self._streams = streams

    def process(self, message) -> Iterable:
        if str(message).startswith(self._streams):
            yield message
