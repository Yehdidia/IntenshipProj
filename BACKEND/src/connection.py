from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from src.config import Config
from sqlalchemy.orm import sessionmaker

class Connect():
    postgres_file_name = "attendance_db"
    #postgres_url = f"postgres:///{postgres_file_name}"
    #postgres_url = "postgresql://username:password@localhost:5432/attendance_db"
 
    engine = AsyncEngine(
        create_engine(Config.DATABASE_URL, echo=True)

    )
    #engine = create_engine(Config.DATABASE_URL)
    #engine = create_engine(postgres_url)

    SessionLocal = sessionmaker(autocommit=False, class_=AsyncSession, autoflush=False, bind=engine)

    
    async def init_db(self):
        async with self.engine.begin() as conn:
            from src.user import model
            await conn.run_sync(SQLModel.metadata.create_all)

    #SQLModel.metadata.create_all(engine)

connect = Connect()