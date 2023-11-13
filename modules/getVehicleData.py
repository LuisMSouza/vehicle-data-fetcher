from playwright.sync_api import sync_playwright
import modules.constants as constants


def transform(app, playwright, plates):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    for proc, plate in plates.items():
        if any(veh_data["plate"] == plate for veh_data in app.vehicles_data.values()):
            continue

        plate = plate.replace("-", "")
        vehicle_info = ""
        page = context.new_page()
        page.goto(constants.PLATE_INFO_URL)
        page.wait_for_load_state()
        page.get_by_placeholder("ABC-1234").click()
        page.get_by_placeholder("ABC-1234").fill(plate)
        page.get_by_role("button", name="BUSCAR DADOS DO VEÍCULO GRÁTIS").click()

        try:
            # page.wait_for_selector(f"text={constants.LIMIT_TEXT}", timeout=10000)
            # if constants.LIMIT_TEXT in page.content():
            #     app.show_secondary_window(
            #         text_message=constants.CONSULT_LIMIT, button="continue"
            #     )
            #     break

            page.wait_for_selector(
                "text=Essas informações são de caráter meramente informativo",
                timeout=30000,
            )
        except Exception as err:
            print(err)

        mark = "Marca: " + page.query_selector_all(".h5.marca")[0].inner_text()
        model = "Modelo: " + page.query_selector_all(".h5.modelo")[0].inner_text()
        uf_plate = "UF: " + page.query_selector_all(".h5.uf_placa")[0].inner_text()
        year_made = "Ano fabricação: "+ page.query_selector_all(".h5.m-0.ano_fabricacao")[0].inner_text()
        year_model = "Ano modelo: "+ page.query_selector_all(".h5.m-0.ano_modelo")[0].inner_text()

        vehicle_info += mark + "\n" + model + "\n" + uf_plate + "\n" + year_made + "\n" + year_model + "\n"

        app.vehicles_data[proc] = {"plate": plate, "data": vehicle_info}

        page.close()

    context.close()
    browser.close()


def run(app, plates):
    with sync_playwright() as playwright:
        transform(app, playwright, plates)

    return
