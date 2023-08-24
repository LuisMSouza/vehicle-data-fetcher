from playwright.sync_api import Playwright, sync_playwright, expect
import modules.constants as constants
import time
from modules.createFile import createDoc

def transform(playwright: Playwright, plates: dict) -> dict:
    vehicles_data = {}
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
            time.sleep(1)
            if constants.LIMIT_TEXT in page.content():
                break

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

    # ---------------------
    context.close()
    browser.close()
    return vehicles_data


def run(plates: dict) -> dict:
    with sync_playwright() as playwright:
        data = transform(playwright, plates)
    
    return data
