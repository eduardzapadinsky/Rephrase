"""
Django views for rephrase api application.
These views use get request to create rearrangements in the sentence as a response.
"""

import nltk
from django.http import JsonResponse
from rest_framework.views import APIView

from .service import detect_noun_phrases, create_nouns_rearrangement


class ParaphraseAPIView(APIView):
    """
    A Django view that accepts a GET request with parameters "tree" and "limit",
    generates rearrangements of the input sentence, and returns the paraphrases in a
    JSON response.
    The input "tree" parameter should contain a string representation of a syntactic tree,
    formatted according to the conventions of the NLTK package.
    The "limit" parameter is an optional integer that limits the number of paraphrases returned.
    If an error occurs during processing, an error message is returned in the JSON response.
    """

    def get(self, request):
        """
        Processes a GET request and returns a JSON response with paraphrased sentences.
        Returns:
        JsonResponse: A JSON response containing a list of rearrangement sentences, or an error message.
        """
        default_limit = 20
        try:
            tree_query = request.GET.get("tree", "")
            tree_from_query = nltk.tree.Tree.fromstring(tree_query)
            limit_query = int(request.GET.get("limit", default_limit))
            noun_phrases = detect_noun_phrases(tree_from_query)
            nouns_rearrangements = create_nouns_rearrangement(tree_from_query, noun_phrases, limit_query)
            data = {"paraphrases": nouns_rearrangements}
        except ValueError as error:
            data = {"error message": str(error).split("\n")[0]}
        return JsonResponse(data, json_dumps_params={"indent": 4, "ensure_ascii": False})
