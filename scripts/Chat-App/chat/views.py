## This will route your views to the chatPage.html that had been created in the templates folder of the chat app.


from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chat/chatPage.html", context)
