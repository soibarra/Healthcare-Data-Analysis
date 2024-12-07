-- Query to identify data anomalies (e.g., missing values)
SELECT * 
FROM dataset
WHERE Treatment_Cost IS NULL;

-- Query to trace data lineage (mapping diagnoses to providers)
SELECT Diagnosis_Code, Provider_ID, COUNT(*) AS Patient_Count
FROM dataset
GROUP BY Diagnosis_Code, Provider_ID;

