from django.core import serializers
import json


def strToJson(string):
    return json.loads(string)


def dicToJson(dic):
    return json.dumps(dic)


def modelsToJson(models):
    json_data = serializers.serialize('json', models)
    return json.loads(json_data)
    # return JsonResponse(json_data, safe=False)
