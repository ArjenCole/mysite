from django.core import serializers
from django.http import JsonResponse
import json


def dicTojson(dic):
    return json.dumps(dic)



def modelsToJson(models):
    json_data = serializers.serialize('json', models)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
