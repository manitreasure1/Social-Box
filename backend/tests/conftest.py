from fastapi.testclient import TestClient
from app import app
import pytest
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel.pool import StaticPool
from app.models.database import Database



@pytest.fixture
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine(
          "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name='client')
def client_fixture(session: Session):
    def get_session_overide():
        return session
    app.dependency_overrides[Database.get_session]= get_session_overide
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
    

    
