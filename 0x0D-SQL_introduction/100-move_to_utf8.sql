-- Used to convert the hbtn_0c_0 database, the first_table table, and the name field to UTF8.

-- Convert the database hbtn_0c_0 to UTF8 (utf8mb4).
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8 (utf8mb4).
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
