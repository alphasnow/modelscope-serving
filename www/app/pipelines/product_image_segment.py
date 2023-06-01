from typing import Any

from app.pipelines.singleton_instance import SingletonInstance
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class ProductImageSegment(SingletonInstance):
    def build(self):
        return pipeline(
            task=Tasks.product_segmentation,
            model='damo/cv_F3Net_product-segmentation',
            model_revision='v1.0.0',  # 20230130
        )

    def handle(self, image: Any):
        res = self.instance()({"input_path": image})
        return res.get("masks")
