from typing import Any, Dict, Tuple

from api.controllers import get_commitment, get_score
from api.financial import SimulatePMT
from api.model.database import Database
from api.policy.base import BasePolicy, PolicyStatus
from api.utils.dates import is_older_then_18


class AgePolicy(BasePolicy):
    def __init__(self, _id, birth_date, testing=None):
        super().__init__(_id, testing)
        self.birth_date = birth_date

    def check(self) -> Tuple[PolicyStatus, Dict[str, Any]]:
        metadata = {"metadata": {}}
        if not is_older_then_18(self.birth_date):
            return self._deny(), metadata
        return self._approve(), metadata

    def set_policy_accepted(self):
        """It just return None"""

    def set_policy_denied(self):
        with Database(self.testing) as db:
            self.loan = db.find_and_set_loan_refused_by_age(self._id)


class ScorePolicy(BasePolicy):
    def __init__(self, _id, cpf, testing=None):
        super().__init__(_id, testing)
        self.score = get_score(cpf)

    def check(self) -> Tuple[PolicyStatus, Dict[str, Any]]:
        metadata = {"metadata": {"score": self.score}}
        if self.score < 600:
            return self._deny(), metadata
        return self._approve(), metadata

    def set_policy_accepted(self):
        """It just return None"""

    def set_policy_denied(self):
        with Database(self.testing) as db:
            self.loan = db.find_and_set_loan_refused_by_score(self._id, self.score)


class CommitmentPolicy(BasePolicy):
    def __init__(self, _id, amount, income, cpf, score, testing=False):
        super().__init__(_id, testing)
        self.commitment = get_commitment(cpf)
        self.score = score
        self.income = income
        self.amount = amount
        self.pmt = None

    def check(self) -> Tuple[PolicyStatus, Dict[str, Any]]:
        available_income = self.income * (1 - self.commitment)
        self.pmt = SimulatePMT(self.amount, available_income, self.score).simulate()

        metadata = {"metadata": {"score": self.score, "commitment": self.commitment}}

        if self.pmt.status:
            return (
                self._approve(),
                metadata,
            )

        return (
            self._deny(),
            metadata,
        )

    def set_policy_accepted(self):
        with Database(self.testing) as db:
            self.loan = db.find_and_set_loan_accept(
                self._id, self.amount, self.pmt.terms, self.score, self.commitment
            )

    def set_policy_denied(self):
        with Database(self.testing) as db:
            self.loan = db.find_and_set_loan_refused_by_commitment(
                self._id, self.score, self.commitment
            )
