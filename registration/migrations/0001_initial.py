# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-17 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('postalCode', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('emailsOk', models.BooleanField(default=False)),
                ('surveyOk', models.BooleanField(default=False)),
                ('volunteerContact', models.BooleanField(default=False)),
                ('volunteerDepts', models.CharField(blank=True, max_length=1000)),
                ('notes', models.TextField(blank=True)),
                ('parentFirstName', models.CharField(blank=True, max_length=200)),
                ('parentLastName', models.CharField(blank=True, max_length=200)),
                ('parentPhone', models.CharField(blank=True, max_length=20)),
                ('parentEmail', models.CharField(blank=True, max_length=200)),
                ('aslRequest', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttendeeOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionValue', models.CharField(max_length=200)),
                ('optionValue2', models.CharField(blank=True, max_length=200)),
                ('optionValue3', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registeredDate', models.DateTimeField(null=True)),
                ('registrationToken', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('badgeName', models.CharField(blank=True, max_length=200)),
                ('badgeNumber', models.IntegerField(blank=True, null=True)),
                ('printed', models.BooleanField(default=False)),
                ('printCount', models.IntegerField(default=0)),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee')),
            ],
        ),
        migrations.CreateModel(
            name='BanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=200)),
                ('lastName', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=400)),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('form', models.CharField(choices=[('Attendee', 'Attendee'), ('Staff', 'Staff'), ('Dealer', 'Dealer'), ('Dealer Assistant', 'Dealer Assistant')], max_length=50)),
                ('formData', models.TextField()),
                ('formHeaders', models.TextField()),
                ('enteredDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('transferedDate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cashdrawer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close'), ('Transaction', 'Transaction'), ('Deposit', 'Deposit')], default='Open', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tendered', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(blank=True, help_text='Charity link', max_length=500, verbose_name='URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationToken', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('approved', models.BooleanField(default=False)),
                ('tableNumber', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('businessName', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('license', models.CharField(max_length=50)),
                ('needPower', models.BooleanField(default=False)),
                ('needWifi', models.BooleanField(default=False)),
                ('wallSpace', models.BooleanField(default=False)),
                ('nearTo', models.CharField(blank=True, max_length=200)),
                ('farFrom', models.CharField(blank=True, max_length=200)),
                ('chairs', models.IntegerField(default=0)),
                ('tables', models.IntegerField(default=0)),
                ('reception', models.BooleanField(default=False)),
                ('artShow', models.BooleanField(default=False)),
                ('charityRaffle', models.TextField(blank=True)),
                ('agreeToRules', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('willSwitch', models.BooleanField(default=False)),
                ('partners', models.TextField(blank=True)),
                ('buttonOffer', models.CharField(blank=True, max_length=200)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('discountReason', models.CharField(blank=True, max_length=200)),
                ('emailed', models.BooleanField(default=False)),
                ('asstBreakfast', models.BooleanField(default=False)),
                ('logo', models.CharField(blank=True, max_length=500)),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Attendee')),
            ],
        ),
        migrations.CreateModel(
            name='DealerAsst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationToken', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('name', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=200)),
                ('license', models.CharField(max_length=50)),
                ('sent', models.BooleanField(default=False)),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('volunteerListOk', models.BooleanField(default=False)),
                ('divisionID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=100)),
                ('percentOff', models.IntegerField(null=True)),
                ('amountOff', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
                ('oneTime', models.BooleanField(default=False)),
                ('used', models.IntegerField(default=0)),
                ('reason', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('staffRegStart', models.DateTimeField(help_text='(Not currently enforced)', verbose_name='Staff Registration Start')),
                ('staffRegEnd', models.DateTimeField(verbose_name='Staff Registration End')),
                ('attendeeRegStart', models.DateTimeField(verbose_name='Attendee Registration Start')),
                ('attendeeRegEnd', models.DateTimeField(verbose_name='Attendee Registration End')),
                ('onlineRegStart', models.DateTimeField(help_text='Start time for /registration/onsite form', verbose_name='On-site Registration Start')),
                ('onlineRegEnd', models.DateTimeField(verbose_name='On-site Registration End')),
                ('eventStart', models.DateField(verbose_name='Event Start Date')),
                ('eventEnd', models.DateField(verbose_name='Event End Date')),
                ('default', models.BooleanField(default=False, help_text='The first default event will be used as the basis for all current event configuration', verbose_name='Default')),
                ('useAuthToken', models.BooleanField(default=True, help_text='Staff cannot register for the event (or take advantage of staff discounts) when auth tokens are not in use. ', verbose_name='Auth Tokens for Staff Registration ')),
                ('staffEventRegistration', models.BooleanField(default=False, help_text='If on, staff will be allowed to register for the event when they fill out the staff form.', verbose_name='Allow event registration during staff signup.')),
                ('allowOnlineMinorReg', models.BooleanField(default=False, help_text='Allow registration for anyone age 13 and older online. Otherwise, registration is restricted to those 18 or older.', verbose_name='Allow online minor registration')),
                ('collectAddress', models.BooleanField(default=True, help_text='Disable to skip collecting a mailing address for each attendee.', verbose_name='Collect Address')),
                ('collectBillingAddress', models.BooleanField(default=True, help_text="Disable to skip collecting a billing address for each order. Note that a billing address and buyer email is required to qualify for Square's Chargeback protection.", verbose_name='Collect Billing Address')),
                ('registrationEmail', models.CharField(blank=True, default=b'registration@example.com', help_text='Email to display on error messages for attendee registration', max_length=200, verbose_name='Registration Email')),
                ('staffEmail', models.CharField(blank=True, default=b'registration@example.com', help_text='Email to display on error messages for staff registration', max_length=200, verbose_name='Staff Email')),
                ('badgeTheme', models.CharField(default='apis', help_text='Name of badge theme to use for printing', max_length=200, verbose_name='Badge Theme')),
                ('codeOfConduct', models.CharField(blank=True, default='/code-of-conduct', help_text='Link to code of conduct agreement', max_length=500, verbose_name='Code of Conduct')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Firebase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('closed', models.BooleanField(default=False)),
                ('cashdrawer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HoldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('settledDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('orgDonation', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('charityDonation', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('notes', models.TextField(blank=True)),
                ('billingName', models.CharField(blank=True, max_length=200)),
                ('billingAddress1', models.CharField(blank=True, max_length=200)),
                ('billingAddress2', models.CharField(blank=True, max_length=200)),
                ('billingCity', models.CharField(blank=True, max_length=200)),
                ('billingState', models.CharField(blank=True, max_length=200)),
                ('billingCountry', models.CharField(blank=True, max_length=200)),
                ('billingPostal', models.CharField(blank=True, max_length=20)),
                ('billingEmail', models.CharField(blank=True, max_length=200)),
                ('billingType', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Credit', 'Credit'), ('Cash', 'Cash'), ('Comp', 'Comp')], default='Credit', max_length=20)),
                ('lastFour', models.CharField(blank=True, max_length=4)),
                ('apiData', models.TextField(blank=True)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Discount')),
            ],
            options={
                'permissions': (('issue_refund', 'Can create refunds'),),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredBy', models.CharField(max_length=100)),
                ('enteredDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('badge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Badge')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PriceLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('optionImage', models.ImageField(blank=True, null=True, upload_to=registration.models.content_file_name)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('basePrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('public', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('group', models.TextField(blank=True)),
                ('emailVIP', models.BooleanField(default=False)),
                ('emailVIPEmails', models.CharField(blank=True, default='', max_length=400)),
                ('isMinor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PriceLevelOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionName', models.CharField(max_length=200)),
                ('optionPrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('optionImage', models.ImageField(blank=True, null=True, upload_to=registration.models.content_file_name)),
                ('required', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('rank', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShirtSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationToken', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('timesheetAccess', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('specialSkills', models.TextField(blank=True)),
                ('specialFood', models.TextField(blank=True)),
                ('specialMedical', models.TextField(blank=True)),
                ('contactName', models.CharField(blank=True, max_length=200)),
                ('contactPhone', models.CharField(blank=True, max_length=200)),
                ('contactRelation', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('checkedIn', models.BooleanField(default=False)),
                ('accommodationType', models.CharField(blank=True, max_length=50)),
                ('roommateRequests', models.CharField(blank=True, max_length=200)),
                ('roomateBlacklist', models.CharField(blank=True, max_length=200)),
                ('discord', models.CharField(blank=True, max_length=200)),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Department')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Division')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
                ('shirtsize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.ShirtSizes')),
            ],
        ),
        migrations.CreateModel(
            name='TableSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('chairMin', models.IntegerField(default=1)),
                ('chairMax', models.IntegerField(default=1)),
                ('tableMin', models.IntegerField(default=0)),
                ('tableMax', models.IntegerField(default=0)),
                ('partnerMin', models.IntegerField(default=1)),
                ('partnerMax', models.IntegerField(default=1)),
                ('basePrice', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TempToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('validUntil', models.DateTimeField()),
                ('used', models.BooleanField(default=False)),
                ('usedDate', models.DateTimeField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('groupNo', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Title'),
        ),
        migrations.AddField(
            model_name='pricelevel',
            name='priceLevelOptions',
            field=models.ManyToManyField(blank=True, to='registration.PriceLevelOption'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='priceLevel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.PriceLevel'),
        ),
        migrations.AddField(
            model_name='dealerasst',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='tableSize',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.TableSize'),
        ),
        migrations.AddField(
            model_name='badge',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AddField(
            model_name='attendeeoptions',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.PriceLevelOption'),
        ),
        migrations.AddField(
            model_name='attendeeoptions',
            name='orderItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.OrderItem'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='holdType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.HoldType'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Attendee'),
        ),
    ]
