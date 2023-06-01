from typing import Any

from app.pipelines.singleton_instance import SingletonInstance
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class AsrParaformer(SingletonInstance):
    def build(self):
        # https://www.modelscope.cn/models/damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1/summary
        return pipeline(
            task=Tasks.auto_speech_recognition,
            model='damo/speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1',
            model_revision='v1.1.8',  # 20230130
        )

    def handle(self, audio: Any):
        res = self.instance()(audio_in=audio)
        return res.get("text")
