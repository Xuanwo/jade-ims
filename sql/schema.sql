DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  title string NOT NULL,
  text  string NOT NULL
);
SELECT *
FROM entries