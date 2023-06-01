from app.internal.utils import base64_to_numpy, numpy_to_base64
from app.pipelines.model_manager import get_model_manager, ModelManager
# from app.pipelines.instances import person_image_segment, product_image_segment
# from app.internal.piplines import word_segmentation_pipeline
from fastapi import APIRouter, Body, Depends, HTTPException

# https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2EAS
router = APIRouter()

@router.post('/image-segment/person')
def post_image_segment_person(
        image: str = Body(embed=True, alias="image", min_length=10),
        model_manager: ModelManager = Depends(get_model_manager)
):
    image_numpy = base64_to_numpy(image)
    if image_numpy is None:
        raise HTTPException(status_code=422, detail="Request Error, invalid image")

    output = model_manager.person_image_segment.handle(image_numpy)

    output_img = numpy_to_base64(output, "png")
    return {
        "image": output_img
    }


@router.post('/image-segment/product')
def post_image_segment_product(
        image: str = Body(embed=True, alias="image", min_length=10),
        model_manager: ModelManager = Depends(get_model_manager)
):
    image_numpy = base64_to_numpy(image)
    if image_numpy is None:
        raise HTTPException(status_code=422, detail="Request Error, invalid image")

    output = model_manager.product_image_segment.handle(image_numpy)

    output_img = numpy_to_base64(output, "png")
    return {
        "image": output_img
    }
