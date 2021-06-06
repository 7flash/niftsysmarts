import pytest

############ Mocks ########################
@pytest.fixture(scope="module")
def dai(accounts, TokenMock):
    dai = accounts[0].deploy(TokenMock,"DAI MOCK Token", "DAI")
    yield dai

@pytest.fixture(scope="module")
def erc721mock(accounts, Token721Mock):
    """
    Simple NFT with URI
    """
    t = accounts[0].deploy(Token721Mock, "Simple NFT with URI", "XXX")
    #t.setURI(0, 'https://maxsiz.github.io/')
    yield t    
############################################


@pytest.fixture(scope="module")
def niftsy20(accounts, Niftsy):
    erc20 = accounts[0].deploy(Niftsy)
    yield erc20 

@pytest.fixture(scope="module")
def wrapper(accounts, Wrapper721, niftsy20):
    t = accounts[0].deploy(Wrapper721, niftsy20.address)
    niftsy20.addMinter(t.address, {'from':accounts[0]})
    yield t 

 



