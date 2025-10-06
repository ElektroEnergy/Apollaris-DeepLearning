import csv
import json

import csv
import json

FIELD_MAP_INVERTER = {
    "type": "name",
    "pdc": "pdc",
    "nppt": "nmmpts",
    "vmpptmax": "vmpmax",
    "vmpptmin": "vmpmin",
    "imppt": "imp",
    "icc1": "isc",
    "ef": "ef",
    "icost": "icost"
}

def csv_to_json_inverters(csv_file, json_file):
    data = []
    
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
        
        for idx, row in enumerate(reader, start=1):
            row = {k.strip().lower(): v.strip() for k, v in row.items()}
            
            inverter = {
                "id": idx,
                "brand_id": 1
            }
            
            for csv_field, json_field in FIELD_MAP_INVERTER.items():
                value = row.get(csv_field, "")
                
                # tenta converter número
                if value and value.replace('.', '', 1).replace('-', '', 1).isdigit():
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                
                inverter[json_field] = value
            
            data.append(inverter)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"JSON file generated: {json_file}")


csv_to_json_inverters("data/converter/inverters.csv", "data/converter/inverters.json")