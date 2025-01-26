from ..linkedinApi import LinkedinApi
from fake_useragent import UserAgent
import requests

ua = UserAgent()

class LinkedinApiImpl(LinkedinApi):
    csrf_token = 'ajax:0629183763095008969'
    base_url = 'https://www.linkedin.com/voyager/api'
    cookie = f'bscookie="v=1&2024030514462291eda998-8161-40aa-8f25-0042c3497584AQG1Tc8-EUoEUeXP9ISwnpxi9Uf9T6kK"; g_state={"i_l":0}; timezone=America/Lima; li_theme=light; li_theme_set=app; bcookie="v=2&1c4de75f-cd3e-4f2d-8ff0-9e30f92950c2"; dfpfpt=e68ae134e8f44728b4bae6cd7c7e9dcf; li_rm=AQGUD24eu5vX9AAAAY8bS6gL55ol2F05fbrkmiWmg_sP4suf_WrQ508oRMq3qWE_L0heNapeo-Ga0bC95hVi6xHXXRmSmDTgRvJsQsz8jH4aTQhAn_vKbz0vGnJSC646Xtw42P1ySxpY_MR3TWgTA2p8B_RvVBBztL_VKa_YN4gYJRYo4WBJ9etvvklMHlZfjoFGaTOlaDcYwaDhZZ_brlKDnk2LZaVj-rvibL8Q-Y7BtRk2S9bvNozflHNI9Le7U4HgmCCoEBui2bAYdKWx3ibKBE98961uRr97SNPRWRwtK0kNry7X6nZhV0h9AkEab2dtervA-rLU28pzk6o; visit=v=1&M; li_sugr=92e7752f-158b-4efd-8880-5ea36327126f; _guid=c8b40c70-90a5-4b09-b54d-4d4e11f4be15; aam_uuid=83529637676287465070865943487562445131; JSESSIONID="ajax:0629183763095008969"; liap=true; _gcl_au=1.1.2033789675.1731710365.1605866843.1737326734.1737326741; li_at=AQEDATDRnnMCSjyoAAABlGrO2nUAAAGUsuj6rk4AZU3orJ_VXarBS0O82hUYZ_KZ3J3hJ308Mq5wRRSFJEvKMxHAJ4TIAA0uHZsJF8De-zrSUaEDy0gE-Wf_JTDNlF7D9LTigNqSvmyTtasthS2K4r6Y; fid=AQH6ql0caALG_QAAAZSO_yGgtugtPvG1oGeEHjgnNoYqhS6UZcPEHLlsqha9jI1ShZtLDfhQYECJ3w; UserMatchHistory=AQL8DgSyX2kzVwAAAZSQIZFMWCuXWYSiDyZDuFaTIOZwIL3MBHIWzE9F67h0BZFMzrUjvYBwHeHWe5TvM3UIjmVkWKrn7ZDIVzWYJFuqompdtblfCoYviOAa4gCqAIQj0NK20NyVIZzY3MWupe_ecBP5ev9hEsWOBOHZNa3KtI3LifvF-diZVWWvaMYwyE3JYxkLUhS1En7-ny_-ErVats3zSoU4opa5nDWHhr5hs4AjQY2qd83BMCGSkRk3g8Gtt-vvk5laodK73tiXVDdSPTEmHH2PjP6cRe0M9GEvofCT2LyqrjCMblBzCLCpqlNmHPqQ2W_86X1OvNl7bRwP5ZxhYQkjerCitBJyaKDQTHMKbVAjsg; AnalyticsSyncHistory=AQI8hLjtmSujCQAAAZSQIZFM5La4VFUZ4xVFMzskIXhqbb1kMGRndzHMbZwwSMTcLShR3H2LdK6BnPJ-0AITxA; lms_ads=AQENk8D72rVlOwAAAZSQIZMsenUhNhwyDTNwLdV-yQCGSRyYTvdRlInerIrbK_BzcGxFZV-EBQY0TYpfCe-IStQiaUzqy2DQ; lms_analytics=AQENk8D72rVlOwAAAZSQIZMsenUhNhwyDTNwLdV-yQCGSRyYTvdRlInerIrbK_BzcGxFZV-EBQY0TYpfCe-IStQiaUzqy2DQ; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; lang="v=2&lang=es-es"; fptctx2=taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1qvSTt3gVsAHifKPNeV3CVqBGpbqBKpLR7wmMGuD67GXHu%252fcEakzk1BaHkRC%252ftH8Z0XYkkT9T0dN1CklPl%252bRV5pnon1uOJtDPpiin7ZQbVf4p0OX80ufdJNNHIrdvydfd1yXv5FCuzAiYFsiTSVtoTBtvravF1E3MHTBG7xAJxDV5yT7GjgmVaXo%252fN7vKmXrO%252bYxkrtOjHUUBA%252b9EFc2baGKPXdtq8DV4aLzO0fq1Og4xAa6V77wOeq8bjHXgMjYrwyEHyU0PYO%252b8IA0qkcUWyMHb43VhAvZganmStrOxv2iaVaiqhBHe%252fKjQWPmqkrVk%253d; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20112%7CMCMID%7C82969317462315327360921931975173472896%7CMCAAMLH-1738340784%7C4%7CMCAAMB-1738340784%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1737743184s%7CNONE%7CMCCIDH%7C1135557743%7CvVersion%7C5.1.1; __cf_bm=VQLjfKFWkql2qJkPZ0IqNQZ2XihR3s1Bd8M.lWfvBmc-1737739182-1.0.1.1-sE3k.McEZ2pyBsjBH9DxKlpNUsWf4vMbWSpO8uwNAp17.eUMAs2x1kioJHg4oySFfECe9CYqPqltBiFZ7Ast5g; lidc="b=TB55:s=T:r=T:a=T:p=T:g=4337:u=1201:x=1:i=1737739553:t=1737804381:v=2:sig=AQEDMEJF5Jz2eklbEC3sS4VmeVD9VtcP"'

    def get(self, url):
        url_final = f'{self.base_url}{url}'
        headers = self._get_headers()
        response = requests.get(url_final, headers=headers)


        if response.status_code != 200:
            return None
        
        return response.json()
    
    def _get_headers(self):
        return {
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'x-li-lang': 'es_ES',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': ua.random,
            'x-li-page-instance': 'urn:li:page:d_flagship3_search_srp_jobs;58HOA6vVTEiIG7tAg5NMDg==',
            'csrf-token': self.csrf_token,
            'x-li-track': '{"clientVersion":"1.13.29432","mpVersion":"1.13.29432","osName":"web","timezoneOffset":-5,"timezone":"America/Lima","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
            'x-restli-protocol-version': '2.0.0',
            'x-li-deco-include-micro-schema': 'true',
            'x-li-pem-metadata': 'Voyager - Careers - Job Details=job-posting',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Linux"',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Cookie': self.cookie,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.linkedin.com/jobs',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',

        }