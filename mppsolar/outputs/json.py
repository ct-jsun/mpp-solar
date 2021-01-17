import json as js
import logging

from .baseoutput import BaseOutput

log = logging.getLogger("MPP-Solar")


class json(BaseOutput):
    def __init__(self, *args, **kwargs) -> None:
        log.debug(f"processor.json __init__ kwargs {kwargs}")

    def output(self, *args, **kwargs):
        log.info("Using output processor: json")
        log.debug(f"processor.json.output kwargs {kwargs}")
        data = self.get_kwargs(kwargs, "data")
        print(js.dumps(data))
