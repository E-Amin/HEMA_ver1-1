#####   Heuristic Ensembl Meta-Analysis (HEMA) ver.1  #####

The Heuristic Ensembl Meta-Analysis platform (HEMA) represents a new user-approachable platform consisting of an adapted Ensembl database schema, data pre-processing pipeline to populate the database tables, and data analysis pipeline containing structured queries that can explore systematic questions of any calculated sequence property associated with any subset of genic features. 

#####   SYSTEM REQUIREMENTS  #####

#Requires setting up an Ensembl Core database on MySQL server. Installing and populating Ensembl Core database tables can be found in the following link: https://m.ensembl.org/info/docs/webcode/mirror/install/ensembl-data.html.

#The Python scripts of pre-processing and data analysis pipelines can be run using Python ver. 2.7.12.

#The pseudo-chromosome FASTA files for the target species.

##### RUNNING HEMA #####

#The first folder (1_ER_model) contains the ER model of HEMA system that able to integrate into the Ensembl Core relational database schema.

#The second folder (2_SQL_statements_DDL) contains the sQL statements that able to create the HEMA table into the Ensembl Core relational database schema.

#The third folder (3_Data_pre-processing_pipeline) contains the three Python scripts that can generate the data for three HEMA-specific tables:
 
1- For the “transcript_feature” and “seq_region_pos” tables, the Python scripts require the pseudo-chromosome FASTA files for the target species.

2- The Python script for the third table “seq_region_pos_attrib_value” can generate the property value for GC-content and for 11 DNA physicochemical properties with different sliding window sizes (11 and 101). 

#The fourth folder (4_Data_analysis_pipeline) contains Pseudo-codes and Python script that can be used to calculated the frequency distribution and the profiles of different properties.
