"""
Copyright 2021 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from dataclasses import dataclass

from google.protobuf.empty_pb2 import Empty
from cloudstate.event_sourced_context import EventSourcedCommandContext
from cloudstate.event_sourced_entity import EventSourcedEntity

from fraud_detection_common_pb2 import FraudDetectionState, ScoredTransactionState
from fraud_detection_domain_pb2 import FraudDetectionCreated, ScoredTransactionAdded, FraudDetectionRuleUpdated
from fraud_detection_service_pb2 import CreateFraudDetectionCommand, AddTransactionCommand, GetFraudDetectionCommand, \
    UpdateFraudDetectionRuleCommand
from fraud_detection_service_pb2 import _FRAUDDETECTIONSERVICE, DESCRIPTOR as FILE_DESCRIPTOR


@dataclass
class FraudDetectionState:
    customer_id: str
    created: bool
    rule_id: str
    max_amount_cents: int
    recent_transactions: []
    MAX_STATE_TRANSACTIONS: int = 100


def init(entity_id: str) -> FraudDetectionState:
    return FraudDetectionState(entity_id, [])


entity = EventSourcedEntity(_FRAUDDETECTIONSERVICE, [FILE_DESCRIPTOR], init)


@entity.command_handler("CreateFraudDetectionCommand")
def create_fraud_detection(state: FraudDetectionState, command: CreateFraudDetectionCommand,
                           ctx: EventSourcedCommandContext):
    if state.created:
        ctx.fail("FraudDetection already created")
    else:
        ctx.emit(FraudDetectionCreated(command.customer_id, command.rule_id, command.max_amount_cents))

    return Empty()


@entity.event_handler(FraudDetectionCreated)
def fraud_detection_created(state: FraudDetectionState, event: FraudDetectionCreated):
    state.created = True


@entity.command_handler("UpdateFraudDetectionRuleCommand")
def update_fraud_detection_rule(state: FraudDetectionState, command: UpdateFraudDetectionRuleCommand,
                                ctx: EventSourcedCommandContext):
    if not state.created:
        ctx.fail("FraudDetection does not exist")
    else:
        ctx.emit(FraudDetectionRuleUpdated(command.customer_id, command.rule_id, command.max_amount_cents))

    return Empty()


@entity.event_handler(FraudDetectionRuleUpdated)
def fraud_detection_rule_updated(state: FraudDetectionState, event: FraudDetectionRuleUpdated):
    state.rule_id = event.rule_id
    state.max_amount_cents = event.max_amount_cents


@entity.command_handler("AddTransactionCommand")
def add_transaction(state: FraudDetectionState, command: AddTransactionCommand, ctx: EventSourcedCommandContext):
    if not state.created:
        ctx.fail("FraudDetection does not exist")
    else:
        potential_fraud = True if command.max_amount_cents > state.max_amount_cents else False
        risk_score = True if potential_fraud else False
        ctx.emit(ScoredTransactionAdded(command.customer_id, command.transaction_id, command.timestamp,
                                        command.amount_cents, potential_fraud, risk_score))

    return Empty()


@entity.event_handler(ScoredTransactionAdded)
def scored_transaction_added(state: FraudDetectionState, event: ScoredTransactionAdded):
    state.recent_transactions.append(event)

    if state.recent_transactions.len() > state.MAX_STATE_TRANSACTIONS:
        state.recent_transactions.pop(0)


@entity.command_handler("GetFraudDetectionCommand")
def get_fraud_detection(state: FraudDetectionState, command: GetFraudDetectionCommand, ctx: EventSourcedCommandContext):
    if not state.created:
        ctx.fail("FraudDetection does not exist")

    return FraudDetectionState(command.customer_id, state.rule_id, state.max_amount_cents, state.recent_transactions)


@entity.snapshot()
def snapshot(state: FraudDetectionState):
    return state
