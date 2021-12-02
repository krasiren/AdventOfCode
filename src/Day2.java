import java.io.BufferedReader;
import java.io.FileReader;

public class Day2 {

	public static void main(String[] args) {
		String inputs = "";

		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day2_i.txt"));
			String line = null;

			while ((line = br.readLine()) != null) {
				inputs += line + "\n";
			}

			String[] lines = inputs.split("\n");

			int hor = prestej(lines, 0);
			int dep = prestej(lines, 1);
			System.out.println(hor * dep);

			// Part two
			dep = prestej(lines, 2);
			System.out.println(hor * dep);

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	// 0 == forward; 1 == up/down
	private static int prestej(String[] lines, int smer) {
		int x = 0;
		int aim = 0;
		for (int i = 0; i < lines.length; i++) {
			String[] line = lines[i].split(" ");
			char first = line[0].charAt(0);
			int temp = Integer.parseInt(line[1]);

			if (smer == 0) {
				if (first == 'f')
					x += temp;
			} else if (smer == 1) {
				if (first == 'd')
					x += temp;
				else if (first == 'u')
					x -= temp;
				
				// Part Two
			} else if (smer == 2) {
				switch (first) {
				case 'f':
					x += temp * aim;
					break;
				case 'd':
					aim += temp;
					break;
				case 'u':
					aim -= temp;
					break;
				}
			}
		}
		return x;
	}

}
