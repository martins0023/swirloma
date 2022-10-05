from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import HomePost, Message, SwirlInfo, ProjectPost
from .forms import contact_me
from django.contrib import messages


#class Home(ListView):
#    model = HomePost
#    template_name = 'home/home.html'
#    context_object_name = 'homes'
    #ordering = ['-date_posted']
    #paginate_by = 1
    
    
        
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['title'] = 'swirloma'
    #    context['home'] = HomePost.objects.all()
    #    context['message'] = Message.objects.all()
    #    return context
    
def home(request):
    if request.method == 'POST':
        form = contact_me(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your message has been sent successfully, we\'ll get back to you asap with the info provided. Thanks !')
            return redirect('home')
    else:
        form = contact_me()
        
    context = {
        'form': form,
        'title': 'swirloma',
        'homes': HomePost.objects.all(),
        'infos': SwirlInfo.objects.all(),
        'projects': ProjectPost.objects.all()
    } 
    return render(request, 'home/home.html', context)