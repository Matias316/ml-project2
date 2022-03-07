import pandas as pd


def get_countries_with_suppliers_or_customers(con):
    """Retrieves countries where suppliers and/or customers are based

    Args:
        con (db_connection): active database connection

    Returns:
        Dataframe with Countries
    """

    rs = con.execute("SELECT c.Country FROM Customer AS c UNION SELECT s.Country FROM Supplier AS s")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    return df
