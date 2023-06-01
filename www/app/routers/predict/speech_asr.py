from app.internal.utils import base64_to_bytes
from app.pipelines.model_manager import get_model_manager, ModelManager
# from app.pipelines.instances import asr_paraformer
from fastapi import APIRouter, Body, Depends

router = APIRouter()


@router.post('/asr/paraformer')
def post_asr_paraformer(
        audio: str = Body(embed=True, alias="audio"),
        model_manager: ModelManager = Depends(get_model_manager),
):
    # 16000 wav
    audio_bytes = base64_to_bytes(audio)

    output = model_manager.asr_paraformer.handle(audio_bytes)

    return {
        "text": output
    }
