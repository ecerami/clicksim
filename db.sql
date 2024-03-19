drop database if exists cbioportal;
create database cbioportal;
use cbioportal;

create table sample_fact (
    /** Context Fields **/
    study_stable_id String,
    sample_stable_id String,
    patient_stable_id String,
    gene_entrez_id UInt32,
    gene_hugo_symbol String,
    clinical_attribute String,

    /** Fact Fields **/
    fact_type String,
    value_str String,
    value_int Int16,
    value_float Float64,
)
ENGINE = MergeTree()
ORDER BY tuple(study_stable_id, sample_stable_id)