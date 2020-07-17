from collections import namedtuple
from math import pow

from api.financial.rate import get_rate
from api.utils.enumerators import Status

Simulation = namedtuple("Simulation", "status pmt terms message")


class SimulatePMT:
    def __init__(self, pv, income, score, terms=None):
        """
        This class will simulate if a loan is available for some client.
        :param pv: Int => future value
        :param income: Int => The 'leftover' income that client has per
                        month, to pay the term
        :param score: Int => The score from this client
        :param terms: The available terms to be evaluated
        """
        self.pv = pv
        self.income = income
        self.score = score
        self.terms = terms or [6, 9, 12]

    def simulate(self) -> Simulation:
        """
        It simulates if is safe to give the loan to the client.
        :return: namedtuple => Simulation(status, pmt, term, message)
        """

        # TODO use recursive function
        for term in self.terms:
            actual_rate = get_rate(self.score, term)
            pmt = PMT(self.pv, actual_rate, term).calculate()
            if pmt <= self.income:
                return Simulation(Status.success.value, pmt, term, "Loan is available")
        else:
            return Simulation(Status.error.value, 0, 0, "Loan is not available")


class PMT:
    def __init__(self, pv, rate, per):
        """
        This class calculate the PMT.
        :param pv: Int => future value
        :param rate: Int => the rate
        :param per: Int => Number of months to be used
        :return: Int => The pmt value
        """
        self.pv = pv
        self.rate = rate
        self.per = per

    def _nper(self):
        return pow((1 + self.rate), self.per)

    def calculate(self) -> float:
        nper = self._nper()

        return self.pv * ((nper * self.rate) / (nper - 1))
