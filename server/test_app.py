from fastapi.testclient import TestClient

from app import application

client = TestClient(application)

def test_predict():
    """This function execute the test in the predict endpoint

    """
    data = {
            "products": [
                            {
                                "title": "Lembrancinha"
                            },
                            {
                                "title": "Roupa de Bebê"
                            },
                            {
                                "title": "Mandala Espírito Santo"
                            }
                        ]
            }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json() == {
                                "categories": [
                                    "Lembrancinhas",
                                    "Bebê",
                                    "Decoração"
                                    ]
                                }