from mtp.core import capital_case

def test_capital_case():
    assert capital_case('capital case') == 'Capital case'
