from lineClass import Line
from pointClass import Point

class Cell:
  def __init__(self, win=None):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.visited = False
    self.x1 = None
    self.y1 = None
    self.x2 = None
    self.y2 = None
    self.win = win

  def draw(self, x1, y1, x2, y2):
    if self.win is None:
      return
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1
    self.y2 = y2
    if self.has_left_wall:
        line = Line(Point(x1, y1), Point(x1, y2))
        self.win.draw_line(line)
    else:
        line = Line(Point(x1, y1), Point(x1, y2))
        self.win.draw_line(line, "white")
    if self.has_top_wall:
        line = Line(Point(x1, y1), Point(x2, y1))
        self.win.draw_line(line)
    else:
        line = Line(Point(x1, y1), Point(x2, y1))
        self.win.draw_line(line, "white")
    if self.has_right_wall:
        line = Line(Point(x2, y1), Point(x2, y2))
        self.win.draw_line(line)
    else:
          line = Line(Point(x2, y1), Point(x2, y2))
          self.win.draw_line(line, "white")
    if self.has_bottom_wall:
        line = Line(Point(x1, y2), Point(x2, y2))
        self.win.draw_line(line)
    else:
          line = Line(Point(x1, y2), Point(x2, y2))
          self.win.draw_line(line, "white")

  # def draw_move(self, to_cell, undo=False):
  #   if self.win is not None:
  #     color = "grey" if undo else "red"
  #     from_x = (self.x1 + self.x2)
  #     from_y = (self.y1 + self.y2)
  #     to_x = (to_cell.x1 + to_cell.x2)
  #     to_y = (to_cell.y1 + to_cell.y2)
  #     line = Line(Point(from_x, from_y), Point(to_x, to_y))
  #     self.win.draw_line(line, color)

  def draw_move(self, to_cell, undo=False):
    half_length = abs(self.x2 - self.x1) // 2
    x_center = half_length + self.x1
    y_center = half_length + self.y1
    half_length2 = abs(to_cell.x2 - to_cell.x1) // 2
    x_center2 = half_length2 + to_cell.x1
    y_center2 = half_length2 + to_cell.y1
    fill_color = "red"
    if undo:
        fill_color = "gray"
    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self.win.draw_line(line, fill_color)