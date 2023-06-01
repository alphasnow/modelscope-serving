from .asr_paraformer import AsrParaformer
from .body_2d_keypoint import Body2DKeypoint
from .chinese_segment import ChineseSegment
from .image_cartoon import ImageCartoon
from .ocr_general import OcrGeneral
from .person_image_segment import PersonImageSegment
from .product_image_segment import ProductImageSegment
from .tts_emotion import TtsEmotion


class ModelManager:
    SINGLETON: bool = True

    def __init__(self):
        self.image_cartoon = ImageCartoon(singleton=self.SINGLETON)
        self.chinese_segment = ChineseSegment(singleton=self.SINGLETON)
        self.product_image_segment = ProductImageSegment(singleton=self.SINGLETON)
        self.person_image_segment = PersonImageSegment(singleton=self.SINGLETON)
        self.tts_emotion = TtsEmotion(singleton=self.SINGLETON)
        self.asr_paraformer = AsrParaformer(singleton=self.SINGLETON)
        self.ocr_general = OcrGeneral(singleton=self.SINGLETON)
        self.body_2d_keypoint = Body2DKeypoint(singleton=self.SINGLETON)

    def initialize(self):
        self.image_cartoon.initialize()
        self.chinese_segment.initialize()
        self.product_image_segment.initialize()
        self.person_image_segment.initialize()
        self.tts_emotion.initialize()
        self.asr_paraformer.initialize()
        self.ocr_general.initialize()
        self.body_2d_keypoint.initialize()


manager = ModelManager()
manager.initialize()


def get_model_manager() -> ModelManager:
    return manager
