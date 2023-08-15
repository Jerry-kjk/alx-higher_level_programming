-- Used to list all records of the table second_table from the specified database.
-- List all records with a name value of the table second_table, ordered by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
