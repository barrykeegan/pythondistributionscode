from Gaussian import Gaussian


def test_pytest():
    assert True

def test_Gaussian_default_values():
    myGauss = Gaussian()
    assert myGauss.mean == 0
    assert myGauss.stdev == 1
    assert len(myGauss.data) == 0

def test_Gaussian_specified_values():
    myGauss = Gaussian(mean = 2, stdev = 3)
    assert myGauss.mean == 2
    assert myGauss.stdev == 3
    assert len(myGauss.data) == 0

