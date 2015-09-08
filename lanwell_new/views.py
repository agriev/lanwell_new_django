from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from lanwell_new.models import CompletedProject, ProjectTag
from lanwell_new.forms import CustomerForm
# Create your views here.

def index(request):

    completed = CompletedProject.objects.all()

    for project in completed:
        project.tags_list = " ".join(map(str, project.tags.all()))
    tags = ProjectTag.objects.all()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CustomerForm()
    return render(request, "lanwell_new/main.html", {'completed': completed, "tags" : tags, 'form' : form})

def upload(request):
    if request.method == "GET":
        return render(request, "lanwell_new/upload.html")
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        filename = request.POST["image"].filename
        input_file = request.POST["image"].file
        #project = CompletedProject(name,description)
        #DBSession.add(project)
        #print(project)
        #DBSession.commit()
        #file_path = os.path.join('/tmp', project.image_name())
        #with open(file_path, 'wb') as output_file:
        #    shutil.copyfileobj(input_file, output_file)
        return render_to_response ("lanwell_new/upload.html")