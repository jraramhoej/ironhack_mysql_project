# create new database
create_database = """CREATE DATABASE switchup3;"""

# create reviews table
create_reviews = """CREATE TABLE IF NOT EXISTS
switchup3.reviews(
id INT PRIMARY KEY AUTO_INCREMENT,
review_id INT NOT NULL UNIQUE,
tagline TEXT,
created_at DATE,
years_since_graduation INT,
overall_score FLOAT,
overall FLOAT,
curriculum FLOAT,
job_support FLOAT,
review_body TEXT,
school_name VARCHAR(50));"""

# create students table
create_students = """CREATE TABLE IF NOT EXISTS
switchup.students(
id INT PRIMARY KEY AUTO_INCREMENT,
review_id INT NOT NULL,
student_name VARCHAR(50),
graduating_year YEAR,
is_alumni BOOLEAN,
job_title VARCHAR(200),
program VARCHAR(200),
school_name VARCHAR(200),
FOREIGN KEY (review_id) REFERENCES reviews(review_id));"""

