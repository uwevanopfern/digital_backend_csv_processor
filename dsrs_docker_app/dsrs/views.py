from rest_framework import viewsets

from . import models, serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from json import JSONEncoder
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


class DSRViewSet(viewsets.ModelViewSet):
    queryset = models.DSR.objects.all()
    serializer_class = serializers.DSRSerializer


@csrf_exempt
@api_view(["GET"])
def resource_percentile(request, number):

    # TODO - Refactor code, reduce dups and apply decoupling pattern, deadline got me thats why i didnt refactor this function

    territory = request.query_params.get("territory")
    period_start = request.query_params.get("period_start")
    period_end = request.query_params.get("period_end")

    if not 1 <= number <= 100:
        error_data = {
            "error": True,
            "message": "Number should be in range of 1 - 100",
            "REASON": "NUMBER_OUT_OF_RANGE",
        }
        return JsonResponse(error_data, status=400)
    else:
        resources = models.Resource.objects.all()
        if territory and period_start and period_end:
            if territory == "GB":
                resources = resources.filter(dsrs__territory__code_2=territory)
                resources = resources.filter(
                    dsrs__period_start__gte=period_start,
                    dsrs__period_end__lte=period_end,
                )
                data = []
                for resource in resources:
                    revenue = resource.revenue * number / 100
                    item = {
                        "id": resource.id,
                        "dsp_id": resource.dsp_id,
                        "title": resource.title,
                        "artists": resource.artists,
                        "isrc": resource.isrc,
                        "usages": resource.usages,
                        "revenue": revenue * 1.17,  # Convert GB to Euro
                        "dsrs": resource.dsrs,
                    }
                    data.append(item)
                serializer = serializers.ResourceSerializer(data, many=True)
                return JsonResponse({"items": serializer.data}, status=200)
            elif territory == "CHF":
                resources = resources.filter(dsrs__territory__code_2=territory)
                resources = resources.filter(
                    dsrs__period_start__gte=period_start,
                    dsrs__period_end__lte=period_end,
                )
                data = []
                for resource in resources:
                    revenue = resource.revenue * number / 100
                    item = {
                        "id": resource.id,
                        "dsp_id": resource.dsp_id,
                        "title": resource.title,
                        "artists": resource.artists,
                        "isrc": resource.isrc,
                        "usages": resource.usages,
                        "revenue": revenue * 0.90,  # Convert Swiss Franc to Euro
                        "dsrs": resource.dsrs,
                    }
                    data.append(item)
                serializer = serializers.ResourceSerializer(data, many=True)
                return JsonResponse({"items": serializer.data}, status=200)
            elif territory == "NO":
                resources = resources.filter(dsrs__territory__code_2=territory)
                resources = resources.filter(
                    dsrs__period_start__gte=period_start,
                    dsrs__period_end__lte=period_end,
                )
                data = []
                for resource in resources:
                    revenue = resource.revenue * number / 100
                    item = {
                        "id": resource.id,
                        "dsp_id": resource.dsp_id,
                        "title": resource.title,
                        "artists": resource.artists,
                        "isrc": resource.isrc,
                        "usages": resource.usages,
                        "revenue": revenue * 0.098,  # Convert Norwegian Krone to Euro
                        "dsrs": resource.dsrs,
                    }
                    data.append(item)
                serializer = serializers.ResourceSerializer(data, many=True)
                return JsonResponse({"items": serializer.data}, status=200)
            else:
                # By default it is a Spain and it is Euro
                resources = resources.filter(dsrs__territory__code_2=territory)
                resources = resources.filter(
                    dsrs__period_start__gte=period_start,
                    dsrs__period_end__lte=period_end,
                )
                data = []
                for resource in resources:
                    revenue = resource.revenue * number / 100
                    item = {
                        "id": resource.id,
                        "dsp_id": resource.dsp_id,
                        "title": resource.title,
                        "artists": resource.artists,
                        "isrc": resource.isrc,
                        "usages": resource.usages,
                        "revenue": revenue,  # Nothing to convert coz its Spain and By default it is EURO
                        "dsrs": resource.dsrs,
                    }
                    data.append(item)
                serializer = serializers.ResourceSerializer(data, many=True)
                return JsonResponse({"items": serializer.data}, status=200)
        else:
            error_data = {
                "error": True,
                "message": "Query params missing, make sure you provide, territory, period_start, period_end",
                "REASON": "QUERY_PARAMS_MISSING",
            }
            return JsonResponse(error_data, status=400)
