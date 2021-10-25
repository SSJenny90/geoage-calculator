__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__authors__ = ['Sam Jennings']
__docformat__ = 'numpy'
__version__ = "1.0.0"
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])
__status__ = 'Stable'

from geoage_calculator import geo_age_lookup, age_range_lookup