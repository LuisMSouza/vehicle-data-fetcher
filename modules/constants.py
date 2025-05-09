WEBSITE_URL = "https://diario.jt.jus.br/cadernos/dejt.html"
PLATE_INFO_URL = "https://api.brabocar.com.br/api/Vehicle/{plate}"
PLATE_INFO_ALTERNATIVE_URL = "https://www.qualveiculo.net/"
APP_TITLE = "Judiciary PDF Extractor"
APP_DIMENSION = "500x350"
APP_ICON_PATH = "img/carro.ico"
APP_ICON_WARN_PATH = "img/aviso.ico"
DOWNLOAD_FILES = "BAIXAR ARQUIVOS"
EXTRACT_FILE_VEHICLE = "EXTRAIR DADOS VEÍCULOS"
EXTRACT_FILE_REGISTRY = "EXTRAIR DADOS CARTÓRIOS"
CREATE_FILE_VEHICLE = "CRIAR PDF VEÍCULOS"
CREATE_FILE_REGISTRY = "CRIAR PDF CARTÓRIOS"
DOWNLOAD_SUCCESS = "✅ ARQUIVOS BAIXADOS COM SUCESSO"
FILES_NOT_FOUND = "❌ ARQUIVOS NÃO ENCONTRADOS.\nCLIQUE EM 'BAIXAR ARQUIVOS'"
DOWNLOADING_FILES = "BAIXANDO ARQUIVOS, AGUARDE..."
EXTRACT_VEHICLE_DATA = "EXTRAINDO DADOS DE VEÍCULOS, AGUARDE..."
EXTRACT_NOTARIES_DATA = "EXTRAINDO DADOS DE CARTÓRIOS, AGUARDE..."
EXTRACT_VEHICLES_SUCCESS = "✅ DADOS DE VEÍCULOS EXTRAÍDOS COM SUCESSO"
EXTRACT_NOTARIES_SUCCESS = "✅ DADOS DE CARTÓRIOS EXTRAÍDOS COM SUCESSO"
PDF_REGISTRY_SUCCESS = "✅ PDF DE CARTÓRIOS GERADO COM SUCESSO."
PDF_VEHICLE_SUCCESS = "✅ PDF DE VEÍCULOS GERADO COM SUCESSO."
CREATING_REGISTRY_PDF = "CRIANDO PDF DE CARTÓRIOS..."
CREATING_VEHICLE_PDF = "CRIANDO PDF DE VEÍCULOS..."
NO_VEHICLES_DATA = (
    "❌ NENHUM REGISTRO DE VEÍCULO EXTRAÍDO\nCLIQUE EM 'EXTRAIR DADOS VEÍCULOS'"
)
NO_NOTARIES_DATA = (
    "❌ NENHUM REGISTRO DE CARTÓRIO EXTRAÍDO\nCLIQUE EM 'EXTRAIR DADOS CARTÓRIOS'"
)
CONSULT_LIMIT = "⚠️ PÁGINA BLOQUEADA POR LIMITE DE CONSULTAS, MUDE DE ENDEREÇO DE IP ALTERANDO A INTERNET EM QUE ESTÁ CONECTADO E CLIQUE EM CONTINUAR."
PROCESS_NUMBER = "NÚMERO DO PROCESSO: {}\n\n"
FIND_AT = "ENCONTRADO EM: {}"
LIMIT_TEXT = "Limite diário de"
PLATE = "PLACA: {}\n\n"
V_DATA = "DADOS DO VEÍCULO: \n\n{}\n\n"
PLATE_REGEX = r"\bplaca\s[A-Z]{3}-?\d{4}\b|\b[A-Z]{3}\d[A-Z]\d{2}\b"
PLATE_NUMBER_REGEX = r"[A-Z]{3}-?\d{4}\b|\b[A-Z]{3}\d[A-Z]\d{2}"
PROCESS_REGEX = r"[0-9]+-[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
NOTARIES_KEYWORDS = [
    "registro de imóveis de belo horizonte",
    "registro de imoveis de belo horizonte",
    "registro de móvel de belo horizonte",
    "belo horizonte cartório",
    "ofício do registro de imóveis da comarca de belo horizonte",
    "tabelionato de notas de belo horizonte",
]
PAGE_HEADERS = {
  'authority': 'api.brabocar.com.br',
  'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://brabocar.com.br',
  'referer': 'https://brabocar.com.br/',
  'sec-ch-ua': 'Not_A',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': 'Windows',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site'
}
MAX_WORKERS=10