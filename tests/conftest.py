import pytest

# Pytest Cassettes: Forget about mocks or live requests
# Reference 1: https://code.kiwi.com/articles/pytest-cassettes-forget-about-mocks-or-live-requests/
# Reference 2: https://www.andreagrandi.it/2022/12/02/ignore-hosts-with-python-vcr/
@pytest.fixture(scope="module")
def vcr_config():
    # Default config for recording cassettes
    return {
        "filter_headers": ["authorization"], # won't record any authorization headers
        "ignore_localhost": True, # only want to record third-party APIs
        "record_mode": "once",
    }