from emission_trading import buy_or_sell, trading


def test_buy_or_sell():
    assert buy_or_sell(500, 250) == True


#def test_buy_or_sell():
#     assert buy_or_sell(100, 250) == print('The company can sell allocations')


def test_trading():
    assert trading(20, 15) == True

def test_trading():
    assert trading(20, 15) == print('Trading is possible...')