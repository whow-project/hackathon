from flask import Blueprint, request
from SPARQLWrapper import JSON, SPARQLWrapper

bathw_api = Blueprint("bathw_api", __name__)


@bathw_api.route("/", methods=["GET"])
def get_datasets():
    sparql = SPARQLWrapper("https://dati.isprambiente.it/sparql/")
    sparql.setReturnFormat(JSON)
    sparql.setQuery(
        """
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX ispra-top: <https://w3id.org/italia/env/onto/top/>
PREFIX ispra-plc: <https://w3id.org/italia/env/onto/place/>

SELECT DISTINCT ?municipality ?province ?region ?quality ?long ?lat
WHERE {
  FILTER (STRLANG(?municipality, "it"))
  FILTER (STRLANG(?province, "it"))
  FILTER (STRLANG(?region, "it"))
  FILTER (STRLANG(?quality, "en"))

  ?ind ispra-top:isMemberOf ?ic ;
    ispra-top:isClassifiedBy/skos:prefLabel ?quality ;
    ispra-top:atTime/ispra-top:year \""""
        + request.args.get("year")
        + """\"^^xsd:gYear .

  ?mun rdfs:label ?municipality ;
    ispra-plc:hasDirectHigherRank/rdfs:label ?province ;
    ispra-plc:hasRegion/rdfs:label ?region .

  GRAPH <https://w3id.org/italia/env/ld/bathw/> {
    ?ic ispra-top:isParametrisedBy <https://w3id.org/italia/env/ld/bathw/parameter/quality> ;
      ispra-top:isPartOf/ispra-top:isPartOf [
        ispra-top:isPartOf <https://w3id.org/italia/env/ld/bathw/dataset> ;
        ispra-top:isCollectionOf ?mun
      ] ;
      ispra-top:isPartOf/ispra-top:isCollectionOf [
        geo:lat ?lat ;
        geo:long ?long
      ] .
  }
}
ORDER BY ?municipality ?province ?region ?quality
"""
    )
    observations = sparql.queryAndConvert()["results"]["bindings"]
    res = []
    for observation in observations:
        res.append(
            {
                "quality": observation["quality"]["value"],
                "region": observation["region"]["value"],
                "province": observation["province"]["value"],
                "municipality": observation["municipality"]["value"],
                "long": observation["long"]["value"],
                "lat": observation["lat"]["value"],
            }
        )
    return res
