from flask import Blueprint
from SPARQLWrapper import JSON, SPARQLWrapper

datasets_api = Blueprint("datasets_api", __name__)


@datasets_api.route("/", methods=["GET"])
def get_datasets():
    sparql = SPARQLWrapper("https://dati.isprambiente.it/sparql/")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(
        """
PREFIX ispra-top: <https://w3id.org/italia/env/onto/top/>
SELECT DISTINCT ?uri ?label
WHERE {
  ?uri a ispra-top:Dataset ;
    rdfs:label ?label .
}
"""
    )
    datasets = sparql.queryAndConvert()["results"]["bindings"]
    res = []
    for dataset in datasets:
        res.append({"uri": dataset["uri"]["value"], "label": dataset["label"]["value"]})
    return res
