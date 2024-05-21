import os
import json
from esercizio_001 import save_car_details

def test_save_car_details():
    filename = save_car_details("Ford", "Mustang", 1964, 147, 'test_car.json')
    
    # Check if the file was created
    assert os.path.exists(filename)

    # Check the content of the file
    with open(filename, 'r') as f:
        data = json.load(f)
        assert data['brand'] == 'Ford'
        assert data['model'] == 'Mustang'
        assert data['year_of_production'] == 1964
        assert data['power_kW'] == 147

    # Clean up after test
    os.remove(filename)