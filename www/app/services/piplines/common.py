from modelscope.hub.snapshot_download import snapshot_download
from modelscope.pipelines import pipeline


def make_pipeline(model: str, task: str):
    return pipeline(task=task, model=model)


def download_model(model: str, cache_dir: str = '/mnt/workspace/.cache/modelscope'):
    return snapshot_download(model, cache_dir=cache_dir)
