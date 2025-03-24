class Solution:
  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    l = []
    intervals.sort()
    for i in intervals:
      if not l or l[-1][1] < i[0]:
        l.append(i)
      else:
        l[-1][1] = max(l[-1][1], i[1])
    return l