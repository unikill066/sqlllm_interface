import duckdb

DB_PATH = "college_admissions.duckdb"

def run_query(query: str, params: tuple | list = None, fetch: bool = True):
    """
    Execute any SQL query on the DuckDB database.
    
    Args:
        query (str): The SQL query to execute.
        params (tuple | list, optional): Parameters for a parameterized query.
        fetch (bool): If True, fetches and returns the result as a DataFrame.
                      If False, executes without returning (e.g. INSERT/UPDATE).
    
    Returns:
        pandas.DataFrame | None: Query results if fetch=True, otherwise None.
    """
    try:
        con = duckdb.connect(DB_PATH)
        if params:
            result = con.execute(query, params)
        else:
            result = con.execute(query)

        if fetch:
            df = result.fetchdf()
            con.close()
            return df
        else:
            con.close()
            return None

    except Exception as e:
        print(f"❌ Error executing query:\n{query}\n{e}")
        return None
