# Leviton Cloud Services API model ActionBlock.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class ActionBlock(BaseModel):
    def __init__(self, session, model_id=None):
        super(ActionBlock, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions/count"
        return session.call_api(api, attribs, 'get')

    def count_activity_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_installation_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions"
        return session.call_api(api, attribs, 'post')

    def create_activity_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_installation_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_activity_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_installation_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def delete_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions"
        return session.call_api(api, attribs, 'delete')

    def delete_activity_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_installation_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_activity_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_installation_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'get')

    def find_by_id_activity_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_installation_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_action_action_block(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Actions/{0}/actionBlock".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_activity(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/activity"
        return session.call_api(api, attribs, 'get')

    def get_activity_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_installation(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/installation"
        return session.call_api(api, attribs, 'get')

    def get_installation_action_blocks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id"
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'put')

    def update_by_id_activity_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_installation_action_blocks(self, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/actionBlocks/{1}".format(self._id, action_block)
        return self._session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
