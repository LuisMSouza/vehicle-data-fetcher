from playwright.sync_api import Playwright, sync_playwright, expect
import constants as constants
import time
from createFile import createDoc

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

vehicles = {'0100223-27.2016.5.01.0040': 'LTB2H18', '0100559-07.2022.5.01.0077': 'FIU7H07', '0100865-51.2017.5.01.0432': 'LLP-8994', '0010479-60.2015.5.01.0491': 'LLP-8994', '0100624-67.2023.5.01.0432': 'QRJ4A61', '0101011-29.2019.5.01.0301': 'LPH-7245', '0000484-84.2011.5.01.0322': 'KZO3339', '1000777-48.2021.5.02.0002': 'EWG-4679', '0003226-74.2013.5.02.0002': 'EWG-4679', '1001175-12.2023.5.02.0006': 'FZI1B46', '1000133-16.2023.5.02.0009': 'EFY8H99', '0000735-69.2015.5.02.0020': 'FKO1833', '1000571-19.2017.5.02.0020': 'FKO1833', '0254200-89.2004.5.02.0021': 'EQL4410', '0011300-80.1997.5.02.0034': 'DZI7010', '1000300-60.2020.5.02.0034': 'DZI7010', '1001296-89.2019.5.02.0035': 'ECH1173', '0001552-88.2015.5.02.0035': 'ECH1173', '1001306-90.2022.5.02.0080': 'FTK-6542', '1001414-61.2018.5.02.0080': 'FTK-6542', '1001985-16.2017.5.02.0614': 'PIN3A22', '1000541-87.2023.5.02.0241': 'DUU1867', '0269400-24.2005.5.02.0241': 'DUU1867', '0000409-67.2012.5.02.0262': 'BXT3593', '1011896-64.2019.8.26.0161': 'BXT3593', '1001604-69.2016.5.02.0411': 'JET8260', '0007200-52.1996.5.02.0411': 'JET8260', '1001521-51.2017.5.02.0465': 'CPX4109', '0001429-28.2012.5.03.0016': 'HDQ-7779', '0010729-39.2015.5.03.0006': 'PYP-3940', '0010379-31.2018.5.03.0108': 'PYP-3940', '0010080-64.2018.5.03.0137': 'PUS8015', '0010888-35.2023.5.03.0027': 'JLP4434', '0010003-89.2021.5.03.0027': 'JLP4434', '0010531-49.2023.5.03.0029': 'HNU8A15', '0011515-67.2022.5.03.0029': 'HNU8A15', '0010065-49.2023.5.03.0031': 'NYA3690', '0010538-55.2023.5.03.0089': 'QOJ2A09', '0001842-84.2010.5.03.0089': 'QOJ2A09', '0011182-65.2017.5.03.0167': 'GPZ5904', '0010808-37.2023.5.03.0103': 'QCX8828', '0010984-57.2023.5.03.0057': 'PXO-4253', '0010983-72.2023.5.03.0057': 'PXO-4253', '0010338-90.2018.5.03.0067': 'OPO-5555', '0011257-95.2017.5.03.0073': 'AAJ4022', '0010029-72.2023.5.03.0074': 'RNS8G12', '0011528-47.2015.5.03.0147': 'OPT9069', '0011138-09.2017.5.03.0147': 'OPT9069', '0020682-86.2023.5.04.0404': 'IHV-9193', '0020549-44.2023.5.04.0016': 'FKW0114', '0020652-61.2022.5.04.0024': 'IXA4032', '0021023-21.2019.5.04.0512': 'LZE5F80', '0020201-46.2022.5.04.0732': 'IES5542', '0020707-90.2020.5.04.0732': 'IHK7812', '0020286-29.2022.5.04.0733': 'IXK-4559', '0020510-64.2022.5.04.0733': 'IXK-4559', '0000248-33.2013.5.04.0661': 'IUE-1045', '0020460-76.2018.5.04.0701': 'IWS7373', '0000198-65.2021.5.05.0251': 'QTX6G02', '0153000-49.2001.5.05.0251': 'QTX6G02', '0000628-24.2022.5.06.0002': 'OHZ-6061', '0001608-49.2014.5.06.0002': 'OHZ-6061', '4002100-49.2000.5.06.0006': 'KGF6020', '0040300-62.2001.5.06.0006': 'KGF6020', '0000648-64.2017.5.06.0301': 'MNX4972', '0000758-43.2022.5.06.0251': 'OVE8603', '0000464-25.2021.5.06.0251': 'KJQ-0544'}

data = run(plates=vehicles)

createDoc(data=data)