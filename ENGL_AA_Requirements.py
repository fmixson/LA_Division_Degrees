import pandas as pd


class MajorRequirements:
    # major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/English_PlanA_GE.csv")
    major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/Copy of COMM_AA.csv")
    major_requirements_dict = {}

    def __init__(self, revised_course_list, completed_ge_courses):
        self.revised_course_list = revised_course_list
        self.completed_ge_courses = completed_ge_courses
        self.major_course_dict = {}
        self.major_courses_list = []
        self.major_courses_list2 = []
        self.major_units_list = []
        self.major_units_dict = {}
        self.area_units_dict = {}

    def major_courses_completed(self, area_name, total_units):
        self.major_courses_list2 = []
        ge_course = False
        major_course = False
        total_area_units = 0
        area_units_list = []
        MajorRequirements.major_requirements_dict[area_name] = total_units

        for i in range(len(self.major_requirements_dataframe[area_name])):
            if total_area_units < total_units:
                for course_key in self.revised_course_list:
                    if course_key == self.major_requirements_dataframe.loc[i, area_name]:
                        if course_key in self.completed_ge_courses.values():
                            ge_course = True
                        if course_key in self.major_courses_list:
                            major_course = True
                        if not major_course:
                            self.area_units_dict[area_name] = self.revised_course_list[course_key]
                            # print(self.area_units_dict)
                            self.major_courses_list.append(course_key)
                            self.major_courses_list2.append(course_key)
                            self.major_course_dict[area_name] = self.major_courses_list2
                            area_units_list.append(self.revised_course_list[course_key])
                            # print(area_units_list)
                            if not ge_course:
                                self.major_units_list.append(self.revised_course_list[course_key])
                    total_area_units = sum(area_units_list)
                    self.area_units_dict[area_name] = total_area_units
