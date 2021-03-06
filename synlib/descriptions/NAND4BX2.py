Desc = cellDescClass("NAND4BX2")
Desc.properties["cell_leakage_power"] = "1447.778610"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BX2"]=Desc
