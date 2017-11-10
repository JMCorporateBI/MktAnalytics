""" Collection of functions for filtering from a data sample 
    without having to install any libraries that are not automatically included in Python.
"""


# Filter rows were columns match a string data type
def filter_col_by_string(the_data, field, filter_condition):
    """ Filter rows were columns match a string t data type """
    filtered_rows = []   
    #find index of field in first row
    col = int(the_data[0].index(field))
    filtered_rows.append(the_data[0])
    for row in the_data[1:]:
        if row[col] == filter_condition:
            filtered_rows.append([str(x).encode('utf8') for x in row])          
    return filtered_rows

# Filter rows were columns match a float data type
def filter_col_by_float(the_data, field, direction, filter_condition):
    """ Filter rows were columns match a float data type """
    filtered_rows = []    
    #find index of field in first row
    col = int(the_data[0].index(field))
    cond = float(filter_condition)    
    for row in the_data[1:]:
        element = float(row[col])       
        if direction == "<":
            if element < cond: filtered_rows.append(row)               
        elif direction == "<=":
            if element <= cond: filtered_rows.append(row)
        elif direction == ">":
            if element > cond: filtered_rows.append(row)
        elif  direction == ">=":
            if element >= cond: filtered_rows.append(row)              
        elif  direction == "==":
            if element == cond: filtered_rows.append(row)
        else:
            raise ValueError("I recognize only '==', '<', '<=', '>', and '>=',.")
        
    return filtered_rows


