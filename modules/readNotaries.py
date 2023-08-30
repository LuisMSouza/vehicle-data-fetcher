import PyPDF2
import re
import os
import modules.constants as constants


def findNotaries():
    matches = {}

    files = os.listdir("tmp")
    keywords = constants.NOTARIES_KEYWORDS
    process_regex = constants.PROCESS_REGEX

    for file_name in files:
        file_path = os.path.join("tmp", file_name)
        reader = PyPDF2.PdfReader(file_path)

        for i, page in enumerate(reader.pages):
            text = page.extract_text().replace('\n', ' ')
            plate_search = re.search(r'|'.join(map(re.escape, keywords)), text.lower())
            if plate_search:
                before_plate_text = text[: plate_search.start()]
                process_search = re.search(process_regex, before_plate_text[::-1])
                if process_search:
                    process_number = process_search.group()[::-1]
                    matches[f"{process_number}"] = f"{'Arquivo: ' + file_name + ' Página: '+ str(i)}"
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
                            matches[f"{process_number}"] = f"{'Arquivo: ' + file_name + ' Página: '+ str(i)}"
                            print(matches)
                        else:
                            print(
                                "Número do processo não encontrado na página anterior."
                            )
                    else:
                        print(
                            "Sem páginas anteriores para procurar o número de processo."
                        )

    return matches

