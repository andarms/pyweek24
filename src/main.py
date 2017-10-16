from . import bootstrap
from .core.managers import SceneManager
from .scenes import title, stats, battle


def main():
    manager = SceneManager(bootstrap.ORIGINAL_CAPTION)
    manager.setup_scenes({
        "TITLE": title.TitleScene(),
        "STATS": stats.StatsScene(),
        "BATTLE": battle.BattleScene()
    }, "BATTLE")
    manager.run()
