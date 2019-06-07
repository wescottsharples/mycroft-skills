# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

import os
import util
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eward'

LOGGER = getLogger(__name__)


class TimeTrackerSkill(MycroftSkill):
    def __init__(self):
        super(TimeTrackerSkill, self).__init__(name="TimeTrackerSkill")

    def initialize(self):
        list_projects_intent = IntentBuilder("ListProjectsIntent"). \
            require("ListProjectsKeyword").build()
        create_projects_intent = IntentBuilder("CreateProjectsIntent"). \
            require("CreateProjectsKeyword").build()
        self.register_intent(create_projects_intent, self.handle_create_projects_intent)

    def handle_list_projects_intent(self, message):
        self.speak_dialog("list.projects")

    def handle_create_projects_intent(self, message):
        util.data_checker()
        self.speak_dialog("create.projects")

    def stop(self):
        pass


def create_skill():
    return TimeTrackerSkill()
