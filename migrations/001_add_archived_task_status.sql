ALTER TABLE tasks
MODIFY COLUMN status ENUM(
    'pending',
    'in_progress',
    'done',
    'archived'
) NOT NULL DEFAULT 'pending';
