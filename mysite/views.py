from django.http import HttpResponse, Http404, HttpResponseRedirect
from mysite.models import Book, Content, RContent, Center, JoinMe, Activities, User
from django.shortcuts import render_to_response
from django.core.mail import send_mail, EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from mysite.forms import ContactForm
import datetime
from django.template import loader
# Create your views here.


def my_homepage_view(request):
    '''ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    ud = request.META.get('REMOTE_ADDR', 'unknown')
    return HttpResponse("Home page!Your browser is %s %s" % (ua, ud))'''
    contents = Content.objects.filter(status=1)
    rcontents = RContent.objects.filter(status=1)
    center = Center.objects.filter(status=1)
    return render_to_response('index.html', {'contents': contents, 'rcontents': rcontents, 'center': center})


@csrf_exempt
def join(request):
    JoinMe.objects.create(fullname=request.POST['fullname'], email=request.POST['email'], myclass=request.POST['myclass'],
                         project=request.POST['project'], describe=request.POST['describe'], status='1')

    return render_to_response('thanks.html')


@csrf_exempt
def joinform(request):
    ac = Activities.objects.filter(status=1)
    return render_to_response('baoming.html', {'ac': ac})


def registerform(request):
    return render_to_response('register.html')


@csrf_exempt
def register(request):
    User.objects.create(fullname=request.POST['fullname'], username=request.POST['username'], password=request.POST['password'], email=request.POST['email'],
                         num=request.POST['num'], describe=request.POST['describe'], myactivities_id='')
    return render_to_response('register1.html')


def joindetail(request):
    j = JoinMe.objects.filter(status=1)
    return render_to_response('joindetail.html', {'j': j})


@csrf_exempt
def login(request):
    u = User.objects.get(username=request.POST['username'])
    if u.password == request.POST['password']:
        ac = Activities.objects.filter(status=1)
        jm = JoinMe.objects.filter(fullname=u.fullname)
        return render_to_response('home.html', {'u': u, 'ac': ac, 'jm': jm})
    else:
        return render_to_response('login.html')


def loginform(request):

    return render_to_response('login.html')


def homeform(request):

    return render_to_response('home.html')


def search(request):
    errors = []
    if 'fullname' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                      {'books': books, 'query': q})

    return render_to_response('thanks.html')


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'],
                      cd['message'],
                      '654543782@qq.com',
                      [cd['email']],
                      fail_silently=False
            )
            return render_to_response('thanks.html')
    else:
            form = ContactForm(
                initial={'subject': 'I love your site!'}
            )
    return render_to_response('contact_form.html', {'form': form})


@csrf_exempt
def contactus(request):
    if request.method == 'POST':
        subject, from_email, to = request.POST['subject'], '654543782@qq.com', 'shuilikexie@163.com'
        html_content = request.POST['fromemail'] + "  " + request.POST['content']
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render_to_response('sendfeedback.html')
    else:
        return render_to_response('contactus.html')


def hello(request):
    return HttpResponse("Hello world!")


def current_time(request):
    current_time = datetime.datetime.now()
    return render_to_response("current_datetime.html", locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render_to_response("main/plus.html", locals())


def all_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


