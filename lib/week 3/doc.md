# Week 3

## Anchors in Django

`href = "{ % url 'view name' % }"`

## Class Meta

Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options. It's completely optional to add Meta class in your model.

<code>
    class MyTable(models.Model):
    class Meta:
        unique_together = (('key1', 'key2'),)

    key1 = models.IntegerField(primary_key=True)
    key2 = models.IntegerField()
</code>


## Django Mail

There are times when you do not want Django to send emails at all. For example, while developing a website, you probably don’t want to send out thousands of emails – but you may want to validate that emails will be sent to the right people under the right conditions, and that those emails will contain the correct content.

The easiest way to configure email for local development is to use the console email backend. This backend redirects all email to stdout, allowing you to inspect the content of mail.

The file email backend can also be useful during development – this backend dumps the contents of every SMTP connection to a file that can be inspected at your leisure.

Another approach is to use a “dumb” SMTP server that receives the emails locally and displays them to the terminal, but does not actually send anything. The aiosmtpd package provides a way to accomplish this:

python -m pip install aiosmtpd
python -m aiosmtpd -n -l localhost:8025

This command will start a minimal SMTP server listening on port 8025 of localhost. This server prints to standard output all email headers and the email body. You then only need to set the EMAIL_HOST and EMAIL_PORT accordingly. For a more detailed discussion of SMTP server options, see the documentation of the aiosmtpd module.

https://docs.djangoproject.com/en/4.0/topics/email/



https://github.com/joaopascoalfariafeup/preference-based-student-group-assignment

https://docs.python.org/3/library/csv.html

https://datatofish.com/import-csv-file-python-using-pandas/