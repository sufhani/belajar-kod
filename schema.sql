DROP TABLE if exists guides;
CREATE TABLE guides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    body TEXT,
    timestamp TIMESTAMP
);