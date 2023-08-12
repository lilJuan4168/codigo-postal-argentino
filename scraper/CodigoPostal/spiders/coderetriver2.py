import scrapy
import pandas as pd


#run after coderetriver1 spider and ETL_coderetriver1.py script

class Coderetriver2Spider(scrapy.Spider):
    name = "coderetriver2"
    allowed_domains = ["codigo-postal.co"]
    start_urls = ["https://codigo-postal.co/argentina/"]


    def parse(self, response):
        bad_data = pd.read_csv('../../../data/bad_data.csv')
        bad_data = bad_data[['Provincia', 'Localidad']].drop_duplicates()
        bad_data = bad_data.to_dict(orient='records')
        url = "https://codigo-postal.co/argentina/"
        for data in bad_data:
            url_mod = url+f"{data['Localidad'].replace(' ','-')}/{data['Provincia'].replace(' ','-')}"
            yield response.follow(url_mod, callback=self.tablas)
    

#datos finales localidades con un solo cpa
    def tablas(self, response):
        localidades = response.css('table tbody tr')
        for localidad in localidades: #para cada fila en filas
            yield {
                "Provincia": localidad.css("td::text")[1].get(),
                "Localidad": localidad.css("td::text")[0].get(),
                "calle_avenida": "",
                "desde":"",
                "hasta":"",
                "aplica":"",
                "cp": localidad.css("td::text")[2].get(),
                "cpa": localidad.css("td::text")[3].get()
            }

    
#run on terminal: scrapy crawl coderetriver2 -O ../../../data/coderetriver2_data.csv
