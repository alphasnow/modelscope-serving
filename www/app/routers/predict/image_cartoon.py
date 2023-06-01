from app.internal.utils import base64_to_numpy, numpy_to_base64
from app.pipelines.model_manager import get_model_manager, ModelManager
from fastapi import APIRouter, Body, Depends, HTTPException

# https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2EAS
router = APIRouter()

@router.post('/image-cartoon')
def post_image_cartoon(
        image: str = Body(embed=True, alias="image", min_length=10),
        algo_type: str = Body(default="anime", embed=True, alias="algo_type"),
        model_manager: ModelManager = Depends(get_model_manager)
):
    if not model_manager.image_cartoon.validate(algo_type):
        raise HTTPException(status_code=422, detail="Request Error, invalid algo_type " + algo_type)

    # https://help.aliyun.com/document_detail/188840.html
    image_numpy = base64_to_numpy(image)
    if image_numpy is None:
        raise HTTPException(status_code=422, detail="Request Error, invalid image")

    output = model_manager.image_cartoon.handle(image_numpy, algo_type)

    output_img = numpy_to_base64(output, "png")
    return {
        "image": output_img
    }
