public class Solution {
	public ArrayList<ArrayList<Integer>> anagrams(final List<String> a) {
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		HashMap<String, ArrayList<Integer>> map = new HashMap<String, ArrayList<Integer>>();
		for (int i = 0; i < a.size(); ++i) {

			char[] array = a.get(i).toCharArray();
			Arrays.sort(array);
			String sorted = new String(array);


			if (!map.containsKey(sorted)) {
				ArrayList<Integer> list = new ArrayList<>();
				list.add(i+1);
				map.put(sorted, list);
			}
			else {
				map.get(sorted).add(i+1);
			}
		}

		for (ArrayList<Integer> val : map.values())
			res.add(val);
		return res;

	}
}

/*
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 
 Note: All inputs will be in lower-case. 
Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4. 
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
*/