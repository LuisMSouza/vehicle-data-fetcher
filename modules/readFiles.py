import PyPDF2
import re
import os
import constants

def readFiles() -> dict:
    matches = {}

    files = os.listdir("tmp")
    plate_regex = constants.PLATE_REGEX
    process_regex = constants.PROCESS_REGEX

    for file_name in files:
        file_path = os.path.join("tmp", file_name)
        reader = PyPDF2.PdfReader(file_path)

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            plate_search = re.search(plate_regex, text)
            if plate_search:
                before_plate_text = text[:plate_search.start()]
                process_search = re.search(process_regex, before_plate_text[::-1])
                if process_search:
                    process_number = process_search.group()[::-1]
                    plate_parsed = plate_search.group().replace("\n", "")
                    plate_number = re.search(constants.PLATE_NUMBER_REGEX, plate_parsed)
                    matches[f"{process_number}"] = f"{plate_number.group()}"
                    print(matches)
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
                            plate_number = re.search(constants.PLATE_NUMBER_REGEX, plate_parsed)
                            matches[f"{process_number}"] = f"{plate_number.group()}"
                            print(matches)
                        else:
                            print("Número do processo não encontrado na página anterior.")
                    else:
                        print("Sem páginas anteriores para procurar o número de processo.")

readFiles()
