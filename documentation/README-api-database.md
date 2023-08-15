<h1 align='center'>API</h1>
<h2>Local</h2>
<pre>
docker build -t apicpa .
docker run --name apicpac -p 8000:8000 apicpa
</pre>

<pre>
#endpoints

"/{provincia}/{localidad}"

"/{provincia}/{localidad}/{calle_avenida}/{desde}/{hasta}"

"/{cpa}/"
</pre>

<p align='center'><img src="img/request1.png" height=400 width=800></p>

<p align='center'><img src="img/request2.png" height=300 width=800></p>

<p align='center'><img src="img/request3.png" height=300 width=800></p>


<h2>Database</h2>

<p>La base de datos es Mongodb con 3 colecciones "localities". "numbers", "streets" y tienen la siguiente estructura.</p>
<h3 align="center">Localities</h3>
<p align='center'><img src="img/localities.png" height=350 width=900></p>
<h3 align="center">Numbers</h3>
<p align='center'><img src="img/numbers.png" height=350 width=900></p>
<h3 align="center">Streets</h3>
<p align='center'><img src="img/streets.png" height=350 width=900></p>
