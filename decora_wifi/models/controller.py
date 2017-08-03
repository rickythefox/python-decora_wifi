# Leviton Cloud Services API model Controller.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Controller(BaseModel):
    def __init__(self, session, model_id=None):
        super(Controller, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_installation_controllers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats/count"
        return session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_installation_controllers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_installation_controllers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_installation_controllers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats"
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_installation_controllers(self, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers/{1}".format(self._id, controller)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'delete')

    def discover(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/discover".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_installation_controllers(self, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers/{1}".format(self._id, controller)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_feed_item_controller(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/controller".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_installation(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/installation"
        return session.call_api(api, attribs, 'get')

    def get_installation_controllers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats"
        return session.call_api(api, attribs, 'get')

    def post_message(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/postMessage".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id"
        return session.call_api(api, attribs, 'put')

    def update_by_id_installation_controllers(self, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/controllers/{1}".format(self._id, controller)
        return self._session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
