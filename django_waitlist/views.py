from django.shortcuts import render

from django_waitlist.forms import UserForm

def sign_up(request):
    is_registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            is_registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    context = {'is_registered': is_registered, 'user_form': user_form}

    return render(request, 'registration/register.html', context)
