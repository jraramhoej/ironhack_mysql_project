# create new database
create_database = """CREATE DATABASE switchup;"""

# create reviews table
create_reviews = """CREATE TABLE IF NOT EXISTS
switchup.reviews(
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
job_title TEXT,
program VARCHAR(50),
school_name VARCHAR(50),
FOREIGN KEY (review_id) REFERENCES reviews(review_id));"""

# create words table
create_words = """CREATE TABLE IF NOT EXISTS
switchup.words(
id INT PRIMARY KEY AUTO_INCREMENT,
review_id INT NOT NULL,
word TEXT,
FOREIGN KEY (review_id) REFERENCES reviews(review_id));"""
