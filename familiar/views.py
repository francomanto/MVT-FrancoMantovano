from familiar.models import Familiar
from django.http import HttpResponse
from django.template import loader

def create_familiar(request, name: str = "familiar", last_name: str = 'familiar', edad: int= 0, year:int=0, month:int=0, day:int= 0, ):

    template = loader.get_template("template_familiar.html")

    familiar = Familiar(name=name, last_name=last_name, edad=edad, year=year, month=month, day=day)
    familiar.save()  # save into the DB

    context_dict = {"familiar": familiar}
    render = template.render(context_dict)
    return HttpResponse(render)
