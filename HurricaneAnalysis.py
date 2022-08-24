#!/usr/bin/env python
# coding: utf-8

# In[97]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[98]:


def update_damages(damages):
    """Convert damages data from string to float and return converted data as a list."""
    updated_damages = []
    for damage in damages:
        if damage != "Damages not recorded":
            if 'M' in damage:
                updated_damages.append(float(damage.replace('M','')) * 1000000)
            elif damage.find('B'):
                updated_damages.append(float(damage.replace('B','')) * 1000000000)
        else:
            updated_damages.append(damage)
    return updated_damages

#update_damages(damages)


# In[99]:


hurricanes = {}
def hurricanes_dict (names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
    for i in range(len(names)):
        hurricanes[names[i]]={"Name":names[i], "Month":months[i], "Year": years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected":areas_affected[i], "Damages":damages[i], "Deaths":deaths[i]}
    return hurricanes

hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, update_damages(damages), deaths)
    
        


# In[100]:


hurricanes_by_year = {}
"""Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""

def hurricanes_year(hurricanes):
    for i in hurricanes:
        current_year = hurricanes[i]["Year"]
        current_cane = hurricanes[i]
        if current_year not in hurricanes_by_year.keys():
            hurricanes_by_year[current_year] = list(current_cane)
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

hurricanes_year(hurricanes)


# In[101]:


affected_areas_count = {}

def hurricane_area(hurricanes):
    """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""

    for i in hurricanes:
        for j in hurricanes[i]["Areas Affected"]:
            if j not in affected_areas_count:
                affected_areas_count[j] = 1
            else:
                affected_areas_count[j] += 1
    return affected_areas_count

hurricane_area(hurricanes)


# In[102]:


def area_count(areas):
    """Find most affected area and the number of hurricanes it was involved in."""
    max_area = ''
    max_area_count = 0
    for k, v in areas.items():
        if v > max_area_count:
            max_area = k
            max_area_count = v
    return max_area, max_area_count;
        
max_area, max_area_count = area_count(affected_areas_count)
print('The most affected area is: ' + str(max_area) + ' with ' + str(max_area_count) + ' hurricanes.')
        


# In[103]:


def mortality(hurricanes):
    """Find the highest mortality hurricane and the number of deaths it caused."""
    max_mortality_cane = ''
    max_mortality = 0
    for i in hurricanes:
        if hurricanes[i]["Deaths"] > max_mortality:
            max_mortality_cane = i
            max_mortality = hurricanes[i]["Deaths"]
    return max_mortality_cane, max_mortality;

max_mortality_cane, max_mortality = mortality(hurricanes)
print("{cane} hurricane is the most lethal hurricane with {deaths} deaths.".format(cane = max_mortality_cane, deaths = max_mortality))
        


# In[104]:


def mortality_rating(hurricanes):
    """Categorize hurricanes by mortality and return a dictionary."""
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
                
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                       
    for i in hurricanes:
        deaths = hurricanes[i]["Deaths"]
        for j in range(len(mortality_scale)-1):
            if deaths > mortality_scale[j] and deaths <= mortality_scale[j+1]: 
                hurricanes_by_mortality[j].append(i)
        if deaths > mortality_scale[4]:
            hurricanes_by_mortality[5].append(i)
    return hurricanes_by_mortality

mortality_rating(hurricanes)
            


# In[105]:


def most_costly(hurricanes):
    """Find the highest damage inducing hurricane and its total cost."""
    max_damage_cane = ''
    max_damage = 0
    for i in hurricanes:
        damages = hurricanes[i]['Damages']
        if damages != "Damages not recorded" and damages > max_damage:
            max_damage_cane = i
            max_damage = damages
    return max_damage_cane, max_damage;

max_damage_cane, max_damage = most_costly(hurricanes)

print("{cane} is the most costly hurricane with ${cost} in damages.".format(cane = max_damage_cane, cost = int(max_damage)))
            


# In[106]:


def damage_scale_function(hurricanes):
    """Categorize hurricanes by damage and return a dictionary."""
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in hurricanes:
        damage = hurricanes[i]['Damages']
        if damage != "Damages not recorded":
            for j in range(len(damage_scale)-1):
                if float(damage) > damage_scale[j] and float(damage) <= damage_scale[j+1]:
                    hurricanes_by_damage[j].append(i)
            if float(damage) > damage_scale[4]:
                hurricanes_by_damage[5].append(i)
    return hurricanes_by_damage

hurricanes_by_damage = damage_scale_function(hurricanes)

print (hurricanes_by_damage[5])

