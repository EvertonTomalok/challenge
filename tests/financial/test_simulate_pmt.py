from functools import partial

from api.financial import PMT, SimulatePMT
from api.financial.rate import get_rate as gt


def test_pmt_calculate(snapshot):
    pmt = PMT(2000, 0.039, 6).calculate()

    snapshot.assert_match(pmt)


def test_pmt_challenge_values():
    """
    In this case we'll assuming score 730
    """
    score = 730

    get_rate = partial(gt, score)

    # 6 terms
    rate_6 = get_rate(6)
    pmt_6 = PMT(2500, rate_6, 6).calculate()
    assert int(pmt_6) == 500
    assert rate_6 == 0.055

    # 9 terms
    rate_9 = get_rate(9)
    pmt_9 = PMT(2500, rate_9, 9).calculate()
    assert int(pmt_9) == 364
    assert rate_9 == 0.058

    # 12 terms
    rate_12 = get_rate(12)
    pmt_12 = PMT(2500, rate_12, 12).calculate()
    assert int(pmt_12) == 299
    assert rate_12 == 0.061


def test_pmt_available(snapshot):
    info = {"pv": 2500, "income": 300, "score": 900}
    simulation = SimulatePMT(**info).simulate()
    status = simulation.status
    pmt = simulation.pmt
    terms = simulation.terms
    message = simulation.message

    snapshot.assert_match(status)
    snapshot.assert_match(pmt)
    snapshot.assert_match(terms)
    snapshot.assert_match(message)


def test_pmt_not_available(snapshot):
    info = {"pv": 5000, "income": 300, "score": 900}
    simulation = SimulatePMT(**info).simulate()
    status = simulation.status
    message = simulation.message

    snapshot.assert_match(status)
    snapshot.assert_match(message)
