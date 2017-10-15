class Scene(object):
    """This is a prototype class for Scenes.  All scenes should inherit from it.
    No direct instances of this class should be created. 
    get_event and update must be overloaded in the childclass.
    startup and cleanup need to be overloaded when there is data that must persist between scenes."""

    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        """Processes events that were passed from the main event loop.
        Must be overloaded in children."""
        pass

    def startup(self, current_time, persistent):
        """Add variables passed in persistent to the proper attributes and
        set the start time of the State to the current time."""
        self.persist = persistent
        self.start_time = current_time

    def cleanup(self):
        """Add variables that should persist to the self.persist dictionary.
        Then reset State.done to False."""
        self.done = False
        return self.persist

    def update(self, dt):
        """Update function for state.  Must be overloaded in children."""
        pass

    def draw(self, surface):
        pass

    def render_font(self, font, msg, color, center):
        """Returns the rendered font surface and its rect centered on center."""
        msg = font.render(msg, 1, color)
        rect = msg.get_rect(center=center)
        return msg, rect
