import java.io.BufferedReader;
import java.io.FileReader;

public class Day1 {

	public static void main(String[] args) {
		String inputs = "";

		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day1_input.txt"));
			String line = null;

			while ((line = br.readLine()) != null) {
				inputs += line + "\n";
			}

			String[] lines = inputs.split("\n");

			int[] measurments = pretvori(lines);
			System.out.println(countInc(measurments));

			int[] threeWindowSlideMeas = convert(measurments);
			System.out.println(countInc(threeWindowSlideMeas));

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	private static int[] convert(int[] measurments) {
		int[] n = new int[measurments.length];
		for (int i = 0; i < n.length - 2; i++) {
			int x = 0;
			for (int j = i; j < i + 3; j++) {
				x += measurments[j];
			}
			n[i] = x;
		}
		return n;
	}

	private static int[] pretvori(String[] lines) {
		int[] n = new int[lines.length];
		for (int i = 0; i < n.length; i++) {
			n[i] = Integer.parseInt(lines[i]);
		}
		return n;
	}

	private static int countInc(int[] lines) {
		int c = 0;
		for (int i = 1; i < lines.length; i++) {
			if (lines[i] > lines[i - 1])
				c++;
		}
		return c;
	}

}
