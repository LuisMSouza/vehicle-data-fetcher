from playwright.sync_api import (
    sync_playwright,
    Browser,
    BrowserContext,
)
import modules.constants as constants
import time
from modules.createFile import createDoc

vehicles_data = {}


def transform(playwright, plates):
    global vehicles_data

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    for proc, plate in plates.items():
        vehicle_info = ""
        page = context.new_page()
        page.goto(constants.PLATE_INFO_URL)
        page.wait_for_load_state()
        page.get_by_placeholder("ABC-1234").click()
        page.get_by_placeholder("ABC-1234").fill(plate)
        page.get_by_role("link", name="Consultar Placa").click()

        try:
            time.sleep(2)
            if constants.LIMIT_TEXT in page.content():
                #alternative_page(plates, context)
                break

            page.wait_for_load_state("load")

            page.wait_for_url("**/resultado.php**")
        except Exception as err:
            print(err)
            continue

        td_elements = page.query_selector_all("td")

        for td_element in td_elements:
            td_content = td_element.text_content()
            vehicle_info += td_content + "\n"

        page.close()

        vehicles_data[proc] = {"plate": plate, "data": vehicle_info}

    context.close()
    browser.close()


def alternative_page(plates, context):
    global vehicles_data

    for proc, plate in plates.items():
        if proc in vehicles_data:
            continue

        page = context.new_page()
        page.goto(constants.PLATE_INFO_ALTERNATIVE_URL)
        page.get_by_placeholder("Placa: AAA-0000").click()
        page.get_by_placeholder("Placa: AAA-0000").fill(plate)
        page.get_by_role("button", name="L").click()

        page.wait_for_selector('//*[@id="resultado"]', state="attached")

        model = page.query_selector("span.dados")
        year_model = page.query_selector("span.dados.texto")
        locate = page.query_selector("span.dados.localidade")

        text_model = "Modelo: " + model.inner_text()
        text_year_model = "Cor\Ano: " + year_model.inner_text()
        text_locate = "Localidade: " + locate.inner_text()

        vehicle_info = text_model + "\n" + text_year_model + "\n" + text_locate + "\n"

        vehicles_data[proc] = {"plate": plate, "data": vehicle_info}

        page.close()


def run(plates):
    global vehicles_data

    with sync_playwright() as playwright:
        transform(playwright, plates)

    return vehicles_data
