#  Copyright 2019 Ian moncrieffe <zellaio600@gmail.com>
#  
# Author:: Ian Moncrieffe (<zellaio600@gmail.com>)
# Copyright:: Copyright (c) 2019 Ian Moncrieffe
# License:: MIT
#
# Licensed under the MIT Licens.
# you may not use this file except in compliance with the License.
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "genny"
__summary__ = """ Unique Identity number generator for your application's, users, documents, applications,
			 software, devices, products, employees, documents etc...			 
			  Doc Tags: String( doc, app, key, job, user, item, code)

			  UseCase: 
			  		>>> import genny
			  		>>> from genny import genid
			  		>>> from genny import genid as gi
			  		
			  		>>> id = genny.genid('user')
			  		>>> id = genid('user')
			  		>>> id = gi('user')

			 Yeilds ... U474390
			 		... U77301642
			 		... U1593055		 
						  
			  """
			  
__uri__ = "https://github.com/Ze6/genny/"

__version__ = "1.0.1"

__author__ = "ZellaCore Inc."
__email__ = "zellaio600@gmail.com"

__license__ = "MIT"
__copyright__ = "Copyright 2019-2020 {0}".format(__author__)
