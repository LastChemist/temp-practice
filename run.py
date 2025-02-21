from plugins.stoichiometry import UI


chemicals = ["A", "B", "=", "C", "D"]
field_names = ["Chemical Formula"] + chemicals
weights = ["weights", 14, 2, "***", 45, 12]
moles = ["Moles", 0.1, 2, "***", 0.8, 0.3]

obj = UI()
print(obj.create_table(field_names=field_names, rows=[weights, moles]))
# table(table_field_names=field_names, rows=[weights, moles])
