from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://SauEW4FB21a5ZEs.root:z9xUrDcEImv0DHCu@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/test"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
base = Base  # Alias to support both lowercase and uppercase imports
