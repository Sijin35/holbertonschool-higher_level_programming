-- Create table with one field with default value and all values unqiue
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (ID)
	);
