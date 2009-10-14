from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from avatar.templatetags import avatar_tags


class GravatarBackupTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username='testuser', first_name='Test', last_name='Johnson', email='test@test.com')
    
    def test_gravatar_backup_setting(self):
        avatar_tags.AVATAR_GRAVATAR_BACKUP = False
        url = avatar_tags.avatar_url(self.user)
        self.assertEquals(settings.AVATAR_DEFAULT_URL, url)
        avatar_tags.AVATAR_GRAVATAR_BACKUP = True
        url = avatar_tags.avatar_url(self.user)
        self.assertTrue(url.startswith("http://www.gravatar.com/"))
        
    def test_gravatar_backup_default_setting(self):
        avatar_tags.AVATAR_GRAVATAR_BACKUP = True
        avatar_tags.AVATAR_GRAVATAR_BACKUP_DEFAULT = 'monsterid'
        url = avatar_tags.avatar_url(self.user)
        self.assertTrue("d=monsterid" in url)
    
    def test_gravatar_backup_rating_setting(self):
        avatar_tags.AVATAR_GRAVATAR_BACKUP = True
        avatar_tags.AVATAR_GRAVATAR_BACKUP_RATING = 'x'
        url = avatar_tags.avatar_url(self.user)
        self.assertTrue("r=x" in url)
        
        
        