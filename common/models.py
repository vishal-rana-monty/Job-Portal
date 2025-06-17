from django.db import models
from users.models import User

# not in use
class ContactInfo(models.Model):
    address = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    map_embed_link = models.TextField(help_text="Google Maps iframe embed link")

    def __str__(self):
        return "Contact Inf0"
    

class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages') 
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_messages')
    subject = models.CharField(max_length=250)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"







