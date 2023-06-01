from app.pipelines.singleton_instance import SingletonInstance
from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.preprocessors import TokenClassificationTransformersPreprocessor
from modelscope.utils.constant import Tasks


class ChineseSegment(SingletonInstance):
    def build(self):
        # https://www.modelscope.cn/models/damo/nlp_structbert_word-segmentation_chinese-base/summary
        model_id = 'damo/nlp_structbert_word-segmentation_chinese-base'
        model = Model.from_pretrained(model_id, revision='v1.0.2')
        tokenizer = TokenClassificationTransformersPreprocessor(model.model_dir)
        pipeline_ins = pipeline(
            task=Tasks.word_segmentation,
            model=model,
            preprocessor=tokenizer,
            model_revision='v1.0.2',  # 20230130
        )
        return pipeline_ins

    def handle(self, text: str):
        result = self.instance()(text)
        return result.get("output")
