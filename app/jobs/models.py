from django.db import models

class JobPosting(models.Model):
    post_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    modality = models.CharField(max_length=100)
    ubigeo = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    logo_url = models.URLField(blank=True, null=True)
    url = models.URLField()
    reposted = models.BooleanField(default=False)
    is_applied = models.BooleanField(default=False)
    status = models.CharField(max_length=100, blank=True, null=True)
    time_response = models.CharField(max_length=100, blank=True, null=True)
    application_type = models.CharField(max_length=100, blank=True, null=True)
    listed_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title