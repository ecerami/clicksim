# clicksim

Experimental scripts to generate simulated cBioPortal data for import to ClickHouse.

Note that this script currently creates simulated mutation and copy number data,
assuming a gene panel of ~500 genes.  It also creates simulated patient-level
or sample-level data.

Create new clickhouse database:

    make init

Create simulated data

    make sim

Load simulated data into clickhouse

    make load

The python script generates simulated data for N patients.  For example:

    python3 sim.py 1000 > data.tsv
