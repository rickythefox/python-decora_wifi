# Leviton Cloud Services API model Preference.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Preference(BaseModel):
    def __init__(self, session, model_id=None):
        super(Preference, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_app_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_person_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_app_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_app_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_person_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_person_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_app_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_person_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_app_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_person_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_app_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_person_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_app(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/:id/app"
        return session.call_api(api, attribs, 'get')

    def get_app_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_person(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/:id/person"
        return session.call_api(api, attribs, 'get')

    def get_person_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/:id"
        return session.call_api(api, attribs, 'put')

    def update_by_id_app_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Apps/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_person_preferences(self, preference, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference)
        return self._session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Preferences/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
