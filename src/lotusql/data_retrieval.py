import sqlite3

def data_retrieval(sql_query: str) -> dict:    
    """
    Executes a SQL query on the specified SQLite database and returns the first result.
    Args:
        sql_query (str): The SQL query to execute.
    Returns:
        The first value of the first row in the result, or None if no results are found.
    """
    db_path="data/train.sqlite"
    print('\n\n\n*** sql_query:\n\n', sql_query)    
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            result = cur.fetchone()
        if result:
            return {"output": result[0], "status": "success"}
        else:
            return {"output": None, "status": "no results"}        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return {"output": None, "status": "SQL query generated is not valid."}

TABLE_SCHEMA = """ CREATE TABLE 'properties' (
'Id' INTEGER,
  'MSSubClass' INTEGER,
  'MSZoning' TEXT,
  'LotFrontage' REAL,
  'LotArea' INTEGER,
  'Street' TEXT,
  'Alley' TEXT,
  'LotShape' TEXT,
  'LandContour' TEXT,
  'Utilities' TEXT,
  'LotConfig' TEXT,
  'LandSlope' TEXT,
  'Neighborhood' TEXT,
  'Condition1' TEXT,
  'Condition2' TEXT,
  'BldgType' TEXT,
  'HouseStyle' TEXT,
  'OverallQual' INTEGER,
  'OverallCond' INTEGER,
  'YearBuilt' INTEGER,
  'YearRemodAdd' INTEGER,
  'RoofStyle' TEXT,
  'RoofMatl' TEXT,
  'Exterior1st' TEXT,
  'Exterior2nd' TEXT,
  'MasVnrType' TEXT,
  'MasVnrArea' REAL,
  'ExterQual' TEXT,
  'ExterCond' TEXT,
  'Foundation' TEXT,
  'BsmtQual' TEXT,
  'BsmtCond' TEXT,
  'BsmtExposure' TEXT,
  'BsmtFinType1' TEXT,
  'BsmtFinSF1' INTEGER,
  'BsmtFinType2' TEXT,
  'BsmtFinSF2' INTEGER,
  'BsmtUnfSF' INTEGER,
  'TotalBsmtSF' INTEGER,
  'Heating' TEXT,
  'HeatingQC' TEXT,
  'CentralAir' TEXT,
  'Electrical' TEXT,
  '1stFlrSF' INTEGER,
  '2ndFlrSF' INTEGER,
  'LowQualFinSF' INTEGER,
  'GrLivArea' INTEGER,
  'BsmtFullBath' INTEGER,
  'BsmtHalfBath' INTEGER,
  'FullBath' INTEGER,
  'HalfBath' INTEGER,
  'BedroomAbvGr' INTEGER,
  'KitchenAbvGr' INTEGER,
  'KitchenQual' TEXT,
  'TotRmsAbvGrd' INTEGER,
  'Functional' TEXT,
  'Fireplaces' INTEGER,
  'FireplaceQu' TEXT,
  'GarageType' TEXT,
  'GarageYrBlt' REAL,
  'GarageFinish' TEXT,
  'GarageCars' INTEGER,
  'GarageArea' INTEGER,
  'GarageQual' TEXT,
  'GarageCond' TEXT,
  'PavedDrive' TEXT,
  'WoodDeckSF' INTEGER,
  'OpenPorchSF' INTEGER,
  'EnclosedPorch' INTEGER,
  '3SsnPorch' INTEGER,
  'ScreenPorch' INTEGER,
  'PoolArea' INTEGER,
  'PoolQC' TEXT,
  'Fence' TEXT,
  'MiscFeature' TEXT,
  'MiscVal' INTEGER,
  'MoSold' INTEGER,
  'YrSold' INTEGER,
  'SaleType' TEXT,
  'SaleCondition' TEXT,
  'SalePrice' INTEGER
);"""

if __name__ == "__main__":
    sql_query = "SELECT COUNT(*) FROM properties;"
    result = data_retrieval(sql_query)
    print(result)