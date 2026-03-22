import sqlite3
import pandas as pd


conn = sqlite3.connect("data.sqlite")

all_employees = pd.read_sql(
    """ 
    SELECT
      firstName,lastName,email
      FROM employees
      WHERE lastName = "Patterson"
      ;
    """,
    conn,
)

employees_5_letter_name = pd.read_sql(
    """
    SELECT 
        *, LENGTH(firstName) as length_name
                FROM employees
                    WHERE length_name = 5
            ;
""",
    conn,
)

employee_substr_L = pd.read_sql(
    """
        SELECT 
            *, SUBSTR(firstName,1,1) as name_substring
            FROM employees
            WHERE name_substring = "L"
            ;
    """,
    conn,
)

order_price_cast_30 = pd.read_sql(
    """
    SELECT 
    *, 
    CAST(ROUND(priceEach) as INTEGER) as rounded
    FROM orderDetails
    WHERE rounded = 30
    ;
    """,
    conn,
)

all_between_day = pd.read_sql(
    """
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE days_late > 0;
""",
    conn,
)

print(all_between_day)
