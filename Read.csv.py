import pandas
import arcpy
import os

csv_path = r"D:\Programming for GIS-3\P6_Working_with_Cursor_2\estab_years.csv"
years_dict = {}

csv_df = pandas.read_csv(csv_path)

for index, row in csv_df.iterrows():
    years_dict[row.NAME] = row.ESTAB


gdb_path = r"D:\Programming for GIS-3\P6_Working_with_Cursor_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["Name", "ESTAB"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        if row[0] in years_dict:
            (row[1]) = years_dict[row[0]]
        else:
            print("Major Attraction: {} not in csv".format(row[0]))
        u_cursor.updateRow(row)


print("Process Completed")
