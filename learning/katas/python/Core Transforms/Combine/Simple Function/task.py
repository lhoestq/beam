#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# beam-playground:
#   name: CombineSimpleFunction
#   description: Task from katas to implement the summation of numbers.
#   multifile: false
#   context_line: 30
#   categories:
#     - Combiners
#   complexity: BASIC
#   tags:
#     - count
#     - combine
#     - numbers

import apache_beam as beam

from log_elements import LogElements


def sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


with beam.Pipeline() as p:

  (p | beam.Create([1, 2, 3, 4, 5])
     | beam.CombineGlobally(sum)
     | LogElements())
