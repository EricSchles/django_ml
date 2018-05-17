from django.shortcuts import render
from model_store.models import TrainedModels
import pickle

# Create your views here.
def index(request):
    model_name = request.GET.get('model_name', '')
    data = request.GET.get('data', '')
    if model_name != '' and data != '':
        model = TrainedModels.objects.filter(model_name=model_name)
        model = pickle.load(model.pickled_model)
        try:
            result = model.predict(data)
            response_data = {
                "result": result,
                "model_name": model_name
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        except:
            print("unimplemented!!")
    return HttpResponse("Some Weird Error Occurred, oops")
