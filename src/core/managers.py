import pygame as pg


class SceneManager(object):
    """Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to scenes as needed.
    Logic for flipping scenes is also found here."""

    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.caption = caption
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 80.
        self.show_fps = True
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self._scene_dict = {}
        self._scene_name = None
        self._scene = None
        self.fullscreen = False

    def setup_scenes(self, scene_dict, start_scene):
        """Given a dictionary of scenes and a State to start in,
        builds the self._scene_dict."""
        self._scene_dict = scene_dict
        self._scene_name = start_scene
        self._scene = self._scene_dict[self._scene_name]

    def update(self, dt):
        """Checks if a state is done or has called for a game quit.
        State is flipped if neccessary and State.update is called."""
        self.current_time = pg.time.get_ticks()
        if self._scene.quit:
            pg.mouse.set_visible(True)
            self.done = True
        elif self._scene.done:
            self.change_scene()
        self._scene.update(dt)
        self._scene.draw(self.screen)

    def change_scene(self):
        """When a State changes to done necessary startup and cleanup functions
        are called and the current State is changed."""
        previous, self._scene_name = self._scene_name, self._scene.next
        persist = self._scene.cleanup()
        self._scene = self._scene_dict[self._scene_name]
        self._scene.startup(persist)
        self._scene.previous = previous

    def event_loop(self):
        """Process all events and pass them down to current State.  The f5 key
        globally turns on/off the display of FPS in the caption"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
                self.toggle_fullscreen(event.key)
            self._scene.get_event(event)

    def toggle_show_fps(self, key):
        """Press f5 to turn on/off displaying the framerate in the caption."""
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)

    def toggle_fullscreen(self, key):
        if key == pg.K_F11:
            screen_size = pg.display.get_surface().get_size()
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                self.screen = pg.display.set_mode(screen_size, pg.FULLSCREEN)
            else:
                self.screen = pg.display.set_mode(screen_size)

    def run(self):
        """Main loop for entire program."""
        while not self.done:
            time_delta = self.clock.tick(self.fps)
            self.event_loop()
            self.update(time_delta)
            pg.display.update()
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)
