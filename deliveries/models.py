from django.db import models
from datetime import date
from gdstorage.storage import GoogleDriveStorage
from activities.models import Activity
from workgroups.models import Workgroup

# Define Google Drive Storage
GD_STORAGE = GoogleDriveStorage()

# Create your models here.

class Delivery(models.Model):
    NOT_AVALIATED = 'NAV'
    AVALIATED_BY_GUEST = 'AGS'
    AVALIATED_BY_ADVISOR = 'AAD'

    DELIVERY_STATUSES = (
        (NOT_AVALIATED, 'Não avaliada'),
        (AVALIATED_BY_GUEST, 'Avaliada pelo co-orientador'),
        (AVALIATED_BY_ADVISOR, 'Avaliada pelo orientador'),
    )

    REQUIRED_FIELDS = (
        'submission_date',
        'main_file',
        'side_file',
        'status',
        'public_comments',
        'private_comments',
        'score',
        'activity',
        'workgroup',
        'created_at',
        'updated_at',
    )

    submission_date = models.DateField(
        default=date.today
    )
    main_file = models.FileField(
        upload_to='submission_files',
        storage=GD_STORAGE,
    )
    side_file = models.FileField(
        upload_to='submission_files',
        storage=GD_STORAGE,
    )
    status = models.CharField(
        max_length=3,
        choices=DELIVERY_STATUSES,
        default=NOT_AVALIATED
    )
    public_comments = models.TextField(
        max_length=500,
        default='',
    )
    private_comments = models.TextField(
        max_length=500,
        default='',
    )
    score = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    workgroup = models.ForeignKey(Workgroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
