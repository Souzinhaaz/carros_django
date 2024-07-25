from django.apps import AppConfig # type: ignore


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        import cars.signals
