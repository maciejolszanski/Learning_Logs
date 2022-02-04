from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def register(request):
    '''Registering the nuew user'''

    if request.method != 'POST':
        # Not POST so probably GET - create empty form
        form = UserCreationForm()
    else:
        # POST, so save the registration data
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            new_user = form.save()
            # Log the user in
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display the empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)