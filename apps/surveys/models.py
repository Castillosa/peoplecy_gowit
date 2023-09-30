
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.companies.models import Company, Component, Attribute
from apps.utils.models import BaseModel


class SurveyType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Survey(BaseModel):
    brand = models.ForeignKey('companies.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    hash_id = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    texto1 = models.TextField(null=True, blank=True)
    texto2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def steps(self):
        if self.surveyquestion_set.all().count() > 0:
            return self.surveyquestion_set.all().order_by('order').last().order

        return 0

    def get_components(self):
        return Component.objects.filter(company=self.company)

    def get_attributes(self):
        return Attribute.objects.filter(component__company=self.company)


QUESTION_TYPES = (
    ('info', _('info')),
    ('enps', _('enps')),
    ('components', _('componentes')),
    ('attributes', _('attributes')),
    ('text', _('text')),
)

ENPS_PROFILES = (
    ('-', None),
    ('detractors', _('detractors')),
    ('neutrals', _('neutrals')),
    ('promoters', _('promoters')),
)


# TODO: add unique constraint to batch and sender_uid
class SurveyQuestion(BaseModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255, help_text=_(
        'Puedes añadir variables con {{variable}} ex: {{componente}} {{atributo}}'))
    type = models.CharField(max_length=255, choices=QUESTION_TYPES)

    enps_filter = models.CharField(max_length=255, choices=ENPS_PROFILES, null=True, blank=True)
    order = models.IntegerField()
    is_required = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    components = models.ManyToManyField(Component, blank=True, help_text=_(
        'Selecciona los componentes que quieres que aparezcan en la pregunta, si no está seleccionado el tipo correcto no surgira efecto'))
    attributes = models.ManyToManyField(Attribute, blank=True, help_text=_(
        'Selecciona los attributos que quieres que aparezcan en la pregunta, si no está seleccionado el tipo correcto no surgira efecto'))
    answer_order_related = models.IntegerField(null=True, blank=True)

    def get_related_answer(self, batch, sender_uid):
        return SurveyAnswer.objects.get(answer_order=self.answer_order_related, batch=batch, sender_uid=sender_uid)

    def get_components(self):
        return self.components.all()

    def get_attributes(self):
        return self.attributes.all()


class SurveyAnswer(BaseModel):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.SET_NULL, null=True)
    delivery_record = models.ForeignKey('delivery.DeliveryRecord', on_delete=models.CASCADE, null=True,blank=True)
    delivery_config = models.ForeignKey('delivery.SurveyDeliveryConfig', on_delete=models.CASCADE, null=True,blank=True)
    value = models.TextField(null=True, blank=True)
    is_anonymous = models.BooleanField(default=False)
    is_enps_filtered = models.BooleanField(default=False)
    enps_profile = models.CharField(max_length=255, choices=ENPS_PROFILES, null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)
    answer_order = models.IntegerField(null=True, blank=True)
