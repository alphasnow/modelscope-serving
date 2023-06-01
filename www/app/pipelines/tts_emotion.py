from app.pipelines.singleton_instance import SingletonInstance
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class TtsEmotion(SingletonInstance):
    emotions = ['neutral', 'happy', 'angry', 'sad', 'fear', 'hate', 'surprise', 'arousal']
    voices = ['zhitian_emo', 'zhiyan_emo', 'zhizhe_emo', 'zhibei_emo']

    def build(self):
        # https://www.modelscope.cn/models/damo/speech_sambert-hifigan_tts_zh-cn_16k/summary
        return pipeline(
            task=Tasks.text_to_speech,
            model='damo/speech_sambert-hifigan_tts_zh-cn_16k',
            model_revision='v1.0.2',  # 20230130
        )

    def handle(self, text: str, voice: str = 'zhiyan_emo', emotion: str = '', intensity: float = 1.0):
        if voice not in self.voices:
            raise ValueError("Voice invalid")
        if emotion != "" and emotion not in self.emotions:
            raise ValueError("Emotion invalid")
        # https://help.aliyun.com/document_detail/101645.html#sectiondiv-g6w-isw-rmw
        # intensity
        if emotion != "":
            text = '<speak><emotion category="%s" intensity="%f">%s</emotion></speak>' % (emotion, intensity, text)

        res = self.instance()(input=text, voice=voice)
        return res[OutputKeys.OUTPUT_PCM]
