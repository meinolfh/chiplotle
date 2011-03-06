from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.core.interfaces.decoratable import Decoratable
from chiplotle.tools.geometrytools.get_center import get_center
from chiplotle.tools.geometrytools.get_centroid import get_centroid
from chiplotle.tools.geometrytools.get_minmax_coordinates \
   import get_minmax_coordinates

class _Shape(Decoratable):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      Decoratable.__init__(self)


   ## OVERRIDES ##

   def __repr__(self):
      return str(self)

   def __str__(self):
      return '%s(%d)' % (self.__class__.__name__, len(self))


   ## PUBLIC PROPERTIES ##

   ## TODO:  cache computed values?
   ## TODO: add 'state' property to keep track of changes?

   @property
   def center(self):
      return get_center(self.points)

   @property
   def centroid(self):
      return get_centroid(self.points)

   @property
   def minmax_coordinates(self):
      return get_minmax_coordinates(self.points)

   @property
   def width(self):
      mn, mx = self.minmax_coordinates
      return mx.x - mn.x

   @property
   def height(self):
      mn, mx = self.minmax_coordinates
      return mx.y - mn.y

   ## corners ##

   @property
   def bottom_left(self):
      return self.minmax_coordinates[0]

   @property
   def bottom_right(self):
      mn, mx = self.minmax_coordinates
      return Coordinate(mx.x, mn.y)

   @property
   def top_left(self):
      mn, mx = self.minmax_coordinates
      return Coordinate(mn.x, mx.y)

   @property
   def top_right(self):
      return self.minmax_coordinates[1]
