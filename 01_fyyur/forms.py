from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, ValidationError
from enum import Enum

###############################################################
# enum classes for custom validators
###############################################################

genres_dict = {
    "Alternative": "Alternative",
    "Blues": "Blues",
    "Classical": "Classical",
    "Country": "Country",
    "Electronic": "Electronic",
    "Folk": "Folk",
    "Funk": "Funk",
    "Hip-Hop": "Hip-Hop",
    "Heavy Metal": "Heavy Metal",
    "Instrumental": "Instrumental",
    "Jazz": "Jazz",
    "Musical Theatre": "Musical Theatre",
    "Pop": "Pop",
    "Punk": "Punk",
    "R&B": "R&B",
    "Reggae": "Reggae",
    "Rock n Roll": "Rock n Roll",
    "Soul": "Soul",
    "Other": "Other"
}

states_dict = {
    "AL": "AL",
    "AK": "AK",
    "AZ": "AZ",
    "AR": "AR",
    "CA": "CA",
    "CO": "CO",
    "CT": "CT",
    "DE": "DE",
    "DC": "DC",
    "FL": "FL",
    "GA": "GA",
    "HI": "HI",
    "ID": "ID",
    "IL": "IL",
    "IN": "IN",
    "IA": "IA",
    "KS": "KS",
    "KY": "KY",
    "LA": "LA",
    "ME": "ME",
    "MT": "MT",
    "NE": "NE",
    "NV": "NV",
    "NH": "NH",
    "NJ": "NJ",
    "NM": "NM",
    "NY": "NY",
    "NC": "NC",
    "ND": "ND",
    "OH": "OH",
    "OK": "OK",
    "OR": "OR",
    "MD": "MD",
    "MA": "MA",
    "MI": "MI",
    "MN": "MN",
    "MS": "MS",
    "MO": "MO",
    "PA": "PA",
    "RI": "RI",
    "SC": "SC",
    "SD": "SD",
    "TN": "TN",
    "TX": "TX",
    "UT": "UT",
    "VT": "VT",
    "VA": "VA",
    "WA": "WA",
    "WV": "WV",
    "WI": "WI",
    "WY": "WY"
}

#########################################################################
# custom validators


def validate_genres(form, field):
    valid_genres = genres_dict.keys()
    for genre in field.data:
        if genre not in valid_genres:
            raise ValidationError(
                f'{genre} is not a genre that is currently supported. Please selece a value from the list')


def validate_states(form, field):
    valid_states = states_dict.keys()
    for state in field.data:
        if state not in valid_states:
            raise ValidationError(
                f'{state} is not valid. Please select a value that from the provided list')
#########################################################################


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[URL()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[(s, s) for s in states_dict.keys()]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired(), validate_genres],
        choices=[(g, g) for g in genres_dict.keys()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_talent = SelectField(
        'seeking_talent', choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
    seeking_description = StringField(
        'seeking_description'
    )


class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )

    address = StringField(
        'address_placeholder', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[(s, s) for s in states_dict.keys()]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired(), validate_genres],
        choices=[(g, g) for g in genres_dict.keys()]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_venue = SelectField(
        'seeking_venue', validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
    seeking_description = StringField(
        'seeking_description'
    )


# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
