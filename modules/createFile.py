import modules.constants as constants
import aspose.pdf as ap
import os
import re


def createDoc(data: dict):
    document = ap.Document()
    page = document.pages.add()

    for proces, dat in data.items():
        data_text = dat["data"]
        text_fragment = ap.text.TextFragment(
            constants.PROCESS_NUMBER.format(proces)
            + constants.PLATE.format(dat["plate"])
            + constants.V_DATA.format(data_text)
        )

        text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")

        page.paragraphs.add(text_fragment)

    if not os.path.exists("transcript"):
        os.mkdir("transcript")

    document.save("transcript/vehicles.pdf")


def createDocNotaries(data: dict):
    document = ap.Document()
    page = document.pages.add()

    for process, dat in data.items():
        text_fragment = ap.text.TextFragment(
            constants.PROCESS_NUMBER.format(process) + constants.FIND_AT.format(dat)
        )

        page.paragraphs.add(text_fragment)

    if not os.path.exists("transcript"):
        os.mkdir("transcript")

    document.save("transcript/notaries.pdf")
