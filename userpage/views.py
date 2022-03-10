from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import hashlib
from .models import User, Post, Comment, Friendlink


def index(request):
    return render(request, 'userpage/index.html')

def newacc(request):
    if(request.POST['newname'] != ""):
        try:
            u = User.objects.get(request.POST['newname'])
        except:
            passstr = request.POST['newpass']
            bypass = bytes(passstr, 'utf-8')
            hashpass = hashlib.sha256(bypass).hexdigest()
            u = User(user_name=request.POST['newname'], password = hashpass, start_date=timezone.now())
            u.save()
            html = HttpResponseRedirect(reverse('page', args=(u.id,))) 
            html.set_cookie('user_cookie', u.id)
            return html
        return HttpResponse("account already exists") 
    else:
        return HttpResponse("please enter a name when creating an account") 

def signin(request):
    if(request.POST['username'] != ""):
        name = request.POST['username']
        passstr = request.POST['password']
        bypass = bytes(passstr, 'utf-8')
        hashpass = hashlib.sha256(bypass).hexdigest()
        try:
            u = get_object_or_404(User, user_name = name)
        except:
            return HttpResponse("Account does not exist")
        if(u.password == hashpass):
            html = HttpResponseRedirect(reverse('page', args=(u.id,))) 
            html.set_cookie('user_cookie', u.id)
            return html
        else:
            return HttpResponse("Incorrect Password")
    else:
        return HttpResponse("please enter a name when creating an account")

def post(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    new_text = request.POST['text_input']
    p = u.post_set.create(post_text = new_text, op=u.user_name, pub_date=timezone.now(), src=1, share=0)
    p.src = p.id
    p.save()
    return HttpResponseRedirect(reverse('page', args=(user_id,))) 

def page(request, user_id):
    try:
        user = get_object_or_404(User, pk=request.COOKIES.get('user_cookie')) 
    except:
        user = 1
    page = get_object_or_404(User, pk=user_id)
    post_list = page.post_set.order_by('-pub_date')[:10]
    friend_request_get = page.user_get.filter(accepted = False)
    friend_request_send = page.user_send.filter(accepted = False)
    friend_get = page.user_get.filter(accepted = True)
    friend_send = page.user_send.filter(accepted = True)
    try:
        f = Friendlink.objects.filter(sender = user).get(receiver = page)
        friendstat = "True"
    except:
        try:
            f = Friendlink.objects.filter(sender = page).get(receiver = user)
            friendstat = "True"
        except:
            friendstat = "False"
    return render(request, 'userpage/page.html', {'page':page, 'user':user, 'post_list':post_list, 'friend_request_get':friend_request_get, 'friend_request_send':friend_request_send, 'friend_get':friend_get, 'friend_send':friend_send, 'friendstat':friendstat})

def search(request):
    try:
        page = get_object_or_404(User, user_name=request.POST['search'])
    except:
        return HttpResponse("page does not exist")
    return HttpResponseRedirect(reverse('page', args=(page.id,))) 

def comment_page(request, post_id):
    user = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
    post = get_object_or_404(Post, pk=post_id)
    page = get_object_or_404(User, pk=post.user.id)
    friend_request_get = page.user_get.filter(accepted = False)
    friend_request_send = page.user_send.filter(accepted = False)
    friend_get = page.user_get.filter(accepted = True)
    friend_send = page.user_send.filter(accepted = True)
    try:
        f = Friendlink.objects.filter(sender = user).get(receiver = page)
        friendstat = "True"
    except:
        try:
            f = Friendlink.objects.filter(sender = page).get(receiver = user)
            friendstat = "True"
        except:
            friendstat = "False"
    return render(request, 'userpage/post.html', {'page':page, 'post':post, 'user':user, 'friend_request_get':friend_request_get, 'friend_request_send':friend_request_send, 'friend_get':friend_get, 'friend_send':friend_send, 'friendstat':friendstat}) 

def comment_post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    new_text = request.POST['text_input']
    p.comment_set.create(user = get_object_or_404(User, pk=request.COOKIES.get('user_cookie')), comment_text = new_text)
    return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))  

def share(request, post_id):
    user = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
    post = get_object_or_404(Post, pk=post_id)
    try:
        user.share_set.get(post=post)
    except:
        share = user.post_set.create(post_text = post.post_text, op=post.user.user_name, src=post.id, pub_date=timezone.now(), share=1)
    return HttpResponseRedirect(reverse('page', args=(user.id,)))
  
def friend(request, user_id):
    try:
        u1 = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
        u2 = get_object_or_404(User, pk=user_id)
        try:
            f = Friendlink.objects.filter(sender = u1).get(receiver = u2)
            f.delete()
            return HttpResponseRedirect(reverse('page', args=(u1.id,)))
        except:
            try:
                f = Friendlink.objects.filter(sender = u2).get(receiver = u1)
                if f.accepted:
                    f.delete()
                    return HttpResponseRedirect(reverse('page', args=(u1.id,)))
                else:
                    if request.POST['friend'] == "1":
                        f.delete()
                        return HttpResponseRedirect(reverse('page', args=(u1.id,)))
                    elif request.POST['friend'] == "0":
                        f.accepted = True
                        f.save()
                        return HttpResponseRedirect(reverse('page', args=(u1.id,)))
                    else:
                        f.delete()
                        return HttpResponseRedirect(reverse('page', args=(u1.id,)))
            except:
                Friendlink.objects.create( sender = u1, receiver = u2 )
                return HttpResponseRedirect(reverse('page', args=(u1.id,)))
    except:
        return HttpResponse('uncaught exception')
            
            

def mesg(request, user_id):
    return HttpResponse('message')

def edit(request, post_id):
    if(request.POST['edit'] == "0"):
        p = get_object_or_404(Post, pk=post_id)
        p.post_text = request.POST['text_input']
        p.save()
        return HttpResponseRedirect(reverse('page', args=(p.user.id,)))
    elif(request.POST['edit'] == "1"):
        p = get_object_or_404(Post, pk=post_id)
        p.post_text = request.POST['text_input']
        p.save()
        return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))
    elif(request.POST['edit'] == "2"):
        c = get_object_or_404(Comment, pk=post_id)
        c.comment_text = request.POST['text_input']
        c.save()
        return HttpResponseRedirect(reverse('comment_page', args=(c.post.id,)))
    else:
        return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))

def delete(request, post_id):
    if(request.POST['del'] == "0"):
        p = get_object_or_404(Post, pk=post_id)
        p.delete()
        return HttpResponseRedirect(reverse('page', args=(p.user.id,)))
    elif(request.POST['del'] == "1"):
        p = get_object_or_404(Post, pk=post_id)
        p.delete()
        return HttpResponseRedirect(reverse('page', args=(p.user.id,)))
    elif(request.POST['del'] == "2"):
        c = get_object_or_404(Comment, pk=post_id)
        c.delete()
        return HttpResponseRedirect(reverse('comment_page', args=(c.post.id,)))
    else:
        return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))

def like(request, post_id):
    if(request.POST['like'] == "0"):
        try:
            u = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
            p = get_object_or_404(Post, pk=post_id)
            try:
                l = u.like_set.get(post = p)
                l.delete()
                return HttpResponseRedirect(reverse('page', args=(p.user.id,)))
            except:
                l = p.like_set.create(user = u)
            return HttpResponseRedirect(reverse('page', args=(p.user.id,)))
        except:
            return HttpResponseRedirect(reverse('page', args=(p.user.id,))) 
    elif(request.POST['like'] == "1"):
        try:
            u = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
            p = get_object_or_404(Post, pk=post_id)
            try:
                l = u.like_set.get(post = p)
                l.delete()
                return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))
            except:
                l = p.like_set.create(user = u)
            return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))
        except:
            return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))
    elif(request.POST['like'] == "2"):
        try:
            u = get_object_or_404(User, pk=request.COOKIES.get('user_cookie'))
            c = get_object_or_404(Comment, pk=post_id)
            try:
                l = u.like_set.get(comment = c)
                l.delete()
                return HttpResponseRedirect(reverse('comment_page', args=(c.post.id,)))
            except:
                l = c.like_set.create(user = u)
            return HttpResponseRedirect(reverse('comment_page', args=(c.post.id,)))
        except:
            return HttpResponseRedirect(reverse('comment_page', args=(c.post.id,)))
    else:
        return HttpResponseRedirect(reverse('comment_page', args=(post_id,)))
    