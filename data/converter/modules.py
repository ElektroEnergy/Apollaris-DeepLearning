import csv
import json

FIELD_MAP = {
    "type": "name",
    "ocv": "voc",
    "scc": "isc",
    "vmax": "vmp",
    "imax": "imp",
    "pmp": "pmp",
    "Vmax": "vmax_sys",
    "ocvt": "tcoef_voc",
    "otvmp": "tcoef_vmp",
    "tcisc": "tcoef_isc",
    "weig": "weight",
    "deph": "depth",
    "widt": "width",
    "leng": "length",
    "area": "area",
    "icost": "icost",
    "ef": "ef",
    "ncel": "ncel",
    "tol": "tol",
    "dur": "dur",
    "tcell": "material",
    "TEMP": "tmax",
    "temp": "tmin",
    "NOCT": "tnm",
    "tier": "tier",
    "Inop": "max_fuse"
}

def csv_to_json(csv_file, json_file):
    data = []
    
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for idx, row in enumerate(reader, start=1):
            module = {
                "id": idx,
                "brand_id": 1 
            }
            
            for csv_field, json_field in FIELD_MAP.items():
                value = str(row.get(csv_field, "") or "").strip()
                
                if value.replace('.', '', 1).replace('-', '', 1).isdigit():
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                
                module[json_field] = value
            
            data.append(module)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"JSON file generated: {json_file}")

csv_to_json("data/converter/modulos.csv", "data/converter/modules.json")