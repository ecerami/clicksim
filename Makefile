LINTER = flake8
FORMATTER = black

init:
	clickhouse client --multiline --multiquery < db.sql

sim:
	python3 sim.py 100000 > data.tsv

load:
	clickhouse client -q "INSERT INTO cbioportal.sample_fact FORMAT TabSeparated" < data.tsv
