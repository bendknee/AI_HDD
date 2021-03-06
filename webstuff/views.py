from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webstuff.hddmlformula import train, ask
from webstuff.preprocessor import gather_data

from .forms import HeartForm


def index(request):
	return render(request, 'index.html', {'form': HeartForm})


@csrf_exempt
def calculate(request):
	query = request.POST['age'] + "," + request.POST['sex'] + "," + request.POST['cp'] + "," + request.POST['trestbps'] + "," + request.POST['chol'] + "," + request.POST['fbs'] + "," + request.POST['restecg'] + "," + request.POST['thalach'] + "," + request.POST['exang'] + "," + request.POST['oldpeak'] + "," + request.POST['slope'] + "," + request.POST['ca'] + "," + request.POST['thal']
	name = request.POST['name']
	dataset = gather_data()
	training = train(dataset)
	tree = training[0]
	accuracy = training[1]
	precision = training[2]
	recall = training[3]
	result = ask(query, tree)
	#if 'dataset' not in request.session:
	#	dataset = gather_data()
	#	request.session['dataset'] = dataset
	#else:
	#	dataset = request.session['dataset']

	#if 'tree' not in request.session:
	#	training = train(dataset)
	#	tree = training[0]
	#	print(type(tree))
	#	accuracy = training[1]
	#	precision = training[2]
	#	request.session['tree'] = tree
	#	request.session['accu'] = accuracy
	#	request.session['prec'] = precision
	#	request.session['recall'] = recall
	#else:
	#	tree = request.session['tree']
	#	#print(type(tree))
	#	accuracy = request.session['accu']
	#	precision = request.session['prec']
	#	recall = request.session['recall']
	#request.session.set_expiry(60)  # Tree data Expires in 1 minute
	#print(tree)
	#result = ask(query, tree)


	return JsonResponse({'name': name, 'result': result, 'accuracy': accuracy, 'precision' : precision, 'recall' : recall})
