import re

STATE_LOADING = 0
STATE_NULL = 1
STATE_PAUSED = 2
STATE_PLAYING = 3
STATE_BUFFERING = 4

_cleanup_regexes = (
    (re.compile(r'(?P<amp>&)(?P<X>\w*[^;\w])'), lambda m: '&amp;'+m.group('X')),
    (re.compile(r'<br/?>'), ''),
    (re.compile(r'</?a.*?>'), '')
)
def cleanup_markup(s):
    for pattern, replace in _cleanup_regexes:
        s = pattern.sub(replace, s)
    return s


class Lock(object):
    def __init__(self, for_obj):
        import thread
        self.obj_thread_ident = thread.get_ident()

    def __enter__(self):
        import gtk
        if thread.get_ident() != self.obj_thread_ident:
            gtk.gdk.threads_enter()

    def __exit__(self, *exc_stuff_that_nobody_needs):
        import gtk
        if thread.get_ident() != self.obj_thread_ident:
            gtk.gdk.threads_leave()
