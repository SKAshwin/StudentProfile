#!/usr/bin/python3

#TODO: test transcript class
import constants as c

#Modules are immutable and hence thread_safe
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


#A report on the specific score a student received on a module, and the semester it was
#taken, as well as what year it was read (can be different from acadlevel)
#score can be a numerical value or a DaVinciGrade/EnrichmentGrade
#Note that it is *always* safe, by definition, to multiply the score attribute with
#anything else, and it is also safe to compare to score of THE SAME TYPE
#No other operation on .score is defined behaviour

#ModuleReport instances are immutable
class ModuleReport:
    def __init__(self, module, score, semester, year):
        self.module = module
        self.score = score
        self.semester = semester
        self.year = year
        self.mc = module.mc #convenience

#CAP is a datatype used to hold cap total scores and mcs, to prevent loss of information about
#the specific credits and scores that resulted in the numeric CAP score
#For example, a cap score of 4.0 could be the result of 100 total score and 25 credits, or
#120 total score and 30 credits. By using a CAP object to encapsulate this data (and calling
#.cap() to get a numeric value), more can be understood about a particular CAP score, and
#the addition of new modules or summing of CAP scores can be done properly.

#CAP instances are immutable. The + 
#operation and the add_module method create new instances. Hence, it is thread safe
class CAP:
    #Two initializers.
    
    #CAP() is an empty cap score, with 0 score and 0 MC. Calling .cap() on an empty CAP() will throw
    #an error

    #CAP(total_score,total_mc), where total_score and total_mc are the total score (obtained by
    #multiplying every component score with the credits) and sum of credits respectively.

    def __init__(self,total_score=0,total_mc=0):
        self.score = total_score
        self.mc = total_mc
    #returns new instance
    def add_module(self, module_report):
        return CAP(self.score + module_report.score*module_report.mc,self.mc+module_report.mc)
    def decompose(self):
        return (self.score,self.mc)
    def cap(self):
        return self.score/self.mc
    #Creates a new CAP instance by summing total score and total_mc
    #not the same as summing up cap and averaging (as used in grad cap calculations)
    def __add__(self, other):
        return CAP(self.score+other.score,self.mc+other.mc)
    def __gt__(self, other):
        return self.cap()>other.cap()
    def __lt__(self, other):
        return other.cap()>self.cap()
    def __ge__(self, other):
        return not self < other
    def __le__(self, other):
        return not self > other
    def __eq__(self, other):
        return self.cap()==other.cap()
    def __ne__(self, other):
        return self.cap()!=other.cap()
    def __str__(self):
        return str(self.decompose())
    __radd__ = __add__
cap1 = CAP(100,20)
cap2 = CAP(120,30)
print((cap1+cap2).cap())
print((cap1.cap()+cap2.cap())/2)
print(cap1>cap2)
print(cap1<cap2+cap1)
print(cap1==CAP(120,24))
ma5404 = Module('ma5404',2)
ma5404r = ModuleReport(module=ma5404, score=4.5, semester=1, year=5)
ma5106 = Module('ma5106',5)
ma5106r = ModuleReport(module=ma5106, score=5.0, semester=1, year=5)
print(CAP().add_module(ma5404r).add_module(ma5106r))

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
    def __core_bi_cap(self, year_type, mt):
        core_cap = CAP()
        for module_report in self.modules:
            module = module_report.module
            if module.year_type()!=year_type or (not mt and module.is_mt()):
                continue
            if not module.is_elective() and not module.is_enrichment():
                core_cap.add_module(module_report)
        return core_cap
    def biennial_cap(self, year_type, mt):
        core_cap = self.__core_bi_cap(year_type, mt)
        base_cap = core_cap.cap()
        for module_report in self.modules:
            module = module_report.module
            if year_type!=module.year_type():
                continue
            if module.is_elective() and module_report.score>base_cap:
                core_cap.add_module(module_report)
        return core_cap
    def grad_cap(self):
        mt_cap = self.biennial_cap(c.INTERMEDIATE,mt=True).cap() + self.biennial_cap(c.ADVANCED, mt=True).cap()
        no_mt_cap = self.biennial_cap(c.INTERMEDIATE,mt=False).cap() + self.biennial_cap(c.ADVANCED, mt=False).cap()
        return max(mt_cap,no_mt_cap)/2

