from django.views.generic.edit import CreateView
from .models import blog 



class blogCreateView(CreateView):
	model = blog
	fields = [
		"title ",
		"description"
	]
	template_name = "index.html"
