#!/usr/bin/python3

#A Module has a module code, modular credits, a score and a semester.
#From these primary attributes, supplied in the constructor, several secondary attributes are
#derived.
#These are subject,acadlevel,module_num,type_digit and suffix
class Module:
    class YearType:
        pass
    class ModuleType:
        pass
    class SuffixType:
        pass
    FOUNDATION,INTERMEDIATE,ADVANCED = YearType(),YearType(),YearType()
    ELECTIVE,CORE,ENRICHMENT,HONOR = ModuleType(),ModuleType(),ModuleType(),ModuleType()
    PRECLUSION,CORE_PREREQ,MT_IN_LIEU,EXTERNAL = SuffixType(),SuffixType(),SuffixType(),SuffixType()
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
            return ENRICHMENT
        elif(is_core()):
            return CORE
        elif(is_elective()):
            return ELECTIVE
        elif(is_honor()):
            return HONOR
        return None


    def is_foundation(self):
        return self.acadlevel ==1 or self.acadlevel==2
    def is_intermediate(self):
        return self.acadlevel==3 or self.acadlevel==4
    def is_advanced(self):
        return self.acadlevel==5 or self.acadlevel==6
    def year_type(self):
        if is_foundation() :
            return FOUNDATION
        elif is_intermediate():
            return INTERMEDIATE
        elif is_advanced():
            return ADVANCED

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
            return PRECLUSION
        elif is_core_prereq():
            return CORE_PREREQ
        elif is_mt_inlieu():
            return MT_IN_LIEU
        elif is_external():
            return EXTERNAL

ma5404 = Module(code='MA5404',mc=2)
print(ma5404.is_advanced())
print(ma5404.is_core())
print(ma5404.subject)

#A report on the specific score a student received on a module, and the semester it was
#taken
class ModuleReport:
    def __init__(self, module, score, semester):
        self.module = module
        self.score = score
        self.semester = semester

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
