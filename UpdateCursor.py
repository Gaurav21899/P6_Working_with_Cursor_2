# Update the value to 1998 of ESTAB if the existing value is 0 using update cursor

import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P5_Working_with-Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path =os.path.join(gdb_path,fc_name)

fields_list = ["NAME", "ESTAB"]

years_dict = {}

# Hotel complex-de anza cove
with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        if row[1] == 0:
            row[1] = 1998

        years_dict[row[0]] = row[1]
        
        u_cursor.updateRow(row)

print(years_dict)
print("Process Completed")