from app.internal.utils import base64_to_numpy
# from app.pipelines.instances import body_2d_keypoint
from app.pipelines.model_manager import get_model_manager, ModelManager
from fastapi import APIRouter, Body, Depends, HTTPException

# https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2EAS
router = APIRouter()

@router.post('/image-body/2d-keypoint')
def post_image_body_2d_keypoint(
        image: str = Body(embed=True, alias="image", min_length=10),
        model_manager: ModelManager = Depends(get_model_manager)
):
    image_numpy = base64_to_numpy(image)
    if image_numpy is None:
        raise HTTPException(status_code=422, detail="Request Error, invalid image")

    result = model_manager.body_2d_keypoint.handle(image_numpy)

    return result
