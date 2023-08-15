-- Used to list all records of the table second_table from the specified database.
-- List all records of the table second_table, ordered by score (top first).
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
