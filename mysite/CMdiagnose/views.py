from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Body, Tongue, Person, Cases, Yao, Xue

class NewDetailView(generic.TemplateView):
    # https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    # model = Person
    template_name = 'CMdiagnose/newdetail.html'


class NewDetailYao(generic.TemplateView):
    
    template_name = 'CMdiagnose/newdetailyao.html'

class NewDetailXue(generic.TemplateView):
    
    template_name = 'CMdiagnose/newdetailxue.html'

class DetailView(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/detail.html'


class ResultsView(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/results.html'

class ResultsYao(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/resultsyao.html'

class ResultsXue(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/resultsxue.html'

class BootIndexView(generic.ListView):
    template_name = 'CMdiagnose/index.html'
    context_object_name = 'Person_list'
    def get_queryset(self):
        return Person.objects.all()

class IndexView(generic.ListView):
    template_name = 'CMdiagnose/index2.html'
    context_object_name = 'Person_list'
    def get_queryset(self):
        return Person.objects.all()

def tell(request, person_id):
    the_person = get_object_or_404(Person, pk=person_id)
    try:
        #envalue the Person object's body situation
        the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, Person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        caselist=Cases.objects.all()
        the_person.body.result=''
        for case in caselist:
            case.case_check(the_person.body)
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:results', args=(the_person.id,)))

def newPerson(request):
    b=Body()
    b.general=''
    b.general += request.POST['generalt']
    # b.general += request.POST['headt']
    # b.general += request.POST['wholet']
    # # b.general += request.POST['tongue_t']
    # b.general += request.POST['eyet']
    # b.general += request.POST['entt']
    # b.general += request.POST['neckt']
    # b.general += request.POST['backt']
    # b.general += request.POST['chestt']
    # b.general += request.POST['stomacht']
    # b.general += request.POST['lowerpartt']
    # b.general += request.POST['limbst']
    # b.general += request.POST['excrut']
    # b.general += request.POST['sleept']
    b.save()
    t=Tongue(body=b)

    
    #get tongue symptoms
    # t.tip += request.POST['t_tipt']
    # # t.root += request.POST['t_roott']
    # t.side += request.POST['t_sidet']
    # t.fur += request.POST['t_furt']
    # t.color += request.POST['t_colort']
    # t.moisture += request.POST['t_moisturet']
    # t.middle += request.POST['t_middlet']
    # t.bottom += request.POST['t_bottomt']
    
    # t_result=''
    # t_result=t.check_()

    #get body symptoms
    
    
    t.save()
    
    try:

        the_person = Person(body=b,tongue=t)
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        
        caselist=Cases.objects.all()
        the_person.body.result=''
        # the_person.body.result=t_result
        for case in caselist:
            case.case_check(the_person.body)
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:results', args=(the_person.id,)))

# def index(request):
#     return HttpResponse("欢迎光临笔花医镜电子诊断系统")

def newPersonExt(request):
    # b=Body()
    # b.general=''
    # b.general += request.POST['generext']

    # b.save()
    # t=Tongue(body=b)

    
    t.save()
    
    try:

        the_person=Person.objects.all()[:1].get()
        the_person.body.general=''
        the_person.body.general = request.POST['generext']
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        
        caselist=Cases.objects.all()
        the_person.body.result=''
        # the_person.body.result=t_result
        for case in caselist:
            case.case_checkext(the_person.body)

        genlist=[]
        genlist=[x.strip() for x in str(b.general).split(',')]
        genlist = [i for i in genlist if i] 
        for genele in set(genlist):
            the_person.body.result=the_person.body.result.replace(genele,'<mg>'+genele+'</mg>')
            
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()

        return HttpResponseRedirect(reverse('CMdiagnose:results', args=(the_person.id,)))




def newYao(request):
    b=Body()
    b.general=''
    b.general += request.POST['generalt']
    b.save()
    t=Tongue(body=b)

    t.save()
    
    try:

        the_person = Person(body=b,tongue=t)
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        
        yaolist=Yao.objects.all()
        the_person.body.result=''
        # the_person.body.result=t_result
        for yao in yaolist:
            yao.yao_check(the_person.body)
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:resultsy', args=(the_person.id,)))


def newYaoExt(request):
    # b=Body()
    # b.general=''
    # b.general += request.POST['generext']
    # b.save()
    # t=Tongue(body=b)

    # t.save()
    
    try:

        the_person=Person.objects.all()[:1].get()
        the_person.body.general=''
        the_person.body.general = request.POST['generext']
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        
        yaolist=Yao.objects.all()
        the_person.body.result=''
        # the_person.body.result=t_result
        for yao in yaolist:
            yao.yao_checkext(the_person.body)

        genlist=[]
        genlist=[x.strip() for x in str(b.general).split(',')]
        genlist = [i for i in genlist if i] 
        for genele in set(genlist):
            the_person.body.result=the_person.body.result.replace(genele,'<mg>'+genele+'</mg>')
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:resultsy', args=(the_person.id,)))



def newXue(request):
    # b=Body()
    # b.general=''
    # b.general += request.POST['generex']
    # b.save()
    # t=Tongue(body=b)

    # t.save()
    
    try:

        the_person=Person.objects.all()[:1].get()
        the_person.body.general=''
        the_person.body.general = request.POST['generex']
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        
        xuelist=Xue.objects.all()
        the_person.body.result=''
        # the_person.body.result=t_result
        for xue in xuelist:
            xue.xue_checkext(the_person.body)

        genlist=[]
        genlist=[x.strip() for x in str(b.general).split(',')]
        genlist = [i for i in genlist if i] 
        # print(genlist)
        for genele in set(genlist):
            the_person.body.result=the_person.body.result.replace(genele,'<mg>'+genele+'</mg>')
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:resultsxue', args=(the_person.id,)))
