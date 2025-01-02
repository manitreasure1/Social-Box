from sqlmodel import create_engine, SQLModel, Session

class DatabaseConfig:
    def __init__(self, sqlite_url: str):
        self.engine = create_engine(sqlite_url)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            try:
                yield session
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()

sqlite_url = "sqlite:///socialbox.db"
Database = DatabaseConfig(sqlite_url)

    

