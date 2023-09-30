from django.db import models


class BaseModel(models.Model):
    """
    Base model that includes default created / updated timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class BaseCsvValueEquivalence(BaseModel):

    def __init__(self, model, *args, **kwargs):
        from apps.clients.models import Client
        super(BaseCsvValueEquivalence, self).__init__(*args, **kwargs)
        self._meta.get_field('column').choices = [('', '--Operation--')] + get_fields_as_choices(model) + [('', '--Client--')] + get_fields_as_choices(Client)

    brand = models.ForeignKey('companies.Brand', on_delete=models.CASCADE)
    column = models.CharField(max_length=40)
    value = models.CharField(max_length=40)
    equivalence = models.CharField(max_length=100)
    operation_type = models.ForeignKey('operations.OperationType', on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='value_equivalences')

    class Meta:
        abstract = True

    @classmethod
    def get_column_from_equivalence(cls, equivalence, column, value, operation_type):
        try:
            return cls.objects.get(equivalence=equivalence, value=value,
                                   operation_type__id_name=operation_type).equivalence
        except cls.DoesNotExist:
            return value

    @classmethod
    def get_equivalence_from_column(cls, column, value, brand, operation_type):
        try:
            return cls.objects.get(column=column, value=value, brand=brand,
                                   operation_type__id_name=operation_type).equivalence
        except cls.DoesNotExist:
            return None

    def populate_from_csv(self, row):
        for header, value in row.items():
            setattr(self, header, value)


class BaseCsvColumnEquivalence(BaseModel):
    def __init__(self, model, *args, **kwargs):
        from apps.clients.models import Client
        super(BaseCsvColumnEquivalence, self).__init__(*args, **kwargs)
        self._meta.get_field('column').choices = ([('', '--Operation--')] + get_fields_as_choices(model)
                                                  + [('', '--Client--')] + get_fields_as_choices(Client))

    brand = models.ForeignKey('companies.Brand', on_delete=models.CASCADE)
    column = models.CharField(max_length=40)
    equivalence = models.CharField(max_length=100)
    is_id_value = models.BooleanField(default=False)
    operation_type = models.ForeignKey('operations.OperationType', on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='column_equivalences')

    def clean_is_id_value(self):
        (self.__class__.objects.
         filter(brand=self.brand, operation_type=self.operation_type).exclude(id=self.id).update(is_id_value=False))

    @classmethod
    def get_column_from_equivalence(cls, equivalence, brand, operation_type):
        try:
            return cls.objects.get(equivalence=equivalence, brand=brand, operation_type__id_name=operation_type).column
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_id_colum(cls, brand, operation_type):
        try:
            return cls.objects.get(is_id_value=True, brand=brand, operation_type__id_name=operation_type).column
        except cls.DoesNotExist:
            raise ValueError(cls.__name__ + _(" No tiene un id seleccionado"))

    class Meta:
        abstract = True


class RawDataImportable(models.Model):
    column_equivalence_class = None
    value_equivalence_class = None

    class Meta:
        abstract = True

    @classmethod
    def create_from_raw_data(cls, raw_data, operation_type, brand):
        data_as_file = StringIO(raw_data)

        created = []
        updated = []
        errors = []
        df = pd.read_csv(data_as_file, sep="\t")
        data_dict = df.to_dict(orient="records")
        for row in data_dict:
            instance_update = False
            instance_save = False
            class_instance = cls()
            class_instance.brand = brand
            class_instance.operation_type = operation_type
            class_instance.initialize_class_from_data(row, brand, operation_type)
            data = class_instance.check_and_get_if_exists(brand, operation_type)
            if data:
                class_instance.id = data.id
                instance_update = True
                class_instance.save(update_fields=class_instance.get_non_null_fields())
            else:
                class_instance.save()

            # manage save errors

            if instance_update:
                updated.append(class_instance)
            else:
                created.append(class_instance)

        return created, updated, errors

    def initialize_class_from_data(self, row_data, brand, operation_type):
        if self.column_equivalence_class is None or self.value_equivalence_class is None:
            raise ValueError("column_class and value_class must be set in child class")

        for header, value in row_data.items():
            column = self.column_equivalence_class.get_column_from_equivalence(header.strip(), brand, operation_type)
            value_equivalence = self.value_equivalence_class.get_equivalence_from_column(column, value, brand,
                                                                                         operation_type)
            if value_equivalence:
                value = value_equivalence

            if column and value:
                value = self.clean_nones(value)

                if 'date' in column and value:
                    print(column, ":", value)
                    try:
                        value = datetime.strptime(value, '%d/%m/%Y').date().strftime('%Y-%m-%d')
                    except ValueError:
                        raise ValueError(
                            f"El valor '{value}' tiene un formato de fecha no válido. Debe estar en formato DD/MM/AAAA.")
                setattr(self, column, value)

    def get_non_null_fields(self):
        non_null_fields = []

        for field in self._meta.fields:
            value = getattr(self, field.name)
            if value is not None:
                if type(field) is not BigAutoField:
                    non_null_fields.append(field.name)

        return non_null_fields

    def check_and_get_if_exists(self, brand, operation_type):
        column = self.get_id_column(brand, operation_type)
        try:
            params = {column: getattr(self, column)}
            return self.__class__.objects.get(**params)
        except FieldError:
            return None
        except self.__class__.DoesNotExist:
            return None

    def get_id_column(self, brand, operation_type):
        return self.column_equivalence_class.get_id_colum(brand, operation_type)

    def clean_nones(self, value):
        none_values = [
            "nan",
            "indefinido"
        ]

        if value != value:
            return None

        if value in none_values:
            return None
        else:
            return value