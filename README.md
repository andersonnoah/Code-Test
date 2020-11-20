# README

## Requirements and instructions for running locally
To run this project locally:
- Download and extract the zip file to desired location
- Using your command-line/terminal window of choice, navigate to directory where the now extracted folder is located. Personally, I use Git Bash on Windows.
- Once you are in the correct directory (you can check this by using a list command), run the program 'test.py' by typing 'python test.py' in your terminal window and pressing 'Enter'. This will execute the program. Then, in your working directory, 'test.py' will automatically generate the two requested JSON files (ChineseArt.json and 1940_1980.json). Note that if you run the program again, both JSON files will be overwritten with updated versions.


## My approach
My approach for this problem was to first inspect the data in the provided database file. To do this, I downloaded an SQLite GUI for Windows from https://sqlitestudio.pl/. Then, programmatically, I created a connection to the database. After establishing a connection, I performed SQL queries to retrieve the requested data. Once I had the data, I temporarily stored it before writing it to a JSON file. For me, this was the most logical way to go about solving the problem. My approach for this test was to solve each step incrementally, only moving to the next part when I had finished the previous step. Answering the question "Were there any alternatives that you considered?," I would say no. While this is true, the way I went about writing the SQL queries did vary. By playing around with different ways to query the data I found out that SQLite does not support RIGHT and FULL OUTER JOINS. So, I had to work around not being able to use those methods.

In addition, I would like to highlight some of the design decisions that I made. First, because the instructions for the task were semi-vague, I was not sure whether the range 1940-1980 was inclusive or not. Selecting the range 1940-1980 in SQL lead to results ranging from 1941-1981. So, I decided to change the range to 1939-1981 to include 1940 and 1980. Also, when referring to the task, I was asked for "All artworks...". Since this could mean accession number, artwork ID, or title, I chose what I thought suited the task best. Piggybacking off of this, for the all artworks in the Chinese Art department part of the task, I decided not to include the department in my query because I felt it was redundant. The last notable decision I made was determining what to do with special characters within the JSON files. Because Python's JSON module takes the "safe" route and escapes non-ascii characters, I chose to leave the special characters as is. In the future, conforming JSON parsers should handle this format correctly.  


## Requirements and dependencies for running the code/generating the JSON files
- Python 3.7.6
