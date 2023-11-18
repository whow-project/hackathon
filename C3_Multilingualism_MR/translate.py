"""
Python module containing the class TranslationManager.\n
The purpose of this class is to manage the translation of RDF triples
written in one language to multiple languages.

@author Marco Ratta
@Version 18/11/2023
"""

import rdflib
from typing import TypeAlias, Union
from rdflib import Literal, URIRef, BNode
import deepl

RDFTriple: TypeAlias = tuple[Union[URIRef, BNode, Literal]]


class TranslationManager:
    """
    Class TranslationManager handles the translation of RDF terms from one
    language to another.
    """
    def __init__(
            self,
            translator: deepl.Translator,
            ) -> None:
        """
        Initialiser for the TranslationManager class.\n
        Args:\n
        translator - a deepl.Translator object.
        """
        self.translator = translator

    def translate_literal(
            self,
            triple: RDFTriple,
            translator_langtag: str,
            rdf_langtag: str,
            ) -> RDFTriple:
        """
        Method to translate the literal value of the passed triple to the
        language specified by the language tag.\n
        Args:\n
        triple - the RDF triple containing the literal to be translated.\n
        translator - a deepl Translator object.\n
        lang_tag - the language tag of the destination language.\n
        Returns:\n
        A new RDF triple with the translated RDF literal.
        """
        translation = self.translator.translate_text(
            triple[2].toPython(), target_lang=translator_langtag
        )
        return tuple(
            [
                triple[0],
                triple[1],
                Literal(translation, lang=rdf_langtag)
            ]
        )

    def translate_property_literals(
            self,
            graph: rdflib.Graph,
            property: rdflib.URIRef,
            translator_langtag: str,
            rdf_langtag: str,
            join: bool = False
            ) -> rdflib.Graph:
        """
        Method to translate all the literals of the passed property argument
        present in the passed graph.\n
        Args:\n
        graph - the rdflib graph the triples of which requires translation.\n
        property - the property the literals of which have to be translated.\n
        translator_langtag - the destination language deepl.Translator tag.\n
        rdf_langtag - the destination language RDF tag.\n
        join - default False will make the method return only the translated
            triples. Set to True will make the method return the join of the
            passed graph and the new triples.
        Returns:
        A rdflib graph.
        """
        new_graph = rdflib.Graph()
        for triple in graph.triples((None, property, None)):
            new_graph.add(
                self.translate_literal(triple, translator_langtag, rdf_langtag)
            )
        if join is True:
            return graph + new_graph
        return new_graph
