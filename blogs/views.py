from django.core import mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm, VirtualReceptionForm
from .models import Post, GalleryImage, GalleryCategory
from . import models, forms

CONST_PAGINATOR_NUMBER = 10


# class FormSubmitSendEmailFormView:
#     def send_mail_to_receivers(self, request, form):
#         # messages.add_message(request, messages.SUCCESS, _("Your appeal was sent successfully"))
#         receivers = [r.mail for r in models.MessageReceiver.objects.filter(category=form.Meta.category_name)]
#
#         connection = mail.get_connection()
#
#         try:
#             connection.open()
#         except Exception as e:
#             # messages.add_message(request, messages.ERROR, _('Sorry, at this time we can\'t receive your request.'))
#             return False
#
#         attachment = None
#
#         email = mail.EmailMessage(
#             subject=message_subject,
#             body=message_text,
#             from_email=settings.EMAIL_HOST_USER,
#             to=receivers,
#             connection=connection
#         )
#
#         if attachment:
#             email.attach(**attachment)
#
#         try:
#             email.send()
#         except:
#             # messages.add_message(request, messages.ERROR, _('Sorry, we can\'t receive your request at this time'))
#             return False
#
#         connection.close()
#         return True

def error_404(request, exception):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html', status=500)


def index_page(request):
    context = {
        'useful_links': models.UsefulLink.objects.all(),
        'partners': models.Partner.objects.all(),
        'news': models.Post.objects.all()[:6],
        'products': models.Product.objects.all(),
        'photogallery': models.GalleryImage.objects.all()[:3],
        'media': models.Media.objects.all()[:3],
        'questions': models.FAQ.objects.all()[:6],
        'company_info': models.CompanyInfo.objects.all(),
        'menu': models.Menu.objects.all(),
        'infographics': models.Infographic.objects.all(),
        'expolinks': models.ExpoLink.objects.all(),
        'short_links': models.ShortLink.objects.filter(parent__isnull=True),
        'menu_links': models.MenuOverlay.objects.all(),
        'vacancys': models.Vacancy.objects.all(),
        'joins': models.HowToJoin.objects.all()
        # 'regions': models.Region.objects.all(),
    }
    return render(request, 'blogs/index.html', context)


def about_page(request):
    context = {
        'vacancy': models.Vacancy.objects.all(),
        'items': models.CompanyInfo.objects.all(),
        # 'employees': models.Staff.objects.all(),
        'legislation': models.Legislation.objects.all(),
        'regional': models.RegionalAdministration.objects.all(),
    }
    return render(request, 'blogs/pages/about/indexAbout.html', context)


def login_page(request):
    return render(request, 'blogs/pages/login/index.html')


class NewsSearchView(generic.ListView):
    queryset = models.Post.objects.filter()
    template_name = 'blogs/pages/news/search_post_result.html'
    context_object_name = 'news'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(NewsSearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = self.request.GET.get('search')

        return self.queryset.filter(
            Q(translations__title__icontains=q) |
            Q(translations__main_text__icontains=q)
        )


# class JoinView(generic.TemplateView):
#     template_name = 'blogs/pages/how_to_join/how_to_join.html'
#     models = models.HowToJoin
#     context_object_name = 'joins'

def join_view(request):
    joins = models.HowToJoin.objects.all()
    context = {
        "joins": joins
    }
    return render(request, "blogs/pages/how_to_join/how_to_join.html", context)


def structure_view(request):
    structure = models.StructureAdmin.objects.all()
    context = {
        "structure": structure
    }
    return render(request, "blogs/pages/structure/structure.html", context)


def history_view(request):
    history = models.HistoryAdmin.objects.all()
    context = {
        "history": history
    }
    return render(request, "blogs/pages/history_of_organization/history_of_organization.html", context)


def partners_view(request):
    partner = models.Partner.objects.all()
    context = {
        "partner": partner
    }
    return render(request, "blogs/pages/partners/partners.html", context)


def press_service_view(request):
    press_service = models.PressServiceAdmin.objects.all()
    context = {
        "press_service": press_service
    }
    return render(request, "blogs/pages/press_service/press_service.html", context)


def moscow_view(request):
    moscow = models.MoscowAdmin.objects.all()
    context = {
        "moscow": moscow
    }
    return render(request, "blogs/pages/press_service/press_service.html", context)


def benefits_view(request):
    benefits = models.BenefitsAdmin.objects.all()
    context = {
        "benefits": benefits
    }
    return render(request, "blogs/pages/benefits/benefits.html", context)


def events_view(request):
    events = models.EventsAdmin.objects.all()
    context = {
        "events": events
    }
    return render(request, "blogs/pages/events/events.html", context)


def presentations_view(request):
    presentations = models.PresentationsAdmin.objects.all()
    context = {
        "presentations": presentations
    }
    return render(request, "blogs/pages/presentations/presentations.html", context)


def press_releases_view(request):
    press_releases = models.PressReleasesAdmin.objects.all()
    context = {
        "press_releases": press_releases
    }
    return render(request, "blogs/pages/press_releases/press_releases.html", context)


def publications_view(request):
    publications = models.PublicationsAdmin.objects.all()
    context = {
        "publications": publications
    }
    return render(request, "blogs/pages/publications/publications.html", context)


def youth_policy_view(request):
    youth_policy = models.YouthPolicyAdmin.objects.all()
    context = {
        "youth_policy": youth_policy
    }
    return render(request, "blogs/pages/youth_policy/youth_policy.html", context)


def territorial_view(request):
    territorial = models.TerritorialAdmin.objects.all()
    context = {
        "territorial": territorial
    }
    return render(request, "blogs/pages/territorial_administrations/territorial_administrations.html", context)


def investmentadmin_view(request):
    potential = models.InvestmentPotentialAdmin.objects.all()
    context = {
        "potential": potential
    }
    return render(request, "blogs/pages/investment_potential/investment_potential.html", context)


def export_potential_view(request):
    export_potential = models.ExportPotentialAdmin.objects.all()
    context = {
        "export_potential": export_potential
    }
    return render(request, "blogs/pages/export_potential/export_potential.html", context)


def export_implementation_view(request):
    export_implementation = models.ExportImplementationAdmin.objects.all()
    context = {
        "export_implementation": export_implementation
    }
    return render(request, "blogs/pages/export_implementation/export_implementation.html", context)


def export_law_view(request):
    export_law = models.ExportLawAdmin.objects.all()
    context = {
        "export_law": export_law
    }
    return render(request, "blogs/pages/export_law/export_law.html", context)


def lex_uz_view(request):
    return redirect("https://lex.uz")


def market_entry_strategies_view(request):
    market_entry_strategies = models.MarketEntryStrategies.objects.all()
    context = {
        "market_entry_strategies": market_entry_strategies
    }
    return render(request, "blogs/pages/market_entry_strategies/market_entry_strategies.html", context)


def subsidaries_view(request):
    subsidaries = models.SubsidariesAdmin.objects.all()
    context = {
        "subsidaries": subsidaries
    }
    return render(request, "blogs/pages/subsidaries/subsidaries.html", context)


def subsidaries2_view(request):
    subsidaries2 = models.SubsidariesAdmin.objects.all()
    context = {
        "subsidaries2": subsidaries2
    }
    return render(request, "blogs/pages/subsidaries/subsidaries2.html", context)


def leadership_view(request):
    leadership = models.Staff.objects.all()
    context = {
        "leadership": leadership
    }
    return render(request, "blogs/pages/about2/leadership.html", context)


def investors_view(request):
    investors = models.InvestorsAdmin.objects.all()
    context = {
        "investors": investors
    }
    return render(request, "blogs/pages/investors/investors.html", context)


def exporters_view(request):
    leadership = models.ExportersAdmin.objects.all()
    context = {
        "leadership": leadership
    }
    return render(request, "blogs/pages/exporters/exporters.html", context)


def foreighn_view(request):
    foreighn = models.ForeighnAdmin.objects.all()
    context = {
        "foreighn": foreighn
    }
    return render(request, "blogs/pages/foreighn_representations/foreign_representations.html", context)


def companys_types_view(request):
    company_types = models.CompanyTypes.objects.all()
    context = {
        "company_types": company_types
    }
    return render(request, "blogs/pages/menu_companys/company_types.html", context)


def menu_companys_view(request, type_slug):
    stir = request.GET.get("stir", None)
    company_type = models.CompanyTypes.objects.filter(slug=type_slug).first()
    if stir:
        menu_companys = models.MenuCompanys.objects.filter(translations__stir__contains=stir.strip(), company_type=company_type)
    else:
        menu_companys = models.MenuCompanys.objects.filter(company_type=company_type)
    context = {
        "menu_companys": menu_companys
    }
    return render(request, "blogs/pages/menu_companys/menu_companys.html", context)


class NewsListView(generic.ListView):
    template_name = "blogs/pages/news/list.html"
    model = models.Post
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.filter(status='published')


class NewsDetailView(generic.DetailView):
    template_name = "blogs/pages/news/detail.html"
    queryset = models.Post.published.all()
    context_object_name = 'post'


class StaticContentView(generic.DetailView):
    template_name = "blogs/pages/static_content/detail.html"
    queryset = models.StaticContent.objects.all()
    slug_url_kwarg = 'slug'


class StatisticListView(generic.ListView):
    template_name = "blogs/pages/statistics/list.html"
    model = models.Statistic
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'items'


class StatisticDetailView(generic.DetailView):
    template_name = "blogs/pages/statistics/detail.html"
    queryset = models.Statistic.objects.all()
    context_object_name = 'item'


class TenderListView(generic.ListView):
    template_name = "blogs/pages/tender/list.html"
    model = models.Tender
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'tenders'

    def get_queryset(self):
        return self.model.objects.filter()


class TenderDetailView(generic.DetailView):
    template_name = "blogs/pages/tender/detail.html"
    queryset = models.Tender.published.all()
    context_object_name = 'tender'


class ProductListView(generic.ListView):
    template_name = "blogs/pages/product/product_list.html"
    model = models.Product
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.filter()


class MembershipListView(generic.ListView):
    template_name = "blogs/pages/membership/list.html"
    model = models.Product
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'memberships'

    def get_queryset(self):
        return self.model.objects.filter()


class MembershipDetailView(generic.DetailView):
    template_name = "blogs/pages/membership/detail.html"
    # queryset = models.Post.published.all()
    context_object_name = 'membership'


class VacancyListView(generic.ListView):
    template_name = "blogs/pages/vacancy/vacancy_list_view.html"
    model = models.Vacancy
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'vacancy'

    def get_queryset(self):
        return self.model.objects.filter()


class LegalDocumentListView(generic.ListView):
    template_name = "blogs/pages/legaldocument/list.html"
    model = models.LegalDocument
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'legal'

    def get_queryset(self):
        return self.model.objects.filter()


class LegalDocumentView(generic.DetailView):
    template_name = "blogs/pages/legaldocument/detail.html"
    queryset = models.LegalDocument.objects.all()
    slug_url_kwarg = 'slug'


class GalleryListView(generic.ListView):
    template_name = "blogs/pages/gallery/indexG.html"
    model = models.GalleryImage
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'images'

    def get_queryset(self):
        return self.model.objects.filter()

    # def Gallery(request):
    #     images = None
    #     categories = GalleryCategory.get_all_categories()
    #     categoryID = request.GET.get('category')
    #     if categoryID:
    #         images = GalleryImage.get_all_images_by_category_id(categoryID)
    #     else:
    #         images = GalleryImage.get_all_images()
    #     data = {}
    #     data['images'] = images
    #     data['categories'] = categories
    #     return render(request, 'blogs/pages/gallery/indexG.html', data)


class MediaListView(generic.ListView):
    template_name = "blogs/pages/video/index.html"
    model = models.Media
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'media'

    def get_queryset(self):
        return self.model.objects.filter()


class FAQListView(generic.ListView):
    template_name = "blogs/pages/faq/list_view.html"
    model = models.FAQ
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'faqs'

    def get_queryset(self):
        return self.model.objects.filter()


def virtual_reception_view(request):
    context = {}
    form = VirtualReceptionForm()
    context['form'] = form
    if request.GET:
        temp = request.GET['field']
        print(temp)
    return render(request, "blogs/pages/virtual_reception/virtual_reception_form.html", context)

    # class VirtualReceptionListView(generic.FormView):
    #     template_name = "blogs/pages/virtual_reception/virtual_reception_form.html"
    #     form_class = forms.VirtualReceptionForm
    #     model = models.VirtualReceptionFormData
    #
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['number'] = "reception"
    #         return context


class EntrepreneursListView(generic.FormView):
    template_name = "blogs/pages/for_entrepreneurs/entrepreneurs.html"
    form_class = forms.ContactForm

    # model = models.FAQ

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = "entrepreneurs"
        return context


class MembershipProcedureListView(generic.ListView):
    template_name = "blogs/pages/membership_procedure/membership_procedure.html"
    model = models.FAQ

    def get_queryset(self):
        return self.model.objects.filter()


# class BenefitTemplateView(generic.TemplateView):
#     template_name = "blogs/pages/benefits/benefits.html"
#     model = models.FAQ
#
#     def get_queryset(self):
#         return self.model.objects.filter()


class ExhibitionListView(generic.ListView):
    template_name = "blogs/pages/exhibition/exhibition_list.html"
    model = models.Exhibition
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'exhibitions'

    def get_queryset(self):
        return self.model.objects.filter()


class ExhibitionDetailView(generic.DetailView):
    template_name = "blogs/pages/exhibition/exhibition_detail.html"
    queryset = models.Exhibition.published.all()
    context_object_name = 'exhibition'

    # class ExportImplementationProcedure(generic.DetailView):
    #     template_name = "blogs/pages/export_implementation_procedure/index.html"
    #     context_object_name = 'item'
    #
    #     def get_object(self, queryset=None):
    #         return models.ExportImplementationProcedure.objects.first()


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            messages.success(request,
                             'Thank you for your inquiry. Your contact information and message was successfully submitted.')
            return render(request, 'blogs/pages/contact_page/contact_form.html')
        else:
            for error in form.errors:
                messages.error(request, f"{error}: {form.errors[error][0]}")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'blogs/pages/contact_page/contact_form.html', context)