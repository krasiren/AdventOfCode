import java.io.BufferedReader;
import java.io.FileReader;

public class Day5 {

	public static void main(String[] args) {

		try {
			BufferedReader br = new BufferedReader(new FileReader("resources\\Day5_input.txt"));
			String line = null;
			String inputs = "";

			while ((line = br.readLine()) != null) {
				inputs += line + "\n";
			}
			br.close();

			Line[] lines = Line.convert(inputs.split("\n"));
			int xMax = getMax(lines, true);
			int yMax = getMax(lines, false);

			createDiagram(lines, xMax, yMax);

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void createDiagram(Line[] lines, int xMax, int yMax) {
		int[][] map = new int[xMax + 1][yMax + 1];

		for (int i = 0; i < lines.length; i++) {
			if (lines[i].horOrVer())
				fill(map, lines[i], true);
			// for partOne comment 'else' block
			else
				fill(map, lines[i], false);
		}

		int count = countIntersections(map);
		System.out.println(count);

	}

	private static int countIntersections(int[][] map) {
		int c = 0;
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (map[i][j] > 1)
					c++;
			}
		}
		return c;
	}

	private static void fill(int[][] map, Line line, boolean horVer) {
		int stI = (line.getxS() < line.getxE()) ? line.getxS() : line.getxE();
		int enI = (line.getxS() > line.getxE()) ? line.getxS() : line.getxE();
		int stJ = (line.getyS() < line.getyE()) ? line.getyS() : line.getyE();
		int enJ = (line.getyS() > line.getyE()) ? line.getyS() : line.getyE();

		if (horVer) {
			for (int i = stI; i <= enI; i++) {
				for (int j = stJ; j <= enJ; j++) {
					map[i][j]++;
				}
			}
		} else {
			int j = line.getyS();
			int i = line.getxS();
			while (i != line.getxE()) {
				map[i][j]++;
				if (line.getxS() < line.getxE())
					i++;
				else
					i--;

				if (line.getyS() < line.getyE())
					j++;
				else
					j--;
			}
			// ker za i == line.getxE() pade ven
			map[i][j]++;
		}
	}

	private static int getMax(Line[] lines, boolean hor) {
		int max = 0;
		for (int i = 0; i < lines.length; i++) {
			if (hor) {
				if (lines[i].getxS() > max)
					max = lines[i].getxS();
				if (lines[i].getxE() > max)
					max = lines[i].getxE();

			} else {
				if (lines[i].getyS() > max)
					max = lines[i].getyS();
				if (lines[i].getyE() > max)
					max = lines[i].getyE();
			}
		}
		return max;
	}

}

class Line {

	private int xS, yS, xE, yE;

	public Line(String start, String start2, String end, String end2) {
		xS = Integer.parseInt(start);
		yS = Integer.parseInt(start2);
		xE = Integer.parseInt(end);
		yE = Integer.parseInt(end2);
	}

	public boolean horOrVer() {
		return ((xS == xE) || (yS == yE));
	}

	public static Line[] convert(String[] arr) {
		Line[] x = new Line[arr.length];
		for (int i = 0; i < x.length; i++) {
			String[] temp = arr[i].split(" -> ");
			String[] start = temp[0].split(",");
			String[] end = temp[1].split(",");
			x[i] = new Line(start[0], start[1], end[0], end[1]);
		}

		return x;
	}

	public int getxS() {
		return xS;
	}

	public int getyS() {
		return yS;
	}

	public int getxE() {
		return xE;
	}

	public int getyE() {
		return yE;
	}
}
