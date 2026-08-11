import dlt
import requests
from config import get_headers,ENDPOINTS


#TODO: dlt

def make_resource(name,url):
    
    @dlt.resource(name=name,write_disposition='replace')
    def _resource():
        data = requests.get(url,headers=get_headers())
        data.raise_for_status()
        yield data.json()[name]

    return _resource

@dlt.source(name='smartup')
def smartup_source():
    return [make_resource(name,url) for name,url in ENDPOINTS.items()]

pipline = dlt.pipeline(
    pipeline_name="smartup_elt",
    destination="postgres",
    dataset_name="smartup_dataset_elt"
)

log_info = pipline.run(smartup_source())      