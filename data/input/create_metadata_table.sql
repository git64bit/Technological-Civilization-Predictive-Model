-- Create the metadata table
CREATE TABLE IF NOT EXISTS metadata (
    id INTEGER PRIMARY KEY,
    table_name TEXT NOT NULL,
    field_name TEXT NOT NULL,
    data_type TEXT,
    description TEXT
);

-- Add initial metadata entries if needed
-- INSERT INTO metadata (table_name, field_name, data_type, description) VALUES ('table_name_here', 'field_name_here', 'data_type_here', 'description_here');
