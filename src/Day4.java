import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day4 {

	public static void main(String[] args) {

		long milis = System.currentTimeMillis();
		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day4_input.txt"));
			String line = br.readLine();
			String[] rndNums = line.split(",");

			int[] numbers = convert(rndNums);
			ArrayList<int[][]> sheets = new ArrayList<>();

			while ((line = br.readLine()) != null) {
				int[][] temp = new int[5][5];

				for (int i = 0; i < 5; i++) {
					line = br.readLine();
					String[] vrstica = line.split(" ");
					vrstica = removeEmpty(vrstica);

					for (int j = 0; j < 5; j++) {
						temp[i][j] = Integer.parseInt(vrstica[j]);
					}

				}
				sheets.add(temp);
			}
			br.close();

//			for (int i = 0; i < 5; i++) {
//				for (int j = 0; j < 5; j++) {
//					System.out.print(sheets.get(5)[i][j] + " ");
//				}
//				System.out.println();
//			}

			bingoPlay(sheets, numbers);

		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println(System.currentTimeMillis() - milis);
	}

	private static void bingoPlay(ArrayList<int[][]> sheets, int[] numbers) {
		ArrayList<boolean[][]> marked = new ArrayList<>();
		boolean[] completed = new boolean[sheets.size()];
		for (int i = 0; i < sheets.size(); i++) {
			boolean[][] temp = new boolean[5][5];
			marked.add(temp);
		}


		for (int i = 0; i < numbers.length; i++) {
			mark(numbers[i], marked, sheets, completed);

			
			int x = checkForCompletedButSkip(marked, completed);
			while (x != -1) {
				completed[x] = true;

				// if u want partOne just uncomment this...
//				System.out.println(getSumOfUnmarked(marked, x, sheets) * numbers[i]);
//				break;

				// ...and comment this
				if (countCompleted(completed) == completed.length)
					System.out.println(getSumOfUnmarked(marked, x, sheets) * numbers[i]);
				
				x = checkForCompletedButSkip(marked, completed);
			}
		}

	}

	private static int countCompleted(boolean[] completed) {
		int c = 0;
		for (int i = 0; i < completed.length; i++) {
			if (completed[i])
				c++;
		}
		return c;
	}

	private static int getSumOfUnmarked(ArrayList<boolean[][]> marked, int x, ArrayList<int[][]> sheets) {
		int sum = 0;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (!marked.get(x)[i][j])
					sum += sheets.get(x)[i][j];
			}
		}
		return sum;
	}

	private static int checkForCompletedButSkip(ArrayList<boolean[][]> marked, boolean[] completed) {
		for (int ix = 0; ix < marked.size(); ix++) {
			if (completed[ix])
				continue;

			// vrstice
			for (int i = 0; i < 5; i++) {
				for (int j = 0; j < 5; j++) {
					if (!marked.get(ix)[i][j])
						break;
					if (j == 4)
						return ix;
				}
			}

			// stolpci
			for (int j = 0; j < 5; j++) {
				for (int i = 0; i < 5; i++) {
					if (!marked.get(ix)[i][j])
						break;
					if (i == 4)
						return ix;
				}
			}
		}

		return -1;
	}

	private static void mark(int num, ArrayList<boolean[][]> marked, ArrayList<int[][]> sheets, boolean[] completed) {
		for (int i = 0; i < sheets.size(); i++) {
			if (completed[i])
				continue;
			int[] pos = new int[2];
			pos = contains(sheets.get(i), num);
			if (pos != null)
				marked.get(i)[pos[0]][pos[1]] = true;
		}
	}

	private static int[] contains(int[][] sheet, int x) {
		for (int i = 0; i < sheet.length; i++) {
			for (int j = 0; j < sheet.length; j++) {
				if (sheet[i][j] == x) {
					int[] temp = { i, j };
					return temp;
				}
			}
		}
		return null;
	}

	private static String[] removeEmpty(String[] vrstica) {
		String[] arr = new String[vrstica.length];
		int j = 0;
		for (int i = 0; i < vrstica.length; i++) {
			if (vrstica[i].equals(""))
				continue;
			arr[j] = vrstica[i];
			j++;
		}

		return arr;
	}

	private static int[] convert(String[] rndNums) {
		int[] arr = new int[rndNums.length];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(rndNums[i]);
		}
		return arr;
	}
}
