/*
make arr[i] = arr[arr[i]]
*/
public class RearrageArr {
	public void arrange(ArrayList<Integer> a) {
	
	        int n =a.size();
	       for(int i=0; i<n; i++){
	           a.set(i, a.get(i)+(a.get(a.get(i))%n)*n);
	       }
	       
	       for(int i=0; i<n; i++){
	           a.set(i, a.get(i)/n);
	       }
	}
}
