from dataclasses import dataclass

LiveRampDataStoreBase = """data_store_segment_id,name,description,provider,price
1004765519,123Push > Consumer > Demographic > Senior Citizens > Age 65+,Individuals living in a household with 3 or more people.,123Push,0.75
1000846336,Alliant > Automotive > ,In-Market model for new vehicle,Alliant,2.75
1000846346,Alliant > Automotive > Auto - In Market for Insurance,In-Market model for auto insurance,Alliant,2.75
1000847476,Alliant > Automotive > Auto - In Market for Used Vehicle,In-Market model for used vehicle,Alliant,2.75
1000846216,Alliant > Demographic > Homeowner,Active multi-channel households who own their home,Alliant,2.0
1000845656,Alliant > Demographic > Age 25-29 years,Active multi-channel households with a person age 25-29 years old present in the HH.,Alliant,1.75
1000848136,Alliant > Demographic > Age 30-34 years,Active multi-channel households with a person age 30-34 years old present in the HH.,Alliant,1.75
1000845646,Alliant > Demographic > Age 35-39 years,Active multi-channel households with a person age 35-39 years old present in the HH.,Alliant,1.75
1000848146,Alliant > Demographic > Age 40-44 years,Active multi-channel households with a person age 40-44 years old present in the HH.,Alliant,1.75"""


# 123Push > 
#   Consumer > 
#     Demographic > 
#       Senior Citizens > 
#         Age 65+1

# 123Push >
#   ...
# Alliant > 
  
#   Automotive > 
#     Auto - In Market for Insurance
#     Auto - In Market New Vehicle
#     Auto - In Market for Used Vehicle

# 1. parse the long csv style string and build a layered structure to represent it

def parseCsv (s: str):
    p2 = len(s)-1
    print(p2)
    comma_index = s.find(",")
    print(comma_index)
    l_lines = s.split('\n')
    print(l_lines)
    comma_indexes = s.split(",")
    print(comma_indexes)
    l_index = s.find(" > ")
    tokens = s[1]
    print(tokens)
    print(l_index)
    # for each > 
    

def simple_splitter (s:str):
    p1 = 0
    p2 = len(s)-1
    while p1 <= p2:
        if s[p1] == ">":
            field_name = f'field{p1}'
            
            string1 = s[:p1] + s[p1+1:]
            string2 = s[:p2] + s[p2+1:]
            return string1 == string1[::-1] or string2 == string2[::-1]
        p1 += 1
        p2 -= 1

@dataclass
class live_ramp:
  data_store: str 
  name: str
  description: str


parseCsv(LiveRampDataStoreBase)
#simple_splitter(LiveRampDataStoreBase)