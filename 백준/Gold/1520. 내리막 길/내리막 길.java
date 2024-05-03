import java.io.*;

public class Main {

	static int M;
	static int N;
	static int[][] map;
	static boolean[][] visited;
	static int D[][];
	static int dx[] = {1, 0, -1, 0};
	static int dy[] = {0, 1, 0, -1};

	public static int execute() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String size[] = br.readLine().split(" ");
		M = Integer.valueOf(size[0]);
		N = Integer.valueOf(size[1]);


		map = new int[M][N];

		D = new int[M][N];
		for(int i = 0; i < M; i++){
			String height[] = br.readLine().split(" ");
			for(int j = 0; j < N; j++){
				map[i][j] = Integer.valueOf(height[j]);
				D[i][j] = -1;
			}
		}

		return DFS(0, 0);
	}

	public static int DFS(int x, int y){
		if(x == M-1 && y == N-1){
			return 1;
		}

		if(D[x][y] == -1){
			D[x][y] = 0;

			for(int i = 0; i < 4 ; i++){
				int xNow = x + dx[i];
				int yNow = y + dy[i];

				if(xNow >= 0 && xNow < M && yNow >= 0 && yNow < N && (map[x][y] > map[xNow][yNow])){
					D[x][y] += DFS(xNow, yNow);
				}
			}
		}
		return D[x][y];

	}

	public static void main(String[] args) throws IOException {
		System.out.println(execute());
	}

}