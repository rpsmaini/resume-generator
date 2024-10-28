from django.db import models

# Create your models here.
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    address = models.TextField()
    location = models.CharField(
        max_length=50,
        choices=[
            ("US/Canada", "United States/Canada"),
            ("UK", "United Kingdom"),
            ("EU", "European Union"),
            ("AUS/NZ", "Australia/New Zealand"),
            ("APAC", "Asia-Pacific (APAC)"),
            ("ME", "Middle East"),
            ("AF", "Africa"),
        ],
        default="US/Canada"
    )
    skills = models.TextField()
    # Add other fields for education, experience, certifications, etc.

    def __str__(self):
        return self.name
