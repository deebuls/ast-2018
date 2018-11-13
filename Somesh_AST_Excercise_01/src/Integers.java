import java.util.*;
public class Integers {
	public static void main(String []args) {
		System.out.println("enter the number of integers : ");
		 List integer_list=new ArrayList();
		Scanner scan=new Scanner(System.in);
		int input=scan.nextInt();
		for (int j=1; j<=input;j++) {
			integer_list.add(scan.nextInt());
		}
	int sum=0;
	int product=1;
	int average=1;
	float var=0;
	for (int j=0; j<integer_list.size();j++) {
	     sum += (Integer)integer_list.get(j);
	     product = product *(Integer)integer_list.get(j);
	     average = sum / input;
	     var +=(((Integer)integer_list.get(j)-average)*((Integer)integer_list.get(j)-average))/input;
		}
	int maxvalue= (Integer)integer_list.get(0);
	for (int j=0; j<integer_list.size();j++) {
		if((Integer)integer_list.get(j) > maxvalue){ 
			maxvalue = (Integer)integer_list.get(j); 
     } 
	}
	int minvalue= (Integer)integer_list.get(0);
	for (int j=0; j<integer_list.size();j++) {
		if((Integer)integer_list.get(j) < minvalue){ 
			minvalue = (Integer)integer_list.get(j); 
     } 
	}
			
		System.out.println("integer list : "+integer_list);
		System.out.println("sum of integers : "+sum);
		System.out.println("product of integers : "+product);
		System.out.println("average of the integers : "+average);
		System.out.println("variance of the integers : "+var);
		System.out.println("maxi value of the integers : "+maxvalue);
		System.out.println("minimum value of the integers : "+minvalue);
		
	}

}
