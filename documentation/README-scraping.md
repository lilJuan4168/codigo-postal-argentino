<h1 align='center'>SCRAPING</h1>

<h2>Tools</h2>
<p>Scrapy was used for the whole process. Pandas was used to do the cleaning and data modeling.</p>

<h2>Run the scraper</h2>
<p>To run the scraper, you have to follow the following steps in order. If you are a linux user you can run the scraping.sh script in bash_scripts folder. Make sure you have the requirements.txt installed.</p>

<pre>
#1 Go to the spider's folder
cd scraper/CodigoPostal/spiders

#2 Run the first spider
scrapy crawl coderetriver1 -O ../../../data/coderetriver1_data.csv

#3 Run the first ETL file, go to the folder ETL
cd ETL
python3 ETL_coderetriver1.py

#4 Run the second spider
scrapy crawl coderetriver2 -O ../../../data/coderetriver2_data.csv

#5 Run the second ETL file, go to the folder ETL
cd ETL
python3 ETL_coderetriver2.py

#6 Run the ETL_concatenation.py file
python3 ETL_concatenation.py

#This is the end

</pre>
