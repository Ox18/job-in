from main.utils.response import Response
from .services.jobService import JobService
from django.http import JsonResponse
import json
from main.apis.implements.linkedinApiImpl import LinkedinApiImpl
class JobsController:
    def __init__(self, jobService: JobService):
        self.jobService = jobService

    def search(self, request):

        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 25)

        data = self.jobService.get_jobs(int(page), int(limit));

        return Response.ok(data, "Jobs is OK")
    
    def save(self, request):
        body_bytes = request.body
        body_str = body_bytes.decode('utf-8')
        data = json.loads(body_str)
        response = self.jobService.save(data, "ACEPTED")
        return Response.ok(response, "Jobs is OK")
    
    def reject(self, request):
        body_bytes = request.body
        body_str = body_bytes.decode('utf-8')
        data = json.loads(body_str)
        response = self.jobService.save(data, "REJECTED")
        return Response.ok(response, "Jobs is OK")
    
    def feedback(self, request):
        post_id = request.GET.get('post_id')


        response = LinkedinApiImpl().get(f'/graphql?variables=(cardSectionTypes:List(HOW_YOU_MATCH_CARD),jobPostingUrn:urn%3Ali%3Afsd_jobPosting%3A{post_id},includeSecondaryActionsV2:true)&queryId=voyagerJobsDashJobPostingDetailSections.bdbac23a4a46e498baa01dc48420f94e')


        elements = response['data']['jobsDashJobPostingDetailSectionsByCardSectionTypes']['elements']

        result = []

        for element in elements:
            jobPostingDetailSections = element['jobPostingDetailSection']
            for jobPostingDetailSection in jobPostingDetailSections:
                result.append(jobPostingDetailSection['howYouMatchCard'])

        result = result[0]

        feedback_data = {}

        feedback_data['headerContent'] = result['headerContent']

        match_section = {
            'title': '',
            'items': []
        }

        for item in result['howYouMatchSection']:
            
            if item.get('itemsMatchSection') is not None:
                group = item.get('itemsMatchSection')['groups'][0]

                match_section['title'] = group['header']

                for group_item in group['items']:

                    ## group_item['subtitle] = Android, Linux y Unix expected ['Android', 'Linux', 'Unix']

                    skills = group_item['subtitle'].replace(' y ', ',').replace(' ', '').split(',')

                    match_section['items'].append({
                        'title': group_item['title'],
                        'status': group_item['imageColor'],
                        'skills': skills
                    })
                break
                

        feedback_data['matchSection'] = match_section



        return Response.ok({
            'feedback_data': feedback_data
        }, "Feedback is OK")
    
    def test(self, request):

        response = LinkedinApiImpl().get('/graphql?variables=(cardSectionTypes:List(HOW_YOU_MATCH_CARD),jobPostingUrn:urn%3Ali%3Afsd_jobPosting%3A4129166449,includeSecondaryActionsV2:true)&queryId=voyagerJobsDashJobPostingDetailSections.bdbac23a4a46e498baa01dc48420f94e')
        print(response)
        return JsonResponse(response, safe=False)