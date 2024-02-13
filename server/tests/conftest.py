import pytest
from server.factory import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()