from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://buscaplacas.com.br/?ref=ericbing")
    page.get_by_placeholder("ABC-1234").click()
    page.get_by_placeholder("ABC-1234").fill("KPP-1707")
    page.get_by_role("link", name="Consultar Placa").click()
    time.sleep(3)
    td_elements = page.query_selector_all('td')

    for td_element in td_elements:
        td_content = td_element.text_content()
        print(td_content)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
