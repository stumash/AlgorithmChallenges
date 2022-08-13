class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else:
            self.x1 = x2
            self.y1 = y2
            self.x2 = x1
            self.y2 = y1
    def max_y(self): return max(self.y1, self.y2)
    def max_x(self): return max(self.x1, self.x2)
    def min_y(self): return min(self.y1, self.y2)
    def min_x(self): return min(self.x1, self.x2)

def intersection(ls1, ls2):
    run1 = ls1.x2 - ls1.x1
    run2 = ls2.x2 - ls2.x1

    if run1 == 0 and run2 == 0:
        if ls1.x1 == ls2.x2:
            if ls1.max_y() >= ls2.min_y() and ls2.max_y() >= ls1.min_y():
                return (ls1.x1, max(ls1.min_y(), ls2.min_y()))
        return None

    if run2 == 0:
        return intersection(ls2, ls1)

    a2 = (ls2.y2 - ls2.y1) / run2
    b2 = ls2.y1 - a2 * ls2.x1

    if run1 == 0:
        if ls2.x1 <= ls1.x1 and ls2.x2 >= ls1.x1:
            return (ls1.x1, ls1.x1 * a2 + b2)
        return None

    a1 = (ls1.y2 - ls1.y1) / run1
    b1 = ls1.y1 - a1 * ls1.x1

    slope_diff = a2 - a1
    x = max(ls1.min_x(), ls2.min_x()) if slope_diff == 0 else (b1 - b2) / slope_diff   
    y = (a1 * x + b1)
    y_ = (a2 * x + b2)

    same_y = y == y_
    y_in_range = y>=ls1.min_y() and y<=ls1.max_y() and y>=ls2.min_y() and y<=ls2.max_y()
    x_in_range = x>=ls1.min_x() and x<=ls1.max_x() and x>=ls2.min_x() and x<=ls2.max_x()
    if same_y and x_in_range and y_in_range:
        return (x, a1 * x + b1)
    return None


print('diagonal yes', intersection(
    LineSegment(0, 0, 2, 2),
    LineSegment(0, 2, 2, 0)
))
print('diagonal no', intersection(
    LineSegment(0, 0, 3, 3),
    LineSegment(0, 4, 7, 5)
))
print('horizontal no', intersection(
    LineSegment(0, 0, 2, 0),
    LineSegment(0, 1, 2, 1),
))
print('horizontal yes', intersection(
    LineSegment(0, 0, 2, 0),
    LineSegment(1, 0, 3, 0),
))
print('vertical no', intersection(
    LineSegment(0, 0, 0, 1),
    LineSegment(1, 0, 1, 1),
))
print('vertical yes', intersection(
    LineSegment(0, 0, 0, 2),
    LineSegment(0, 1, 0, 3),
))
print('verthor yes', intersection(
    LineSegment(1, 0, 1, 2),
    LineSegment(0, 1, 2, 1),
))
print('verthor yes', intersection(
    LineSegment(0, 0, 0, 2),
    LineSegment(0, 0, 2, 0),
))
print('horvert yes', intersection(
    LineSegment(0, 1, 2, 1),
    LineSegment(1, 0, 1, 2),
))
print('horvert yes', intersection(
    LineSegment(0, 1, 2, 1),
    LineSegment(0, 0, 0, 1),
))
