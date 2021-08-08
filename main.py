import pandas as pd
pd.set_option('display.max_columns', None)
from ENGL_AA_Requirements import MajorRequirements


class StudentInfo:
    not_eligible_courses = ['MATH 80A', 'MATH 60', 'ENGL 72', 'ENGL 52', 'ACLR 90', 'ACLR 91', 'ACLR 92', 'CHEM 95A',
                            'CHEM 95B',
                            'CHEM 95C', 'CHEM 95D', 'CHEM 95E', 'CHEM 95F', 'LIBR 50', 'LAW 98', 'LAW 99', 'BCOT 5A']
    not_eligible_numbers = ['21A', '21B', '5A',  '18.1', '3T', '1T', '6T',  '42.07', '42.05']

    eligible_course_numbers = ['50B', '50C', '51A', '51B', '51C', '52A', '52B', '52C', '62B', '71C', '60A', '62A','70A',
                               '71A', '71B', '60L', '50A', '54A', '61A', '70C', '60B', '61B']

    def __init__(self, student_id, courses, major):
        self.major = major
        self.student_id = student_id
        self.courses = courses
        self.student_course_dict = {}
        self.degree_applicable_courses_dict = {}
        # self.completed_ge_course = {}
        # print(self.courses)

    def eligible_course_list(self):
        # print(len(self.courses))
        for i in range(len(self.courses)):
            # print(i)
            # print(student_course_list.loc[i, "ID"])
            # print(self.student_id)
            if self.student_id == student_course_list.loc[i, "ID"]:
                if student_course_list.loc[i, "Class Subject"] != "AED":
                    if student_course_list.loc[i, "Course"] not in StudentInfo.not_eligible_courses:
                        # print(student_course_list.loc[i, "Class Catalog Number"])
                        if student_course_list.loc[i, "Class Catalog Number"] not in StudentInfo.not_eligible_numbers:
                            if student_course_list.loc[i, "Course"] != "MATH 80A":
                                if student_course_list.loc[i, "Class Catalog Number"] != "21A":
                                    if student_course_list.loc[i, "Class Catalog Number"] != "21B":
                                        if student_course_list.loc[i, "Class Catalog Number"] != "5A":
                                            course_number = student_course_list.loc[i, "Class Catalog Number"]
                                            # print("course number", course_number)
                                            # print(len(course_number))
                                            if student_course_list.loc[i, 'Class Catalog Number'] in StudentInfo.eligible_course_numbers:
                                                 course_number = course_number[0:2]
                                                 print('eligible', course_number)
                                            else:
                                                if len(course_number) > 3:
                                                    course_number = course_number[0:3]

                                                # print(course_number)
                                            if course_number == "80B":
                                                self.student_course_dict[student_course_list.loc[i, "Course"]] = \
                                                    student_course_list.loc[i, "Units"]
                                            elif course_number == "5L":
                                                self.student_course_dict[student_course_list.loc[i, "Course"]] = \
                                                    student_course_list.loc[i, "Units"]
                                            elif int(course_number) >= 50:
                                                # print(student_course_list.loc[i, 'Official Grade'])
                                                if student_course_list.loc[i, 'Official Grade'] == 'A' \
                                                        or student_course_list.loc[i, 'Official Grade'] == 'B' \
                                                        or student_course_list.loc[i, 'Official Grade'] == 'C' \
                                                        or student_course_list.loc[i, 'Official Grade'] == 'P':
                                                    # if student_course_list.loc[i, 'Official Grade'] == "B":
                                                    #     if student_course_list.loc[i, 'Official Grade'] == "C":
                                                    #         if student_course_list.loc[i, 'Official Grade'] == "P":
                                                    print('official grade', student_course_list.loc[i, 'Official Grade'])
                                                    self.student_course_dict[
                                                        student_course_list.loc[i, "Course"]] = \
                                                        student_course_list.loc[i, "Units"]

                                                    # print(self.student_id, self.student_course_dict)
                                                    self.degree_applicable_courses_dict = self.student_course_dict
        return self.degree_applicable_courses_dict


class GeRequirements:
    ge_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/PlanA_GE.csv")

    def __init__(self, revised_course_list):
        self.revised_course_list = revised_course_list
        self.completed_ge_courses = {}
        self.completed_ge_units = []

    def ge_courses_completed(self, area_name):

        for i in range(len(self.ge_dataframe[area_name])):
            for key in self.revised_course_list:
                if key == self.ge_dataframe.loc[i, area_name]:
                    if area_name not in self.completed_ge_courses:
                        self.completed_ge_courses[area_name] = key
                        if "Proficiency" not in area_name:
                            self.completed_ge_units.append(self.revised_course_list[key])
                        total = sum(self.completed_ge_units)

    def area_e_ge_requirements(self):
        area_e_list = []
        total_ge_units = sum(self.completed_ge_units)
        # print("total ge units", total_ge_units)
        for i in range(len(self.ge_dataframe['AreaE'])):
            for key in self.revised_course_list:
                if key == self.ge_dataframe.loc[i, 'AreaE']:
                    if len(self.completed_ge_courses) == 9:
                        if total_ge_units < 18:
                            area_e_list.append(key)
                            self.completed_ge_courses['AreaE'] = area_e_list
                            self.completed_ge_units.append(self.revised_course_list[key])
        return self.completed_ge_courses

    def reading_proficiency(self):
        if 'Reading Proficiency' not in self.completed_ge_courses:
            if sum(self.completed_ge_units) > 10:
                self.completed_ge_courses['Reading_Proficiency'] = 'Met(GE Units)'


class DegreeApplicableUnits(GeRequirements):

    def __init__(self, revised_course_list, major_courses_list, completed_ge_courses, completed_ge_units,
                 major_units_list):
        self.major_courses_list = major_courses_list
        self.revised_course_list = revised_course_list
        self.completed_ge_courses = completed_ge_courses
        self.completed_ge_units = completed_ge_units
        self.major_units_list = major_units_list
        self.elective_course_list = []
        self.elective_units_list = []
        self.elective_dict = {}

    def elective_courses(self):
        ge_course = False
        major_course = False
        degree_units = 0
        for course_key in self.revised_course_list:

            if degree_units < 60:
                ge_course = False
                major_course = False

                if course_key in self.completed_ge_courses.values():
                    ge_course = True

                if course_key in self.major_courses_list:
                    major_course = True

                if course_key in self.elective_course_list:
                    elective_course = True

                if ge_course == False:
                    if not major_course:
                        # print(course_key)
                        self.elective_course_list.append(course_key)
                        self.elective_dict[course_key] = self.revised_course_list[course_key]
                        self.elective_units_list.append(self.revised_course_list[course_key])
                        degree_units = sum(self.completed_ge_units) + sum(self.major_units_list) + sum(
                            self.elective_units_list)


class DegreeProgressReports:
    columns = ['Student_ID', 'Math_Proficiency', 'Writing_Proficiency', 'Reading_Proficiency', 'Health_Proficiency',
               'AreaA', 'AreaB1',
               'AreaB2', 'AreaC',
               'AreaD1', 'AreaD2', 'AreaE', 'Electives', 'GE_Units']
    df = pd.DataFrame(columns=columns)
    AA_ge_requirements = {'Math_Proficiency': 0, 'Writing_Proficiency': 0, 'Reading_Proficiency': 0,
                          'Health_Proficiency': 0, 'AreaA': 0,
                          'AreaB1': 0, 'AreaB2': 0, 'AreaC': 0, 'AreaD1': 0, 'AreaD2': 0, 'AreaE': 0, 'Electives': 0}

    def __init__(self, completed_ge_courses, completed_ge_units, student_id):
        self.student_id = student_id
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses

    def ge_requirements_completed(self):
        length = len(DegreeProgressReports.df)
        for ge_key in DegreeProgressReports.AA_ge_requirements:

            if ge_key not in self.completed_ge_courses:
                DegreeProgressReports.df.loc[length, ge_key] = "0"

            else:
                DegreeProgressReports.df.loc[length, ge_key] = self.completed_ge_courses[ge_key]
        total_ge_units = sum(self.completed_ge_units)
        DegreeProgressReports.df.loc[length, 'GE_Units'] = total_ge_units
        DegreeProgressReports.df.loc[length, 'Student_ID'] = self.student_id


class MajorProgressReport(MajorRequirements):
    columns = ['Student_ID', 'Major1', 'Major2', 'Major3', 'Major4', 'Major5']
    major_df = pd.DataFrame(columns=columns)
    requirements = []

    def __init__(self, student_id, major_course_dict, major_units, area_units):
        self.area_units = area_units
        self.student_id = student_id
        self.major_course_dict = major_course_dict
        self.major_units = major_units
        self.major_df = pd.DataFrame
        self.requirements_dict = {}

    def major_requirements_completed(self):

        requirements_for_major = dict.fromkeys(self.columns, 0)
        length = len(MajorProgressReport.major_df)

        for major_key in requirements_for_major:
            if major_key not in self.major_course_dict:
                MajorProgressReport.major_df.loc[length, major_key] = '0'
            else:
                MajorProgressReport.major_df.loc[length, major_key] = self.major_course_dict[major_key]

        MajorProgressReport.major_df.loc[length, 'Student_ID'] = self.student_id


class DegreeCompletion:
    columns = ['Student_ID', 'Major', 'GE_Units', 'Major_Units', 'Elective_Units', 'Degree_Units']
    degree_units_df = pd.DataFrame(columns=columns)
    degree_units_df.sort_values(by=['Degree_Units'], inplace=True, ascending=False)
    columns2 = ['Student_ID', 'Major', 'Degree_Units', 'GE_Courses', 'Major_Courses', 'Elective_Courses']
    degree_courses_df = pd.DataFrame(columns=columns2)

    def __init__(self, completed_ge_courses, completed_ge_units, major_course_dict, area_units_dict, elective_courses,
                 elective_units, student_id):
        self.elective_units = elective_units
        self.elective_courses = elective_courses
        self.area_units_dict = area_units_dict
        self.major_course_dict = major_course_dict
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.major_requirements_dict = {}

    def degree_completion(self):
        length = len(DegreeCompletion.degree_units_df)
        # length = len(DegreeCompletion.degree_courses_df)
        # if len(self.completed_ge_courses) >= 10:
        #     if sum(self.completed_ge_units) >= 18:
        #         if len(self.major_course_dict) == len(MajorRequirements.major_requirements_dict):
        #             if sum(major_requirements.area_units_dict.values()) >= sum(MajorRequirements.major_requirements_dict.values()):
        #                 if sum(self.completed_ge_units) + sum(self.major_units) + sum(self.elective_units) >= 60:
        #
        DegreeCompletion.degree_units_df.loc[length, 'Student_ID'] = student.student_id
        DegreeCompletion.degree_units_df.loc[length, 'Major'] = student.major
        DegreeCompletion.degree_units_df.loc[length, 'GE_Units'] = sum(self.completed_ge_units)
        major_units_total_value = sum(self.area_units_dict.values())
        DegreeCompletion.degree_units_df.loc[length, 'Major_Units'] = major_units_total_value
        DegreeCompletion.degree_units_df.loc[length, 'Elective_Units'] = sum(self.elective_units)
        DegreeCompletion.degree_units_df.loc[length, 'Degree_Units'] = sum(self.completed_ge_units) + sum(
            self.elective_units) + major_units_total_value

        DegreeCompletion.degree_courses_df.loc[length, 'Student_ID'] = student.student_id
        DegreeCompletion.degree_courses_df.loc[length, 'Major'] = student.major
        DegreeCompletion.degree_courses_df.loc[length, 'Degree_Units'] = sum(self.completed_ge_units) + sum(
            self.elective_units) + major_units_total_value
        ge_list = self.completed_ge_courses.items()
        DegreeCompletion.degree_courses_df.loc[length, 'GE_Courses'] = ge_list
        major_list = self.major_course_dict.items()
        DegreeCompletion.degree_courses_df.loc[length, 'Major_Courses'] = major_list
        DegreeCompletion.degree_courses_df.loc[length, 'Elective_Courses'] = self.elective_courses

        # DegreeCompletion.degree_courses_df.loc[length, 'Major_Courses'] = self.major_course_dict
        # DegreeCompletion.degree_courses_df.loc[length, 'Elective_Courses'] = self.elective_courses
        # DegreeCompletion.degree_courses_df.loc[length, 'Degree_Units'] = sum(self.completed_ge_units) + sum(
        #     self.elective_units) + sum(self.major_units)
        # print(DegreeCompletion.degree_courses_df)


student_course_list = pd.read_csv(
    "C:/Users/family/Desktop/Programming/Enrollment Histories/EnrollmentHistory_20210602.csv")
# student_course_list = pd.read_csv("C:/Users/family/Desktop/Programming/shortlist_studentlist.csv")
student_id_list = []
student_course_dict = {}
# degree_courses = pd.read_csv("C:/Users/family/Desktop/Programming/PlanA_GE.csv")

for i in range(len(student_course_list)):
    if student_course_list.loc[i, "ID"] not in student_id_list:
        student_id_list.append(student_course_list.loc[i, "ID"])
# print(student_id_list)

for student_id in student_id_list:
    student = StudentInfo(student_id=student_id, courses=student_course_list, major='Comm-AA')
    student.eligible_course_list()
    # print(student.student_id, student.student_course_dict)
    ge_requirements = GeRequirements(student.degree_applicable_courses_dict)
    ge_requirements.ge_courses_completed('Math_Proficiency')
    ge_requirements.ge_courses_completed('Writing_Proficiency')
    ge_requirements.ge_courses_completed('Health_Proficiency')
    ge_requirements.ge_courses_completed('Reading_Proficiency')
    ge_requirements.ge_courses_completed('AreaA')
    ge_requirements.ge_courses_completed('AreaB1')
    ge_requirements.ge_courses_completed('AreaB2')
    ge_requirements.ge_courses_completed('AreaC')
    ge_requirements.ge_courses_completed('AreaD1')
    ge_requirements.ge_courses_completed('AreaD2')
    ge_requirements.area_e_ge_requirements()
    major_requirements = MajorRequirements(student.eligible_course_list(), ge_requirements.area_e_ge_requirements())
    major_requirements.major_courses_completed(area_name="Major1", total_units=3)
    major_requirements.major_courses_completed(area_name="Major2", total_units=3)
    major_requirements.major_courses_completed(area_name="Major3", total_units=6)
    major_requirements.major_courses_completed(area_name="Major4", total_units=6)
    # major_requirements.major_courses_completed(area_name="Major4", total_units=6)
    degree_applicable_units = DegreeApplicableUnits(student.eligible_course_list(),
                                                    major_requirements.major_courses_list,
                                                    ge_requirements.area_e_ge_requirements(),
                                                    ge_requirements.completed_ge_units,
                                                    major_requirements.major_units_list)
    degree_applicable_units.elective_courses()
    ge_requirements.reading_proficiency()
    degree_reports = DegreeProgressReports(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                           student.student_id)
    degree_reports.ge_requirements_completed()
    major_report = MajorProgressReport(student_id=student.student_id,
                                       major_course_dict=major_requirements.major_course_dict,
                                       major_units=major_requirements.major_units_list,
                                       area_units=major_requirements.area_units_dict)
    # major_report.dataframe()
    major_report.major_requirements_completed()

    degree_completion = DegreeCompletion(completed_ge_courses=ge_requirements.completed_ge_courses,
                                         completed_ge_units=ge_requirements.completed_ge_units,
                                         major_course_dict=major_requirements.major_course_dict,
                                         area_units_dict=major_requirements.area_units_dict,
                                         elective_courses=degree_applicable_units.elective_course_list,
                                         elective_units=degree_applicable_units.elective_units_list,
                                         student_id=student.student_id)
    degree_completion.degree_completion()
    # major_report.major_requirements_assigned(df="major_df")
    # print(degree_reports)
    # print(degree_reports.AA_ge_requirements)
    # print(student.student_id, student.student_course_dict)
    # print(student.student_id, student.courses )
    # print(student.student_id, ge_requirements.completed_ge_courses)
    # print(student.student_id, ge_requirements.completed_ge_units, sum(ge_requirements.completed_ge_units))
    # print(student.student_id, major_requirements.major_course_dict)
    # # print(student.student_id, major_requirements.major_units_list, sum(major_requirements.major_units_list))
    # # print(sum(ge_requirements.completed_ge_units) + sum(major_requirements.major_units_list))
    # print()
    # # ge_courses.ge_courses_completed('Math_Proficiency')
    # # print(ge_courses.completed_ge_courses)
    # # DegreeProgressReports.df.to_csv('E:/Work/Division/Student_Progress_GE.csv')
    # # MajorProgressReport.major_df.to_csv('D:/Work/Division/Student_Progress_Major.csv')
    # print(DegreeProgressReports.df)
    # print(MajorProgressReport.major_df)
DegreeCompletion.degree_units_df.sort_values(by=['Degree_Units'], inplace=True, ascending=False)
# print(DegreeCompletion.degree_units_df)
DegreeCompletion.degree_courses_df.sort_values(by=['Degree_Units'], inplace=True, ascending=False)
# print(DegreeCompletion.degree_courses_df)
# DegreeProgressReports.df.to_csv('E:/Work/Division/EnglishAA_Student_Progress.csv')
DegreeCompletion.degree_units_df.to_csv('E:/Work/Division/COMM_AA_Units.csv')
DegreeCompletion.degree_courses_df.to_csv('E:/Work/Division/COMM_AA_Courses.csv')

