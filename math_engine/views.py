import json, datetime

from django.views.generic import View
from django.core import serializers

from braces.views import JSONResponseMixin

from .models import MathRequest

class AjaxMixin(JSONResponseMixin):

    def error(self, msg="not a valid request"):
        response = {
            "result": "ERROR: %s" % msg
        }
        return self.render_json_response(response)


class MathView(AjaxMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if not request.method.lower() in [u'get', u'post']:
            return self.http_method_not_allowed(request, *args, **kwargs) 
        values = request.REQUEST.get("values", None)
        if not values:
            return self.error()
        if len(values)>=256: 
            return self.error("c'mon, really? that's far too long")
        try: values = json.loads(values)
        except: return self.error("could not decode parameter")
        total = 0
        prod = 1
        for val in values:
            try:
                total += int(val)
                prod *= int(val)
            except:
                return self.error("only accepts integers")
        MathRequest.objects.create(
            ip = request.META.get("REMOTE_ADDR", 0),
            values = json.dumps(values),
            sum = total,
            product = prod
        ) 
        return self.render_json_response({"sum": total, "product": prod}) 


class HxView(AjaxMixin, View):

    def get(self, request, *args, **kwargs):
        zero = datetime.datetime(2000, 1, 1)
        since = request.GET.get("since", zero)
        try:
            queryset = MathRequest.objects.filter(timestamp__gt=since)
        except:
            return self.error("time must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format") 
        response = []
        for obj in queryset:
            json_obj = {
                "ip": obj.ip,
                "timestamp": obj.timestamp,
                "values": obj.values,
                "sum": obj.sum,
                "product": obj.product
            } 
            response.append(json_obj)
        return self.render_json_response(response)
