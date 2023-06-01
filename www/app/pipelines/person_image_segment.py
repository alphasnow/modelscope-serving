from typing import Any

from app.pipelines.singleton_instance import SingletonInstance
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class PersonImageSegment(SingletonInstance):
    def build(self):
        return pipeline(
            task=Tasks.portrait_matting,
            model='damo/cv_unet_image-matting',
            model_revision='v1.0.0',  # 20230130
        )

    def handle(self, image: Any):
        res = self.instance()(image)
        return res.get("output_img")
