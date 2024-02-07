# Copyright 2015 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from main import app  # Assuming the Flask app object is named 'app' in your main.py

def test_hello():
    app.testing = True  # This line enables testing mode for Flask, ensuring exceptions propagate rather than emitting a 500 response
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Expected Output'


