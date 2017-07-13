import java.util.*;
public class ThreeSum{

	public ArrayList<ArrayList<Integer>> threeSum(ArrayList<Integer> a){

		Collections.sort(a);		
		
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		boolean incrementi = false;
		
		for(int i=0; i<a.size(); i++){
			int start=i+1, end=a.size()-1;
			while(start < end){
				System.out.println("i="+i+" start="+start+" end="+end);
				int ni = a.get(i);
				int nstart = a.get(start);
				int nend = a.get(end);
				
				int sum = ni + nstart + nend;				
				if(sum == 0){
					ArrayList<Integer> temp = new ArrayList<Integer>();
					temp.add(ni);
					temp.add(nstart);
					temp.add(nend);
					if(!res.contains(temp)){
						res.add(new ArrayList(temp));
					}
					start++;
					end--;
				}

				else if(sum < 0){	
					start++;													}
				else{
					end--;		
				}				
			}
		}	

		return res;
	}

	public static void main(String args[])throws Exception{
		ThreeSum ts = new ThreeSum();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		arr.add(-1);
		arr.add(0);
		arr.add(1);
		arr.add(2);
		arr.add(-1);
		arr.add(-4);
		System.out.println(ts.threeSum(arr));
	}}
