from ..jobService import JobService
from ...repositories.jobRepository import JobRepository
from ...adapters.jobAdapter import jobAdapter
import math

class JobServiceImpl(JobService):
    def __init__(self, jobRepository: JobRepository):
        self.jobRepository = jobRepository

    def get_jobs(self, page: int, limit: int = 25):
        if page < 1:
            page = 1

        start = (page * limit) - limit

        jobs_list = self.jobRepository.getPaginated(start, limit)

        if jobs_list is None:
            return {
                'jobs': [],
                'result': None
            }

        jobs = []

        country = jobs_list['metadata']['geo']['fullLocalizedName']


        paging = jobs_list['paging']

        total_items = paging['total']


        for job in jobs_list['elements']:
            job_adapted = jobAdapter(job, country)
            jobs.append(job_adapted)


        total_pages = math.floor(total_items / limit)

        return {
            'jobs': jobs,
            'pagination': {
                'total_items': total_items,
                'limit': limit,
                'start': start,
                'page': page,
                'total_pages': total_pages
            }
        }

    def save(self, job, action):
        return self.jobRepository.save(job, action)
        
