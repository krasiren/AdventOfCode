import java.io.BufferedReader;
import java.io.FileReader;

public class Day6 {

	public static void main(String[] args) {

		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day6_input.txt"));
			String line = null;
			String inputs = "";

			while ((line = br.readLine()) != null) {
				inputs += line;
			}
			br.close();

			solve(inputs.split(","), 80);
			// probaj najt analiticno resitev
			solve(inputs.split(","), 256);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void solve(String[] inputs, int days) {
		long[] fish = new long[9];

		for (int i = 0; i < inputs.length; i++) {
			int x = Integer.parseInt(inputs[i]);
			fish[x]++;
		}

		for (int i = 0; i < days; i++) {
			long[] temp = new long[fish.length];
			for (int j = 0; j < 8; j++) {
				temp[j] = fish[j + 1];
			}
			temp[8] = fish[0];
			temp[6] += fish[0];
			fish = temp;
		}

		System.out.println(sum(fish));
	}

	private static long sum(long[] fish) {
		long sum = 0;
		for (int i = 0; i < fish.length; i++) {
			sum += fish[i];
		}
		return sum;
	}

}
