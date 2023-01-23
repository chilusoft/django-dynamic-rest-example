# Copyright 2023 USER
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
import json
import names
from random import randint

from time import sleep

from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        year_count = 0
        max_num = 1320
        for i in range(max_num):
            progress = i/max_num * 100
            years = randint(1,randint(1,100))
            year_count = year_count + years
            self.send(json.dumps({
                'message': str(years) + f' years - {names.get_full_name()}',
                    'count': f'{i}',
                    'progress': f'{progress}', 
                'total_years': f'{year_count}'
            }))
            sleep(0.001)
        self.close()

        
