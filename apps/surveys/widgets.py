from apps.companies.models import Component


class ENPSWidget:
    template_name = 'widgets/enps.html'


class InfoWidget:
    template_name = 'widgets/info.html'

    def __init__(self, text):
        self.text = text


class ComponentWidget:
    template_name = 'widgets/components.html'

    def __init__(self, survey):
        self.survey = survey

    def get_components(self):
        return Component.objects.all()
