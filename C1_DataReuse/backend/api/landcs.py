from flask import Blueprint, request
from SPARQLWrapper import JSON, SPARQLWrapper

landcs_api = Blueprint("landcs_api", __name__)


@landcs_api.route("/", methods=["GET"])
def get_datasets():
    sparql = SPARQLWrapper("https://dati.isprambiente.it/sparql/")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(
        """
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ispra-top: <https://w3id.org/italia/env/onto/top/>
PREFIX ispra-plc: <https://w3id.org/italia/env/onto/place/>
PREFIX ispra-emf: <https://w3id.org/italia/env/onto/inspire-mf/>
PREFIX clvapit: <https://w3id.org/italia/onto/CLV/>

SELECT DISTINCT ?comune ?percentuale ?poly
WHERE {
  FILTER(STRSTARTS(str(?poly), "POLYGON ("))
  FILTER(STRLANG(?comune, "it"))

  ?mun a ispra-plc:Municipality ;
    rdfs:label ?comune ;
    ispra-plc:hasRegion [
      a ispra-plc:Region ;
      ispra-top:name \""""
        + request.args.get("region")
        + """\"^^xsd:string ;
      clvapit:hasRankOrder "2"
    ] ;
    ispra-plc:hasGeometry/ispra-plc:geometry ?poly .

  ?icc a ispra-emf:IndicatorCollection ;
    ispra-top:isPartOf/ispra-top:isPartOf [
      a ispra-top:Collection ;
      ispra-top:isPartOf <https://w3id.org/italia/env/ld/soilc/dataset> ;
      ispra-top:isCollectionOf ?mun
    ] ;
    ispra-top:isParametrisedBy <https://w3id.org/italia/env/ld/soilc/parameter/csuolo4> .

  ?URI a ispra-emf:Indicator ;
    ispra-top:isMemberOf ?icc ;
    ispra-top:atTime/ispra-top:year \""""
        + request.args.get("year")
        + """\"^^xsd:gYear ;
    ispra-top:hasValue/ispra-top:value ?percentuale .
}
"""
    )
    observations = sparql.queryAndConvert()["results"]["bindings"]
    res = []
    for observation in observations:
        res.append(
            {
                "comune": observation["comune"]["value"],
                "percentuale": observation["percentuale"]["value"],
                "poly": observation["poly"]["value"],
            }
        )
    return res
