# Generated by Django 5.0.6 on 2024-05-17 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fams", "0001_initial"),
        ("users", "0003_faculty_department"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publication",
            name="credential_id",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="credential_url",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="expiration_date",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="name",
        ),
        migrations.AddField(
            model_name="publication",
            name="authors",
            field=models.CharField(default=None, max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="journal_name",
            field=models.CharField(default="ABC Journal", max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="page_number",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="publisher_name",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="title",
            field=models.CharField(default="unknown title", max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="volume",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="work_type",
            field=models.CharField(
                choices=[
                    ("article", "Article"),
                    ("article_in_press", "Article in Press"),
                    ("book", "Book"),
                    ("book_chapter", "Book Chapter"),
                    ("conference_paper", "Conference Paper"),
                    ("conference_proceedings", "Conference Proceedings"),
                    ("editorial", "Editorial"),
                    ("erratum", "Erratum"),
                    ("letter", "Letter"),
                    ("note", "Note"),
                    ("review", "Review"),
                    ("retracted_article", "Retracted Article"),
                    ("short_survey", "Short Survey"),
                    ("other", "Other"),
                ],
                default="article",
                max_length=225,
            ),
        ),
        migrations.AddField(
            model_name="publication",
            name="year",
            field=models.IntegerField(
                choices=[
                    (1980, 1980),
                    (1981, 1981),
                    (1982, 1982),
                    (1983, 1983),
                    (1984, 1984),
                    (1985, 1985),
                    (1986, 1986),
                    (1987, 1987),
                    (1988, 1988),
                    (1989, 1989),
                    (1990, 1990),
                    (1991, 1991),
                    (1992, 1992),
                    (1993, 1993),
                    (1994, 1994),
                    (1995, 1995),
                    (1996, 1996),
                    (1997, 1997),
                    (1998, 1998),
                    (1999, 1999),
                    (2000, 2000),
                    (2001, 2001),
                    (2002, 2002),
                    (2003, 2003),
                    (2004, 2004),
                    (2005, 2005),
                    (2006, 2006),
                    (2007, 2007),
                    (2008, 2008),
                    (2009, 2009),
                    (2010, 2010),
                    (2011, 2011),
                    (2012, 2012),
                    (2013, 2013),
                    (2014, 2014),
                    (2015, 2015),
                    (2016, 2016),
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                ],
                default=2024,
            ),
        ),
        migrations.AlterField(
            model_name="publication",
            name="issuing_organization",
            field=models.CharField(default="Unknown Organization", max_length=225),
        ),
        migrations.CreateModel(
            name="Committee_membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("organization", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="committee_memberships",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctoral_thesis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("researchers_name", models.CharField(max_length=225)),
                ("title", models.CharField(max_length=225)),
                ("institute", models.CharField(max_length=225)),
                ("description", models.TextField()),
                (
                    "awarded_year",
                    models.IntegerField(
                        choices=[
                            (1980, 1980),
                            (1981, 1981),
                            (1982, 1982),
                            (1983, 1983),
                            (1984, 1984),
                            (1985, 1985),
                            (1986, 1986),
                            (1987, 1987),
                            (1988, 1988),
                            (1989, 1989),
                            (1990, 1990),
                            (1991, 1991),
                            (1992, 1992),
                            (1993, 1993),
                            (1994, 1994),
                            (1995, 1995),
                            (1996, 1996),
                            (1997, 1997),
                            (1998, 1998),
                            (1999, 1999),
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                        ],
                        default=2024,
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctoral_theses",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Honors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("issuing_organization", models.CharField(max_length=225)),
                (
                    "issue_year",
                    models.IntegerField(
                        choices=[
                            (1980, 1980),
                            (1981, 1981),
                            (1982, 1982),
                            (1983, 1983),
                            (1984, 1984),
                            (1985, 1985),
                            (1986, 1986),
                            (1987, 1987),
                            (1988, 1988),
                            (1989, 1989),
                            (1990, 1990),
                            (1991, 1991),
                            (1992, 1992),
                            (1993, 1993),
                            (1994, 1994),
                            (1995, 1995),
                            (1996, 1996),
                            (1997, 1997),
                            (1998, 1998),
                            (1999, 1999),
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                        ],
                        default=2024,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="honors",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("inventors", models.CharField(max_length=225)),
                ("application_number", models.CharField(max_length=225)),
                ("patent_number", models.CharField(max_length=225)),
                ("filing_country", models.CharField(max_length=225)),
                ("subject_category", models.CharField(max_length=225)),
                ("filing_date", models.DateField()),
                ("publication_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("published", "Published"),
                            ("granted", "Granted"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patents",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professional_membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("member_type", models.CharField(max_length=225)),
                ("organization", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professional_memberships",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResearchProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("ongoing", models.BooleanField(default=False)),
                ("role", models.CharField(max_length=225)),
                ("funding_agency", models.CharField(max_length=225)),
                ("grant_number", models.CharField(max_length=225)),
                (
                    "status",
                    models.CharField(
                        choices=[("completed", "Completed"), ("ongoing", "Ongoing")],
                        max_length=50,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="research_projects",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-17 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fams", "0001_initial"),
        ("users", "0003_faculty_department"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publication",
            name="credential_id",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="credential_url",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="expiration_date",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="name",
        ),
        migrations.AddField(
            model_name="publication",
            name="authors",
            field=models.CharField(default=None, max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="journal_name",
            field=models.CharField(default="ABC Journal", max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="page_number",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="publisher_name",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="title",
            field=models.CharField(default="unknown title", max_length=225),
        ),
        migrations.AddField(
            model_name="publication",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="volume",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name="publication",
            name="work_type",
            field=models.CharField(
                choices=[
                    ("article", "Article"),
                    ("article_in_press", "Article in Press"),
                    ("book", "Book"),
                    ("book_chapter", "Book Chapter"),
                    ("conference_paper", "Conference Paper"),
                    ("conference_proceedings", "Conference Proceedings"),
                    ("editorial", "Editorial"),
                    ("erratum", "Erratum"),
                    ("letter", "Letter"),
                    ("note", "Note"),
                    ("review", "Review"),
                    ("retracted_article", "Retracted Article"),
                    ("short_survey", "Short Survey"),
                    ("other", "Other"),
                ],
                default="article",
                max_length=225,
            ),
        ),
        migrations.AlterField(
            model_name="publication",
            name="issuing_organization",
            field=models.CharField(default="Unknown Organization", max_length=225),
        ),
        migrations.CreateModel(
            name="Committee_membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("organization", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="committee_memberships",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctoral_thesis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("researchers_name", models.CharField(max_length=225)),
                ("title", models.CharField(max_length=225)),
                ("institute", models.CharField(max_length=225)),
                ("description", models.TextField()),
                (
                    "awarded_year",
                    models.IntegerField(
                        choices=[
                            (1980, 1980),
                            (1981, 1981),
                            (1982, 1982),
                            (1983, 1983),
                            (1984, 1984),
                            (1985, 1985),
                            (1986, 1986),
                            (1987, 1987),
                            (1988, 1988),
                            (1989, 1989),
                            (1990, 1990),
                            (1991, 1991),
                            (1992, 1992),
                            (1993, 1993),
                            (1994, 1994),
                            (1995, 1995),
                            (1996, 1996),
                            (1997, 1997),
                            (1998, 1998),
                            (1999, 1999),
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                        ],
                        default=2024,
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctoral_theses",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Honors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("issuing_organization", models.CharField(max_length=225)),
                (
                    "issue_year",
                    models.IntegerField(
                        choices=[
                            (1980, 1980),
                            (1981, 1981),
                            (1982, 1982),
                            (1983, 1983),
                            (1984, 1984),
                            (1985, 1985),
                            (1986, 1986),
                            (1987, 1987),
                            (1988, 1988),
                            (1989, 1989),
                            (1990, 1990),
                            (1991, 1991),
                            (1992, 1992),
                            (1993, 1993),
                            (1994, 1994),
                            (1995, 1995),
                            (1996, 1996),
                            (1997, 1997),
                            (1998, 1998),
                            (1999, 1999),
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                        ],
                        default=2024,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="honors",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("inventors", models.CharField(max_length=225)),
                ("application_number", models.CharField(max_length=225)),
                ("patent_number", models.CharField(max_length=225)),
                ("filing_country", models.CharField(max_length=225)),
                ("subject_category", models.CharField(max_length=225)),
                ("filing_date", models.DateField()),
                ("publication_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("published", "Published"),
                            ("granted", "Granted"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patents",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professional_membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("member_type", models.CharField(max_length=225)),
                ("organization", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professional_memberships",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResearchProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("ongoing", models.BooleanField(default=False)),
                ("role", models.CharField(max_length=225)),
                ("funding_agency", models.CharField(max_length=225)),
                ("grant_number", models.CharField(max_length=225)),
                (
                    "status",
                    models.CharField(
                        choices=[("completed", "Completed"), ("ongoing", "Ongoing")],
                        max_length=50,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="research_projects",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
    ]
