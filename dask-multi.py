

### With multi threading -
### Downloaded sample parquet from below : 
### ftp.ebi.ac.uk/pub/databases/opentargets/platform/22.09/output/etl/parquet/targets

import dask.dataframe as dd

from distributed import Client, LocalCluster

cluster = LocalCluster(n_workers=8, threads_per_worker=4)

client = Client(cluster, asynchronous=True)

client

ddf = dd.read_parquet('/Users/abhishek/Downloads/block*.parquet')

###Command to test the performance

%time ddf

%time ddf('id').value_counts().compute()

%time ddf['approvedSymbol'].value_counts().compute()
