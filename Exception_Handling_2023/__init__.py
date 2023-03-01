from .celery import celery_app

# __all__ means exportable and importable from all other places
__all__ = ('celery_app',)