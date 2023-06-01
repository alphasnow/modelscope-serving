from typing import Any

from app.pipelines.singleton_instance import SingletonInstance
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class Body2DKeypoint(SingletonInstance):
    def build(self):
        # https://www.modelscope.cn/models/damo/cv_hrnetv2w32_body-2d-keypoints_image/summary
        return pipeline(
            task=Tasks.body_2d_keypoints,
            model='damo/cv_hrnetv2w32_body-2d-keypoints_image',
            model_revision='v1.0.0',  # 20230130
        )

    def handle(self, image: Any):
        output = self.instance()(image)
        return output


'''
{
    "boxes": [
        [128.6999969482422, 0, 531.2999877929688, 952]
    ],
    "keypoints": [
        [
            [366.6999969482422, 156.1875],
            [351.8249969482422, 275.1875],
            [232.8249969482422, 290.0625],
            [173.3249969482422, 438.8125],
            [217.9499969482422, 557.8125],
            [455.9499969482422, 275.1875],
            [470.8249969482422, 468.5625],
            [470.8249969482422, 632.1875],
            [292.3249969482422, 647.0625],
            [307.1999969482422, 885.0625],
            [322.0749969482422, 885.0625],
            [426.1999969482422, 661.9375],
            [470.8249969482422, 885.0625],
            [455.9499969482422, 885.0625],
            [366.6999969482422, 647.0625]
        ]
    ],
    "scores": [
        [0.9475298, 0.91467255, 0.9309549, 0.93212634, 0.91439706, 0.92376846, 0.9559441, 0.92240274, 0.92409635, 0.70719063, 0.09392133, 0.9165937, 0.76593524, 0.1276727, 0.9233127]
    ]
}
'''
