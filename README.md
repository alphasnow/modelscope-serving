# ModelScope Serving
![modelscope-serving](https://socialify.git.ci/alphasnow/modelscope-serving/image?description=1&font=Inter&language=1&name=1&pattern=Plus&theme=Auto)

Use the following command to easily start ModelScope Serving
```bash
git clone https://github.com/alphasnow/modelscope-serving.git
cd modelscope-serving
docker-compose up -f docker-compose.yml -d
```

## Example
```bash
# request
curl 'http://127.0.0.1:8800/api/predict/image-cartoon' \
-H 'Content-Type:application/json' \
-X POST \
-d '{"image":"TdbnJ6cHh9mV09O5qu+z6Sv3j06vPvJvcePHqdrLa...","algo_type":"anime"}'
# response
{"image":"Yc+a9/V3bHXmnZSu26oXaBa66pbLpbd4f7+8dHxj370o..."}
```

## Features
- Automatic Speech Recognition `/asr/paraformer`
- Text To Speech `/tts/emotion`
- Photo to Cartoon `/image-cartoon`
- Image segmentation `/image-segment/person` `/image-segment/product`
- Optical Character Recognition `/image-ocr/general`
- Word Segment `/word-segmentation`
- Body Detection `/image-body/2d-keypoint`

## Dependencies
- docker
- docker-compose
- modelscope
- python
- fastapi
- opencv
- uvicorn

## License
This project is licensed under the [Apache License (Version 2.0)](LICENSE).