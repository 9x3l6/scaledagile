from django.shortcuts import render



def index_views(request):
    return render(request,'training/index.html')



def SP_views(request):
    return render(request,'training/SP.html')



def form_views(request):

    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phoneNumber=request.POST['phoneNumber']
        print(name)
        print(email)
        print(phoneNumber)
        return render(request, 'training/index.html')

    else:
        return render(request,'training/formCopy.html')



def contact_views(request):
    return render(request,'training/contact.html')



def ourCourses_views(request):
    return render(request,'training/courses.html')



def leadingSAFe_views(request):
    return  render(request,'training/leadingSAFe.html')



def SAFePOPM_views(request):
    return  render(request,'training/SAFePOPM.html')



def SAFeSSM_views(request):
    return  render(request,'training/SAFeSSM.html')



def ADSAFeSSM_views(request):
    return  render(request,'training/ADSAFeSSM.html')



def SAFeDevOps_views(request):
    return  render(request,'training/SAFeDevOps.html')



def about_views(request):
    return render(request,'training/about-1.html')



def privacy_views(request):
    return render(request,'training/privacy.html')



def policies_views(request):
    return render(request,'training/policies.html')



def faq_views(request):
    return render(request,'training/faq-1.html')



def slug_views(request,slug):
    return render(request,'training/error-404.html')
