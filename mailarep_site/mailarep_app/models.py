from django.db import models


class Sender(models.Model):
    """
    Model to store names, addresses, and contact info
    """
    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    )

    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES, blank=False)
    zip_code = models.CharField("ZIP code", max_length=10)
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(blank=True)
    # TODO: link to Charity
    # TODO: link to Payment

    def __unicode__(self):
        return "%s from %s, %s" % (self.name, self.city, self.state)


class Letter(models.Model):
    """
    Model to store actual letter written by constituent
    """
    letter_text = models.TextField()
    date_sent = models.DateTimeField(auto_now=True, blank=True)
    sender = models.ForeignKey(Sender)  # TODO: OneToOneField?