# from app.pipelines.instances import chinese_segment
# from app.internal.piplines import word_segmentation_pipeline
from app.pipelines.model_manager import get_model_manager, ModelManager
from fastapi import APIRouter, Body, Depends

# https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2EAS
router = APIRouter()

@router.post('/word-segmentation')
def post_word_segmentation(
        text: str = Body(embed=True, alias="text", min_length=6),
        model_manager: ModelManager = Depends(get_model_manager),
):
    output = model_manager.chinese_segment.handle(text)
    return {
        "text": output
    }
