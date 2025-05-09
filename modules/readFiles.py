import PyPDF2
import re
import os
import concurrent.futures

import modules.constants as constants

from modules.getVehicleData import transform

def process_pdf_file(file_name, plate_regex, process_regex):
    file_path = os.path.join("tmp", file_name)
    reader = PyPDF2.PdfReader(file_path)
    plates = {}

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        plate_search = re.search(plate_regex, text)
        if plate_search:
            before_plate_text = text[: plate_search.start()]
            process_search = re.search(process_regex, before_plate_text[::-1])
            if process_search:
                process_number = process_search.group()[::-1]
                plate_parsed = plate_search.group().replace("\n", "")
                plate_number = re.search(constants.PLATE_NUMBER_REGEX, plate_parsed)
                plates[f"{process_number}"] = f"{plate_number.group()}"
                print(plates)
            else:
                previous_page_text = None
                if i > 0:
                    previous_page = reader.pages[i - 1]
                    previous_page_text = previous_page.extract_text()

                if previous_page_text:
                    process_numbers = re.findall(process_regex, previous_page_text)
                    if process_numbers:
                        process_number = process_numbers[-1]
                        plate_parsed = plate_search.group().replace("\n", "")
                        plate_number = re.search(
                            constants.PLATE_NUMBER_REGEX, plate_parsed
                        )
                        plates[f"{process_number}"] = f"{plate_number.group()}"
                        print(plates)
                    else:
                        print(
                            "Número do processo não encontrado na página anterior."
                        )
                else:
                    print(
                        "Sem páginas anteriores para procurar o número de processo."
                    )
    
    return plates

def readFiles(app):
    app.plates = {}

    files = os.listdir("tmp")
    plate_regex = constants.PLATE_REGEX
    process_regex = constants.PROCESS_REGEX

    with concurrent.futures.ThreadPoolExecutor(max_workers=constants.MAX_WORKERS) as executor:
        results = executor.map(lambda file: process_pdf_file(file, plate_regex, process_regex), files)

    for result in results:
        app.plates.update(result)

    transform(app, app.plates)
    return
