
from itertools import count
from multiprocessing import Value
import readline
import os 
import sys
from time import time
from unittest import result
from xmlrpc.client import Boolean

from prompt_toolkit import prompt
import time


############################################### READ ME ##################################################################
''' for this assignment I attempted a HD level response. Most of the functionalities are complete. Except for HD level command line arguments and exceptions.
Essentially, this is because I've run out of time. 

The design is centred around the competition class as the main class. The core of which is the competition constructors will enables smooth autogeneration of the report in
both the terminal and saved as a file. 

learning from the previous assignment, I've kept things as modular as possible. Also, when variables are important they are assigned property status, given that 
this is essentially a report generator statistics such as averages define the 'state' of the object. At least, that was the premise of this design. 

'''


###########################################################################################################################
''' the results class represents results as the object. The format has been based on the initial results file and has been applied to both challenges and students.'''
''' essentially an object with a dictionary attribute '''
'''accessibility: results objects can be found via a find_result method implemented in the competition class. '''

class Result(): # results are objects that can be stored in the student objects or challenges objects
                # for example for students the results will be (student_ID: {challenge_ID: Outcome, Challenge_ID: Outcome})
    def __init__(self, result_ID, key_outcome_dict):
        self.result_ID = result_ID
        self.key_outcome_dict = key_outcome_dict
        #self.key_count = [ c = 0 for k in [key_outcome_dict.keys() c += 1 ]] #syntax is incorrect but I want to count the number of keys in dict
        #self.average = key_count/sum(for s.values in key_outcome_dictionary.values())
        '''In addition the results class will have attributes such as 
        - 'average' (e.g if key is challenge and outcome is time, then average refers to average time for the student)'''

    
    
    def __str__(self):
        return ', '.join([str(i) if i is not None else '' for i in [self.result_ID,self.key_outcome_dict]])

    @property
    def get_result_ID(self):
        return self.result_ID
    
    @property
    def get_key_outcome_dict(self): ## the results object is the same stored in students. 
        return self.key_outcome_dict
    
    @get_key_outcome_dict.setter
    def set_key_outcome_dict(self, prompt):
        self.key_outcome_dict = prompt
        
 
############################################################################################################################################################################# 
    
class Challenge(): #this object stores information about a challenge including the results 
    
    def __init__(self, challenge_ID,  challenge_Type, challenge_Name, weight ):
        self.challenge_ID = challenge_ID
        self.challenge_Type = challenge_Type
        self.challenge_Name = challenge_Name
        self.challenge_weight = weight
        self.challenge_count = 0
        #self.challenge_count = len([c for c in self.challenge]) #this is tricky because I did not put the results in the challenges object as I did in students
        self.Nongoing = 0 # the cal_Ongoing_challenges method is called in competition constructor
        self.Nfinished = 0 #self.challenge_count - self.Nongoing can't be done here needs a method
        self.average_time = 0
        
    '''accessibility: challenge objects can be found via a find_challenge method implemented in the competition class. 
       - methods have been located in the main competition class.
       - setters and getters have been used as much as possible to simplify the accessing and changing of properties/attributes.'''

    def __str__(self):
        return ', '.join([str(i) if i is not None else '' for i in [self.challenge_ID,self.challenge_Name,self.challenge_Type,self.challenge_weight,self.challenge_count,self.Nongoing,self.Nfinished, self.average_time]])
    
    @property
    def get_challenge_ID(self):
        return self.challenge_ID
    
    @property
    def get_challenge_Type(self):
        return self.challenge_Type
    
    @property
    def get_challenge_name(self):
        return self.challenge_Type
    
    @property
    def get_challenge_weight(self):
        return self.challenge_weight
    
    @property
    def get_Nongoing(self):
        return self.Nongoing 
    
    @get_Nongoing.setter
    def set_Nongoing(self, prompt):
        self.Nongoing = int(prompt)
        
    @property
    def get_Nfinished(self):
        return self.Nfinished
    
    @get_Nfinished.setter
    def set_Nfinished(self, prompt):
        self.Nfinished = prompt
        
    @property
    def get_average_time(self):
        return self.average_time
    
    @get_average_time.setter
    def set_average_time(self, prompt):
        self.average_time = prompt


    @property
    def get_challenge_count(self):
        return self.challenge_count
    
    @get_challenge_count.setter
    def set_challenge_count(self, prompt):
        self.challenge_count = prompt
    
    
#################################################################################################################################################################################
    
class Student():
    
    '''accessibility: - student objects can be found via a find_student method implemented in the competition class. 
                      - methods have been located in the main competition class. 
                      - setters and getters have been used as much as possible to simplify the accessing and changing of properties/attributes.  '''
    
    
    def __init__(self, student_ID, results): #in read_results method results is an object with a key_outcome_dict as an attribute. Therefore the ID is repeated twice
        self.student_ID = student_ID
        ''' student_Name, student_Type, passed_requirments are
        default placeholder attributes to be change by methods, allows instantiation with incomplete information 
        (e.g retreiving complete information from multiple files).'''
        self.student_Name = ''
        self.student_Type = 'NA' #default is unknown 
        self.results = results #results is an object with a dictionary attribute
        #self.student_name = student_name
        filtered_list = [x for x in self.results.key_outcome_dict.values() if x.strip() not in ['444', '-1']]
        #print('##### FILTERED LIST #####')
        #print(filtered_list)
        self.challenge_count = len(filtered_list)
        self.Nongoing = 0 # the cal_Ongoing_students method is called in competition constructor
        self.Nfinished = self.challenge_count - self.Nongoing
        self.average = 0 # adjusted through setter in all student averages method in competition class
        '''  passed_requirements method is in competition. '''
        self.passed = False # as default forces verification and prenvents bugs of loose permission.  
        ''' default needs to be changed '''
        self.score = 0
        self.weighted_score = 0
        
   
    def __str__(self):
        return ', '.join([str(i) if i is not None else '' for i in [self.student_ID,self.results,self.student_Name, self.student_Type,self.challenge_count,self.Nongoing,self.Nfinished, self.average, self.get_passed, self.score, self.weighted_score]]) # might be as issue as results is a dict. 
        
        
    @property
    def get_student_ID(self):
       return self.student_ID
   
    @property
    def get_student_result(self):
       return self.results # an object in a object
   
    @property
    def get_average(self):
        return self.average
    
    @get_average.setter
    def set_average(self, prompt):
        self.average = prompt
    
    @property
    def get_Nongoing(self):
        return self.Nongoing
    
    @get_Nongoing.setter
    def set_Nongoing(self, prompt):
        self.Nongoing = prompt
        
    @property
    def get_Nfinished(self):
        return self.Nfinished
    
    @get_Nfinished.setter
    def set_Nfinished(self, prompt):
        self.Nfinished = prompt
    
    @property
    def get_student_count(self):
        return self.challenge_count
    
    @get_student_count.setter
    def set_student_count(self, prompt):
        self.challenge_count = prompt
    
    @property
    def get_student_Name(self):
        return self.student_Name
    
    @get_student_Name.setter
    def set_student_Name(self, prompt):
        self.student_Name = prompt  
      
    @property
    def get_student_Type(self):
        return self.student_Type
    
    @get_student_Type.setter
    def set_student_Type(self, prompt):
        self.student_Type = prompt
     
    @property
    def get_passed(self): #prompt is student ID
        return self.passed #value is boolean
     
    @get_passed.setter
    def set_passed(self, prompt):
        self.passed = prompt
    
    @property 
    def get_score(self):
        return self.score
    
    @get_score.setter
    def set_score(self, prompt):
        self.score = prompt 
        
    @property
    def get_weighted_score(self):
        return self.weighted_score
    
    @get_weighted_score.setter
    def set_weighted_score(self, prompt):
        self.weighted_score = prompt
       
 ################################################################################################################################################################################       
        
class Competition():  # THIS seems to be the main class. This stores the lists. It is also where things will be displayed (printed from)
    argv = sys.argv
    #print('### ARGV ###')
    #print(argv)
    if not argv: argv = ['results.txt'] #, 'products.txt', 'orders.txt']
    #print('### ARGV ###')
    #print(argv)
    print(len(argv))
    if len(argv) not in (1, 2, 4):
            sys.stdout.write('Illegal number of file arugments.\n')
            sys.stdout.write(f'[Usage:] {os.path.basename(__file__)}\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} <results_file>\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} <results_file> <students_file> <orders_file>\n')
            exit()

    
    sys.stdout.write('\n \n \n')
        
    
    
    #MAIN LISTS/DICTIONARIES
    ''' students_list is a list of student objects. Student objects have two attributes.
        1. They have a student_ID (which should be a string)
        2. They have a results attribute which is a Results object.
            That results object has two attributes.                                                     
             1. result_ID
             2. key_outcome_dict'''
    
    ''' challenges list is a list of challenge objects.  '''
    ''' student_results_dict is a dictionary that has result objects structured to access results data '''
    ''' challenges_results_dict is a dictionary has results objects structured specifically to access results data'''
                      
    @property
    def get_challenges_list(self):
        return self.challenges_list

    @property
    def get_students_list(self):
        return self.students_list
    
    property
    def get_student_results_dict(self):
        return self.student_results_dict
    
    
    def __init__(self, results_file, challenges_file, students_file): 
        print(argv)
        print(results_file)
        self.challenges_list = []
        self.students_list = []
        self.student_results_dict = {}
        self.challenge_results_dict = {}
        self.students_file = students_file
        self.challenges_file = challenges_file
        self.results_file = results_file
        #read challenges occurs first, so that challenges can be instantiated. Then info can be added by read results method.
        self.read_challenges(challenges_file)
        self.read_results(results_file) #auto loads when competition is instantiated.
        self.read_students(students_file) 
        self.challenges_print_list = [str(c.challenge_ID) for c in self.get_challenges_list[1:]]
        self.challenges_print_list.insert(0, 'RESULTS')
        self.student_count = len(self.get_students_list)
        self.challenge_count = len(self.challenges_list) #different to the challenge attribute challenge_count
        self.create_challenges_results_dict()
        self.get_all_student_averages()
        self.get_all_challenge_averages()
        self.cal_Ongoing_challenges()
        self.cal_Ongoing_students()
        self.calculate_all_challenge_count()
        self.calculate_all_Nfinished_challenges()
        self.calculate_all_Nfinished_students()
        self.pass_requirement_for_all()  
        self.display_information() #auto displays when competition is instantiated. 
        self.print_competition_report()
    
    def __str__(self):
       return ', '.join([str(i) for i in [self.students_list, self.challenges_list, self.student_results_dict, self.challenge_results_dict]])
    
    def __repr__(self) -> str:
        return f"({self.students_list}, {self.challenges_list}, {self.challenge_results_dict}, {self.student_results_dict})"    
     
    ''' Read challenges occurs before read results. This wasy information from results can add information to the already instantiated objects
        For example, the required information for the constructors exists in the challenges file. But attributes such as NumOngoing and NumFinish can 
        only be  derrived from information in results file. (at least at credit level)'''
    def read_challenges(self, challenges_file):
        #print('#### READ CHALLENGES METHOD IN COMPETITION CLASS #####')
        #print('#### CHALLENGES FILE ####')
        #print(challenges_file)
        file_object = open(challenges_file, 'r')
        current_line = file_object.readline().strip()
        #current_line is true while there is another line of data in file
        while current_line:
            challenge_info_list = current_line.split(',')
            challenge_info_list = [x.strip('\n') for x in challenge_info_list] #strips the line break. Was giving me issues before. 
            challenge_ID = challenge_info_list[0]
            challenge_Name = challenge_info_list[1]
            challenge_name = challenge_info_list[2]
            challenge_weight = challenge_info_list[3]
            a_challenge = Challenge(challenge_ID, challenge_Name, challenge_name, challenge_weight)
            self.add_challenge_challenges_list(a_challenge)
            current_line = file_object.readline()
        #print('#### DISPLAY CHALLENGES LIST FROM READ CHALLENGES METHOD IN COMPETITION CLASS #####')
        self.display_challenges_list
        file_object.close() 
            
        
    def read_results(self, results_file): #for pass level can assume only 5 challenges
        file_object = open(results_file, "r")
        first_line = file_object.readline().strip() # reads one line at a time # holds internal counter for which line. 
        first_line.strip()
        
        ''' challengeID_list block'''
        # create list of challenge_ID string from first line of results file. 
        # Then replaces empty strings with results
        challengeID_list = first_line.split(',') # hypothesis: it prints a list of strings that are challenge IDs
        challengeID_list = [x.strip() for x in challengeID_list] #split adds whitespace, hence strip again. 
        challengeID_list = [x.replace ('\n', '') for x in challengeID_list]
        #print('#### CHALLENGE ID LIST #####')
        #print(challengeID_list)
        '''OUTCOME: ['', ' C03', ' C04', ' C09', ' C12', ' C15']'''
        

        current_line = file_object.readline().strip()
        #current line is true while there is another line of data in file. 
        #print('### FIRST CURRENT LINE ####')
        #print(current_line)
        while current_line:
            
            student_result_list = current_line.strip().split(',') #student result is a list of string. Can access to instantiate student
            #print('#### STUDENT_RESULT_LIST ####') # it's printing same line so readline() is not being called again on assingment. 
            student_ID = student_result_list[0]
            outcome_1 = student_result_list[1]
            outcome_2 = student_result_list[2]
            outcome_3 = student_result_list[3]
            outcome_4 = student_result_list[4]
            outcome_5 = student_result_list[5]
            #print('#### STUDENT RESULTS LIST #####')
            #print(student_result_list)
            '''OUTCOME: ['S001', '12.5', '6.8', '17.6', '444', '-1']'''
            
            #now I need to add or to/recreate a dictionary because that's what result stores.
            key_outcome_dict = {}
            keys = challengeID_list[1:]
            outcomes = student_result_list[1:]
            for i in range(len(keys)):
                #print('##### i in loop #####')
                #print(i)
                ''' i is printing the range index '''
                key_outcome_dict[keys[i]] = outcomes[i]
                
                # at this point all relevant information has been assigned to variables locally.
            
            #print('#### KEY_OUTCOME_DICT ######')
            #print(key_outcome_dict)
            
                
            # go to next line in file
            current_line = file_object.readline().strip()    
            #print('#### RESULT OBJECT SECTION IN READ_RESULTS METHOD ####')
             
            student_result = Result(student_ID, key_outcome_dict) #student_ID as result identifier
            #print('#### STUDENT_RESULT.get_result_ID')
            #print(student_result)
            #print('#### STUDENT_RESULT.get_result_ID')
            #print(student_result.get_result_ID)
            #print('#### STUDENT_RESULT.get_key_outcome_dict')
            #print(student_result.get_key_outcome_dict)
            #print('### TEST VAR ####')
            #test = student_result.get_result_ID  
            #print(test)
            self.add_student_result_student_results_dict(student_result) #adds result object to results_dict
            #print('#### STUDENT OBJECT SECTION IN READ_RESULTS METHOD ####')
            
            #print('### A STUDENT ####')
            a_student = Student(student_ID, student_result) #second is a results object, first parameter is string
            #print(a_student.get_student_ID)
            self.add_student_student_list(a_student)
                
                
        ### WHILE LOOP UP TO HERE ###
        #when current line is false, close file.
        file_object.close()
        
        '''For testing only'''
        #print('####### DISPLAY_STUDENT_LIST METHOD in read_results method #######')
        #self.display_student_list() 
        #print('#### DISPLAY_student_student_results_dict in read_results method #######')
        #self.display_student_results_dict()
            
       
    ''' At distinction level design, the read students needs to come AFTER ALL credit level functionalities called in
        the competition constructor methods. For example, it loops through self.students_list, 
        this means that credit level data structure should be in place, for the logic of this method to execute properly. '''       
    
    def read_students(self, students_file):
        
        # first varoable is a list of all student_IDs from results file. 
        # Used to check if there is a student from student_file with no results yet (e.g they just joined so they do not have -1 or 444)
        # note that this might create a hole in the passed_requirments group of methods 
        # (but this hole should not be an issue for the stated requirements of the assignment)
        students_with_results = [x.get_student_ID.strip() for x in self.students_list]
        
        file_object = open(students_file, 'r')
        current_line = file_object.readline().strip().strip('\n')   
        
        while current_line:
            student_info_list = current_line.split(',')
            student_ID = student_info_list[0]
            student_Name = student_info_list[1]
            student_Type = student_info_list[2]
           
            for student_object in self.students_list: 
                #should loop through a list of objects
                #therefore, iterator is an object. 
                if student_object.get_student_ID == student_ID:
                    #uses setters 
                    student_object.set_student_Name = student_Name
                    student_object.set_student_Type = student_Type
                    ''' the elif below deals with possibility of very new students '''
                elif student_object.get_student_ID not in students_with_results:
                    empty_dict = {}
                    student_result = Result(student_ID, empty_dict)
                    a_student = Student(student_ID, student_result)
                    a_student.set_student_Name = student_Name
                    a_student.set_student_Type = student_Type
            current_line = file_object.readline().strip().strip('\n')
                    
        
        
    
        
        ''' DISPLAY INFORMATION METHOD '''
        ''' Integrates competition, challenges, students. '''  
        ''' given the functionality of the program as a report generator I saw no short term value in creating different display functions'''
        ''' Designed in this way, adjustments to report formatting need only be made to THIS method and Print_report method'''
    
    def display_information(self): #formerly display competition
        
        
        ''' there are two parts of the display_competition method.
            1. part that prints RESULTS string and challenge IDs
            2. part that print studentID and their times.'''
        
        '''Part 1: the information is correct. Now have to add formatting for the primary line.
            There will also be two dynamic lines. One above and one below. '''

        # because the join list comprehension syntax forms one string the expection is that print won't go to next line.
        #print(self.challenges_print_list)
        ## to make the RESULTS column dynamic it might have to be based on len of the str in challenges_print_list
        print("\n")
        
        
        ''' #### Competition dashboard Code Block #### '''
        #report_file = open('report.txt', 'a')
        #report_file.write('COMPETITION DASHBOARD\n')
        print('COMPETITION DASHBOARD')
        sys.stdout.write('----------+-') #this string is hardcoded with length of RESULT string as first element of line. 
        line_length = [len(i.get_challenge_ID) for i in self.get_challenges_list[0:]] #dynamic code, deals with anynumber of challenges permitted by screen limitations
        length = len(line_length) #this variable is redundant as it's represented implicitly in the below for loop. 
        for x in line_length:
            sys.stdout.write(('--'* x )+'--+')#(str(x) for x in line_length))
        print('')

        string = '| Result' + '  | '+'|'.join([f'{str(ch.get_challenge_ID):^8}' for ch in self.get_challenges_list])+ '|'
        print(string)
        
        sys.stdout.write('----------+-')
        for x in line_length:
            #int(x)
            sys.stdout.write(('--'* x )+'--+')
        print('')
        
        for k, v in self.student_results_dict.items():
            replace_values = {"444": "   --  ", "-1":"       "}
            final_string = '| ' + f"{k:^7} {'|':^1} {' |'.join(f'{v:^7}'if float(v.strip())>0 and v.strip()!='444' else replace_values[v.strip()] for v in v.values())}"+' |'
            print(final_string)

        sys.stdout.write('----------+-')
        for x in line_length:
            #int(x)
            sys.stdout.write(('--'* x )+'--+')
        
        print('')
        
        print(f'There are {self.student_count} students and {self.challenge_count} challenges.')
        
        best_student_time_list = self.best_student()
        print(f'The top student is {best_student_time_list[0]} with an average time of {best_student_time_list[1]:.2f} ')
        
        
        
        
        ''' #### challenge information code block #### '''
        
        print('')
        print('CHALLENGE INFORMATION')
        challenge_report_line = '----------------------+' + '--------------------+' + '--------------------+' + '--------------------+' + '--------------------+' + '----------------+'
        print(challenge_report_line)
        
        
        challenge_attributes = ['         Name       ','        Weight      ', '      Nfinish       ', '      Nongoing      ' , '   AverageTime  ']
        
        
        string = '|      Challenge      |'+'|'.join([f'{str(ch):}' for ch in challenge_attributes])+ '|'
        #string2 = f"{'Challenge':^15}{'Name':^16}{'Weight':^12}{'Nfinish':^12}{'Nongoing':^12}{'AverageTime':^20}"
        #print(string2)
        print(string)
        print(challenge_report_line)
        
        
        ''' this is the body for the challenges information'''
        
        sorted_challenges = self.sort_challenges_by_average() #should be a tupple of challenge objects.
        #print('##### SORTED CHALLENGES ######')
        #print(sorted_challenges)
        hardest_challenge = sorted_challenges[-1]
        hardest_challenge_name = hardest_challenge.challenge_Name.strip()
        hardest_challenge_ID = hardest_challenge.get_challenge_ID
        hardest_challenge_time = hardest_challenge.get_average_time

        for c in sorted_challenges: 
            
            #to_print = [str(x) for x in s if x not in irrelevant]
            to_print = f"|       {c.challenge_ID:^8}      |  ({c.challenge_Type.strip()}){c.challenge_Name:<15}|       {c.challenge_weight:^8}     |       {c.Nfinished:^8}     |       {c.Nongoing:^8}     |     {c.average_time:^8}   |"
            print(to_print)
        print(challenge_report_line)
        
        print(f"The most difficult challenge is {hardest_challenge_name} ({hardest_challenge_ID}) with an average time of {hardest_challenge_time} minutes. ")
        print('Report competition_report.txt generated!')
        
        ''' for testing purposes only '''
        #print('################### attributes dict ####################')
        #print(attribute_dict)
        #print('##### ITEMS TO PRINT #####')
        #print(items_to_print)
        #print('###### VALUES #######')
        #print(values)
       
             
        ''' STUDENT INFORMATION CODE BLOCK '''
        
        print('')
        print('STUDENT INFORMATION')
        student_report_line = '-------------+' + '-----------+' + '------------+' + '------------+' + '------------+' + '----------------+' + '----------------+' + '----------------+'
        print(student_report_line)
        
        
        student_attributes = [' Name '.center(11),' Type '.center(12), ' Nfinish '.center(12), ' Nongoing '.center(12) , ' AverageTime '.center(16), ' Score '.center(16), ' Wscore '.center(16)]
        
        string = '| StudentID  |'.center(12) +'|'.join([f'{str(ch):}' for ch in student_attributes])+ '|'
        print(string)
        print(student_report_line)

        

        sorted_students = self.sort_students_by_average()
        best_student = sorted_students[-1]
        best_student_name = best_student.student_Name.strip()
        best_student_ID = best_student.student_ID
        best_student_time = best_student.average

        sorted_students = self.sort_students_by_weighted_score() #should be a tupple of student objects.
        for s in sorted_students: 
            
            passed_display = 'error'
            if s.passed == True: #accesses student object attribute
                passed_display = ''
            elif s.passed == False: #accesses student object attribute
                passed_display = '!'
            else:
                print('#### ERROR IN passed_display ####')
            #to_print = [str(x) for x in s if x not in irrelevant]
            print_student = f"|{s.student_ID.center(12)}|{passed_display:>3}{s.student_Name.strip():<8}|{s.student_Type.center(12)}|{str(s.Nfinished).center(12)}|{str(s.Nongoing).center(12)}|{str(s.average).center(16)}|{str(s.score).center(16)}|{str(s.weighted_score).center(16)}|"
            print(print_student)
        print(student_report_line)
        
        print(f"The student with the fastest average time is {best_student_ID} ({best_student_name}) with an average time of {best_student_time} minutes")
        print('Report competition_report.txt generated!')
        print('\n\n')
        
        ''' student information testing block only '''
        #print('#### ATTRIBUTE_DICT 2 ####')
        #print(attribute_dict2)
        #print('#### ITEMS TO PRINT 2 ####')
        #print(items_to_print2)
        #print('#### values 2 ####')
        #print(values2)
        
        
        
       
    '''#### Add methods ####'''   
    
        #adds to lists
    def add_challenge_challenges_list(self, challenge_ID):
        self.get_challenges_list.append(challenge_ID)

    def add_student_student_list(self, student_object):
        self.students_list.append(student_object)
        
        #adds to dictionaries
    def add_student_result_student_results_dict(self, student_result):
        self.student_results_dict[student_result.get_result_ID] = student_result.get_key_outcome_dict # e.g {'student_identifer': {'challenge_identifer': outcome, 'challenge_identifier': outcome}}
    
    def add_challenge_result_challenge_results_dict(self, challenge_result):
        self.challenge_results_dict[challenge_result.get_result_ID] = challenge_result.get_key_outcome_dict # e.g {'challenge_identifer': {'student_identifer': outcome, 'student_identifier': outcome}}
    
    
    '''### PRINT TOOLS (Useful when developing) ####'''
    
    def display_student_list(self):
        for s in self.students_list:
            print (s)
    def display_challenges_list(self):
        for c in self.get_challenges_list:
            print (c)
    def display_student_results_dict(self):
        for r in self.student_results_dict.items():
            print(r)
    def display_challenge_results_dict(self):
        for r in self.challenge_results_dict.items():
            print(r)
    
    
    '''#### find methods ####'''
        
    ''' the next 2 methods access objects from list'''
        
        #finds a student object from from student list (attribute of competition class)
    def find_student(self, student_ID):
        #print('#### FIND STUDENT ####')
        the_student = [c for c  in self.get_students_list if  c.get_student_ID == student_ID]
        #print(the_student)
        return the_student
        
        #finds a challenge object from challenge list (attribute of competition class)
    def find_challenge(self, challenge_ID):
        the_challenge = [c for c in self.get_challenges_list if c.get_challenge_ID == challenge_ID]
        #print('#### FIND CHALLENGE ####')
        #print(the_challenge)
        return the_challenge

    ''' the next 2 methods access objects from dictionary'''
        
        #finds a result object from challenge_results_dict (attribute of competition class)
    def find_challenge_dict(self, prompt):
        #print('#### FIND CHALLENGE DICT METHOD ####')
        challenge_dict = {k.strip(): v for k,v in self.challenge_results_dict.items() if k == prompt.strip() }
        #object in dictionary
        '''output: {'C03': {'S001': ' 12.5', 'S052': ' 10.6', 'S125': ' 9.4', 'S098': ' 13.8', 'S246': ' 9.9', 'S012': ' 11.2', 'S099': ' 10.0'}}'''
        return challenge_dict
    
        #finds a result object from student_results_dict (attribute of competition class)
    def find_student_dict(self, prompt):
        student_dict = {k: v for k,v in self.student_results_dict.items() if k == prompt.strip() }
        return student_dict
    
    
    '''#### Creates a challenges_results_dict ####'''
    
    ''' converts information from student_results_dict to challenges_results_dict '''
    
    def create_challenges_results_dict(self): 
        ## below is similar to the code block in read results
        studentID_list = [x.get_student_ID for x in self.students_list]
        #print('#### studentID_list ####')
        #print(studentID_list)
        challengeID_list = [x.get_challenge_ID for x in self.challenges_list]
        #print('#### challengeID_list ####')
        #print(challengeID_list)
        keys = studentID_list
        outcomes = []
        challenge_results_dict = self.challenge_results_dict
       
        dict_of_dict = {} # the loop adds to this variable
        for key, dic in self.student_results_dict.items(): # I think it iterates through attribute which is a dictionary
            for k, v in dic.items():
                #print('#### K ####')
                '''this adds a challenge key with a dictionary with studentID as keys and the index as value'''
                if k not in dict_of_dict.keys():
                    dict_of_dict[k] = {w: i for i, w in enumerate(studentID_list)}
                
                     
        #print('### DICT OF DICT####')
        #print(dict_of_dict)     
        '''OUTCOME: {'C03': {'S001': 0, 'S052': 1, 'S125': 2, 'S098': 3, 'S246': 4, 'S012': 5}, 
        'C04': {'S001': 0, 'S052': 1, 'S125': 2, 'S098': 3, 'S246': 4, 'S012': 5}, 
        'C09': {'S001': 0, 'S052': 1, 'S125': 2, 'S098': 3, 'S246': 4, 'S012': 5}, 
        'C12': {'S001': 0, 'S052': 1, 'S125': 2, 'S098': 3, 'S246': 4, 'S012': 5}, 
        'C15': {'S001': 0, 'S052': 1, 'S125': 2, 'S098': 3, 'S246': 4, 'S012': 5}}'''
        
        
        for student, dic in self.student_results_dict.items():
            # d_chalange_results
            for chal, res in dic.items():
                #print(dict_of_dict[chal])
                dict_of_dict[chal].update({student:res})
        #print('### DICT OF DICT FINAL ###')               
        #print(dict_of_dict)
        '''OUTCOME: {'C03': {'S001': ' 12.5', 'S052': ' 10.6', 'S125': ' 9.4', 'S098': ' 13.8', 'S246': ' 9.9', 'S012': ' 11.2'}, 
        'C04': {'S001': ' 6.8', 'S052': ' 7.0', 'S125': ' 6.2', 'S098': ' -1', 'S246': ' 5.9', 'S012': ' 444'}, 
        'C09': {'S001': ' 17.6', 'S052': ' 20.1', 'S125': ' 18.2', 'S098': ' 19.5', 'S246': ' 17.9', 'S012': ' 19.5'}, 
        'C12': {'S001': ' 444', 'S052': ' -1', 'S125': ' -1', 'S098': ' 25.3', 'S246': ' 20.1', 'S012': ' -1'}, 
        'C15': {'S001': ' -1', 'S052': ' 444', 'S125': ' -1', 'S098': ' 444', 'S246': ' -1', 'S012': ' 10.4'}}'''
        
        # loops through this dict and instantiate each loop as an object
        for id, result in dict_of_dict.items():
            challenge_result = Result(id, result)
            #print('### CHALLENGE RESULT VAR')
            #print(challenge_result)
            self.add_challenge_result_challenge_results_dict(challenge_result)
            
        
           
       
        '''#### CALCULATION METHODS SECTION ####'''   
        
        ''' setters were implemented where possible (and remembered) as they made the development of code more efficient'''  
        ''' these methods demostrate modularity in the design. '''  
        ''' The design of the initial classes e.g results class, allowed code to be reused for different classes.'''
        ''' the exeception being the existence of results in the student_list objects but not in the challenges objects.'''
        ''' I have not had time to reflect on whether or not the results objects in the students objects in the students list are reduandant 
            or whether they provide accessibility. With adequate time, most likley, the design would be resolved to be consistent with either having results
            in BOTH students and challenges objects OR having it in neither. '''
        
    def calculate_student_average(self, student_ID):
        #print('### CALCULATE AVERAGE ###')
        the_student = self.find_student(student_ID) #should be a list with an object
        #print(the_student)                          
        #print(str(type(the_student)))
        sum_list = []
        challenge_counter = 0
        student_result = the_student[0]
        #print('#### STUDENT RESULT #####')
        #print(student_result)
        result_outcomes_dict = student_result.get_student_result #attempting to access object attribute which is a dictionary
        #print('#### OUTCOMES DICT #####')
        #print(result_outcomes_dict)    # assuming I'm correct that outcomes_dict is accessible as a dictionary    
        iterable_outcomes = result_outcomes_dict.get_key_outcome_dict
        for k, v in iterable_outcomes.items():
            #print('#### K ####')
            #print(k)
            #print('#### V #####')
            #print(v)       
            if float(v.strip()) not in [444, -1]:
                    sum_list.append(float(v))
                    challenge_counter += 1
        #print('### SUM LIST ###')
        #print(sum_list)
        #print('### CHALLENGE COUNTER ###')
        #print(challenge_counter)
        total_time = sum(sum_list[0:]) #might not be right syntax for sum method
        #print('### TOTAL TIME ###')
        #print(total_time) 
        average = total_time/challenge_counter
        #print('### average ###')
        #print(average)
        return round(average, 2)
    
    
    ''' Most of the code blocks below are instantiated in the competition constructor '''
    ''' the design thinking behind it was to increase the efficiency of and simplicity of the program by using building around 
        constructors methods as much as possible. This was in part driven by the functional requirments of the program. It is essence, a report generator. 
        So like a written report, it comes "as is" with everything written on the page when you open the cover. 
        (or at least, that was the goal.'''
    def get_all_student_averages(self): ### average for all events
        #print('#### GET ALL STUDENT AVERAGES METHOD IN COMPETITION CLASS #####')
        students = []
        average_times = []
        for s in self.students_list: # a list of student objects 
            student_ID = s.get_student_ID # accessing and assigning the attribute. 
            average = self.calculate_student_average(student_ID) # method should return a numeric value
            students.append(student_ID)
            average_times.append(average)
        #print('#### AVERAGE TIMES ####')
        #print(average_times)
        #print('#### STUDENTS ####')
        #print(students)
        #print('#### AVERAGES DICT ####') 
        averages_dict = dict(zip(students, average_times))
        for k, v in averages_dict.items():
            obj_in_list = self.find_student(k) #returns list with an object
            a_student = obj_in_list[0]
            #print('####### A STUDENT VAR #######')
            #print(a_student)
            #print(type(a_student))
            a_student.average = v
        #print(averages_dict)
        #print('#### BEST STUDENT ####')
        #best_student = min(averages_dict, key = averages_dict.get) #this variable should be the one printed in display method
        #print(best_student)
        #print('#### BEST TIME ####')
        #best_time = min(averages_dict, value = averages_dict.get)
        #print(best_time)         
   
   
        #complexity of this method is remnant developing it before get_all_studen_averages_method
    def best_student(self):
        #print('#### BEST STUDENT METHOD #####')
        students = []
        average_times = []
        for s in self.students_list: # a list of student objects 
            student_ID = s.get_student_ID # accessing and assigning the attribute. 
            average = self.calculate_student_average(student_ID) # method should return a numeric value
            students.append(student_ID)
            average_times.append(average)
        #print('#### AVERAGE TIMES ####')
        #print(average_times)
        #print('#### STUDENTS ####')
        #print(students)
        #print('#### AVERAGES DICT ####') 
        averages_dict = dict(zip(students, average_times))
        sorted_tupples = sorted(averages_dict.items(), key=lambda x: x[1]) #it returns tuppleS in a list
        #print('#### SORTED_TUPPLE #####')
        #print(sorted_tupples)
        best_key_val = sorted_tupples[0]
        best_student = str(best_key_val[0])
        best_time = str(best_key_val[1])
        #print(averages_dict)
        #print('#### BEST STUDENT #####')
        #print(best_student)
        #print('#### BEST TIME #####')
        #print(best_time)
        return best_key_val #returns tupple and that tupple is accessed via indices in the display_information method
     
   
    def sort_students_by_average(self): #sorts all students
        list_of_students = [s for s in self.students_list]
        sorted_students = sorted(list_of_students, key = lambda x: x.average )
        return sorted_students
    
    def sort_students_by_weighted_score(self):
        list_of_students = [s for s in self.students_list]   
        sorted_students = sorted(list_of_students, key = lambda x: x.weighted_score, reverse = True )
        return sorted_students
        
    def calculate_all_challenge_count(self): #prompt is ID
        
        for ch in self.challenges_list: #list of objects
            #print('### CHALLENGE RESULT DICT #######')
            #print(self.challenge_results_dict)
            #print('### CALCULATE ALL CHALLENGES #######')
            #print('#### CH ####')
            #print(ch)
            temptdict = self.challenge_results_dict[ch.get_challenge_ID] #value of key is dictionary
            #print('### temptdict ####')
            #print(temptdict)
            #print(type(temptdict))
            count = len([str(x.strip()) for x in temptdict.values() if x not in ' 444'])
            #print('#### COUNT ###')
            #print(count)
            #self.challenges_list[prompt].set_challenge_count = count
            ch.set_challenge_count = count #setter updates directly
    
    
    def calculate_all_student_count(self): #prompt is ID
        
        for ch in self.students_list: #list of objects
            #print('### CHALLENGE RESULT DICT #######')
            #print(self.student_results_dict)
            #print('### CALCULATE ALL CHALLENGES #######')
            #print('#### CH ####')
            #print(ch)
            temptdict = self.student_results_dict[ch.get_student_ID] #value of key is dictionary
            #print('### temptdict ####')
            #print(temptdict)
            #print(type(temptdict))
            count = len([str(x.strip()) for x in temptdict.values() if x not in ' 444'])
            #print('#### COUNT ###')
            #print(count)
            #self.challenges_list[prompt].set_challenge_count = count
            ch.set_student_count = count #setter updates directly
    
    
    def calculate_challenge_average(self, challenge_ID):
        #print('### CALCULATE AVERAGE ###')
        #print('#### CHALLENGEID ARGUMENTS PASSED INTO THE METHOD')
        #print(challenge_ID)
        #UP TO HERE IS CORRECT
        ''' bug: THE CHALLENGE is returning an empty value even though in first iteration CHALLENGE ID shows C03'''
        the_challenge = self.find_challenge_dict(challenge_ID)
        #print('### THE CHALLENGE VARIABLE found via find_challenge_dict method ###')
        #print(the_challenge) 
        #print(type(the_challenge))
        # but why is the challenge type <class '__main__.Student'>?
        #WORKS UP TO HERE
        sum_list = []
        challenge_counter = 0
        #print('#### CHALLENGE RESULT #####')
        #print(challenge_result)
        iterable_outcomes_dict = the_challenge.values()
        #print('#### ITERABLE OUTCOMES DICT ####')
        #print(iterable_outcomes_dict)
        #print(type(iterable_outcomes_dict))
        #print('#### OUTCOMES DICT #####')
        #print(result_outcomes_dict)    # assuming I'm correct that outcomes_dict is accessible as a dictionary    
        for k, v in list(iterable_outcomes_dict)[0].items():
            #print('#### K ####')
            #print(k)
            #print('#### V #####')
            #print(v)       
            if float(v.strip()) not in [444, -1]:
                    sum_list.append(float(v))
                    challenge_counter += 1
        #print('### SUM LIST ###')
        #print(sum_list)
        #print('### STUDENT COUNTER ###')
        #print(student_counter)
        total_time = sum(sum_list[0:]) #might not be right syntax for sum method
        #print('### TOTAL TIME ###')
        #print(total_time) 
        average = total_time/challenge_counter
        #print('### average ###')
        #print(average)
        return average
   
   
   
    def get_all_challenge_averages(self): ### average for all events
        #print('#### GET ALL CHALLENGES AVERAGES METHOD IN COMPETITION CLASS #####')
        challenges = []
        average_times = []
        for s in self.challenges_list: # a list of student objects 
            challenge_ID = s.get_challenge_ID # accessing and assigning the attribute. 
            #print('#### CHALLENGE ID ####')
            #print(challenge_ID)
            
            #UP TO HERE IS CORRECT 
            
            average = self.calculate_challenge_average(challenge_ID) # method should return a numeric value
            #print('#### CHALLENGE ID ####')
            #challenges.append(challenge_ID)
            #average_times.append(average)
            s.average_time = round(average, 2)
            #averages_dict = dict(zip(challenges, average_times))
            #for k, v in averages_dict.items():
                #'''bug: the problem is that it is using the wrong find challenge method'''
                #a_challenge = self.find_challenge_dict(k) #should return a dictionary
                ##a_challenge = obj_in_list[0]
                #a_challenge[k] = self.challenge_results_dict
                
    ''' works correcttly '''
    def sort_challenges_by_average(self): #sorts all students
        list_of_challenges = [s for s in self.challenges_list]
        sorted_challenges = sorted(list_of_challenges, key = lambda x: x.average_time )
        #print('#### Sorted Challenges #####')
        #print (sorted_challenges) 
        # the above is printng a list of objects
        #for s in sorted_challenges:
         #   print(str(s)) #this is printing the correct information. 
        # above is just for testing
        return sorted_challenges
   
                
        
        
        
        '''#### Number Ongoing and Number Finished methods  ####'''
        
    def cal_Ongoing_challenges(self):
        
        challengeID_list = [c.get_challenge_ID for c in self.get_challenges_list]
        #print('################## challengeID_list (cal ongoing challenges method) ##########################')
        #print(challengeID_list)
        
        ''' in the end this was relatively simple. 1) create a counter dict 2) loop through challenge_results_dict if the value of result is true then increase counter. '''
            
        counter_dict = {i:0 for i in challengeID_list} # creates a dict with challengeID as key 0 as value
        #print('######## COUNTER DICT PROTO #########')
        #print(counter_dict)

        for challenge, student_data in self.challenge_results_dict.items():
            for student, result in student_data.items():
                if result  ==  ' 444': #if I strip string in future, this needs to change
                    counter_dict[challenge] = counter_dict[challenge] + 1
        #print(counter_dict)
                    
        #print('#### COUNTER DICT cal_Ongoing_challenges (CHALLENGES) ####')
        #print(counter_dict) #this counter_dict holds the count for ongoing. 
        
        #both iterables are based on the same challengeID_list comprehension, so there indexes should be the same
        for c in self.challenges_list:
            c.Nongoing = counter_dict[c.get_challenge_ID]
        
        
    def cal_Ongoing_students(self):
        studentID_list = [c.get_student_ID for c in self.get_students_list]
        counter_dict = {i:0 for i in studentID_list}
        
        for student, challenge_data in self.student_results_dict.items():
            for challenge, result in challenge_data.items():
                if result.strip() == '444': #if I strip string in future, this needs to change
                    counter_dict[student] = counter_dict[student] + 1
        #print('#### COUNTER DICT cal_Ongoing_students (STUDENTS) ####')
        #print(counter_dict) #this counter_dict holds the count for finished. 
        
        #below both iterables are based on the same studentID_list comprehension, so there indexes should be the same
        #for student, counter in counter_dict.items(): 
        for s in self.students_list:
            s.Nongoing = counter_dict[s.get_student_ID]
        
        
    def calculate_all_Nfinished_challenges(self):
        for c in self.challenges_list:
            challenge_count = c.get_challenge_count
            Nongoing = c.get_Nongoing
            c.set_Nfinished = challenge_count - Nongoing  
    
    def calculate_all_Nfinished_students(self):
        for s in self.students_list:
            student_count = s.get_student_count
            Nongoing = s.get_Nongoing
            s.set_Nfinished = student_count - Nongoing
        
    def cal_absent_challenges(self):
        challengeID_list = [c.get_student_ID for c in self.get_challenge_list]
        counter_dict = {i:0 for i in challengeID_list}
        
        for challenge, student_data in self.student_results_dict.items():
            for student, result in student_data.items():
                if result.strip() == '-1': #if I strip string in future, this needs to change
                    counter_dict[student] = counter_dict[student] + 1
        #print('#### COUNTER DICT cal_absent_challenges (CHALLENGES) ####')
        #print(counter_dict) #this counter_dict holds the count for absent. 
        
        
    def calculate_score_and_weight_score_for_all (self): 
        #challengeIDs = [x.get_challenge_ID for x in self.challenges_list]
        #weight = [x.get_challenge_weight for x in self.challenges_list]
        #weighted_dic = dict(zip(challengeIDs, weight))
        ''' made the above 1 line '''
        ''' used to get challenge ID and weight for calculating sc'''
        weighted_dic = {x.get_challenge_ID: float(x.get_challenge_weight.strip()) for x in self.challenges_list}
        print('###### WEIGHTED DICT ####')
        print(weighted_dic)
        
        for challenge, results in self.challenge_results_dict.items():
            results = dict(sorted(results.items(), key=lambda x: float(x[1].strip())))
            score = 3
            counter = 0
            for student, ou in results.items():
                counter +=1
        
                if len(results) == counter:
                    score = -1
                elif score == 0:
                    continue
                stud_obj = self.find_student(student)[0]
                stud_obj.set_score = stud_obj.score + score
                stud_obj.set_weighted_score = round(stud_obj.score * weighted_dic[challenge], 2)
                score -= 1
                

    
    def cal_absent_students(self):
        studentID_list = [c.get_student_ID for c in self.get_students_list]
        counter_dict = {i:0 for i in studentID_list}
        
        for student, challenge_data in self.student_results_dict.items():
            for challenge, result in challenge_data.items():
                if result == ' -1': #if I strip string in future, this needs to change
                    counter_dict[student] = counter_dict[student] + 1
        #print('#### COUNTER DICT cal_absent_students (STUDENTS) ####')
        #print(counter_dict) #this counter_dict holds the count for absent. 
   
   
    '''#### Verification methods ####'''
    
    ''' overview: 
    1) passed_requirements_for_all method loops through student lists and applies the passed_requirements method to each object
    2) passed_requirements is called 
    3) passed_requirements calls has_passed_mandatory method, latter returns boolean
    4) passed_requirments calls has_passed_special method, latter returns boolean
    5) pass_requirements returns a boolean '''
    
    def passed_mandatory(self, prompt):
        ''' testing: assumes that find student method returns a list of a single filtered object '''
        has_passed = True  
        student_obj_list = self.find_student(prompt)
        student_obj = student_obj_list[0]
        student_result = student_obj.get_student_result #results is a dictionary object
        results_dict = student_result.get_key_outcome_dict # accessing the dictionary attribute {'C002': 10.5}
        
        
        '''testing: list comprehension to get Mandatory challenges'''
        mandatory_events_list = [str(evt.get_challenge_ID) for evt in self.challenges_list if evt.get_challenge_Type == ' M']
        incomplete_indicators = ['-1', 'NA', 'na', 'N/A', 'n/a', 'x', 'X', 'incomplete', '0'] 
        ''' OUTPUT: ['C03', 'C04']'''
        #removed '444' and 'ongoing' from incomplete indicators because requirements say 'need to participate in all mandatory challenges'. 444 is ongoing participation. 
        #in other words, requirements do not state students need to have participated (past tense).
        for k, v in results_dict.items():# e.g {'C002': 10.5, ......}
            if k in mandatory_events_list and v in incomplete_indicators:
                has_passed = False
                return has_passed 
        #if loop condition is not met then return true
        return has_passed
    
    def passed_special(self, prompt): #prompt is student_ID
        counter = 0
        #has_passed = True
        student_obj_list = self.find_student(prompt)
        student_obj = student_obj_list[0]
        student_result = student_obj.get_student_result #results is a dictionary object
        results_dict = student_result.get_key_outcome_dict # accessing the dictionary attribute {'C002': 10.5}
        special_events_list = [str(evt.get_challenge_ID) for evt in self.challenges_list if evt.get_challenge_Type == ' S']
        ''' OUTCOME: ['C15', 'C09', 'C12'] '''
        incomplete_indicators = [' -1', ' NA', ' na', ' N/A', ' n/a', ' x', ' X', ' incomplete', ' 0']
        #removed '444' and 'ongoing' from incomplete indicators because requirements say 'need to participate in all mandatory challenges'. 444 is ongoing participation.
        #in other words, requirements do not state students need to have participated (past tense).
        
        ''' counts number of special events are completed OR ongoing (see comment above)'''
        for k, v in results_dict.items():# e.g {'C002': 10.5, ......}
            if k in special_events_list and v not in incomplete_indicators:
                counter += 1
                
        if student_obj.get_student_Type in ['U', ' U', 'u', ' u']:
            if counter >= 1:
                return True
            elif counter == 0:
                return False
            else: #TESTING PURPOSES
                print('#### ERROR IN PASSED SPECIAL METHOD #####')
                print('#### undergrad counter is incorrectly recognized ####')
                return False
        
        elif student_obj.get_student_Type in ['P', ' P', 'p', ' p']:
            if counter >= 2:
                return True
            elif counter == 1 or counter == 0:
                return False
            else: #TESTING PURPOSES
                print('#### ERROR IN PASSED SPECIAL METHOD #####')
                print('#### undergrad counter is incorrectly recognized ####')
                return False
        
        
    def passed_requirements(self, prompt): #prompt is student identifier 
        ''' testing: assumes that find student method returns a list of a single filtered object'''
        #The below is probably redunant. 
        #student_obj_list = self.find_student(prompt)
        #student_obj = student_obj_list[0]
        #student_id = student_obj.get_student_ID 
        has_passed_mandatory = self.passed_mandatory(prompt)
        has_passed_special = self.passed_special(prompt)
        
        if has_passed_mandatory and has_passed_special:
            return True
        elif has_passed_mandatory and not has_passed_special:
            #print('#### passed mandatory but NOT passed special')
            return False
        elif has_passed_special and not has_passed_mandatory:
            #print('#### has passsed special but NOT passed mandatory')
            return False
        else: #TESTING PURPOSES
            print('############### ERROR ###############')
            print('#### pass requirements not recognized by if statements block ####')
            
    def pass_requirement_for_all(self):
        #loops through student lists and applies the passed_requirements chain of methods. 
        for student in self.students_list: # student is object
            ID = student.get_student_ID
            has_passed = self.passed_requirements(ID) # returns boolean
            # boolean should be assigned to stored object instance via setter
            student.set_passed = has_passed 

   
    ''' this is not working properly. 
        might be worth fixing so that I can all it easily. '''
    def replace_ongoing_missed(self, prompt):
        #print('#### REPLACE ONGOING MISSED METHOD ####')
        #print('#### STRING INPUT #####')
        #print(string)
        list_of_strings = prompt.strip().split(',')
        #print('#### LIST OF STRINGS ####')
        #print(list_of_strings)
        '''potential bug: because I corrected the strip and spaces for the 444 and -1 strings'''
        for s in list_of_strings:
            s.replace('444','-- ')
            s.replace('-1', '  ')
        #print('##### LIST OF STRING AFER REPLACE #####')
        #print(list_of_strings)
        return list_of_strings ### it should return a list of strings which is good so it can be iterated on again. 
    
    
    def print_competition_report(self):
        file_object = open('report.txt', 'a')
        
        ''' #### Competition dashboard Code Block #### '''
        
        file_object.write('COMPETITION DASHBOARD\n')
        file_object.write('----------+-') #this string is hardcoded with length of RESULT string as first element of line. 
        line_length = [len(i.get_challenge_ID) for i in self.get_challenges_list[0:]] #dynamic code, deals with anynumber of challenges permitted by screen limitations
        length = len(line_length) #this variable is redundant as it's represented implicitly in the below for loop. 
        for x in line_length:
            file_object.write(('--'* x )+'--+')#(str(x) for x in line_length))
        file_object.write('\n')

        string = '| Result' + '  | '+'|'.join([f'{str(ch.get_challenge_ID):^8}' for ch in self.get_challenges_list])+ '|\n'
        file_object.write(string)
        
        file_object.write('----------+-')
        
        for x in line_length:
            file_object.write(('--'* x )+'--+')
        file_object.write('\n')
        
        for k, v in self.student_results_dict.items():
            replace_values = {"444": "   --  ", "-1":"       "}
            final_string = '| ' + f"{k:^7} {'|':^1} {' |'.join(f'{v:^7}'if float(v.strip())>0 and v.strip()!='444' else replace_values[v.strip()] for v in v.values())}"+' |\n'
            file_object.write(final_string)

        file_object.write('----------+-')
        for x in line_length:
            
            file_object.write(('--'* x )+'--+')
        
        file_object.write('\n')
        
        file_object.write(f'There are {self.student_count} students and {self.challenge_count} challenges.\n')
        
        best_student_time_list = self.best_student()
        file_object.write(f'The top student is {best_student_time_list[0]} with an average time of {best_student_time_list[1]:.2f} \n')
        
        
        
        
        ''' #### challenge information code block #### '''
        
        file_object.write('\n')
        file_object.write('CHALLENGE INFORMATION\n')
        challenge_report_line = '----------------------+' + '--------------------+' + '--------------------+' + '--------------------+' + '--------------------+' + '----------------+'+'\n'
        file_object.write(challenge_report_line)
        
        
        challenge_attributes = ['         Name       ','        Weight      ', '      Nfinish       ', '      Nongoing      ' , '   AverageTime  ']
        
        
        string = '|      Challenge      |'+'|'.join([f'{str(ch):}' for ch in challenge_attributes])+ '|\n'
    
        file_object.write(string)
        file_object.write(challenge_report_line)
        
        
        ''' this is the body for the challenges information'''
        
        sorted_challenges = self.sort_challenges_by_average() #should be a tupple of challenge objects.
        
        hardest_challenge = sorted_challenges[-1]
        hardest_challenge_name = hardest_challenge.challenge_Name.strip()
        hardest_challenge_ID = hardest_challenge.get_challenge_ID
        hardest_challenge_time = hardest_challenge.get_average_time

        for c in sorted_challenges: 
            
            
            challenge_print = f"|       {c.challenge_ID:^8}      |  ({c.challenge_Type.strip()}){c.challenge_Name:<15}|       {c.challenge_weight:^8}     |       {c.Nfinished:^8}     |       {c.Nongoing:^8}     |     {c.average_time:^8}   |\n"
            file_object.write(challenge_print)
        file_object.write(challenge_report_line)
        
        file_object.write(f"The most difficult challenge is {hardest_challenge_name} ({hardest_challenge_ID}) with an average time of {hardest_challenge_time} minutes.\n")
        file_object.write('Report competition_report.txt generated!\n')
        
        
             
        ''' STUDENT INFORMATION CODE BLOCK '''
        
        file_object.write('\n')
        file_object.write('STUDENT INFORMATION\n')
        student_report_line = '-------------+' + '-----------+' + '------------+' + '------------+' + '------------+' + '----------------+' + '----------------+' + '----------------+'+'\n'
        file_object.write(student_report_line)
        
        
        student_attributes = [' Name '.center(11),' Type '.center(12), ' Nfinish '.center(12), ' Nongoing '.center(12) , ' AverageTime '.center(16), ' Score '.center(16), ' Wscore '.center(16)]
        
        string = '| StudentID  |'.center(12) +'|'.join([f'{str(ch):}' for ch in student_attributes])+ '|\n'
        file_object.write(string)
        file_object.write(student_report_line)

        

        sorted_students = self.sort_students_by_average()
        best_student = sorted_students[-1]
        best_student_name = best_student.student_Name.strip()
        best_student_ID = best_student.student_ID
        best_student_time = best_student.average

        sorted_students = self.sort_students_by_weighted_score() #should be a tupple of student objects.
        for s in sorted_students: 
            
            passed_display = 'error'
            if s.passed == True: #accesses student object attribute
                passed_display = ''
            elif s.passed == False: #accesses student object attribute
                passed_display = '!'
            else:
                print('#### ERROR IN passed_display ####')
            print_student = f"|{s.student_ID.center(12)}|{passed_display:>3}{s.student_Name.strip():<8}|{s.student_Type.center(12)}|{str(s.Nfinished).center(12)}|{str(s.Nongoing).center(12)}|{str(s.average).center(16)}|{str(s.score).center(16)}|{str(s.weighted_score).center(16)}|\n"
            file_object.write(print_student)
        file_object.write(student_report_line)
        
        file_object.write(f"The student with the fastest average time is {best_student_ID} ({best_student_name} with an average time of {best_student_time} minutes)\n")
        file_object.write('Report competition_report.txt generated!\n')
        file_object.write('\n\n')
        
       
        
        file_object.close()
   
'''#### COMMAND LINE CODE BLOCK ####'''

if __name__  ==  '__main__':
    print('######## SYS.ARGV #########')

    argv = sys.argv
    if len(argv) == 1:
        print('### LEN ARGV == 1 ###')
        sys.stdout.write(f'[Usage:] {os.path.basename(__file__)} <results_file> <challenges_file> <students_file> \n')
        
        ''' REMEMBER TO REMOVE THIS BELOW TO TEST THE COMMAND LINE LATER'''
        
        results_file = 'results.txt'
        challenges_file = 'challenges.txt'
        students_file = 'students.txt'
        comp = Competition(results_file, challenges_file, students_file)
    if len(argv) == 2 :
        print('### LEN ARGV == 2 ###')
        results_file = str(argv[1])
        comp = Competition(results_file)
    elif len(argv) == 3:
        results_file = argv[1]
        challenges_file = argv[2]
        comp = Competition(results_file, challenges_file)
    elif len(argv) == 4 :
        print('### LEN ARGV == 4 ###')
        results_file = argv[1]
        challenges_file = argv[2]
        students_file = argv[3]
        comp = Competition(results_file, students_file, results_file)
    else:
        print('##### ERROR IN COMMAND LINE ####')    
