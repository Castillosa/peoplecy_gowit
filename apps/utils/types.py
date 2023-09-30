OPERATION_TYPE_CHOICES = (
    ('client', 'Cliente'),
    ('visit', 'Visita'),
    ('budget', 'Presupuesto'),
    ('purchase', 'Compra'),
    ('payment', 'Pago'),
    ('delivery', 'Entrega'),
    ('issue', 'Incidencia'),
    ('return', 'Devolución'),
    ('order', 'Pedido'),
    ('service', 'Servicio'),
    ('reservation', 'Reserva'),
    ('hire', 'Contratación'),
    ('meal', 'Comida'),
    ('stay', 'Estancia'),
    ('hospitalization', 'Hospitalización'),
    ('claim', 'Siniestro'),
    ('advice', 'Asesoramiento'),
    ('course', 'Curso'),
    ('event', 'Evento'),
)


FILE_TYPE_CHOICES = OPERATION_TYPE_CHOICES + (
    ('client_csv_value_equivalences', 'Client Csv Value Equivalences'),
    ('client_csv_column_equivalences', 'Client Csv Column Equivalences'),
    ('operation_csv_value_equivalences', 'Operation Csv Value Equivalences'),
    ('operation_csv_column_equivalences', 'Operation Csv Column Equivalences'),
)


INTERVAL_CHOICES = (
    ('hour', 'Hora'),
    ('day', 'Día'),
    ('week', 'Semana'),
    ('month', 'Mes'),
    ('year', 'Año')
)

LOG_TYPE_SUCCESS = 'success'
LOG_TYPE_WARNING = 'warning'
LOG_TYPE_ERROR = 'error'
LOG_TYPE_INFO = 'info'

LOG_TYPE_CHOICES = (
    (LOG_TYPE_INFO, 'Info'),
    (LOG_TYPE_WARNING, 'Warning'),
    (LOG_TYPE_ERROR, 'Error'),
    (LOG_TYPE_SUCCESS, 'Success'),
)


ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'

ACTION_CHOICES = (
    (ACTION_CREATE, 'Create'),
    (ACTION_UPDATE, 'Update'),
    (ACTION_DELETE, 'Delete'),
)


LANGUAGE_CHOICES = (
    ('es', 'Español'),
    ('en', 'Inglés'),
)
