/* Schema tells me each row has same number columns with values for columns formatted the same way. e.g column 1  is string
 column 2 is float. missing values are set to nan or 0  A schema could convert a number to a string if a number was 
 entered in a string column */

SELECT * FROM aadhaar_data
LIMIT 20 /* show 20 rows from data base */

SELECT district FROM aadhaar_data
LIMIT 20 /* show 20 districts */

/* more comlex */

SELECT * FROM aadhaar_data
WHERE state = 'Gujrat'

/* aggreate funtion: count min max, sum */
SELECT district SUM(aadhaar_generated)
FROM aadhaar_data GROUP BY district

/* goup by ... only want one row per district
can add where clause etc */

