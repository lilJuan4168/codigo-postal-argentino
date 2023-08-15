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

<h2>Database</h2>

<p>La base de datos es Mongodb con la siguiente estructura</p>

<pre>
#24 collections uno para cada provincia
#adentro de cada collection

{
  "provincia": str,
  "localidad": str,
  "data": [
    {
      "calle_avenida": str,
      "desde": str,
      "hasta": str,
      "aplica": str,
      "cp": int,
      "cpa": str
    }
  ]
}
#la key data es una lista de diccionarios

</pre>