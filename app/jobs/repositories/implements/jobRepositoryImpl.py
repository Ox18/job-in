from ..jobRepository import JobRepository
from main.apis.linkedinApi import LinkedinApi
from ...models import JobPosting
from django.utils.timezone import make_aware
from datetime import datetime
from django.forms.models import model_to_dict


class JobRepositoryImpl(JobRepository):
    def __init__(self, linkedinApi: LinkedinApi):
        self.linkedinApi = linkedinApi

    def getPaginated(self, start: int, limit: int) -> dict:
        url = f'/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-216&count={limit}&q=jobSearch&query=(currentJobId:4129885247,origin:JOBS_HOME_SEARCH_BUTTON,locationUnion:(geoId:105646813),spellCorrectionEnabled:true)&start={start}'

        return self.linkedinApi.get(url)
    
    def getRecluter(self, job_id):
        url = f'/voyagerHiringDashJobHiringSocialHirersCards?decorationId=com.linkedin.voyager.dash.deco.hiring.FullJobHiringSocialHirersCard-9&jobPosting=urn%3Ali%3Afsd_jobPosting%3A{job_id}&q=jobPosting&start=0'

        return self.linkedinApi.get(url)
    
    def save(self, data, action):

        listed_date_naive = datetime.fromisoformat(data['listed_date'])

        # Convertir a una fecha con zona horaria
        listed_date_aware = make_aware(listed_date_naive)

        job = JobPosting(
            post_id = data['post_id'],
            title = data['title'],
            company_name = data['company_name'],
            modality = data['modality'],
            ubigeo = data['ubigeo'],
            country = data['country'],
            logo_url = data['logo_url'],
            url = data['url'],
            reposted = data['reposted'],
            is_applied = data['is_applied'],
            status = data['status'],
            time_response = data['time_response'],
            application_type = data['application_type'],
            listed_date=listed_date_aware,  # Usa la fecha con zona horaria
            action = action
        )

        job.save()

        job_dict = model_to_dict(job)


        return job_dict
