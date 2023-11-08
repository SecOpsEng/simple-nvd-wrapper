from nvd_rest.CoreObjects.Session import Session

class CVE:
    def __init__(self, api_key):
        self.session = Session(api_key)
        self.base_endpoint = '/cves/2.0'

    def search(self, filters={}):
        def build_filter_string(filters={}):
            # Validate filters
            if filters == {}:
                return ""
            # Build filter string once filters are validated
            else:
                filter_string = "?"
                for filter in filters.keys():
                    if filter_string == "?":
                        filter_string += "{}={}".format(filter, filters[filter])
                    else:
                        filter_string += "&{}={}".format(filter, filters[filter])
                        print(filter_string)
                return filter_string
        #Send request
        response = self.session.get(self.base_endpoint + build_filter_string(filters))
        return response

class Report:
    def __init__(self, cve, filters={}, columns=['id','sourceIdentifier','published','lastModified','vulnStatus','descriptions','metrics','weaknesses','configurations','references']):
        if isinstance(cve, CVE) == False:
            self = None
            print("Invalid CVE object.")
        else:
            results = cve.search(filters)
            self.contents = []
            for result in results['vulnerabilities']:
                result = {column:result['cve'][column] for column in columns}
                if 'descriptions' in columns:
                    result['descriptions'] = [description['value'] for description in result['descriptions']]
                self.contents.append(result)
