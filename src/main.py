from . import bootstrap
from .core.managers import SceneManager
from .scenes import title, stats


def main():
    manager = SceneManager(bootstrap.ORIGINAL_CAPTION)
    manager.setup_scenes({
        "TITLE": title.TitleScene(),
        "STATS": stats.StatsScene()
    }, "TITLE")
    manager.run()
