import pandas as pd


def get_high_freight(con):
    """Find the 4 countries with the maximum arithmetic mean of Freight involving the last 24 months of order data
    where the end date corresponds to the maximum OrderDate

    Args:
        con (db_connection): active database connection

    Returns:
        Dataframe with median and Country name
    """
    rs = con.execute("SELECT ROUND(AVG(Freight),5) AS AverageFreight, ShipCountry "
                     "FROM \'Order\' "
                     "WHERE OrderDate >= datetime((SELECT MAX(OrderDate) FROM \'Order\'), \'-24 months\') "
                     "GROUP BY ShipCountry "
                     "ORDER BY AverageFreight DESC "
                     "LIMIT 4")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    return df
