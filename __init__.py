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
import requests
from adapt.intent import IntentBuilder
rom mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eward'

LOGGER = getLogger(__name__)


class InteractionSkill(MycroftSkill):
    def __init__(self):
        super(InteractionSkill, self).__init__(name="InteractionSkill")




    @intent_handler(IntentBuilder("").require("Wikipedia").
                require("ArticleTitle"))
    def handle_intent(self, message):
    # Extract what the user asked about
        name=message.data.get("ArticleTitle")

        self.speak_dialog(name)




    def stop(self):
        pass


def create_skill():
    return InteractionSkill()
