"""
    Simple database with a dictionary
    that contains the declined names
    of Russian cities for correct
    spelling in the weather forecast
"""

# --- Lists and dictionary ---#
keys = []                     #
values = []                   #
cities_dict = {}              #
# ----------------------------#

# --- Extracting the names of the cities from the file -----------------------------#
with open('Russian_cities.txt', encoding='utf-8') as cdb:                           #
    read_file = cdb.read()                                                          #
    clean_text = read_file.replace('\n', ',')                                       #
    split_text = clean_text.split(',')                                              #
    keys.append(split_text[0])  # <-----------------------------------------\       #
    # I didn't find the way to add the first element of the list with cycle__\      #
# ----------------------------------------------------------------------------------#

# --- Filling the "keys" list with the names
# of the cities in nominative case -----------#
count = -1                                    #
for i in split_text:                          #
    count += 1                                #
    if count == 6:                            #
        keys.append(i)                        #
        count = 0                             #
# --------------------------------------------#

# --- Filling the "values" list with the
# declined names of the cities ----------#
count_2 = 0                              #
for i in split_text:                     #
    count_2 += 1                         #
    if count_2 == 6:                     #
        values.append(i)                 #
        count_2 = 0                      #
# ---------------------------------------#

# --- Creating the dictionary ----#
for key in keys:                  #
    for value in values:          #
        cities_dict[key] = value  #
        values.remove(value)      #
        break                     #
# --------------------------------#

