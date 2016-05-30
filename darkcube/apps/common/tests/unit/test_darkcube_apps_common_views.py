#
# DarkCube
# Copyright 2016 DarkCube developers
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#

from django.template.response import TemplateResponse

from darkcube.apps.common.views import LayoutView


class TestLayoutView(object):
    def test__layout_html_is_used(self, rf):
        response = LayoutView.as_view()(rf.get('/'))
        assert isinstance(response, TemplateResponse)
        assert response.template_name == ['darkcube/apps/common/layout.html']
