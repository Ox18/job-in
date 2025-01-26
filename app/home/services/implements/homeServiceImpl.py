from ..homeService import HomeService
from django.urls import get_resolver

class HomeServiceImpl(HomeService):
    def getRoutes(self):
        urlconf = get_resolver()
        routes = self._extract_routes(urlconf.url_patterns)
        return routes
    
    def _extract_routes(self, url_patterns, prefix=""):
        routes = []
        for pattern in url_patterns:
            if hasattr(pattern, "url_patterns"):
                routes += self._extract_routes(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                routes.append({
                    "pattern": prefix + str(pattern.pattern),
                    "name": pattern.name
                })
        return routes