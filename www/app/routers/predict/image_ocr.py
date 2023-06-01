from app.internal.utils import base64_to_numpy
from app.pipelines.model_manager import get_model_manager, ModelManager
# from app.pipelines.instances import ocr_general
# from app.internal.piplines import word_segmentation_pipeline
from fastapi import APIRouter, Body, Depends, HTTPException

# https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2EAS
router = APIRouter()

@router.post('/image-ocr/general')
def post_image_ocr_general(
        image: str = Body(embed=True, alias="image", min_length=10),
        model_manager: ModelManager = Depends(get_model_manager)
):
    image_numpy = base64_to_numpy(image)
    if image_numpy is None:
        raise HTTPException(status_code=422, detail="Request Error, invalid image")

    texts, positions = model_manager.ocr_general.handle(image_numpy)

    return {
        "text": texts,
        "position": positions,
    }
