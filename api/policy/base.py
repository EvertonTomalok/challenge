from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Any, Dict, Tuple

from api.utils.enumerators import Status

PolicyStatus = namedtuple("PolicyStatus", "status loan")


class BasePolicy(ABC):
    def __init__(self, _id, testing=False):
        self._id = _id
        self.testing = testing
        self.loan = None

    @abstractmethod
    def check(self) -> Tuple[PolicyStatus, Dict[str, Any]]:
        """Check if the policy is valid"""

    def _approve(self) -> PolicyStatus:
        """Approve the policy"""
        self.set_policy_accepted()
        return PolicyStatus(Status.success.value, self.loan)

    def _deny(self) -> PolicyStatus:
        self.set_policy_denied()
        return PolicyStatus(Status.error.value, self.loan)

    @abstractmethod
    def set_policy_accepted(self):
        """
        Set loan accepted on Database and set the property self.loan
        """

    @abstractmethod
    def set_policy_denied(self):
        """
        Set loan denied on Database and set the property self.loan
        """
