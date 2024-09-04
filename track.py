class Track(object):
  def __init__(self, artist, title, duration):
    self._artist = artist
    self._title = title
    self._duration = duration

  @property
  def artist(self):            # now one can use artist instead of artist()
    return self._artist

  @property
  def title(self):
    return self._title

  @property
  def duration(self):
    return self._duration

  def __str__(self):
    return '%s - %s - %s' % (self._artist, self._title, self._duration)

if __name__ == "__main__":
  track = Track("Ravi Shankar", "Bairagi Todi", 25)
  print(track)

  # access directly
  print ('%s - %s - %s' % (track.artist, track.title, track.duration))
