# PurePython_ReportGenerator
Outcome of a 1 week coding challenge, for masters course work. 

############################################ PART 1: STAR ANALYSIS ######################################################################

SITUATION: 

We were given 1 week to complete this assessement. At this point, I completed 2 cash_register projects (also using pure python) - a functional programming version and a OOP version.
The cash_register OOP version was my first serving of spaghetti code (see PurePython_CashRegister_OOPversion). I was determined the lessons I learned from that project and design modulated and highly readable code. 

TASK:

The task was to create a report generator for students entering in 'challenges'. We were instructed to complete the assignment level by level (e.g pass, credit, distinction, high distinction) with each 
level increasing in difficulty. Below are some key parameters of the project (full specifications are provided in PART 2 of this README).

- pure python code. No imports except for sys and datetime. 
- 1 week. 
- Individual assignment. 
- strictly OOP. 

ACTION:

- First, I spent some time considering the full use cases for the HD level and designed the classes and data structures around efficient accessibility. 
- Then I built the classes. 
- Then I started working on each piece of functionality, treating each piece of functionality as a method or a combination of methods where multiple methods seemed reasonable. 
- I tried to design methods to be reusable and flexible. 

RESULT:

- I was able to get the majority of the HD level requirements completed. 
- However I did run out of time and was not able to complete the command line functionality (to HD level) and also was not able to implement the try and except statements for
the use cases. Essentially I ran out of time. 
- Overall, while I'm still waiting on my mark and the feedback, I think it's a vast improvement on my previous project. The code and design is far more modulated and demonstrates the
notions of high cohesion and low coupling relatively well (as far as I can tell). 
- The print to file function (that prints the reports visually identical to the terminal display visualizaton) is inefficient as due to time constraints I was not able to create a single accumulative variable to print. 

############################################ PART 2: Assignment specifications/ Use cases ###############################################


------------------------------------------ PASS LEVEL (15 marks) -------------------------------------- 

Your  project  is  to  implement  the  required  functionalities  in  the  Object-Oriented  (OO)  style  with  at 
least three classes: Competition, Student, and Challenge. You need to design appropriate 
static/instance variables, constructors, and static/instance methods in these classes. The class related 
info should be encapsulated inside the corresponding class. 

In this level, your program can read data from a file specified in the command line. The file stores the 
students'  results  in  a  competition.  Your  program  should  create  a  list  of  Student  objects,  a  list  of 
Challenge objects, and a 2D-list (or other data types) to store the students' results. You should design 
the classes properly so that these actions can be encapsulated within the appropriate classes. Note that, 
at this level, we only know the IDs of the students, and the IDs of the challenges. 

In the main class, your program should create a Competition object, call its read_results(file_name) 
method to load data from the file (file_name), and then call its display_results() method to display the 
results in the required format (as specified in the following). 

Below is an example of the file that stores the students' results – see the next page (in the sequel, we 
will call this file as the result file). The data fields are separated by commas and new lines. The first 
row contains the challenges' IDs, and the first column contains the students' IDs. The first field in the 
data, the top left corner, is always empty. The file stores all students' results in all the challenges. These 
are the amount of time each student needs to solve each challenge. A result of "-1" means the student 
does  not  participate  in  the  challenge,  and  a  result  of  "444"  means  the  student  is  working  on  the 
challenge (ongoing) and the result is not available yet. In this level, you can assume the real results 

(not the -1 nor 444) are all positive floating-point numbers. You can assume there are no duplicate or 
redundant rows or columns. And you can assume the format of the data in the file is always correct. 
 
Your program should show usage if no result file is passed in as a command line argument. Otherwise, 
it can display a table showing the students' results, and a message showing the student with the fastest 
(smallest) average time. Note this average time is computed over all the finished  results only. In the 
printed table, if a student does not participate in a challenge (i.e., when the result is -1), the data field 
at that location of challenge and student is empty. If a result is ongoing (i.e., when the result is 444), a 
double dash (--) is shown at that data field. The printed message needs to be exactly as below: 

1. This is when no result file is passed in as a command line argument. 
 
2. This is when the result file is passed in as a command line argument. Note, users can specify 
a different file name, not necessary the name results.txt. 
 
 
----------------------- CREDIT LEVEL (3 marks, you must only attempt this level after 
completing the PASS level ------------------------- 

In this level, your program can support more information of challenges. Now, apart from the ID, each 
challenge will have a name and a weight; all IDs, names and weights can be modified. There are two 
types  of  challenges:  one  is  Mandatory  Challenge,  and  one  is  Special  Challenge. All  the mandatory 
challenges have a same weight, by default, it is 1.0. Each special challenge will have its own weight 
and  the  weights  of  the  special  challenges  are  required  to  be  larger  than  1.0.  You  should  define 
appropriate private/hidden variables, getters, and setters for challenges. 

Also, a challenge should have a method to compute some statistics: number of  students finished the 
challenge,  number  of  on-going  students,  average  time  of  each  challenge,  etc.  (it  is  your  choice  to 
compute the necessary statistics). You can define extra methods for the challenges if necessary. 
Your  program  now  can  read  one  more  file  specified  in  the  command  line.  This  file  stores  the 
information  of  the  challenges  (see  an  example  below,  in  the  sequel,  we  will  call  this  file  as  the 
challenge file). The file includes the challenge IDs, the challenge names, the types of the challenges 
("M"  means mandatory and  "S"  means  special), and  the  weight  of  each  challenge. You  can assume 
there  are  no  duplicate  or  redundant  challenges.  You  can  assume  all  challenges  available  in  the 
competition appeared in this file and in the previous result file (in the PASS level). 
 
Your program now can print the challenge summary on screen and save that summary into a file named 
competition_report.txt. For example, given the above  challenges.txt file and the  results.txt file as in 
the  PASS  level,  the  displayed  message  should  look  like  below  (note  the  content  within  the 
competition_report.txt  should  also  look  the  same).  Also,  users  can  specify  different  file  names,  not 
necessary the names results.txt and challenges.txt. The first file is always the result file, and the second 
file is the challenge information file. 

In the above message, the Weight column displays the weights with 1 digit after the decimal point. The 
Nfinish  column  displays  the  number  of  students  who  already  finished  the  challenge  (need  to  be 
integers). The Nongoing column displays the number of students who started working on the challenge 
but haven't finished yet (need to be integers). The AverageTime column displays the average time (2 
digits after the decimal point) the challenge is solved (based on finished students only). In the Name 
column, apart from the names of the challenges, your program should also display the challenge types 
("M" for mandatory challenges and "S" for special challenges). 

Note, apart from a challenge information table, your program should also display a message indicating 
the most difficult challenge. The most difficult challenge is the one with the highest average time. If 
there  are  multiple  challenges  with  the  highest  average  time,  you  can  choose  to  either  display  one 
challenge or display multiple challenges. 

Finally,  note  that  the  printed  message  includes  the  printed  message  from  the  PASS  level  (and  the 
competition_report.txt file should also include the table and the message from the PASS level). 
 
--------------- DI LEVEL (3 marks, you must only attempt this level after completing 
the CREDIT level) --------------- 

In this level, your program can support two types of students: Undergraduate Students and 
Postgraduate Students. All students need to participate in all the mandatory challenges. An 
undergraduate student needs to participate in at least 1 special challenge whilst a postgraduate student 
needs  to  participate  in  at  least  2  special  challenges.  The  classes  defined  for  students  should  have 
methods to check whether a student meets these requirements. Also, a student should have a method 
to compute some useful statistics for the student, e.g., number of finished challenges, number of on-
going challenges, average time, etc. You can define extra methods for the students if necessary. 

Your program now can read the student information from a file specified in the command line.  This 
file stores information about the students (in the sequel, we will call this file as the student file). The 
file includes the students' IDs, the students' names, and the types of the students ("U" for undergraduate 
students  and  "P"  for  postgraduate  students).  You  can  assume  there  are  no  duplicate  or  redundant 
students. You can assume all students in the competition appeared in this file and in the previous result 
file (in the PASS level). An example of the student file is as follows. 
 
Your program now can print a summary of students on screen and store that summary in the text file 
competition_report.txt (from the CREDIT level). Given the students.txt file above, the challenges.txt 
file in the CREDIT level, and the results.txt file in the PASS level, the displayed message should look 
like below (and so does the content in the competition_report.txt file) – see the next page. Note in the 
command line, users can specify different file names, not necessary the names results.txt, 
challenges.txt and students.txt. You can assume users always type the file names in the right order in 
the command line, e.g., the result file first, the challenge file second, and the student file third. 

The Type column stores the types of students ("U" for undergraduate students and "P" for postgraduate 
students).  The  Nfinish  column  stores  the number  of  challenges each  student finished,  the  Nongoing 
column  stores  the  number  of  challenges  each  student  started  working  but  has  not  finished  yet.  The 
AverageTime  column  stores  the  average  time  (with  two  digits  after  the  decimal  point)  the  students 
spent working on the challenges (computed based on finished challenges only). If a student hasn't had 
any result yet, then the value in the AverageTime column is a double dash (--). 
In  addition,  in  the  Name  column,  if  a  student  doesn't  satisfy  the  requirements  on  the  number  of 
mandatory  challenges  and  minimum  special  challenges,  an  exclamation  mark  (!)  is  added  at  the 
beginning of their names (e.g., "!Mary", "!Scott" and "!Harry" in the screenshot below). 
Finally, a message indicating the student with the fastest average time will also be displayed. Note, the 
content in the competition_report.txt needs to be the same as the printed message. 

-------------- HD LEVEL (6 marks, you must only attempt this level after completing 
the DI level) --------------- 
In this level, your program can handle some variations in the files using exceptions: 

1. When  the  result  file  is  empty,  your  program  will  exit  and  display  a  message  indicating  no 
results are available for the competition.

2. Results in the result file might be characters (e.g., "NA", "x"). In these cases, they will be treated 
as same as -1, except "TBA" or "tba", which means the challenge is ongoing (same as 444). 

3. When  there  are  any  formatting  issues  in  any  line  of  the  files  (e.g.,  other  delimiters  are  used 
instead  of  commas,  IDs  are  not  in  the  right  format, more columns compared to  the  required 
number of columns), the program will exit and display a message indicating there is a problem 
with the corresponding file. 

4. When  the  files  are  missing  or  cannot  be  found,  then  your  program  should  print  a  message 
indicating the names of the files are missing and then quit gracefully. You can assume users 
always type the file names in the right order in the command line, e.g., the result file first, the 
challenge file second, and the student file third. 

The program will have some additional requirements (some might be challenging): 
1. The competition_report.txt is accumulated, which means when the program is run, it will not 
overwrite the previous report, but instead,  it places the new report on top of the file (i.e., the 
newest report is always at the top of the competition_report.txt file). In addition, the date and 
time  when  the  report  was  generated  (in  the  format  dd/mm/yyyy  hh:mm:ss,  e.g.  01/03/2021 
09:45:00) are also saved in the text file for each report. 

2. The student information table (produced from the DI level) now has two new columns: Score 
and Wscore. 
a. The Score column is computed based on the scores the students obtained if they come 
first, second, third or last in a challenge. A student obtains 3 pts if they come first, 2 pts 
if they come second, 1 pts if they come third, and -1 pts if they come last in a challenge. 
Students come after the third place and before the last place will not have any points. 
The  total  score  of  a  student  is  the  total  score  of  all  the  challenges  they  finished.  A 
challenge only has scores when it is finished, i.e., there are no on-going students (note 
a challenge can still finish when there exist students who do not participate on it). If a 
challenge has less than 4 students participating, then the students are still awarded the 
points  when  they  come  first,  second,  or  third  even  in  these  cases,  a  student  comes 
third/second/first  might  also  come  last.  For  example,  if  there  are  only  3  students 
participating in a challenge, they are still awarded 3 pts, 2 pts, and 1 pts respectively. 
b. The  Wscore  column  is  computed  based  on  the  scores  the  student  obtained  in  each 
challenge and the weight of that challenge. For example, if the student comes first in a 
challenge with the weight being 1.2, then they will obtain a weighted score of 3*1.2=3.6 
pts  for  that  challenge.  The  total  weighted  score  is  the  total  weighted  score  of  all  the 
challenges the student finished. The weighted scores in the Wscore column have at most 
1 digit after the decimal point. 
See the below screenshot an example of how the new student information table with the Score 
and Wscore columns look like. 

3. Messages indicating students with the highest scores and weighted scores are also be displayed 
(see the below screenshot). 

4. The challenge information table (produced from the CREDIT level) is sorted (from low to high) 
based on average time. 

5. The student information table is sorted (from high to low) based on the weighted scores. 
