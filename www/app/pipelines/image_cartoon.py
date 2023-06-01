from typing import Any

from app.internal.utils import base64_to_numpy, numpy_to_base64
from modelscope.pipelines import pipeline, Pipeline
from modelscope.utils.constant import Tasks


# from modelscope.pipelines.cv.image_cartoon_pipeline import ImageCartoonPipeline


class ImageCartoon:
    STYLE_ANIME = "anime"
    STYLE_3D = "3d"
    STYLE_HANDDRAWN = "handdrawn"
    STYLE_SKETCH = "sketch"
    STYLE_ARTSTYLE = "artstyle"

    _styles = [STYLE_ANIME, STYLE_3D, STYLE_HANDDRAWN, STYLE_SKETCH, STYLE_ARTSTYLE]

    _models = {
        STYLE_ANIME: "damo/cv_unet_person-image-cartoon_compound-models",
        STYLE_3D: "damo/cv_unet_person-image-cartoon-3d_compound-models",
        STYLE_HANDDRAWN: "damo/cv_unet_person-image-cartoon-handdrawn_compound-models",
        STYLE_SKETCH: "damo/cv_unet_person-image-cartoon-sketch_compound-models",
        STYLE_ARTSTYLE: "damo/cv_unet_person-image-cartoon-artstyle_compound-models"
    }

    _pipelines = {
        STYLE_ANIME: None,
        STYLE_3D: None,
        STYLE_HANDDRAWN: None,
        STYLE_SKETCH: None,
        STYLE_ARTSTYLE: None,
    }

    def __init__(self, singleton: bool = True):
        self.singleton = singleton

    def _new_pipeline(self, style: str = STYLE_ANIME) -> Pipeline:
        model = self._models.get(style)
        return pipeline(
            task=Tasks.image_portrait_stylization,
            model=model,
            model_revision='v1.0.0',  # 20230130
        )

    def _get_pipeline(self, style: str = STYLE_ANIME):
        pipe = self._pipelines.get(style)
        if pipe is None:
            # pipe = self.new_pipeline(style)
            # self._pipelines[style] = pipe
            raise ValueError("CartoonPipeline is not initialize, style is %s" % style)
        return pipe

    def initialize(self):
        if not self.singleton:
            return

        for v in self._styles:
            self._pipelines[v] = self._new_pipeline(v)

    def validate(self, style: str):
        if style not in self._styles:
            # raise ValueError("Cartoon style is invalid, error value was %s." % style)
            return False
        return True

    def handle(self, image: Any, style: str = STYLE_ANIME):
        if self.singleton:
            pipe = self._get_pipeline(style)
        else:
            pipe = self._new_pipeline(style)

        result = pipe(image)
        return result.get("output_img")

    def handle_base64(self, image: str, style: str = STYLE_ANIME):
        image_numpy = base64_to_numpy(image)
        result = self.handle(image_numpy, style)
        output_img = numpy_to_base64(result, "png")
        return output_img
