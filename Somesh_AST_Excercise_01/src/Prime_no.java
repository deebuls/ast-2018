public class Prime_no {
	public static void main(String args[]){
		long startTime = System.nanoTime();
		int status=1;
		int number=3;
		System.out.println("prime numbers are : ");
		System.out.println(2);
		for(int i=2;i<=20;){ 
			for(int j=2;j<=Math.sqrt(number);j++){ 
				if(number % j== 0) {
					status=0;
					break;
				}
			}
			if(status != 0) {
				System.out.println(number);
				i++;
			}
			status=1;
			number++;
		}
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("time in nanosec : " +totalTime);

				
	}
}	

