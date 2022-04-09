from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userpage.views import index, newacc, signin, post, page, search, comment_page, comment_post, share, friend, mesg, edit, delete, like, chng_pass

class TestUrls(SimpleTestCase):

    def test_list_url_index(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_list_url_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_list_url_newacc(self):
        url = reverse('newacc')
        self.assertEquals(resolve(url).func, newacc)

    def test_list_url_signin(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_list_url_chng_pass(self):
        url = reverse('chng_pass')
        self.assertEquals(resolve(url).func, chng_pass)

    def test_list_url_comment_page(self):
        url = reverse('comment_page', args=[2])
        self.assertEquals(resolve(url).func, comment_page)

    def test_list_url_share(self):
        url = reverse('share', args=[2])
        self.assertEquals(resolve(url).func, share)

    def test_list_url_like(self):
        url = reverse('like', args=[2])
        self.assertEquals(resolve(url).func, like)

    def test_list_url_comment_post(self):
        url = reverse('comment_post', args=[2])
        self.assertEquals(resolve(url).func, comment_post)

    def test_list_url_delete(self):
        url = reverse('delete', args=[2])
        self.assertEquals(resolve(url).func, delete)

    def test_list_url_edit(self):
        url = reverse('edit', args=[2])
        self.assertEquals(resolve(url).func, edit)

    def test_list_url_page(self):
        url = reverse('page', args=[2])
        self.assertEquals(resolve(url).func, page)

    def test_list_url_mesg(self):
        url = reverse('mesg', args=[2])
        self.assertEquals(resolve(url).func, mesg)

    def test_list_url_friend(self):
        url = reverse('friend', args=[2])
        self.assertEquals(resolve(url).func, friend)

    def test_list_url_post(self):
        url = reverse('post', args=[2])
        self.assertEquals(resolve(url).func, post)
