from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_default_groups, sender=self)


def create_default_groups(sender, **kwargs):
    from django.contrib.auth.models import Group
    for group_name in ['admin', 'editor', 'viewer']:
        Group.objects.get_or_create(name=group_name)
