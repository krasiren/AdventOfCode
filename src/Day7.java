import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class Day7 {

	public static void main(String[] args) {

		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day7_input.txt"));
			String line = null;
			String inputs = "";

			while ((line = br.readLine()) != null) {
				inputs += line;
			}
			br.close();

			calculate(inputs.split(","));

			secondPart(inputs.split(","));

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void secondPart(String[] inputs) {
		int[] tab = new int[inputs.length];
		for (int i = 0; i < tab.length; i++) {
			tab[i] = Integer.parseInt(inputs[i]);
		}
		Arrays.sort(tab);

		int min = -1;
		for (int i = 0; i < tab[tab.length - 1]; i++) {
			int sum = 0;
			for (int j = 0; j < tab.length; j++) {
				sum += fuel(tab[j], i);
			}
			if (sum < min || min < 0)
				min = sum;
		}

		System.out.println(min);
	}

	private static int fuel(int a, int b) {
		int c = 0;
		for (int j = 1; j <= Math.abs(a - b); j++) {
			c += j;
		}
		return c;
	}

	private static void calculate(String[] inputs) {
		int[] numArray = new int[inputs.length];
		for (int i = 0; i < numArray.length; i++) {
			numArray[i] = Integer.parseInt(inputs[i]);
		}
		Arrays.sort(numArray);
		double median;
		if (numArray.length % 2 == 0)
			median = ((double) numArray[numArray.length / 2] + (double) numArray[numArray.length / 2 - 1]) / 2;
		else
			median = (double) numArray[numArray.length / 2];

		int sum = 0;
		for (int i = 0; i < inputs.length; i++) {
			sum += Math.abs(Integer.parseInt(inputs[i]) - median);
		}

		System.out.println(sum);
	}

}
