from django.shortcuts import render

from contact.models import Contact


def index(request):
    context = {
        'contacts': Contact.objects.all()
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context
    )
