from datetime import datetime


def jobAdapter(job, country: str):
    
    jobCardUnion = job['jobCardUnion']
    jobPostingCard = jobCardUnion['jobPostingCard']

    title = jobPostingCard['title']

    primaryDescription = jobPostingCard['primaryDescription']

    jobPosting = jobPostingCard['jobPosting']

    secondaryDescription = jobPostingCard['secondaryDescription']

    jobSeekerJobState = jobPostingCard['jobSeekerJobState']


    location = secondaryDescription['text']

    modality = location.split('(')[1].replace(')', '')

    ubigeo = location.split('(')[0].strip()

    logoData = jobPostingCard['logo']

    logo_url = ''

    try:
        for logo_attribute in logoData['attributes']:
            if logo_attribute['detailData']['companyLogo']['logo']['vectorImage'] is None:
                continue

            logoDetailData = logo_attribute['detailData']['companyLogo']['logo']['vectorImage']
            artifacts = logoDetailData['artifacts']

            baseUrlLogo = logoDetailData['rootUrl']

            for artifact in artifacts:
                logo_url = baseUrlLogo + artifact['fileIdentifyingUrlPathSegment']  
    except Exception as e:
        print('Error al conseguir imagen:', e)

    post_id = jobPosting['entityUrn'].split(':')[-1]

    is_applied = False

    status = 'NOT_VIEWED'


    indexStateAction = -1

    for stateAction in jobSeekerJobState['jobSeekerJobStateActions']:
        indexStateAction += 1

        if indexStateAction == 0:
            status = stateAction['jobSeekerJobStateEnums']

        if stateAction['jobSeekerJobStateEnums'] == 'APPLIED':
            is_applied = True
            break

    timeResponse = None

    if jobPostingCard.get('relevanceInsight') is not None:
        timeResponse = jobPostingCard['relevanceInsight']['text']['text']

    applicationType = 'Solicitar en el sitio web'

    listedDate = None

    for footerItem in jobPostingCard['footerItems']:
        if footerItem['type'] == 'EASY_APPLY_TEXT':
            applicationType = footerItem['text']['text']

        if footerItem['type'] == 'LISTED_DATE':
            listedDate = footerItem['timeAt']
            listedDate = datetime.fromtimestamp(listedDate / 1000)

    return {
        'post_id': post_id,
        'title': title['text'].strip(),
        'company_name': primaryDescription['text'].strip(),
        'modality': modality,
        'ubigeo': ubigeo,
        'country': country,
        'logo_url': logo_url,
        'url': f'https://www.linkedin.com/jobs/view/{post_id}',
        'reposted': jobPosting['repostedJob'],
        'is_applied': is_applied,
        'status': status,
        'time_response': timeResponse,
        'application_type': applicationType,
        'listed_date': listedDate
    }