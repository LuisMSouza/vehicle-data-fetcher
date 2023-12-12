import json
import requests
import time

import modules.constants as constants


def transform(app, plates):
    for proc, plate in plates.items():
        if any(veh_data["plate"] == plate for veh_data in app.vehicles_data.values()):
            continue

        time.sleep(2)

        plate = plate.replace("-", "")

        vehicle_info = ""
        url = constants.PLATE_INFO_URL.format(plate=plate)
        response = requests.request("GET", url, headers=constants.PAGE_HEADERS, data={})
        data = json.loads(response.text)

        mark = "Marca: " + data["data"]["marca"]
        model = "Modelo: " + data["data"]["modelo"]
        uf_plate = "UF: " + data["data"]["uf"]
        year_made = "Ano fabricação: "+ data["data"]["anoFabricacao"]
        year_model = "Ano modelo: "+ data["data"]["anoModelo"]

        vehicle_info += mark + "\n" + model + "\n" + uf_plate + "\n" + year_made + "\n" + year_model
        app.vehicles_data[proc] = {"plate": plate, "data": vehicle_info}

