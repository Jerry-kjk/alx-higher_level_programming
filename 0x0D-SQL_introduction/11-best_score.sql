-- Used to list all records with a score >= 10 from the table second_table in the specified database.
-- List all records with a score >= 10 from the table second_table, ordered by score (top first).
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
