from sqlalchemy import create_engine


def connect_db(path_to_db):
    """Create a connection to database

    Args:
        path_to_db

    Returns:
        con: DB connection object
    """
    engine = create_engine('sqlite:///' + path_to_db)
    con = engine.connect()
    return con
