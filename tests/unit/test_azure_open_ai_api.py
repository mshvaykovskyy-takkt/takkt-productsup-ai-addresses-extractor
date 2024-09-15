import unittest
from connector.container_utils import AzureOpenAIApi


class TestAzureOpenAIApi(unittest.TestCase):
    def test_init_with_valid_values(self):
        azure_open_ai_api = AzureOpenAIApi(
            model="test_model",
            endpoint="https://test.endpoint.com",
            api_key="test_api_key",
            api_version="test_api_version",
        )
        self.assertEqual(azure_open_ai_api.model, "test_model")
        self.assertEqual(azure_open_ai_api.endpoint, "https://test.endpoint.com")
        self.assertEqual(azure_open_ai_api.api_key, "test_api_key")
        self.assertEqual(azure_open_ai_api.api_version, "test_api_version")


if __name__ == "__main__":
    unittest.main()
