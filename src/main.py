from . import bootstrap
from .core.managers import SceneManager
from .scenes import title


def main():
    manager = SceneManager(bootstrap.ORIGINAL_CAPTION)
    manager.setup_scenes({
        "TITLE": title.TitleScene()
    }, "TITLE")
    manager.run()
