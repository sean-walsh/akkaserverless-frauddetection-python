"""
Copyright 2021 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from cloudstate.cloudstate import CloudState
from fraud_detection_entity import entity as fraud_detection_entity
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    CloudState().register_event_sourced_entity(fraud_detection_entity).start()
