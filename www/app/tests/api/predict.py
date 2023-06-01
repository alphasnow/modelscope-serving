import cv2
from app.internal.utils import numpy_to_base64, base64_to_numpy, base64_to_file
from app.main import app
from app.tests.common import stub
from fastapi.testclient import TestClient


def test_word_segmentation():
    with TestClient(app) as client:
        data = {"text": "测试分词功能"}
        response = client.post("/api/predict/word-segmentation", json=data)

        result_data = response.json()

        assert response.status_code == 200


def test_image_cartoon():
    algo = "anime"
    image = stub("avatar.jpg")

    image_data = numpy_to_base64(cv2.imread(image), 'jpg')
    data = {"image": image_data, "algo_type": algo}
    with TestClient(app) as client:
        response = client.post("/predict/image-cartoon", json=data)

        result_data = base64_to_numpy(response.json()['image'])
        result = stub("tmp/image-cartoon_" + algo + ".png")
        cv2.imwrite(result, result_data)

        assert response.status_code == 200


def test_image_segment():
    image = stub("avatar.jpg")

    image_data = numpy_to_base64(cv2.imread(image), 'jpg')
    data = {"image": image_data}
    with TestClient(app) as client:
        response = client.post("/api/predict/image-segment/person", json=data)

        result = stub("tmp/image-segment.png")
        base64_to_file(response.json()['image'], result)

        assert response.status_code == 200
