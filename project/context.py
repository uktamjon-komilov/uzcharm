from blogs import models


def defaults(req):
    return {
        "menus": models.Menu.objects.filter(parent__isnull=True),
        "menu_settings": models.MenuSettings.objects.first(),
        "regions": models.Region.objects.first(),
        "menu_links": models.MenuOverlay.objects.filter(),
        "banners": models.Banner.objects.filter()
    }