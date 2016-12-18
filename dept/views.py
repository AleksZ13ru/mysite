from django.shortcuts import render


def dept_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'dept/dept_list.html')
