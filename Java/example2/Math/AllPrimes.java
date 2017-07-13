/*
 * 
 */
import java.util.*;
public class AllPrimes {
    public static ArrayList<Integer> sieve(int a) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int[] primes = new int[a + 1];
        for(int i = 0; i <= a; i++) {
            primes[i] = 1;
        }
        primes[0] = 0;
        primes[1] = 0;
        
        for(int i = 2; i <= Math.sqrt(a); i++) {
            if(primes[i] == 1) {
                for(int j = 2; i * j <= a; j++)
                    primes[i * j] = 0;
            }
        }
        
        for(int i = 2; i <= a; i++){
            if(primes[i] == 1)
                result.add(i);
        }
        return result;
    }
    
    public static int countPrimes(int n){
        boolean[] isPrime = new boolean[n+1];
        for(int i = 2; i <= n; i++){
            isPrime[i] = true;
        }
        
        for(int i = 2; i * i <= n; i++){
            if(isPrime[i]){
                for(int j = i; i * j <= n; j++){
                    isPrime[i*j] = false;
                }
            }
        }
        int count = 0;
        for(int i = 2; i <= n; i++){
            if(isPrime[i])
                count++;
        }
        return count;
    }
    public static void main(String[] args) {
        System.out.println(sieve(Integer.parseInt(args[0])));
        System.out.println(countPrimes(Integer.parseInt(args[0])));
    }
}
