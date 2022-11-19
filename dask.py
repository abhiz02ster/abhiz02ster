import dask.dataframe as dd
ddf = dd.read_parquet('/Users/abhishek/targets/*.parquet', engine='pyarrow')
%time ddf
%time ddf['approvedSymbol'].value_counts().compute()
