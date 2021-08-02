import parler.models
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField
from mapbox_location_field import models as mapbox_models
from parler import models as parler_models, managers as parler_managers
from ckeditor import fields as ckeditor_fields
from ckeditor_uploader import fields as ckeditor_uploader_fields
from mptt import models as mptt_models
from slugify import slugify
from . import managers


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class TranslatablePublishedManager(parler_managers.TranslatableManager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


def generate_slug(obj):
    return slugify(obj.title)


class Post(parler_models.TranslatableModel):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, verbose_name=_("title")),
        short_description=models.CharField(max_length=500, null=True, verbose_name=_(" short_description")),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )

    slug = models.SlugField(max_length=200, null=True)
    # slug = AutoSlugField(populate_from=generate_slug, always_update=True, max_length=250),
    image = models.ImageField(null=True, upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name=_('status'))

    # objects = models.Manager()  # The default manager.
    published = TranslatablePublishedManager()

    def get_absolute_url(self):
        return reverse('blogs:news_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title


class Tender(parler_models.TranslatableModel):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, verbose_name=_("Title")),
        short_description=models.CharField(max_length=250, null=True, verbose_name=_("Short description")),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )
    slug = models.SlugField(max_length=200, null=True)
    # slug = AutoSlugField(populate_from=generate_slug, always_update=True, max_length=250)
    image = models.ImageField(null=True, upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # objects = models.Manager()
    published = TranslatablePublishedManager()

    def get_absolute_url(self):
        return reverse('blogs:tender_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = _('Tender')
        verbose_name_plural = _('Tenders')

    def __str__(self):
        return self.title


class Product(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )
    slug = models.SlugField(max_length=200, null=True)
    # slug = AutoSlugField(populate_from=generate_slug, always_update=True, max_length=250)
    image = models.ImageField(null=True, upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = models.Manager()
    # published = TranslatablePublishedManager()

    def get_absolute_url(self):
        return reverse('blogs:', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class UsefulLink(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250)
    )
    image = models.ImageField(null=True, upload_to='images/')
    link_to_website = models.URLField(null=True, blank=True, verbose_name=_('Website link'))

    def __str__(self):
        return self.link_to_website

    class Meta:
        verbose_name = _('Useful Link')
        verbose_name_plural = _('Useful Links')


class ExpoLink(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250)
    )
    image = models.ImageField(null=True, upload_to='images/')
    link_to_website = models.URLField(null=True, blank=True, verbose_name=_('Website link'))

    def __str__(self):
        return self.link_to_website

    class Meta:
        verbose_name = _('Expo Link')
        verbose_name_plural = _('Expo Links')


class Partner(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        name_of_partner=models.CharField(max_length=250, verbose_name='Name of Partner'),
        adress=models.CharField(max_length=250, null=True, verbose_name=_('adress')),
        telefon=models.CharField(max_length=12, null=True, verbose_name='Phone'),

    )
    image = models.ImageField(null=True, upload_to='images/')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name_of_partner

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')


class Vacancy(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250),
        description=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text")),
        speciality=models.CharField(max_length=250, blank=True, null=True),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancys')


class GalleryCategory(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250)
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_categories():
        return GalleryCategory.objects.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Gallery Category")
        verbose_name_plural = _("Gallery Categorys")


class GalleryImage(parler_models.TranslatableModel):
    # category = models.ForeignKey("GalleryCategory", on_delete=models.CASCADE, null=True)
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250),
    )
    slug = models.SlugField(max_length=200, null=True)
    # slug = models.SlugField(max_length=100, unique=True, null=True)
    image = models.ImageField(null=True, upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_images():
        return GalleryCategory.objects.all()

    @staticmethod
    def get_all_images_by_category_id(category_id):
        if category_id:
            return GalleryImage.objects.filter(category=category_id)
        else:
            return GalleryImage.get_all_images()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Gallery Image")
        verbose_name_plural = _("Gallery Images")


class Media(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, null=True)
    )
    link = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")


class Infographic(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, null=True),
        value=models.IntegerField(null=True)
    )
    icon = models.CharField(max_length=250, null=True)
    order = models.PositiveIntegerField(default=0, editable=False)
    added = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Infographic")
        verbose_name_plural = _("Infographics")


class StaticContent(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Content"))
    )
    slug = models.SlugField(max_length=200, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Static Content")
        verbose_name_plural = _("Static Contents")


class LegalDocument(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Content"))
    )
    slug = models.SlugField(max_length=200, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Legal Document")
        verbose_name_plural = _("Legal Documents")


class Statistic(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Content"))
    )
    slug = models.SlugField(max_length=200, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Statistic")
        verbose_name_plural = _("Statistics")


class Menu(mptt_models.MPTTModel, parler_models.TranslatableModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    translations = parler_models.TranslatedFields(
        name=models.CharField(blank=False, default='', max_length=128, null=True),
        link=models.CharField(blank=True, null=True, default='', max_length=128)
    )
    objects = managers.CustomMpttManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or ''

    class Meta:
        verbose_name = _("Menu item")
        verbose_name_plural = _("Menu items")


class ShortLink(mptt_models.MPTTModel, parler_models.TranslatableModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    translations = parler_models.TranslatedFields(
        name=models.CharField(blank=False, default='', max_length=128),
    )
    url = models.CharField(blank=True, null=True, default='', max_length=128)
    objects = managers.CustomMpttManager()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _("ShortLink item")
        verbose_name_plural = _("ShortLink items")


class Staff(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        name=models.CharField(max_length=255, null=True),
        position=models.CharField(max_length=255, null=True)
    )
    image = models.ImageField(upload_to='uploads/staff_image/')
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    reception = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')


class CompanyInfo(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        intro_about_us=models.TextField(null=True),
        about_us_content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("content about us")),
        about_us_history=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("history about us")),
        company_structure=ckeditor_uploader_fields.RichTextUploadingField(null=True,
                                                                          verbose_name=_("company_structure")),
        company_report=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("company_report")),
    )
    about_us_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = _('Company Info')
        verbose_name_plural = _('Company Infos')


class FAQ(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        question=models.CharField(max_length=255, null=True),
        answer=models.CharField(max_length=500, null=True)
    )
    order = models.IntegerField()

    class Meta:
        ordering = ["order"]
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')

    def __str__(self):
        return self.question


class SiteSetting(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        address=models.CharField(max_length=255, null=True, blank=True)
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = mapbox_models.LocationField(null=True, blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('Site Setting')
        verbose_name_plural = _('Site Settings')


class Exhibition(parler_models.TranslatableModel):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250),
        short_description=models.CharField(max_length=250, null=True),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )
    slug = AutoSlugField(populate_from=generate_slug, always_update=True, max_length=250)
    image = models.ImageField(null=True, upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    # objects = models.Manager()
    published = TranslatablePublishedManager()

    def get_absolute_url(self):
        return reverse('blogs:', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
        verbose_name = _('Exhibition')
        verbose_name_plural = _('Exhibitions')


class VirtualReception(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
    )

    REGION_CHOICES = (
        ('andijan', "Andijan"),
        ('bukhara', "Bukhara"),
        ('fergana', "Fergana"),
        ('jizzakh', "Jizzakh"),
        ('khorezm', "Khorezm"),
        ('namangan', "Namangan"),
        ('navoiy', "Navoiy"),
        ('kashkadarya', "Kashkadarya"),
        ('samarkand', "Samarkand"),
        ('sirdarya', "Sirdarya"),
        ('surkhandarya', "Surkhandarya"),
        ('tashkent', "Tashkent"),
        ('tashkent_city', "Tashkent city"),
        ('karakalpakstan', "Karakalpakstan"),
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=REGION_CHOICES, default='tashkent')
    address = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='male')
    marital_status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='single')
    file_upload = models.FileField(null=True)
    message = models.TextField()

    def __str__(self): return f"{self.full_name}"

    class Meta:
        verbose_name = _("Virtual Reception")
        verbose_name_plural = _("Virtual Reception")


class VirtualReceptionFormData(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _("Request form: Contact form data")
        verbose_name_plural = _("Request forms: Contact form data")

    def __str__(self): return f"{self.full_name} - {self.subject}"


class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('full_name'))
    email = models.EmailField()
    phone_number = models.CharField(max_length=255, verbose_name=_('phone_number'))
    subject = models.CharField(max_length=255, verbose_name=_('subject'))
    message = models.TextField()

    def __str__(self): return f"{self.full_name} - {self.subject}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class ContactFormData(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('full_name'))
    phone = models.CharField(max_length=255, verbose_name=_('phone'))
    email = models.EmailField()
    subject = models.CharField(max_length=255, verbose_name=_('subject'))
    message = models.TextField()

    class Meta:
        verbose_name = _("Request form: Contact form data")
        verbose_name_plural = _("Request forms: Contact form data")

    def __str__(self): return f"{self.full_name} - {self.subject}"


class Legislation(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, null=True, verbose_name=_('Title')),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Legislation')
        verbose_name_plural = _('Legislations')


class RegionalAdministration(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, null=True, verbose_name=_('Title')),
        main_text=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Full text"))
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Regional Administration')
        verbose_name_plural = _('Regional Administration')


class MenuSettings(parler_models.TranslatableModel):
    """ MENU SITE SETTINGS MODEL """
    translations = parler_models.TranslatedFields(
        logo_text=models.CharField(max_length=255, blank=True, verbose_name=_('Logo text')),
        logo_text_footer=models.CharField(max_length=255, blank=True, verbose_name=_('Logo text footer')),
        address=models.CharField(max_length=255, blank=True, verbose_name=_('Address')),
        operating_mode=models.TextField(blank=True, null=True, verbose_name=_('Operating Mode')),
        content=models.TextField(blank=True, null=True, verbose_name=_('Content')),
        home_page_text=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Home Page Text')),
    )
    logo = models.ImageField(upload_to='images/', verbose_name=_('Image'))
    tel_first = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Tel First'))
    tel_second = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Tel Second'))
    tel_third = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Tel Third'))
    tel_fourth = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Tel Fourth'))
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    since = models.CharField(blank=True, null=True, max_length=50, verbose_name=_('Since'))

    facebook = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)

    site_background = models.ImageField(upload_to='images/', null=True, verbose_name=_('Site Background'))
    site_background2 = models.ImageField(upload_to='images/', null=True, verbose_name=_('Site Background 2'))


class Meta:
    verbose_name = _('Menu Settings')
    verbose_name_plural = _('Menu Settings')


class Banner(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        text=models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Text'))
    )
    banner_carousel = models.ImageField(upload_to='images/', null=True, verbose_name=_('Banner Carousel'))

    class Meta:
        verbose_name = _('Banners')
        verbose_name_plural = _('Banners')


class Region(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        Andijan=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Andijan')),
        Bukhara=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Bukhara')),
        Fergana=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Fergana')),
        Jizzakh=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Jizzakh')),
        Xorazm=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Xorazm')),
        Namangan=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Namangan')),
        Navoiy=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Navoiy')),
        Qashqadaryo=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Qashqadaryo')),
        Samarqand=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Samarqand')),
        Sirdaryo=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Sirdaryo')),
        Guliston=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Guliston')),
        Surxondaryo=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Surxondaryo')),
        TashkentRegion=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('TashkentRegion')),
        Karakalpakstan=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Karakalpakstan')),
        Tashkent=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Tashkentt')),
    )
    AndijanNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('AndijanNumber'))
    BukharaNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('BukharaNumber'))
    FerganaNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('FerganaNumber'))
    JizzakhNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('JizzakhNumber'))
    XorazmNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('XorazmNumber'))
    NamanganNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('NamanganNumber'))
    NavoiyNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('NavoiyNumber'))
    QashqadaryoNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('QashqadaryoNumber'))
    SamarqandNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('SamarqandNumber'))
    SirdaryoNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('SirdaryoNumber'))
    SurxondaryoNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('SurxondaryoNumber'))
    TashkentNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('TashkentNumber'))
    GulistonNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('GulistonNumber'))
    KarakalpakstanNumber = models.CharField(max_length=20, blank=True, null=True,
                                            verbose_name=_('KarakalpakstanNumber'))
    TashkentRegionNumber = models.CharField(max_length=20, blank=True, null=True,
                                            verbose_name=_('TashkentRegionNumber'))

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class MenuOverlay(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=250, blank=True, null=True, verbose_name=_('title'))
    )
    link = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('link'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Menu Overlay')


class HowToJoin(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_("Content"))
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('How to join')


class CompanyTypes(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_("name"))
    )

    image = models.ImageField(verbose_name=_("image"))
    slug = models.SlugField(verbose_name=_("slug"))


class MenuCompanys(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        stir=models.CharField(max_length=20, verbose_name=_('stir')),
        title=models.CharField(max_length=240, verbose_name=_('title')),
        region=models.CharField(max_length=100, verbose_name=_('region'))
    )
    image = models.ImageField(null=True, verbose_name=_('image'))
    company_type = models.ForeignKey(CompanyTypes, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Menu Companys')


class BenefitsAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=140, null=True, verbose_name=_('Title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name="content")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Benefits')


class StructureAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name='title')
    )
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Structure')


class HistoryAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('History of Organization')


class TerritorialAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Territorial Administration')


class SubsidariesAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Subsidaries')


class Subsidaries2Admin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Subsidaries2')


class ForeighnAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Foreighn Representation')


class PressServiceAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Press service')


class MoscowAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Moscow')


class EventsAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    image = models.ImageField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class InvestmentPotentialAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    media = models.FileField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Investment potential')


class ExportPotentialAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    media = models.FileField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Export Potential')


class ExportImplementationAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    media = models.FileField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Export Implementation')


class ExportLawAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    media = models.FileField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Export Law')


class MarketEntryStrategies(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    media = models.FileField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Market entry strategies')


class PresentationsAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Presentations')


class PressReleasesAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Press Releases')


class YouthPolicyAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Youth Policy')


class PublicationsAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Publications')


class InvestorsAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )
    image = models.ImageField(null=True, upload_to='images/')
    image2 = models.ImageField(null=True, upload_to='images/')
    image3 = models.ImageField(null=True, upload_to='images/')
    image4 = models.ImageField(null=True, upload_to='images/')


def __str__(self):
    return self.title


class Meta:
    verbose_name = _('Investors')


class ExportersAdmin(parler_models.TranslatableModel):
    translations = parler.models.TranslatedFields(
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('title')),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, verbose_name=_('content')),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Exporters')
