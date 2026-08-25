import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Bien module-level -> chi duoc khoi tao 1 lan / execution environment
_engine = None
_SessionFactory = None


def _build_db_url() -> str:
    user = os.environ.get("DB_USER", "postgres")
    password = os.environ.get("DB_PASSWORD", "postgres")
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    name = os.environ.get("DB_NAME", "appdb")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


def get_engine():
    global _engine
    if _engine is None:
        logger.info("[COLD START] Tao SQLAlchemy engine + connection pool moi")
        _engine = create_engine(
            _build_db_url(),
            pool_size=int(os.environ.get("DB_POOL_SIZE", "2")),       # nho vi moi container co pool rieng
            max_overflow=int(os.environ.get("DB_MAX_OVERFLOW", "0")),  # khong cho tao vuot pool_size
            pool_timeout=int(os.environ.get("DB_POOL_TIMEOUT", "5")),  # cho toi da 5s de lay duoc connection
            pool_recycle=int(os.environ.get("DB_POOL_RECYCLE", "280")),  # tai tao connection cu
            pool_pre_ping=True,  # ping truoc khi dung, tu dong bo qua connection da chet
            future=True,
        )
    else:
        logger.info("[WARM START] Tai su dung engine + connection pool san co")
    return _engine


def get_session():
    global _SessionFactory
    if _SessionFactory is None:
        _SessionFactory = scoped_session(
            sessionmaker(bind=get_engine(), autoflush=False, autocommit=False, future=True)
        )
    return _SessionFactory()


def dispose_engine():
    global _engine, _SessionFactory
    if _engine is not None:
        _engine.dispose()
        _engine = None
        _SessionFactory = None
