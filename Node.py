class Node:
  def __init__(self, data, item = None, obstacle = False, npc = None):
      self.data = data
      self.next = None
      self.item = item
      self.obstacle = obstacle
      self.npc = npc
      self.dialogue = None
