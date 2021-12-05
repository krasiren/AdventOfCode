import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day3 {

	public static void main(String[] args) {

		String inputs = "";
		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day3_input.txt"));
			String line = null;

			while ((line = br.readLine()) != null) {
				inputs += line + "\n";
			}
			br.close();
			String[] lines = inputs.split("\n");

			System.out.println(calcPowCons(lines));

			// Part two

			System.out.println(calcLifeSuppRating(lines));

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static int calcLifeSuppRating(String[] lines) {
		ArrayList<String> oxygen = new ArrayList<>();
		ArrayList<String> co2 = new ArrayList<>();
		char mostCom = getMostCommon(lines, 0);

		for (int i = 0; i < lines.length; i++) {
			if (lines[i].charAt(0) == mostCom)
				oxygen.add(lines[i]);
			else
				co2.add(lines[i]);
		}

		return (calc(oxygen, true, 1) * calc(co2, false, 1));
	}

	private static int calc(ArrayList<String> list, boolean most, int j) {
		if (list.size() == 1)
			return Integer.parseInt(list.get(0), 2);

		String[] arr = new String[list.size()];
		arr = list.toArray(arr);
		char mostCom = getMostCommon(arr, j);

		ArrayList<String> temp = new ArrayList<>();
		for (String line : list) {
			if (most) {
				if (line.charAt(j) == mostCom)
					temp.add(line);
			} else {
				if (line.charAt(j) != mostCom)
					temp.add(line);
			}
		}

		return calc(temp, most, j + 1);
	}

	private static char getMostCommon(String[] lines, int j) {
		int ones = 0;
		for (int i = 0; i < lines.length; i++) {
			if (lines[i].charAt(j) == '1')
				ones++;
			if (lines.length % 2 == 0 && ones >= lines.length / 2)
				return '1';
			else if (lines.length % 2 == 1 && ones > lines.length / 2)
				return '1';
		}
		return '0';
	}

	// Part one
	private static int calcPowCons(String[] lines) {
		String gamma = "";
		String epsilon = "";
		for (int i = 0; i < lines[0].length(); i++) {
			int countOnes = 0;
			for (int j = 0; j < lines.length; j++) {
				if (lines[j].charAt(i) == '1')
					countOnes++;
				if (countOnes > lines.length / 2)
					break;
			}

			if (countOnes > lines.length / 2) {
				gamma += "1";
				epsilon += "0";
			} else {
				gamma += "0";
				epsilon += "1";
			}

		}

		return (Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2));

	}

}
