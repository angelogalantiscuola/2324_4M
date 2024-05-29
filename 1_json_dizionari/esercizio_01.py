"""
1. Create a dictionary that contains the following details about a car:
   - Brand
   - Model
   - Year of production
   - Power in kW

2. Save these details into a JSON file.
"""

import json

def save_car_details(brand, model, year_of_production, power_kW, filename):
    # Create a dictionary
    car = {
        "brand": brand,
        "model": model,
        "year_of_production": year_of_production,
        "power_kW": power_kW
    }

    # Save the dictionary into a JSON file
    with open(filename, 'w') as json_file:
        json.dump(car, json_file)
    
    return filename