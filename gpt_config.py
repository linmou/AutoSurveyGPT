import os

gen_query_model = "gpt-4o-mini"
html_parse_model = "gpt-4o-mini"
abstract_parse_model = "gpt-4o-mini"
pdf_extraction_model = "gpt-4o-mini"

def get_driver_path():
    if os.name == 'nt':
        return 'driver/chromedriver.exe'
    else:
        return '/Users/admin/Downloads/chromedriver-mac-arm64/chromedriver'
