"""Slashing module messages types."""

from __future__ import annotations

import attr
from terra_proto.cosmos.slashing.v1beta1 import MsgUnjail as MsgUnjail_pb

from terra_sdk.core import ValAddress
from terra_sdk.core.msg import Msg
from typing import cast
__all__ = ["MsgUnjail"]


@attr.s
class MsgUnjail(Msg):
    """Attempt to unjail a jailed validator (must be submitted by same validator).

    Args:
        validator_addr: validator address to unjail"""

    type_amino = "slashing/MsgUnjail"
    """"""
    type_url = "/cosmos.slashing.v1beta1.MsgUnjail"
    """"""
    action = "unjail"
    """"""

    validator_addr: ValAddress = attr.ib()

    def to_amino(self) -> dict:
        return {"type": self.type_amino, "value": {"validator_addr": self.validator_addr}}

    @classmethod
    def from_data(cls, data: dict) -> MsgUnjail:
        return cls(validator_addr=data["validator_addr"])

    def to_proto(self) -> MsgUnjail_pb:
        return MsgUnjail_pb(validator_addr=self.validator_addr)

    @classmethod
    def from_proto(cls, proto: MsgUnjail_pb) -> MsgUnjail:
        return cls(validator_addr=cast(ValAddress, proto.validator_addr))
