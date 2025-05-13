import os
print("Reading DB from:", os.path.abspath("dev.duckdb"))

import duckdb
con = duckdb.connect("dev.duckdb")
print(con.execute("SELECT * FROM U").fetchall())

import duckdb
con = duckdb.connect('dev.duckdb')
print(con.execute("SHOW TABLES").fetchall())
