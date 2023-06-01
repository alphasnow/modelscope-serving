from app.internal.utils import bytes_to_base64
from app.pipelines.model_manager import get_model_manager, ModelManager
# from app.pipelines.instances import tts_emotion
from app.pipelines.utils import pcm_to_bytes
from fastapi import APIRouter, Body, Depends

router = APIRouter()


@router.post('/tts/emotion')
def post_tts_emotion(
        text: str = Body(embed=True, alias="text"),
        voice: str = Body(embed=True, alias="voice", default="zhiyan_emo"),
        emotion: str = Body(embed=True, alias="emotion", default=""),
        intensity: float = Body(embed=True, alias="intensity", default=1.0),
        model_manager: ModelManager = Depends(get_model_manager),
):
    output = model_manager.tts_emotion.handle(text, voice, emotion, intensity)

    audio = bytes_to_base64(pcm_to_bytes(output))
    return {
        "audio": audio
    }
