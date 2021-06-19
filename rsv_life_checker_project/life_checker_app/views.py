from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return (render(
            request,
            'frm.html'))


def check(request):

    table_osmotry = open("./life_checker_app/templates/table_templates/1_table_osmotry_template.txt", "r").read()
    table_labmet = open("./life_checker_app/templates/table_templates/1_table_lab_met_issled_template.txt", "r").read()
    table_instr_metody = open("./life_checker_app/templates/table_templates/1_table_instr_met_issled_template.txt", "r").read()
    table_innye_metody = open("./life_checker_app/templates/table_templates/1_table_innye_met_issled_template.txt", "r").read()
    table_learstv = open("./life_checker_app/templates/table_templates/table_lekarstv_template.txt", "r").read()


    print('Получен запрос', request.method)
    if request.method == 'GET':
        return (render(
            request,
            'index.html', {
                'table_osmotry': table_osmotry,
                'table_labmet': table_labmet,
                'table_instr_metody': table_instr_metody,
                'table_innye_metody': table_innye_metody,
                'table_learstv': table_learstv,}))
    elif request.method == 'POST':
        print('Получен запрос ПОСТ', request.POST)
        return (render(
            request,
            'index.html', {
                'table_osmotry': table_osmotry,
                'table_labmet': table_labmet,
                'table_instr_metody': table_instr_metody,
                'table_innye_metody': table_innye_metody,
                'table_learstv': table_learstv,}))
                
def check_2(request):

    table_osmotry = open("./life_checker_app/templates/table_templates/1_table_osmotry_template.txt", "r").read()
    table_labmet = open("./life_checker_app/templates/table_templates/1_table_lab_met_issled_template.txt", "r").read()
    table_instr_metody = open("./life_checker_app/templates/table_templates/1_table_instr_met_issled_template.txt", "r").read()
    table_innye_metody = open("./life_checker_app/templates/table_templates/1_table_innye_met_issled_template.txt", "r").read()
    table_learstv = open("./life_checker_app/templates/table_templates/table_lekarstv_template.txt", "r").read()


    print('Получен запрос', request.method)
    if request.method == 'GET':
        return (render(
            request,
            'index_sl.html', {
                'table_osmotry': table_osmotry,
                'table_labmet': table_labmet,
                'table_instr_metody': table_instr_metody,
                'table_innye_metody': table_innye_metody,
                'table_learstv': table_learstv,}))
    elif request.method == 'POST':
        print('Получен запрос ПОСТ', request.POST)
        return (render(
            request,
            'index_sl.html', {
                'table_osmotry': table_osmotry,
                'table_labmet': table_labmet,
                'table_instr_metody': table_instr_metody,
                'table_innye_metody': table_innye_metody,
                'table_learstv': table_learstv,}))


def testcall(request):
   #Get the variable text
   text = request.POST['text']
   print(text)
   #Do whatever with the input variable text
   response = text + ":)"
   #Send the response 

   return HttpResponse(222)
   
   



from .forms import InputForm
  
# Create your views here.
def home_view(request):
    context= InputForm()
    return render(request, "frm.html", {'context':context})