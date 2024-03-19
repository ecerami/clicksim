# clicksim

Experimental scripts to generate simulated cBioPortal data for import to ClickHouse.

Create new clickhouse database:

    make init

Create simulated data

    make sim

Load simulated data into clickhouse

    make load

The python script generates simulated data for N patients.  For example:

    python3 sim.py 1000 > data.tsv
