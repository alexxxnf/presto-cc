from werkzeug import exceptions as e


class BadRequest(e.BadRequest):
    pass


class NotFound(e.NotFound):
    pass
