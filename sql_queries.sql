# switchup queries

# Which school and program has highest ratings?
SELECT switchup.students.program AS PROGRAM, 
switchup.students.school_name AS SCHOOL, 
AVG(switchup.reviews.overall_score) AS AVERAGE_SCORE, 
COUNT(switchup.students.review_id) AS NUMBER_OF_REVIEWS
FROM switchup.reviews
INNER JOIN switchup.students
ON switchup.reviews.review_id = switchup.students.review_id
GROUP BY PROGRAM, SCHOOL
ORDER BY AVERAGE_SCORE DESC;

# The proportion of reviews that contain the word "intensive"
SELECT switchup.students.program AS PROGRAM, 
switchup.students.school_name AS SCHOOL, 
(COUNT(review_freq.FREQUENCY) / COUNT(switchup.students.review_id))*100 AS PROPORTION_OF_REVIEW_MENTIONS
FROM switchup.students
LEFT JOIN (SELECT switchup.reviews.review_id, COUNT(switchup.reviews.review_id) AS FREQUENCY
FROM switchup.reviews
WHERE switchup.reviews.review_body LIKE "%expensive%"
GROUP BY switchup.reviews.review_id) AS review_freq
ON switchup.students.review_id = review_freq.review_id
GROUP BY PROGRAM, SCHOOL
ORDER BY PROPORTION_OF_REVIEW_MENTIONS DESC;


# average score less than one year after graduation
SELECT AVG(switchup.reviews.overall_score) AS AVERAGE_SCORE_LESS_THAN_1_YEAR, (SELECT AVG(switchup.reviews.overall_score)
FROM switchup.reviews
WHERE switchup.reviews.years_since_graduation > 0) AS AVERAGE_SCORE_MORE_THAN_1_YEAR
FROM switchup.reviews
WHERE switchup.reviews.years_since_graduation = 0;

# Average score for those who had finished the program by the time of the review and those who didn't
SELECT switchup.students.is_alumni AS FINISHED_PROGRAM, 
AVG(switchup.reviews.overall_score) AS OVERALL_SCORE
FROM switchup.students
INNER JOIN switchup.reviews
ON switchup.students.review_id = switchup.reviews.review_id
GROUP BY FINISHED_PROGRAM;

# How many finsihed program and how many didn't
SELECT switchup.students.is_alumni AS FINISHED_PROGRAM, COUNT(switchup.students.is_alumni)
FROM switchup.students
GROUP BY FINISHED_PROGRAM;

# Average score by job title
SELECT switchup.students.job_title AS JOB_TITLE, AVG(switchup.reviews.overall_score) AS OVERALL_SCORE, COUNT(switchup.reviews.review_id) AS NUMBER_OF_REVIEWS
FROM switchup.students
INNER JOIN switchup.reviews
ON switchup.students.review_id = switchup.reviews.review_id
GROUP BY JOB_TITLE;



