class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Set the passed in item to evaluate to the current item in storage.
    self.storage[self.current] = item
    # If the current value is less than the overall capacity.
    if self.current < self.capacity - 1:
      # Add it to the list
      self.current += 1
    else:
      # Otherwise set current value to 0
      self.current = 0

  def get(self):
    pass