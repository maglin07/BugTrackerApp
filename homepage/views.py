from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from customuser.models import CustomUser
from customuser.forms import LoginForm, CustomUserCreationForm

from homepage.models import TicketModel
from homepage.forms import TicketForm


# Create your views here.
@login_required(login_url='loginview')
def home(request):
    tickets = TicketModel.objects.all()
    new = TicketModel.objects.filter(status='New')
    inprogess = TicketModel.objects.filter(status='In Progress')
    done = TicketModel.objects.filter(status='Done')
    invalid = TicketModel.objects.filter(status='Invalid')

    return render(request, 'home.html', {
        'tickets': tickets,
        'new': new,
        'inprogress': inprogess,
        'done': done,
        'invalid': invalid})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


@login_required(login_url='loginview')
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = CustomUser.objects.create_user(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_form.html', {'form': form})


@login_required(login_url='loginview')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='loginview')
def ticket_submission_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_submit = request.user
            TicketModel.objects.create(
                title=data['title'],
                description=data['description'],
                ticket_submitted=user_submit,
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, 'ticket_submission.html', {'form': form})


@login_required(login_url='loginview')
def ticket_detail_view(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


@login_required(login_url='loginview')
def user_detail_view(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    ticket = TicketModel.objects.get(id=user_id)
    submitted = TicketModel.objects.filter(ticket_submitted=user_id)
    assigned = TicketModel.objects.filter(ticket_assigned=user_id)
    completed = TicketModel.objects.filter(ticket_completed=user_id)

    return render(request, 'user_detail.html', {
        'user': user,
        'ticket': ticket,
        'submitted': submitted,
        'assigned': assigned,
        'completed': completed,
    })


@login_required(login_url='loginview')
def edit_ticket_view(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
        return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))

    form = TicketForm(initial={
        'title': ticket.title,
        'description': ticket.description,
    })
    return render(request, 'edit_ticket.html', {'form': form})


@login_required(login_url='loginview')
def assigned_to(request, id):
    ticket = TicketModel.objects.get(id=id)
    ticket.status = 'In Progress'
    ticket.ticket_assigned = request.user
    ticket.ticket_completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))


@login_required(login_url='loginview')
def completed_by(request, id):
    ticket = TicketModel.objects.get(id=id)
    ticket.status = "Done"
    ticket.ticket_assigned = None
    ticket.ticket_completed = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))


@login_required(login_url='loginview')
def mark_invaild(request, id):
    ticket = TicketModel.objects.get(id=id)
    ticket.status = "Invalid"
    ticket.ticket_completed = None
    ticket.ticket_assigned = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))
