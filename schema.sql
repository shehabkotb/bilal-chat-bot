-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  surah_reciter VARCHAR(255) DEFAULT 'afs',
  verse_reciter VARCHAR(255) DEFAULT 'ar.alafasy'
);

