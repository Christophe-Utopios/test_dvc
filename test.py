import duckdb


duckdb.sql("COPY (SELECT * FROM 'data/exports/features.parquet' WHERE rayon <> 'boissons') TO 'data/exports/v2.parquet' (FORMAT PARQUET)")