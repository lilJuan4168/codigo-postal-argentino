import scrapy


class CoderetriverSpider(scrapy.Spider):

    name = "coderetriver"
    allowed_domains = ["codigo-postal.co"]
    start_urls = ["https://codigo-postal.co/argentina/"]
    def __init__(self):
      self.prov = ""
      self.local = ""
      self.calle_av = ""

#iteracion provincias
    def parse(self, response):
        links_provincias = response.css('.column-list a::attr(href)') 
        for provincia in links_provincias: 
            yield response.follow(str(provincia.get()), callback=self.localidad)

#iteracion localidades
    def localidad(self,response):
        links_localidades = response.css('.cities a::attr(href)')
        for localidad in links_localidades:
            yield response.follow(str(localidad.get()), callback=self.tablas)

#datos finales localidades con un solo cpa ---------------------------->
    def tablas(self, response):
        calles = response.css('table tbody tr')
        for calle in calles:
            if calle.css('td a::text').get() != 'Buscar CPA':
               datos = calle.css('td::text')
               self.prov = datos[0].get()
               self.local = datos[1].get() 
               yield{
                "Provincia":datos[0].get(),
                "Localidad":datos[1].get(),
                "calle_avenida":"",
                "desde":"",
                "hasta":"",
                "aplica":"",
                "cp":datos[2].get(),
                "cpa": calle.css('td a::text').get()
               }
            else:
               yield response.follow(str(calle.css('td')[3].css("a::attr(href)").get()), callback=self.buscar_cpa) 

#calles dentro de buscar cpa
    def buscar_cpa(self, response):
        calles = response.css(".three_columns li")
        for calle in calles:
            yield response.follow(str(calle.css("a::attr(href)").get()), callback=self.data)

    
    def data(self, response):
        filas = response.css("table tbody tr")
        for fila in filas:
            yield {
                "Provincia": response.css(".col-md-12 span")[2].css("a span::text").get(),
                "Localidad": response.css(".col-md-12 span")[4].css("span span::text").get(),
                "calle_avenida": fila.css("td::text")[0].get(),
                "desde": fila.css("td::text")[1].get(),
                "hasta": fila.css("td::text")[2].get(),
                "aplica": fila.css("td::text")[3].get(),
                "cp": fila.css("td::text")[4].get(),
                "cpa": fila.css("td a::text").get()
            }
        
#run on terminal: scrapy crawl coderetriver1 -O ../../../data/coderetriver1_data.csv



