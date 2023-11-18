import rdflib
import pysparql_anything as sa
import deepl
from translate import TranslationManager

# Create a Deepl translator
auth_key = '7ff63113-581e-10ab-9d57-8c3964402eb4:fx'
translator = deepl.Translator(auth_key)

# Create a sa engine object:
engine = sa.SparqlAnything()

# Generate rdflib representation:
g1 = engine.construct(q='./get_name.sparql')
g2 = engine.construct(q='./get_labels.sparql')
g = g1 + g2  # a rdflib graph.

# Construct a TranslationManager object:
tm = TranslationManager(translator)

# RDF namespace configuration:
ispra_top = rdflib.Namespace('https://w3id.org/italia/env/onto/top/')

# translation script:
new_g = tm.translate_property_literals(g, ispra_top.name, 'EN-GB', 'en')
for t in new_g:
    print(t)
