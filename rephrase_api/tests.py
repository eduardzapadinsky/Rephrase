import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase


class ParaphraseAPIViewTest(APITestCase):
    """
    Tests for ParaphraseAPIView class and dependent functions.
    """

    def setUp(self) -> None:
        """
        Initializes the test case.
        """

        self.client = APIClient()
        self.url_name = "rephrase-api:paraphrase"

    def test_successful_request_default_limit(self):
        """
        Tests a successful GET request with default limit.
        Comparing data from expected-result-example.json with returned from ParaphraseAPIView class data
        """

        with open("expected-result-example.json", encoding="utf-8") as f:
            expected_data = json.load(f)
            expected_data_trees = expected_data["paraphrases"]
        sorted_expected_data = sorted(expected_data_trees, key=lambda x: x["tree"])
        tree = "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )"

        url = reverse(self.url_name)
        response = self.client.get(url, {"tree": tree})
        response_data = response.json()["paraphrases"]
        sorted_response_data = sorted(response_data, key=lambda x: x["tree"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(sorted_response_data, sorted_expected_data)
