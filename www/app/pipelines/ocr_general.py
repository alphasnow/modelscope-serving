from typing import Any

from app.pipelines.singleton_instance import SingletonInstance
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

from .utils import order_point, crop_image


class OcrGeneral(SingletonInstance):
    def build(self):
        # https://modelscope.cn/headlines/article/42
        ocr_detection = pipeline(
            Tasks.ocr_detection,
            model='damo/cv_resnet18_ocr-detection-line-level_damo',
            model_revision='v1.0.0',  # 20230130
        )
        ocr_recognition = pipeline(
            Tasks.ocr_recognition,
            model='damo/cv_convnextTiny_ocr-recognition-general_damo',
            model_revision='v1.0.0',  # 20230130
        )
        return ocr_detection, ocr_recognition

    def handle(self, image: Any):
        ocr_detection, ocr_recognition = self.instance()
        det_result = ocr_detection(image)['polygons']
        data_result = []
        for i in range(det_result.shape[0]):
            pts = order_point(det_result[i])
            image_crop = crop_image(image, pts)
            result = ocr_recognition(image_crop)
            text = result['text']
            position = [int(e) for e in list(pts.reshape(-1))]
            data_result.append([text, position])
        data_result.sort(key=lambda v: v[1][1])
        return [v[0] for v in data_result], [v[1] for v in data_result]
