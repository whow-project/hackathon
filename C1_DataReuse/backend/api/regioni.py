from flask import Blueprint
from SPARQLWrapper import JSON, SPARQLWrapper

regioni_api = Blueprint("regioni_api", __name__)


@regioni_api.route("/", methods=["GET"])
def get_datasets():
    sparql = SPARQLWrapper("https://dati.isprambiente.it/sparql/")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(
        """
PREFIX ispra-top: <https://w3id.org/italia/env/onto/top/>
PREFIX ispra-plc: <https://w3id.org/italia/env/onto/place/>
SELECT ?nomeregione
WHERE {
  ?s a ispra-plc:Region ;
    ispra-top:name ?nomeregione .
}
ORDER BY ?nomeregione
"""
    )
    datasets = sparql.queryAndConvert()["results"]["bindings"]
    res = []
    for dataset in datasets:
        res.append({"nomeregione": dataset["nomeregione"]["value"]})
    return res
