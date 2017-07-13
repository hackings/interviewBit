/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public ArrayList<Interval> merge(ArrayList<Interval> intervals) {
        Collections.sort(intervals, new IntervalComparator());
        ArrayList<Interval> result = new ArrayList<Interval>();
        int first = intervals.get(0).start;
        int last = intervals.get(0).end;
        for (int i = 1; i < intervals.size(); ++i) {
            if (last > intervals.get(i).end)
                continue;
            else if (last < intervals.get(i).start) {
                Interval interval = new Interval(first, last);
                result.add(interval);
                first = intervals.get(i).start;
                last = intervals.get(i).end;
            }
            else
                last = intervals.get(i).end;
        }
        Interval interval = new Interval(first, last);
        result.add(interval);
        return result;
    }
    private class IntervalComparator implements Comparator<Interval> {
        @Override
        public int compare(Interval interval1, Interval interval2) {
            int cmp = Integer.compare(interval1.start, interval2.start);
            if (cmp != 0)
                return cmp;
            cmp = Integer.compare(interval1.end, interval2.end);
            return cmp;
        }
    }
}
