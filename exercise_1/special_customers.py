import pandas as pd


def get_special_customers(con):
    """Identify special customers: customers with at least 1 order with a
        total value (including the discounts) equal to $65000 or more

    Args:
        con (db_connection): active database connection

    Returns:
        Dataframe with CustomerId and Total amount (Sum of all orders that fulfill the criteria grouped by customer)
    """
    rs = con.execute(
        "SELECT SpecialCustomers.CustomerID AS CustomerID, ROUND(SUM(SpecialCustomers.TotalPerOrder),2) AS Total FROM "
        "(SELECT c.Id AS CustomerID, SUM((od.UnitPrice - od.Discount) * od.Quantity) AS TotalPerOrder "
        "FROM Customer AS c INNER JOIN \'Order\' AS o ON c.Id = o.CustomerId "
        "INNER JOIN OrderDetail AS od ON o.Id = od.OrderId "
        "WHERE SUBSTR(o.OrderDate, 1, 4) = \'2015\' "
        "GROUP BY o.Id "
        "HAVING SUM((od.UnitPrice - od.Discount) * od.Quantity) >= 65000) AS SpecialCustomers "
        "GROUP BY CustomerID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    return df
