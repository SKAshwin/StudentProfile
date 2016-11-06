#!/usr/bin/python3
import constants as c
class Module:
    @staticmethod
    def SUBJECT_CODES():
        return ('AE','CL','EL','GM','MA','PE','AR','CM','EN','HD','MH','TH',
                'BG','CS','FR''HY','ML','TL','BL','DV','GE','IH','MU','UD','CH',
                'EC','GJ','JP','PC')
    @staticmethod
    def SUBJECT_MAPPINGS():
        return (('Mathematics',('MA','CS')),('Mother Tongue',('GM','HD','MH','TH',
                'TL','BG','ML','CL','FR','UD','CH','GJ','JP')),('Physics',('PC',)),
                ('Humanities',('EN','AR','HY','GE','IH','MU','EC')),('English',('EL',)),
                ('Chemistry',('CM',)),('Biology',('BL',)))
    #obtains subject for provided module code
    @staticmethod
    def calc_subject(code):
        for mapping in Module.SUBJECT_MAPPINGS():
            corresponding_codes = mapping[1]
            if code[0:2] in corresponding_codes:
                return mapping[0]
        return None
    @staticmethod
    def calc_module_num(code):
        return code[4:6]
    #gets type digit in a module code: type digit indicates if it is core, elective, honors etc
    @staticmethod
    def calc_type_digit(code):
        return int(code[3])
    #gets suffix of module code: empty string if no suffix. Suffix is a final letter present in
    #some module codes
    @staticmethod
    def calc_suffix(code):
        if(len(code)<7):
            return ''
        return code[-1]
    #gets the academic level indicated by a module code - academic level is the year in which the
    #module is usually read
    @staticmethod
    def calc_acadlevel(code):
        return int(code[2])


    def __init__(self,code,mc):
        self.code = code
        self.mc = mc
        self.subject = Module.calc_subject(code)
        self.acadlevel = Module.calc_acadlevel(code)
        self.module_num = Module.calc_module_num(code)
        self.type_digit = Module.calc_type_digit(code)
        self.suffix = Module.calc_suffix(code)
    
    def is_elective(self):
        return self.type_digit==2
    def is_core(self):
        return self.type_digit==1
    def is_enrichment(self):
        return self.type_digit==3
    def is_honor(self):
        return self.type_digit==4
    #Returns a ModuleType instance; one of 4 constants
    def module_type(self):
        if(is_enrichment()):
            return c.ENRICHMENT
        elif(is_core()):
            return c.CORE
        elif(is_elective()):
            return c.ELECTIVE
        elif(is_honor()):
            return c.HONOR
        return None


    def is_foundation(self):
        return self.acadlevel ==1 or self.acadlevel==2
    def is_intermediate(self):
        return self.acadlevel==3 or self.acadlevel==4
    def is_advanced(self):
        return self.acadlevel==5 or self.acadlevel==6
    def year_type(self):
        if is_foundation() :
            return c.FOUNDATION
        elif is_intermediate():
            return c.INTERMEDIATE
        elif is_advanced():
            return c.ADVANCED

    #checks if module is a mother tongue module
    #used in calculating grad cap
    def is_mt(self):
        return self.subject == 'Mother Tongue'
    
    def is_preclusion(self):
        return self.suffix=='A'
    def is_core_prereq(self):
        return self.suffix=='C'
    def is_mt_inlieu(self):
        return self.suffix=='M'
    def is_external(self):
        return self.suffix=='V'
    def suffix_type():
        if is_preclusion():
            return c.PRECLUSION
        elif is_core_prereq():
            return c.CORE_PREREQ
        elif is_mt_inlieu():
            return c.MT_IN_LIEU
        elif is_external():
            return EXTERNAL



print(c.UNSATISFACTORY>c.MERIT)
print(c.PASS>c.FAIL)
print(c.MERIT>c.PASS)
print(c.MERIT>c.DISTINCTION)
#A report on the specific score a student received on a module, and the semester it was
#taken, as well as what year it was read (can be different from acadlevel)
#score can be a numerical value or a DaVinciGrade/EnrichmentGrade
#Note that it is *always* safe, by definition, to multiply the score attribute with
#anything else, and it is also safe to compare to score of THE SAME TYPE
#No other operation on .score is defined behaviour
class ModuleReport:
    def __init__(self, module, score, semester, year):
        self.module = module
        self.score = score
        self.semester = semester
        self.year = year

#The transcript consists of *all* the modules taken by a student
#the report for a specific semester should be represented by a ReportCard instance
#transcript should be able to generate ReportCards, as well as give biennial cap and
#grad cap
class Transcript:
    def __init__(self, identity):
        self.identity = identity
        self.modules = []
    #add a ModuleReport instance to this transcript
    def add_module(module_report):
        self.modules.append(module_report)
    def remove_module(module_report):
        self.modules.remove(module_report)
    def __core_cap():
        pass
