import polars as pl


def describe(df: pl.DataFrame, tbl_rows: int | None = None) -> pl.DataFrame:
    with pl.Config() as plc:
        plc.set_tbl_rows(tbl_rows or (len(df.columns) + 1))
        return (
            df.describe()
            .with_columns(pl.col("statistic").str.to_uppercase())
            .transpose(include_header=True)
            .with_columns(pl.col("column").str.to_uppercase())
        )
